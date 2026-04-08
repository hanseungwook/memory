"""Scorer for AIME math problems."""

import re

from math_verify import ExprExtractionConfig, LatexExtractionConfig, parse
from math_verify.errors import TimeoutException
from sympy import Integer, simplify
from sympy.core.basic import Basic

from memgen.data.base import Problem
from memgen.scoring.base import ScoreResult

ANSWER_LINE_RE = re.compile(r"^\s*ANSWER:\s*(?P<fragment>.*?)\s*$")
BOXED_ANSWER_RE = re.compile(r"^\\boxed\s*\{(?P<inner>.*)\}$", re.DOTALL)
PERCENT_RE = re.compile(r"(?i)(?:%|percent(?:age)?|pct\b)")
PLAIN_EXPRESSION_RE = re.compile(r"^[\d\s()+\-*/.^]+$")
SEPARATE_INTEGER_RE = re.compile(r"\d\s+\d")


class MathScorer:
    def score(self, problem: Problem, generation: str, index: int) -> ScoreResult:
        """Score a single math generation against the ground truth."""
        expected, expected_reason = self._normalize_gold(problem.answer)
        details = {
            "reason": expected_reason,
            "expected": expected,
            "answer_line": None,
            "answer_fragment": None,
            "extracted": None,
        }

        if expected is None:
            return self._result(problem, index, False, details)

        answer_line, answer_fragment = self._extract_answer_line(generation)
        details["answer_line"] = answer_line
        details["answer_fragment"] = answer_fragment

        if answer_fragment is None:
            details["reason"] = "missing_answer_line"
            return self._result(problem, index, False, details)

        extracted, extract_details = self._parse_integer_answer(answer_fragment)
        details.update(extract_details)

        correct = extracted == expected and details["reason"] == "ok"
        if details["reason"] == "ok":
            details["reason"] = "correct" if correct else "value_mismatch"

        return self._result(problem, index, correct, details)

    def score_batch(self, problem: Problem, generations: list[str]) -> list[ScoreResult]:
        """Score all K generations for one problem."""
        return [self.score(problem, gen, i) for i, gen in enumerate(generations)]

    def _result(
        self, problem: Problem, index: int, correct: bool, details: dict
    ) -> ScoreResult:
        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=1.0 if correct else 0.0,
            tier="correct" if correct else "incorrect",
            details=details,
        )

    def _extract_answer_line(self, text: str) -> tuple[str | None, str | None]:
        """Return the final ANSWER line and its fragment, if present."""
        nonempty_lines = [line for line in text.splitlines() if line.strip()]
        if not nonempty_lines:
            return None, None

        last_line_match = ANSWER_LINE_RE.match(nonempty_lines[-1])
        if last_line_match:
            return nonempty_lines[-1], last_line_match.group("fragment")

        for line in reversed(nonempty_lines[:-1]):
            match = ANSWER_LINE_RE.match(line)
            if match:
                return line, match.group("fragment")

        return None, None

    def _parse_integer_answer(self, fragment: str) -> tuple[str | None, dict]:
        """Parse and canonicalize the answer fragment to an exact integer string."""
        details = {"reason": "ok", "extracted": None}
        stripped_fragment = fragment.strip()

        if not stripped_fragment:
            details["reason"] = "empty_answer_fragment"
            return None, details

        if PERCENT_RE.search(stripped_fragment):
            details["reason"] = "percentage_not_allowed"
            return None, details

        if not self._is_valid_answer_fragment(stripped_fragment):
            details["reason"] = "invalid_answer_fragment"
            return None, details

        try:
            parsed = parse(
                stripped_fragment,
                extraction_config=[LatexExtractionConfig(), ExprExtractionConfig()],
                fallback_mode="no_fallback",
                extraction_mode="any_match",
                parsing_timeout=5,
                raise_on_error=True,
            )
        except TimeoutException:
            details["reason"] = "parse_timeout"
            return None, details
        except Exception as exc:
            details["reason"] = "parse_error"
            details["parser_error"] = f"{type(exc).__name__}: {exc}"
            return None, details

        if not parsed:
            details["reason"] = "parse_failure"
            return None, details

        canonical = self._canonicalize_integer(parsed[0])
        if canonical is None:
            details["reason"] = "non_integer"
            return None, details

        details["extracted"] = canonical
        return canonical, details

    def _is_valid_answer_fragment(self, fragment: str) -> bool:
        """Allow only a single boxed value or plain arithmetic expression."""
        candidate = fragment.strip()

        while boxed_match := BOXED_ANSWER_RE.fullmatch(candidate):
            candidate = boxed_match.group("inner").strip()

        if not candidate:
            return False

        if not PLAIN_EXPRESSION_RE.fullmatch(candidate):
            return False

        return SEPARATE_INTEGER_RE.search(candidate) is None

    def _canonicalize_integer(self, value: object) -> str | None:
        """Return the exact integer string for supported parsed values."""
        if isinstance(value, Integer):
            return str(value)

        if isinstance(value, Basic):
            simplified = simplify(value)
            if isinstance(simplified, Integer):
                return str(simplified)

        return None

    def _normalize_gold(self, value: str | None) -> tuple[str | None, str]:
        if value is None:
            return None, "missing_gold_answer"

        try:
            return self._normalize(value), "ok"
        except ValueError:
            return None, "invalid_gold_answer"

    def _normalize(self, value: str) -> str:
        """Normalize answer: strip whitespace and leading zeros."""
        return str(int(value.strip()))
