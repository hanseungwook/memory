from __future__ import annotations

import pytest

from memgen.config import EvaluationConfig
from memgen.data.base import Problem
from memgen.evaluation.evaluator import EvaluationRun, Evaluator
from memgen.memory.prompts import Memory, MemoryItem
from memgen.scoring.base import ScoreResult


class FakeGenerator:
    async def generate_k(
        self,
        problem: Problem,
        system_prompt: str,
        user_prompt: str,
        k: int | None = None,
    ) -> list[str]:
        del problem, system_prompt, k

        if "Before solving, consider these reusable insights" in user_prompt:
            return ["augmented good", "augmented bad"]
        return ["baseline good", "baseline bad"]


class FakeScorer:
    def score(self, problem: Problem, generation: str, index: int) -> ScoreResult:
        del problem

        passed = "good" in generation
        return ScoreResult(
            problem_id="p1",
            generation_index=index,
            score=1.0 if passed else 0.0,
            tier="correct" if passed else "incorrect",
            details={"generation": generation},
        )


@pytest.mark.asyncio
async def test_evaluate_problem_returns_artifact_outputs():
    evaluator = Evaluator(EvaluationConfig(k=2), FakeScorer())
    evaluator._generator = FakeGenerator()

    problem = Problem(id="p1", domain="math", statement="Compute 2 + 2.", answer="4")
    memory = Memory(
        problem_id="p1",
        items=[
            MemoryItem(
                title="Validate Final Step",
                description="Check the last arithmetic or symbolic step before finalizing.",
                content="A short verification pass catches many otherwise correct solutions that fail at the end.",
                reasoning="",
            )
        ],
        raw_response=(
            "<memories><memory><title>Validate Final Step</title>"
            "<description>Check the last arithmetic or symbolic step before finalizing.</description>"
            "<content>A short verification pass catches many otherwise correct solutions that fail at the end.</content>"
            "</memory></memories>"
        ),
    )

    run = await evaluator.evaluate_problem(problem, memory)

    assert isinstance(run, EvaluationRun)
    assert run.result.baseline_pass_rate == 0.5
    assert run.result.augmented_pass_rate == 0.5
    assert run.artifact.baseline_solutions == ["baseline good", "baseline bad"]
    assert run.artifact.augmented_solutions == ["augmented good", "augmented bad"]
    assert "Compute 2 + 2." in run.artifact.baseline_prompt.user_prompt
    assert "Validate Final Step" in run.artifact.augmented_prompt.user_prompt
    assert "Check the last arithmetic or symbolic step before finalizing." in run.artifact.augmented_prompt.user_prompt
