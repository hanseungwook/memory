from __future__ import annotations

import re
from dataclasses import dataclass

from memgen.data.base import Problem


@dataclass
class Memory:
    problem_id: str
    key_insight: str
    successful_strategies: list[str]
    common_pitfalls: list[str]
    generalizable_technique: str
    raw_response: str


MEMORY_SYSTEM_PROMPT = (
    "You are an expert analyst studying problem-solving approaches. Your job is "
    "to extract GENERALIZABLE, TRANSFERABLE insights from comparing successful "
    "and unsuccessful solution attempts. CRITICAL: Do NOT produce "
    "problem-specific advice. Every insight you produce must be applicable to a "
    "broad class of similar problems. Think of yourself as writing entries for "
    "a problem-solving playbook that a student would consult before attempting "
    "any problem in this domain."
)

_MAX_SOLUTIONS_PER_TIER = 5
_SECTION_NAMES = (
    "KEY INSIGHT",
    "SUCCESSFUL STRATEGIES",
    "COMMON PITFALLS",
    "GENERALIZABLE TECHNIQUE",
)


def build_memory_creation_prompt(
    problem: Problem, grouped_solutions: dict[str, list[str]]
) -> str:
    sections = [
        "Analyze the problem and the contrasted solution attempts below.",
        "Your output must focus on insights that GENERALIZE beyond this specific problem.",
        "Do not mention the exact answer, problem-specific numbers, or any advice tied only to this prompt.",
        "",
        "## Problem Statement",
        problem.statement.strip(),
        "",
        "## Solution Attempts Grouped by Outcome",
    ]

    for tier, solutions in grouped_solutions.items():
        tier_solutions = solutions[:_MAX_SOLUTIONS_PER_TIER]
        sections.append(f"### {tier.upper()}")
        for index, solution in enumerate(tier_solutions, start=1):
            sections.append(f"Attempt {index}:")
            sections.append(solution.strip())
            sections.append("")
        omitted_count = max(len(solutions) - len(tier_solutions), 0)
        if omitted_count:
            sections.append(f"[{omitted_count} additional {tier} attempts omitted for brevity]")
            sections.append("")

    sections.extend(
        [
            "Compare the stronger and weaker attempts.",
            "Identify what transfers to other problems in the same domain.",
            "Respond in this exact format:",
            "",
            "**KEY INSIGHT:**",
            "[One sentence: the single most important transferable lesson]",
            "",
            "**SUCCESSFUL STRATEGIES:**",
            "- [Strategy 1]",
            "- [Strategy 2]",
            "- [Strategy 3: if applicable]",
            "",
            "**COMMON PITFALLS:**",
            "- [Pitfall 1]",
            "- [Pitfall 2]",
            "- [Pitfall 3: if applicable]",
            "",
            "**GENERALIZABLE TECHNIQUE:**",
            "[One paragraph: reusable problem-solving technique for similar problems. Do NOT reference the specific problem.]",
        ]
    )
    return "\n".join(sections)


def parse_memory_response(problem_id: str, raw: str) -> Memory:
    def extract_section(name: str) -> str:
        pattern = rf"\*\*{re.escape(name)}:\*\*\s*(.*?)(?=\n\s*\*\*[A-Z ]+:\*\*|\Z)"
        match = re.search(pattern, raw, flags=re.DOTALL)
        if not match:
            return ""
        return match.group(1).strip()

    def extract_bullets(section_text: str) -> list[str]:
        items: list[str] = []
        for line in section_text.splitlines():
            bullet = re.match(r"^\s*[-*]\s+(.*)$", line)
            if bullet:
                item = bullet.group(1).strip()
                if item:
                    items.append(item)
        return items

    parsed_sections = {name: extract_section(name) for name in _SECTION_NAMES}
    key_insight = " ".join(parsed_sections["KEY INSIGHT"].split())
    generalizable_technique = parsed_sections["GENERALIZABLE TECHNIQUE"].strip()

    return Memory(
        problem_id=problem_id,
        key_insight=key_insight,
        successful_strategies=extract_bullets(parsed_sections["SUCCESSFUL STRATEGIES"]),
        common_pitfalls=extract_bullets(parsed_sections["COMMON PITFALLS"]),
        generalizable_technique=generalizable_technique,
        raw_response=raw,
    )
