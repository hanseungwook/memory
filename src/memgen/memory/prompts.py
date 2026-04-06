from __future__ import annotations

import re
from dataclasses import dataclass

from memgen.data.base import Problem


@dataclass
class MemoryItem:
    insight: str
    reasoning: str


@dataclass
class Memory:
    problem_id: str
    items: list[MemoryItem]
    raw_response: str


MEMORY_SYSTEM_PROMPT = (
    "You are an expert analyst studying problem-solving approaches. Your job is "
    "to extract and summarize useful insights in the format of memory items "
    "based on comparing successful and unsuccessful solution attempts. "
    "Every insight you produce must be GENERALIZABLE and TRANSFERABLE to other "
    "problems — never tied to one specific problem's details."
)

_MAX_SOLUTIONS_PER_TIER = 5


def build_memory_creation_prompt(
    problem: Problem, grouped_solutions: dict[str, list[str]]
) -> str:
    sections = [
        "## Guidelines",
        "You need to extract and summarize useful insights in the format of memory items "
        "based on comparing the successful and unsuccessful solution attempts below.",
        "The goal of summarized memory items is to be GENERALIZABLE and TRANSFERABLE — "
        "each insight must be useful not just for this problem, but for a broad class of "
        "similar problems. Write each memory as advice that would help someone who has "
        "never seen this specific problem.",
        "",
        "## Important notes",
        "- You must first think about why certain attempts succeeded and others failed, then summarize the insights.",
        "- You can extract multiple memory items from the comparison. Each should capture a distinct, independent insight.",
        "- Do NOT mention specific values, answers, variable names, or problem-specific details. "
        "Every memory item must stand on its own as a general problem-solving principle or technique "
        "that transfers across different problems in the same domain.",
        "",
        "<problem>",
        problem.statement.strip(),
        "</problem>",
        "",
        "<solution_attempts>",
    ]

    for tier, solutions in grouped_solutions.items():
        tier_solutions = solutions[:_MAX_SOLUTIONS_PER_TIER]
        sections.append(f"<tier name=\"{tier}\">")
        for index, solution in enumerate(tier_solutions, start=1):
            sections.append(f"<attempt index=\"{index}\">")
            sections.append(solution.strip())
            sections.append("</attempt>")
        omitted_count = max(len(solutions) - len(tier_solutions), 0)
        if omitted_count:
            sections.append(f"<!-- {omitted_count} additional {tier} attempts omitted for brevity -->")
        sections.append("</tier>")

    sections.append("</solution_attempts>")
    sections.append("")
    sections.extend(
        [
            "## Response format",
            "First write your analysis inside <reasoning> tags, then produce one or more memory items.",
            "Each memory item must be a self-contained, generalizable insight that transfers to other problems.",
            "A good memory reads like a reusable principle; a bad memory reads like a hint for one specific problem.",
            "",
            "<reasoning>Think about why certain attempts succeeded and others failed. What patterns distinguish them?</reasoning>",
            "",
            "<memories>",
            "<memory>A concise, generalizable insight that would help solve similar problems in the future.</memory>",
            "<memory>Another distinct insight, if applicable.</memory>",
            "</memories>",
        ]
    )
    return "\n".join(sections)


def parse_memory_response(problem_id: str, raw: str) -> Memory:
    reasoning_match = re.search(r"<reasoning>(.*?)</reasoning>", raw, flags=re.DOTALL)
    reasoning = reasoning_match.group(1).strip() if reasoning_match else ""

    memories_match = re.search(r"<memories>(.*?)</memories>", raw, flags=re.DOTALL)
    items: list[MemoryItem] = []
    if memories_match:
        block = memories_match.group(1)
        for m in re.finditer(r"<memory>(.*?)</memory>", block, flags=re.DOTALL):
            insight = m.group(1).strip()
            if insight:
                items.append(MemoryItem(insight=insight, reasoning=reasoning))

    return Memory(
        problem_id=problem_id,
        items=items,
        raw_response=raw,
    )
