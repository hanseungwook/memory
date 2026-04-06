"""Scorer for AIME math problems."""

import re

from memgen.data.base import Problem
from memgen.scoring.base import ScoreResult


class MathScorer:
    def score(self, problem: Problem, generation: str, index: int) -> ScoreResult:
        """Score a single math generation against the ground truth."""
        extracted = self._extract_answer(generation)
        expected = self._normalize(problem.answer) if problem.answer else None

        if extracted is not None and expected is not None:
            correct = self._normalize(extracted) == expected
        else:
            correct = False

        return ScoreResult(
            problem_id=problem.id,
            generation_index=index,
            score=1.0 if correct else 0.0,
            tier="correct" if correct else "incorrect",
            details={"extracted": extracted, "expected": expected},
        )

    def score_batch(self, problem: Problem, generations: list[str]) -> list[ScoreResult]:
        """Score all K generations for one problem."""
        return [self.score(problem, gen, i) for i, gen in enumerate(generations)]

    def _extract_answer(self, text: str) -> str | None:
        """Extract integer answer from generation text."""
        # Try "ANSWER: <number>" pattern first
        match = re.search(r"ANSWER:\s*(\d+)", text)
        if match:
            return match.group(1)

        # Fallback: last integer in text
        integers = re.findall(r"\b(\d+)\b", text)
        if integers:
            return integers[-1]

        return None

    def _normalize(self, value: str) -> str:
        """Normalize answer: strip whitespace and leading zeros."""
        return str(int(value.strip()))
