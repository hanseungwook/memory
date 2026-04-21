"""Scorer for competitive programming problems."""

import re

from memgen.config import LLMConfig, ScoringConfig
from memgen.data.base import Problem
from memgen.request_limiter import RequestLimiter
from memgen.scoring.base import ScoreResult
from memgen.scoring.sandbox import (
    ExecutionResult,
    execute_function_based,
    execute_stdin_based,
)


_TRUNCATION_SUFFIX = "...[truncated]"


def _truncate_text(value: str, max_length: int) -> str:
    if max_length <= 0 or len(value) <= max_length:
        return value
    if max_length <= len(_TRUNCATION_SUFFIX):
        return value[:max_length]
    return value[: max_length - len(_TRUNCATION_SUFFIX)] + _TRUNCATION_SUFFIX


def _is_function_based(problem: Problem) -> bool:
    """Determine if a problem uses call-based (function) execution."""
    return bool(problem.metadata.get("func_name"))


class CodingScorer:
    def __init__(self, config: ScoringConfig):
        self.timeout = config.timeout_seconds
        self.max_output_length = config.max_output_length

    def score(self, problem: Problem, generation: str, index: int) -> ScoreResult:
        """Score a single coding generation by running it against test cases."""
        code = self._extract_code(generation)
        test_cases = problem.test_cases or []

        if not test_cases:
            return ScoreResult(
                problem_id=problem.id,
                generation_index=index,
                score=0.0,
                tier="fail",
                details={"error": "no test cases"},
            )

        all_inputs = [tc.get("input", "") for tc in test_cases]
        all_outputs = [tc.get("output", "") for tc in test_cases]

        if _is_function_based(problem):
            func_name = problem.metadata["func_name"]
            results = execute_function_based(
                code,
                func_name,
                all_inputs,
                all_outputs,
                timeout=self.timeout,
                max_output_length=self.max_output_length,
            )
        else:
            results = execute_stdin_based(
                code,
                all_inputs,
                all_outputs,
                timeout=self.timeout,
                max_output_length=self.max_output_length,
            )

        passed = sum(1 for r in results if r.passed)
        total = len(test_cases)
        case_results = [
            {
                "passed": r.passed,
                "expected": _truncate_text(exp.strip() if exp else "", self.max_output_length),
                "actual": _truncate_text(r.actual, self.max_output_length),
                "error": _truncate_text(r.error or "", self.max_output_length),
            }
            for r, exp in zip(results, all_outputs)
        ]

        ratio = passed / total
        if ratio == 0.0:
            tier = "fail"
        elif ratio < 1.0:
            tier = "partial"
        else:
            tier = "full"

        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=ratio,
            tier=tier,
            details={"passed": passed, "total": total, "cases": case_results},
        )

    def score_batch(self, problem: Problem, generations: list[str]) -> list[ScoreResult]:
        """Score all K generations for one problem."""
        return [self.score(problem, gen, i) for i, gen in enumerate(generations)]

    def _extract_code(self, text: str) -> str:
        """Extract code from generation text (last fence wins, per official LCB)."""
        # Find all triple-backtick fence pairs and take the last one
        matches = re.findall(r"```(?:\w*\s*\n)?(.*?)```", text, re.DOTALL)
        if matches:
            return matches[-1].strip()
        # Official returns empty string when no fence pair exists
        return ""

    def _build_test_program(self, code: str, test_case: dict) -> str:
        """Build a test program. For stdin/stdout format, just use the code directly."""
        return code


def get_scorer(
    domain: str,
    config: ScoringConfig,
    llm_config: LLMConfig | None = None,
    judge_model: str | None = None,
    request_limiter: RequestLimiter | None = None,
):
    """Factory function returning the appropriate scorer for the domain."""
    normalized = str(domain).strip().lower()
    if normalized == "math":
        from memgen.scoring.math_scorer import MathScorer
        return MathScorer()
    elif normalized == "coding":
        return CodingScorer(config)
    elif normalized == "guru":
        from memgen.scoring.guru_scorer import GuruScorer
        return GuruScorer(
            config,
            llm_config=llm_config,
            judge_model=judge_model,
            request_limiter=request_limiter,
        )
    else:
        raise ValueError(f"Unknown domain: {domain}")
