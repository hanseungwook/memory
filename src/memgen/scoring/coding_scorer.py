"""Scorer for competitive programming problems."""

import re

from memgen.config import ScoringConfig
from memgen.data.base import Problem
from memgen.scoring.base import ScoreResult
from memgen.scoring.sandbox import execute_code


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

        passed = 0
        case_results = []
        for tc in test_cases:
            stdin_input = tc.get("input", "")
            expected = tc.get("output", "").strip()

            stdout, stderr, returncode = execute_code(
                code, stdin_input=stdin_input, timeout=self.timeout
            )

            actual = stdout.strip()
            ok = returncode == 0 and actual == expected
            if ok:
                passed += 1
            case_results.append({
                "passed": ok,
                "expected": expected,
                "actual": actual,
                "stderr": stderr[:500] if stderr else "",
                "returncode": returncode,
            })

        total = len(test_cases)
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
        # Try ```python ... ``` blocks - take the last one
        matches = re.findall(r"```python\s*\n(.*?)```", text, re.DOTALL)
        if matches:
            return matches[-1].strip()

        # Try ``` ... ``` blocks - take the last one
        matches = re.findall(r"```\s*\n(.*?)```", text, re.DOTALL)
        if matches:
            return matches[-1].strip()

        # Raw text
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
