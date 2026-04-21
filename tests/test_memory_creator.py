from __future__ import annotations

import pytest

from memgen.config import MemoryConfig
from memgen.data.base import Problem
from memgen.memory.creator import MemoryCreator
from memgen.memory.prompts import Memory, MemoryItem
from memgen.scoring.base import ScoreResult


@pytest.mark.asyncio
async def test_create_memory_allows_single_tier_solution_pool(monkeypatch):
    creator = MemoryCreator(MemoryConfig())
    problem = Problem(id="p1", domain="math", statement="Solve the task.", answer="42")

    async def fake_request(prompt: str) -> str:
        assert "Only one outcome tier is available in this batch: Incorrect." in prompt
        return (
            "<reasoning>Repeated failures skipped verification.</reasoning>"
            "<memories><memory>"
            "<title>Validate Intermediate Claims</title>"
            "<description>Check each transformed claim against the original constraints.</description>"
            "<content>Repeated wrong attempts often hide an unchecked transformation. Add a verification pass before building on a derived statement.</content>"
            "</memory></memories>"
        )

    monkeypatch.setattr(creator, "_request_memory", fake_request)

    memory = await creator.create_memory(
        problem,
        {"incorrect": ["attempt 1", "attempt 2"]},
        [
            ScoreResult(problem_id="p1", generation_index=0, score=0.0, tier="incorrect"),
            ScoreResult(problem_id="p1", generation_index=1, score=0.0, tier="incorrect"),
        ],
    )

    assert memory is not None
    assert [item.title for item in memory.items] == ["Validate Intermediate Claims"]


@pytest.mark.asyncio
async def test_create_refined_memory_allows_single_tier_solution_pool(monkeypatch):
    creator = MemoryCreator(MemoryConfig())
    problem = Problem(id="p1", domain="coding", statement="Solve the task.", answer="")
    previous_memory = Memory(
        problem_id="p1",
        items=[
            MemoryItem(
                title="Track Invariants",
                description="Keep the key invariant explicit while updating state.",
                content="A compact invariant makes it easier to check each transition.",
            )
        ],
        raw_response="",
    )

    async def fake_request(prompt: str) -> str:
        assert "If the pool collapses to a single outcome tier" in prompt
        assert "Only one outcome tier is available in this batch: Incorrect." in prompt
        return (
            "<reasoning>The memory missed a final validation step.</reasoning>"
            "<memories><memory>"
            "<title>Validate Final State Updates</title>"
            "<description>Check that each update preserves the intended invariant.</description>"
            "<content>When many attempts fail the same way, identify the missing validation that would have caught the drift early.</content>"
            "</memory></memories>"
        )

    monkeypatch.setattr(creator, "_request_memory", fake_request)

    memory = await creator.create_refined_memory(
        problem,
        {"fail": ["attempt 1", "attempt 2"]},
        previous_memory,
        iteration=2,
    )

    assert memory is not None
    assert [item.title for item in memory.items] == ["Validate Final State Updates"]
