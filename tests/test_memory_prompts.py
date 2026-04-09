from __future__ import annotations

from memgen.data.base import Problem
from memgen.memory.prompts import (
    MemoryItem,
    build_memory_creation_prompt,
    parse_memory_response,
)


def test_parse_memory_response_reads_structured_memory_items():
    raw = """
<reasoning>
Successful attempts formalized the constraints and verified risky algebraic steps.
</reasoning>
<memories>
  <memory>
    <title>Constraint-First Reformulation</title>
    <description>Turn informal requirements into explicit constraints before solving.</description>
    <content>Rewrite vague conditions as equations, inequalities, or state rules. That gives you a reliable basis for casework and validation.</content>
  </memory>
  <memory>
    <title>Validate Risky Transformations</title>
    <description>Check transformed candidates against the original problem.</description>
    <content>Operations like squaring or relaxing conditions can introduce artifacts. Run a direct verification pass before finalizing.</content>
  </memory>
</memories>
""".strip()

    memory = parse_memory_response("p1", raw)

    assert len(memory.items) == 2
    assert memory.items[0].title == "Constraint-First Reformulation"
    assert memory.items[0].description == "Turn informal requirements into explicit constraints before solving."
    assert "equations, inequalities, or state rules" in memory.items[0].content
    assert "formalized the constraints" in memory.items[0].reasoning


def test_memory_item_from_dict_supports_legacy_insight_entries():
    item = MemoryItem.from_dict(
        {
            "insight": "Verify candidates against the original constraints after any lossy transformation.",
            "reasoning": "Old-format memory item.",
        }
    )

    assert item.title == "Verify Candidates Against The Original"
    assert item.description == "Verify candidates against the original constraints after any lossy transformation."
    assert item.content == "Verify candidates against the original constraints after any lossy transformation."
    assert item.reasoning == "Old-format memory item."


def test_build_memory_creation_prompt_uses_simple_solution_sections():
    problem = Problem(id="p1", domain="coding", statement="Solve the task.", answer="")
    prompt = build_memory_creation_prompt(
        problem,
        {
            "full": ["correct solution"],
            "partial": ["partial solution"],
            "fail": ["failed solution"],
        },
    )

    assert "### Problem" in prompt
    assert "### Solutions" in prompt
    assert "#### Correct" in prompt
    assert "#### Partially Correct" in prompt
    assert "#### Incorrect" in prompt
    assert "<tier name=" not in prompt
    assert "<solution_attempts>" not in prompt
