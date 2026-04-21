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
    assert "including across domains when the reasoning structure matches" in prompt
    assert "## Example memories" not in prompt


def test_build_memory_creation_prompt_adds_math_specific_guidance():
    problem = Problem(id="p1", domain="math", statement="Solve the task.", answer="42")
    prompt = build_memory_creation_prompt(
        problem,
        {
            "correct": ["correct solution"],
            "incorrect": ["incorrect solution"],
        },
    )

    assert "## Math-specific guidance" in prompt
    assert "Name the reasoning move, not the theorem or topic." in prompt
    assert "representation, invariant, completeness, and validation moves" in prompt
    assert "## Example memories" not in prompt


def test_build_memory_creation_prompt_supports_single_tier_analysis():
    problem = Problem(id="p1", domain="math", statement="Solve the task.", answer="42")
    prompt = build_memory_creation_prompt(
        problem,
        {
            "incorrect": ["wrong solution 1", "wrong solution 2"],
        },
    )

    assert "## Analysis mode" in prompt
    assert "Only one outcome tier is available in this batch: Incorrect." in prompt
    assert "Do not say the task requires contrast." in prompt
    assert "Rewrite those failure patterns as positive, reusable guidance" in prompt
    assert "- Outcome tiers present: Incorrect" in prompt


def test_build_memory_creation_prompt_keeps_math_specific_guidance_out_of_coding():
    problem = Problem(id="p1", domain="coding", statement="Solve the task.", answer="")
    prompt = build_memory_creation_prompt(
        problem,
        {
            "full": ["correct solution"],
            "fail": ["failed solution"],
        },
    )

    assert "## Math-specific guidance" not in prompt
    assert "## Example memories" not in prompt


def test_build_memory_creation_prompt_adds_science_specific_guidance():
    problem = Problem(id="p1", domain="science", statement="Explain the phenomenon.", answer="")
    prompt = build_memory_creation_prompt(
        problem,
        {
            "correct": ["good explanation"],
            "incorrect": ["bad explanation"],
        },
    )

    assert "## Science-specific guidance" in prompt
    assert "Prefer mechanism, evidence, and unit/scale checks" in prompt
    assert "## Example memories" not in prompt


def test_build_memory_creation_prompt_supports_table_alias_domain():
    problem = Problem(id="p1", domain="tabular", statement="Answer the question from the table.", answer="")
    prompt = build_memory_creation_prompt(
        problem,
        {
            "correct": ["good table reasoning"],
            "incorrect": ["bad table reasoning"],
        },
    )

    assert "## Table-specific guidance" in prompt
    assert "slice, scope, denominator, and aggregation checks" in prompt
    assert "## Example memories" not in prompt
