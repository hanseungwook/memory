from __future__ import annotations

import re
from dataclasses import dataclass

from memgen.data.base import Problem


@dataclass
class MemoryItem:
    title: str
    description: str
    content: str
    reasoning: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> "MemoryItem":
        title = _normalize_inline_text(str(data.get("title", "")))
        description = _normalize_inline_text(str(data.get("description", "")))
        content = _normalize_block_text(str(data.get("content", "")))
        reasoning = _normalize_block_text(str(data.get("reasoning", "")))

        legacy_insight = _normalize_block_text(str(data.get("insight", "")))
        if legacy_insight and not any((title, description, content)):
            description = _first_sentence(legacy_insight) or legacy_insight
            content = legacy_insight
            title = _derive_title(description)

        if content and not description:
            description = _first_sentence(content) or content
        if description and not title:
            title = _derive_title(description)
        if title and not content:
            content = description

        return cls(
            title=title,
            description=description,
            content=content,
            reasoning=reasoning,
        )


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
    "problems — never tied to one specific problem's details. Prefer reusable "
    "meta-reasoning patterns such as reformulating constraints, choosing a "
    "better state or invariant, validating risky transformations, or selecting "
    "a simpler counting/search strategy."
)

_MAX_SOLUTIONS_PER_TIER = None  # Use all solutions
_PROMPT_TIER_LABELS = {
    "correct": "Correct",
    "full": "Correct",
    "partial": "Partially Correct",
    "incorrect": "Incorrect",
    "fail": "Incorrect",
}
_PROMPT_TIER_ORDER = ("Correct", "Partially Correct", "Incorrect")


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
        "- Prioritize GENERAL META-REASONING techniques over object-level hints. Favor principles about representation choice, constraint formalization, invariant selection, validation, decomposition, debugging, or algorithm selection.",
        "- Convert failure observations into POSITIVE reusable guidance. Do not write memories that are just restatements of one wrong step.",
        "- Do NOT mention specific values, answers, variable names, or problem-specific details. "
        "Every memory item must stand on its own as a general problem-solving principle or technique "
        "that transfers across different problems in the same domain.",
        "- Avoid narrow one-off tricks unless they clearly transfer to a recurring class of problems. Fewer high-quality memories are better than many repetitive ones.",
        "- Emphasize high-level strategies that would still make sense on a different problem in the same domain.",
        "",
        "## Examples of good meta-reasoning memories",
        "- Title: Constraint-First Reformulation",
        '  Description: Turn informal requirements into explicit constraints before solving.',
        "  Content: Rewrite vague conditions as equations, inequalities, parity rules, or state constraints. Use those formal constraints to guide the solution and reject invalid branches early.",
        "- Title: Validate Risky Transformations",
        '  Description: Check any step that can introduce invalid candidates against the original problem.',
        "  Content: Squaring, dividing, relaxing constraints, or compressing state can create artifacts that look valid only in the transformed setting. Add a direct verification pass against the original conditions before committing to an answer.",
        "- Title: Model the Smallest Faithful State",
        '  Description: Reduce the problem to the minimal state that still determines future decisions.',
        "  Content: If only parity, remainder class, last element, or turn matters, build the reasoning or DP around that reduced state instead of the full object. This shrinks search and makes transitions easier to verify.",
        "",
        "### Problem",
        problem.statement.strip(),
        "",
        "### Solutions",
    ]

    for label, solutions in _group_prompt_solutions(grouped_solutions).items():
        sections.append(f"#### {label}")
        for index, solution in enumerate(solutions, start=1):
            sections.append(f"Attempt {index}")
            sections.append(solution.strip())
            sections.append("")
    sections.append("")
    sections.extend(
        [
            "## Response format",
            "First write your analysis inside <reasoning> tags, then produce one or more memory items.",
            "Each memory item must be a self-contained, generalizable insight that transfers to other problems.",
            "A good memory reads like a reusable principle; a bad memory reads like a hint for one specific problem.",
            "Each memory item must use this schema:",
            '- "title": a short label for the memory item',
            '- "description": one sentence summary of the memory item',
            '- "content": 1-3 sentences describing the insight learned for successfully accomplishing similar tasks',
            "",
            "<reasoning>Think about why certain attempts succeeded and others failed. What patterns distinguish them?</reasoning>",
            "",
            "<memories>",
            "<memory>",
            "<title>The title of the memory item</title>",
            "<description>One sentence summary of the memory item.</description>",
            "<content>One to three sentences describing the reusable insight learned from the comparison.</content>",
            "</memory>",
            "<memory>",
            "<title>Another distinct reusable principle</title>",
            "<description>One sentence summary of the second memory item.</description>",
            "<content>One to three sentences describing the second reusable insight.</content>",
            "</memory>",
            "</memories>",
        ]
    )
    return "\n".join(sections)


def parse_memory_response(problem_id: str, raw: str) -> Memory:
    reasoning_match = re.search(r"<reasoning>(.*?)(?:</reasoning>|$)", raw, flags=re.DOTALL)
    reasoning = _normalize_block_text(reasoning_match.group(1)) if reasoning_match else ""

    memories_match = re.search(r"<memories>(.*?)</memories>", raw, flags=re.DOTALL)
    memory_region = memories_match.group(1) if memories_match else raw
    items: list[MemoryItem] = []
    for m in re.finditer(
        r"<memory>(.*?)(?:</memory>|(?=<memory>)|$)",
        memory_region,
        flags=re.DOTALL,
    ):
        block = m.group(1).strip()
        if not block:
            continue

        title = _extract_tag(block, "title", normalize=_normalize_inline_text)
        description = _extract_tag(
            block,
            "description",
            normalize=_normalize_inline_text,
        )
        content = _extract_tag(block, "content", normalize=_normalize_block_text)

        if any((title, description, content)):
            item = MemoryItem.from_dict(
                {
                    "title": title,
                    "description": description,
                    "content": content,
                    "reasoning": reasoning,
                }
            )
        else:
            item = MemoryItem.from_dict({"insight": block, "reasoning": reasoning})

        if any((item.title, item.description, item.content)):
            items.append(item)

    return Memory(
        problem_id=problem_id,
        items=items,
        raw_response=raw,
    )


def _extract_tag(text: str, tag: str, normalize) -> str:
    match = re.search(fr"<{tag}>(.*?)</{tag}>", text, flags=re.DOTALL)
    if not match:
        return ""
    return normalize(match.group(1))


def _normalize_inline_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _normalize_block_text(text: str) -> str:
    stripped = text.strip()
    if not stripped:
        return ""
    normalized = re.sub(r"[ \t]+\n", "\n", stripped)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    return normalized.strip()


def _first_sentence(text: str) -> str:
    normalized = _normalize_inline_text(text)
    if not normalized:
        return ""
    match = re.match(r"(.+?[.!?])(?:\s|$)", normalized)
    return match.group(1).strip() if match else normalized


def _derive_title(text: str) -> str:
    normalized = _normalize_inline_text(text)
    if not normalized:
        return "Reusable Insight"

    words = re.findall(r"[A-Za-z0-9']+", normalized)
    if not words:
        return "Reusable Insight"

    title_words = words[:5]
    return " ".join(word.capitalize() if word.islower() else word for word in title_words)


def _group_prompt_solutions(
    grouped_solutions: dict[str, list[str]]
) -> dict[str, list[str]]:
    merged: dict[str, list[str]] = {}

    for tier, solutions in grouped_solutions.items():
        if not solutions:
            continue
        display_label = _PROMPT_TIER_LABELS.get(tier, tier.replace("_", " ").title())
        tier_solutions = (
            solutions
            if _MAX_SOLUTIONS_PER_TIER is None
            else solutions[:_MAX_SOLUTIONS_PER_TIER]
        )
        merged.setdefault(display_label, []).extend(tier_solutions)

    ordered: dict[str, list[str]] = {}
    for label in _PROMPT_TIER_ORDER:
        if label in merged:
            ordered[label] = merged.pop(label)
    for label, solutions in merged.items():
        ordered[label] = solutions

    return ordered
