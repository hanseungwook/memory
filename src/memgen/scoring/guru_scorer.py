from __future__ import annotations

import ast
import json
import os
import re
from contextlib import nullcontext
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Any

from math_verify import ExprExtractionConfig, LatexExtractionConfig, parse
from math_verify.errors import TimeoutException as MathParseTimeout
from sympy import simplify
from sympy.core.basic import Basic

from memgen.config import LLMConfig, ScoringConfig
from memgen.data.base import Problem
from memgen.llm import create_openai_client
from memgen.request_limiter import RequestLimiter
from memgen.scoring.base import ScoreResult
from memgen.scoring.sandbox import (
    ExecutionResult,
    execute_python_assertions,
    execute_stdin_based,
)

_BOXED_RE = re.compile(r"\\boxed\s*\{", re.DOTALL)
_ANSWER_LINE_RE = re.compile(r"^\s*ANSWER:\s*(?P<answer>.*?)\s*$", re.IGNORECASE)
_CODE_BLOCK_RE = re.compile(r"```(?:\w+)?\s*(.*?)```", re.DOTALL)
_ANSWER_TAG_RE = re.compile(r"<answer>(.*?)</answer>", re.DOTALL | re.IGNORECASE)
_JSON_OBJECT_RE = re.compile(r"\{[\s\S]*\}")
_INVALID_STRUCTURE = object()


@dataclass
class _ScalarScore:
    score: float
    tier: str
    details: dict[str, Any]


class GuruScorer:
    def __init__(
        self,
        config: ScoringConfig,
        llm_config: LLMConfig | None = None,
        judge_model: str | None = None,
        request_limiter: RequestLimiter | None = None,
    ):
        self.timeout = config.timeout_seconds
        self.max_output_length = config.max_output_length
        self.llm_config = llm_config or LLMConfig()
        self.judge_model = judge_model
        self.request_limiter = request_limiter
        self._judge_client = None

    def score(self, problem: Problem, generation: str, index: int) -> ScoreResult:
        data_source = str(problem.metadata.get("data_source") or "")
        ground_truth = problem.metadata.get("ground_truth")
        extra_info = problem.metadata.get("extra_info") or {}

        if data_source.startswith("codegen__"):
            return self._score_code(problem, generation, index, ground_truth, extra_info)
        if data_source.startswith("simulation__codeio"):
            return self._score_codeio(problem, generation, index, ground_truth)
        if data_source.startswith("logic__zebra_puzzle"):
            return self._score_zebra(problem, generation, index, ground_truth)
        if data_source.startswith("logic__ordering_puzzle"):
            return self._score_ordering(problem, generation, index, ground_truth)
        if data_source.startswith("logic__graph"):
            return self._score_graph(problem, generation, index, ground_truth)
        if data_source.startswith(("simulation__arcagi", "simulation__barc")):
            return self._score_arc(problem, generation, index, ground_truth)
        if data_source.startswith("table__"):
            return self._score_scalar(problem, generation, index, ground_truth, allow_judge=False)
        if data_source.startswith(("stem__web", "stem_web")):
            return self._score_science(problem, generation, index, ground_truth, extra_info)
        if data_source.startswith("math__"):
            return self._score_scalar(problem, generation, index, ground_truth, allow_judge=False)

        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=0.0,
            tier="incorrect",
            details={"error": f"unsupported_data_source:{data_source}"},
        )

    def score_batch(self, problem: Problem, generations: list[str]) -> list[ScoreResult]:
        return [self.score(problem, generation, index) for index, generation in enumerate(generations)]

    def _score_code(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
        extra_info: dict[str, Any],
    ) -> ScoreResult:
        code = self._extract_code(generation)
        if not code:
            return ScoreResult(
                problem_id=problem.id,
                generation_index=index,
                score=0.0,
                tier="fail",
                details={"error": "missing_code_block"},
            )

        parsed_ground_truth = self._parse_ground_truth_json(ground_truth)
        if not isinstance(parsed_ground_truth, dict):
            return ScoreResult(
                problem_id=problem.id,
                generation_index=index,
                score=0.0,
                tier="fail",
                details={"error": "invalid_ground_truth"},
            )

        prefix = str(extra_info.get("prefix") or "")
        combined_code = f"{prefix.rstrip()}\n{code}".strip() if prefix else code

        if "functional" in parsed_ground_truth:
            result = execute_python_assertions(
                combined_code,
                str(parsed_ground_truth["functional"]),
                timeout=self.timeout,
                max_output_length=self.max_output_length,
            )
            score = 1.0 if result.passed else 0.0
            return ScoreResult(
                problem_id=problem.id,
                generation_index=index,
                score=score,
                tier="full" if score == 1.0 else "fail",
                details={
                    "mode": "functional",
                    "actual": result.actual,
                    "error": result.error,
                },
            )

        stdin_inputs = parsed_ground_truth.get("inputs")
        stdout_outputs = parsed_ground_truth.get("outputs")
        if not isinstance(stdin_inputs, list) or not isinstance(stdout_outputs, list):
            return ScoreResult(
                problem_id=problem.id,
                generation_index=index,
                score=0.0,
                tier="fail",
                details={"error": "unsupported_code_ground_truth"},
            )

        results = execute_stdin_based(
            combined_code,
            [str(item) for item in stdin_inputs],
            [str(item) for item in stdout_outputs],
            timeout=self.timeout,
            max_output_length=self.max_output_length,
        )
        passed = sum(1 for result in results if result.passed)
        total = len(results) or 1
        ratio = passed / total
        tier = "fail" if ratio == 0.0 else "partial" if ratio < 1.0 else "full"
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=ratio,
            tier=tier,
            details={
                "mode": "stdin",
                "passed": passed,
                "total": len(results),
                "cases": [
                    {
                        "passed": result.passed,
                        "actual": result.actual,
                        "error": result.error,
                    }
                    for result in results
                ],
            },
        )

    def _score_codeio(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
    ) -> ScoreResult:
        predicted = self._normalize_object(self._extract_json_answer(generation))
        truth = self._normalize_object(self._convert_codeio_ground_truth(ground_truth))
        correct = predicted == truth and predicted is not None
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=1.0 if correct else 0.0,
            tier="correct" if correct else "incorrect",
            details={"predicted": predicted, "expected": truth},
        )

    def _score_zebra(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
    ) -> ScoreResult:
        answer = self._extract_answer_tag_object(generation)
        score = 0.0
        if isinstance(answer, dict) and isinstance(ground_truth, dict):
            rows = ground_truth.get("rows") or []
            header = ground_truth.get("header") or []
            total_cells = len(rows) * len(header)
            if total_cells:
                correct_cells = 0
                answer_rows = answer.get("rows") or []
                for row_idx, expected_row in enumerate(rows):
                    for col_idx, expected_cell in enumerate(expected_row):
                        candidate_row = (
                            answer_rows[row_idx]
                            if row_idx < len(answer_rows) and isinstance(answer_rows[row_idx], list)
                            else None
                        )
                        if (
                            candidate_row is not None
                            and col_idx < len(candidate_row)
                            and candidate_row[col_idx] == expected_cell
                        ):
                            correct_cells += 1
                score = correct_cells / total_cells
        tier = "fail" if score == 0.0 else "partial" if score < 1.0 else "full"
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=score,
            tier=tier,
            details={"predicted": answer, "expected": ground_truth},
        )

    def _score_ordering(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
    ) -> ScoreResult:
        predicted = self._extract_answer_tag_object(generation)
        if isinstance(predicted, tuple):
            predicted = list(predicted)
        score = 0.0
        if isinstance(predicted, list) and isinstance(ground_truth, list):
            if predicted == ground_truth:
                score = 1.0
            else:
                edit_distance = self._list_edit_distance(predicted, ground_truth)
                max_len = max(len(predicted), len(ground_truth), 1)
                score = max(0.0, 1.0 - (edit_distance / max_len))
        tier = "fail" if score == 0.0 else "partial" if score < 1.0 else "full"
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=score,
            tier=tier,
            details={"predicted": predicted, "expected": ground_truth},
        )

    def _score_graph(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
    ) -> ScoreResult:
        predicted = self._extract_answer_tag_text(generation)
        truth = str(ground_truth or "").strip().lower()
        correct = bool(predicted) and predicted.lower() == truth
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=1.0 if correct else 0.0,
            tier="correct" if correct else "incorrect",
            details={"predicted": predicted, "expected": ground_truth},
        )

    def _score_arc(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
    ) -> ScoreResult:
        predicted = self._extract_answer_tag_object(generation)
        score = self._grid_similarity(predicted, ground_truth)
        tier = "fail" if score == 0.0 else "partial" if score < 1.0 else "full"
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=score,
            tier=tier,
            details={"predicted": predicted, "expected": ground_truth},
        )

    def _score_science(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
        extra_info: dict[str, Any],
    ) -> ScoreResult:
        scalar = self._score_scalar(problem, generation, index, ground_truth, allow_judge=False)
        if scalar.score == 1.0:
            return scalar

        extracted_answer = self._extract_scalar_answer(generation)
        question = str(extra_info.get("question") or problem.statement).strip()
        judged = self._judge_science_equivalence(question, extracted_answer, str(ground_truth or ""))
        if judged:
            return ScoreResult(
                problem_id=problem.id,
                generation_index=index,
                score=1.0,
                tier="correct",
                details={
                    "predicted": extracted_answer,
                    "expected": ground_truth,
                    "judge": "llm",
                },
            )
        return scalar

    def _score_scalar(
        self,
        problem: Problem,
        generation: str,
        index: int,
        ground_truth: Any,
        allow_judge: bool,
    ) -> ScoreResult:
        del allow_judge
        extracted = self._extract_scalar_answer(generation)
        correct = self._scalar_answers_equal(extracted, str(ground_truth or ""))
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=1.0 if correct else 0.0,
            tier="correct" if correct else "incorrect",
            details={"predicted": extracted, "expected": ground_truth},
        )

    def _judge_science_equivalence(self, question: str, student_answer: str, reference_answer: str) -> bool:
        if not question or not student_answer or not reference_answer:
            return False

        base_url = self.llm_config.base_url or os.getenv("STEM_LLM_JUDGE_URL")
        model = os.getenv("MEMGEN_STEM_JUDGE_MODEL") or self.judge_model
        if not model:
            return False
        if self._judge_client is None:
            judge_config = LLMConfig(
                provider=self.llm_config.provider,
                base_url=base_url,
                api_key=self.llm_config.api_key,
                timeout_seconds=self.llm_config.timeout_seconds,
                max_retries=self.llm_config.max_retries,
            )
            self._judge_client = create_openai_client(judge_config)

        prompt = (
            f"### Question: {question}\n\n"
            f"### Ground Truth Answer: {reference_answer}\n\n"
            f"### Student Answer: {student_answer}\n\n"
            "For the above question, verify if the student's answer is equivalent to the ground truth answer. "
            "Do not solve the question yourself. If the student's answer is correct, output "
            '"Final Decision: Yes". If the student answer is incorrect, output "Final Decision: No".'
        )
        limit_ctx = (
            self.request_limiter.sync_slot()
            if self.request_limiter is not None
            else nullcontext()
        )
        with limit_ctx:
            response = self._judge_client.chat.completions.create(
                model=model,
                temperature=0.0,
                messages=[{"role": "user", "content": prompt}],
            )
        content = response.choices[0].message.content or ""
        return "Final Decision: Yes" in content

    def _extract_code(self, generation: str) -> str:
        matches = _CODE_BLOCK_RE.findall(generation or "")
        if matches:
            return matches[-1].strip()
        return ""

    def _parse_ground_truth_json(self, ground_truth: Any) -> Any:
        if isinstance(ground_truth, str):
            try:
                return json.loads(ground_truth)
            except json.JSONDecodeError:
                return ground_truth
        return ground_truth

    def _extract_scalar_answer(self, text: str) -> str:
        text = self._strip_thinking(text)
        answer_tag = self._extract_answer_tag_text(text)
        if answer_tag:
            return answer_tag

        boxed = self._extract_last_boxed(text)
        if boxed:
            return boxed

        for line in reversed([line for line in text.splitlines() if line.strip()]):
            match = _ANSWER_LINE_RE.match(line)
            if match:
                return match.group("answer").strip()

        lines = [line.strip() for line in text.splitlines() if line.strip()]
        return lines[-1] if lines else text.strip()

    def _scalar_answers_equal(self, predicted: str, ground_truth: str) -> bool:
        if not predicted or not ground_truth:
            return False

        predicted_options = self._scalar_variants(predicted)
        truth_options = self._scalar_variants(ground_truth)

        for candidate in predicted_options:
            for truth in truth_options:
                if self._normalized_text(candidate) == self._normalized_text(truth):
                    return True
                if self._numeric_equal(candidate, truth):
                    return True
                if self._symbolic_equal(candidate, truth):
                    return True

        return False

    def _scalar_variants(self, value: str) -> list[str]:
        cleaned = self._cleanup_scalar_text(value)
        variants = [cleaned]
        if "=" in cleaned:
            variants.append(cleaned.split("=")[-1].strip())
        return [variant for variant in variants if variant]

    def _cleanup_scalar_text(self, value: str) -> str:
        cleaned = str(value).strip()
        cleaned = cleaned.replace("{eq}", "").replace("{/eq}", "")
        cleaned = cleaned.replace("$", "")
        cleaned = cleaned.replace("\\,", "")
        cleaned = cleaned.replace("\\!", "")
        cleaned = cleaned.replace("\\;", "")
        cleaned = cleaned.replace("\\%", "%")
        return cleaned.strip()

    def _normalized_text(self, value: str) -> str:
        return re.sub(r"\s+", "", self._cleanup_scalar_text(value).lower())

    def _numeric_equal(self, left: str, right: str) -> bool:
        try:
            left_value = Decimal(self._cleanup_scalar_text(left).replace(",", ""))
            right_value = Decimal(self._cleanup_scalar_text(right).replace(",", ""))
        except (InvalidOperation, ValueError):
            return False
        return left_value == right_value

    def _symbolic_equal(self, left: str, right: str) -> bool:
        try:
            parsed_left = parse(
                self._cleanup_scalar_text(left),
                extraction_config=[LatexExtractionConfig(), ExprExtractionConfig()],
                fallback_mode="no_fallback",
                extraction_mode="any_match",
                parsing_timeout=5,
                raise_on_error=True,
            )
            parsed_right = parse(
                self._cleanup_scalar_text(right),
                extraction_config=[LatexExtractionConfig(), ExprExtractionConfig()],
                fallback_mode="no_fallback",
                extraction_mode="any_match",
                parsing_timeout=5,
                raise_on_error=True,
            )
        except (MathParseTimeout, Exception):
            return False

        if not parsed_left or not parsed_right:
            return False

        return self._sympy_equivalent(parsed_left[0], parsed_right[0])

    def _sympy_equivalent(self, left: Any, right: Any) -> bool:
        if left == right:
            return True
        if isinstance(left, Basic) or isinstance(right, Basic):
            try:
                return simplify(left - right) == 0
            except Exception:
                return False
        return False

    def _extract_last_boxed(self, text: str) -> str | None:
        match_positions = list(_BOXED_RE.finditer(text or ""))
        if not match_positions:
            return None

        start = match_positions[-1].end() - 1
        depth = 0
        for index in range(start, len(text)):
            if text[index] == "{":
                depth += 1
                if depth == 1:
                    start = index + 1
            elif text[index] == "}":
                depth -= 1
                if depth == 0:
                    return text[start:index].strip()
        return None

    def _extract_answer_tag_text(self, text: str) -> str | None:
        matches = _ANSWER_TAG_RE.findall(text or "")
        if not matches:
            return None
        return matches[-1].strip()

    def _extract_answer_tag_object(self, text: str) -> Any:
        answer_text = self._extract_answer_tag_text(text)
        if not answer_text:
            return None
        return self._safe_parse_structure(answer_text)

    def _extract_json_answer(self, text: str) -> Any:
        stripped = self._strip_thinking(text)
        code_blocks = _CODE_BLOCK_RE.findall(stripped)
        candidates = [candidate.strip() for candidate in code_blocks if candidate.strip()]
        if not candidates:
            json_match = _JSON_OBJECT_RE.findall(stripped)
            candidates = [candidate.strip() for candidate in json_match if candidate.strip()]
        for candidate in reversed(candidates):
            parsed = self._safe_parse_structure(candidate)
            if parsed is not None:
                if isinstance(parsed, dict):
                    return parsed.get("output", parsed.get("input", parsed))
                return parsed
        return None

    def _convert_codeio_ground_truth(self, ground_truth: Any) -> Any:
        if isinstance(ground_truth, str) and ('"input":' in ground_truth or '"output":' in ground_truth):
            text = ground_truth.strip()
            if not (text.startswith("{") and text.endswith("}")):
                text = "{" + text + "}"
            parsed = self._safe_parse_structure(text)
            if isinstance(parsed, dict):
                return parsed.get("input", parsed.get("output", parsed))
        return self._safe_parse_structure(ground_truth) if isinstance(ground_truth, str) else ground_truth

    def _safe_parse_structure(self, value: Any) -> Any:
        if not isinstance(value, str):
            normalized = self._normalize_structure(value)
            if normalized is not _INVALID_STRUCTURE:
                return normalized
        if value is None:
            return None

        text = str(value).strip()
        if not text:
            return None

        for parser in (json.loads, ast.literal_eval):
            try:
                parsed = parser(text)
            except Exception:
                continue
            normalized = self._normalize_structure(parsed)
            if normalized is not _INVALID_STRUCTURE:
                return normalized
        return None

    def _normalize_object(self, value: Any) -> Any:
        if value is Ellipsis or isinstance(value, (set, frozenset)):
            return None
        if isinstance(value, str):
            text = value.strip()
            if (text.startswith("{") and text.endswith("}")) or (text.startswith("[") and text.endswith("]")):
                parsed = self._safe_parse_structure(text)
                if parsed is not None:
                    return self._normalize_object(parsed)
            lowered = text.lower()
            if lowered in {"true", "false"}:
                return lowered == "true"
            return text
        if isinstance(value, list):
            return [self._normalize_object(item) for item in value]
        if isinstance(value, tuple):
            return [self._normalize_object(item) for item in value]
        if isinstance(value, dict):
            return {str(key): self._normalize_object(item) for key, item in value.items()}
        return value

    def _normalize_structure(self, value: Any) -> Any:
        if value is Ellipsis or isinstance(value, (set, frozenset)):
            return _INVALID_STRUCTURE
        if value is None or isinstance(value, (str, bool, int, float)):
            return value
        if isinstance(value, list):
            normalized_items = []
            for item in value:
                normalized = self._normalize_structure(item)
                if normalized is _INVALID_STRUCTURE:
                    return _INVALID_STRUCTURE
                normalized_items.append(normalized)
            return normalized_items
        if isinstance(value, tuple):
            normalized_items = []
            for item in value:
                normalized = self._normalize_structure(item)
                if normalized is _INVALID_STRUCTURE:
                    return _INVALID_STRUCTURE
                normalized_items.append(normalized)
            return normalized_items
        if isinstance(value, dict):
            normalized_dict = {}
            for key, item in value.items():
                normalized_key = self._normalize_structure(key)
                normalized_item = self._normalize_structure(item)
                if (
                    normalized_key is _INVALID_STRUCTURE
                    or normalized_item is _INVALID_STRUCTURE
                ):
                    return _INVALID_STRUCTURE
                normalized_dict[str(normalized_key)] = normalized_item
            return normalized_dict
        return _INVALID_STRUCTURE

    def _grid_similarity(self, predicted: Any, ground_truth: Any) -> float:
        if not isinstance(predicted, list) or not isinstance(ground_truth, list):
            return 0.0
        if not predicted or not ground_truth:
            return 0.0

        predicted_rows = [row if isinstance(row, list) else [row] for row in predicted]
        truth_rows = [row if isinstance(row, list) else [row] for row in ground_truth]
        max_rows = max(len(predicted_rows), len(truth_rows))
        max_cols = max(
            max((len(row) for row in predicted_rows), default=0),
            max((len(row) for row in truth_rows), default=0),
        )
        if max_rows == 0 or max_cols == 0:
            return 0.0

        total = max_rows * max_cols
        correct = 0
        for row_idx in range(max_rows):
            for col_idx in range(max_cols):
                predicted_value = (
                    predicted_rows[row_idx][col_idx]
                    if row_idx < len(predicted_rows) and col_idx < len(predicted_rows[row_idx])
                    else None
                )
                truth_value = (
                    truth_rows[row_idx][col_idx]
                    if row_idx < len(truth_rows) and col_idx < len(truth_rows[row_idx])
                    else None
                )
                if predicted_value == truth_value and truth_value is not None:
                    correct += 1
        return correct / total

    def _list_edit_distance(self, left: list[Any], right: list[Any]) -> int:
        dp = [[0 for _ in range(len(right) + 1)] for _ in range(len(left) + 1)]
        for i in range(len(left) + 1):
            dp[i][0] = i
        for j in range(len(right) + 1):
            dp[0][j] = j
        for i in range(1, len(left) + 1):
            for j in range(1, len(right) + 1):
                if left[i - 1] == right[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],
                        dp[i][j - 1],
                        dp[i - 1][j - 1],
                    )
        return dp[-1][-1]

    def _strip_thinking(self, text: str) -> str:
        return str(text or "").split("</think>")[-1].strip()
