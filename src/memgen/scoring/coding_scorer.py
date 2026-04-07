"""Scorer for competitive programming problems."""

import re

from memgen.config import ScoringConfig
from memgen.data.base import Problem
from memgen.scoring.base import ScoreResult
from memgen.scoring.sandbox import (
    ExecutionResult,
    execute_function_based,
    execute_stdin_based,
)


def _is_function_based(problem: Problem) -> bool:
    """Determine if a problem uses call-based (function) execution."""
    return bool(problem.metadata.get("func_name") and problem.starter_code)


class CodingScorer:
    def __init__(self, config: ScoringConfig):
        self.timeout = config.timeout_seconds

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
                code, func_name, all_inputs, all_outputs, timeout=self.timeout
            )
        else:
            results = execute_stdin_based(
                code, all_inputs, all_outputs, timeout=self.timeout
            )

        passed = sum(1 for r in results if r.passed)
        total = len(test_cases)
        case_results = [
            {
                "passed": r.passed,
                "expected": exp.strip() if exp else "",
                "actual": r.actual,
                "error": r.error or "",
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
        """Extract code from generation text."""
        match = re.search(r"```python\s*\n(.*?)```", text, re.DOTALL)
        if match:
            return match.group(1).strip()

        match = re.search(r"```\s*\n(.*?)```", text, re.DOTALL)
        if match:
            return match.group(1).strip()

        return text.strip()

    def _build_test_program(self, code: str, test_case: dict) -> str:
        """Build a test program. For stdin/stdout format, just use the code directly."""
        return code


def get_scorer(domain: str, config: ScoringConfig):
    """Factory function returning the appropriate scorer for the domain."""
    if domain == "math":
        from memgen.scoring.math_scorer import MathScorer
        return MathScorer()
    elif domain == "coding":
        return CodingScorer(config)
    else:
        raise ValueError(f"Unknown domain: {domain}")
