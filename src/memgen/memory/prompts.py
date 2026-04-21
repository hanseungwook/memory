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
    "You are an expert analyst. Extract reusable memory items from one or more "
    "tiers of solution attempts. If multiple tiers are present, use contrast; "
    "if one tier is present, mine recurring patterns. Produce cross-domain "
    "insights that transfer whenever the reasoning structure matches. Favor "
    "meta-reasoning and problem-solving techniques over problem-specific facts."
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
    domain = _resolve_domain_family(problem.domain)
    non_empty_tiers = [tier for tier, items in grouped_solutions.items() if items]
    sections = [
        "## Guidelines",
        "Analyze the solution attempts below and extract reusable memory items.",
        "Use contrast when tiers differ. If only one tier is present, mine repeated patterns within that tier.",
        "Write advice that transfers across problems, including across domains when the reasoning structure matches.",
        "",
        "## Important notes",
        "- Prioritize GENERAL META-REASONING and PROBLEM-SOLVING techniques over object-level hints.",
        "- Convert failures into positive reusable guidance.",
        "- Do NOT mention specific values, answers, variable names, or problem-specific details.",
        "- Favor fewer, stronger memories that still make sense when the surface domain changes.",
        "",
    ]
    sections.extend(_analysis_mode_guidance(non_empty_tiers))
    sections.extend(
        [
            "## Solution Pool",
            f"- Outcome tiers present: {_describe_solution_pool(non_empty_tiers)}",
            "",
        ]
    )
    sections.extend(_domain_specific_guidance(domain))
    sections.extend(
        [
        "### Problem",
        problem.statement.strip(),
        "",
        "### Solutions",
        ]
    )

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
            "First write analysis in <reasoning>, then produce one or more memory items.",
            "Each memory must be a self-contained principle, not a hint for one specific problem.",
            "Each memory item must use this schema:",
            '- "title": a short label for the memory item',
            '- "description": one sentence summary of the memory item',
            '- "content": 1-3 sentences describing the reusable insight',
            "",
            "<reasoning>Identify the patterns that support transferable advice. Use cross-tier contrasts when available; otherwise use repeated patterns within the single tier.</reasoning>",
            "",
            "<memories>",
            "<memory>",
            "<title>The title of the memory item</title>",
            "<description>One sentence summary of the memory item.</description>",
            "<content>One to three sentences describing the reusable insight.</content>",
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


def _normalize_domain(domain: str) -> str:
    return str(domain).strip().lower()


def _resolve_domain_family(domain: str) -> str:
    normalized = _normalize_domain(domain)
    aliases = {
        "math": {"math"},
        "coding": {"coding", "code", "programming"},
        "science": {"science"},
        "logic": {"logic"},
        "simulation": {"simulation", "sim"},
        "table": {"table", "tables", "tabular", "tabular_reasoning", "table_reasoning"},
    }

    for family, names in aliases.items():
        if normalized in names:
            return family

    return "generic"


def _analysis_mode_guidance(non_empty_tiers: list[str]) -> list[str]:
    if len(non_empty_tiers) >= 2:
        return [
            "## Analysis mode",
            "- Multiple outcome tiers are available. Use the gap between stronger and weaker attempts to identify what transfers.",
            "- Explain which decisions, checks, or representations separate the better attempts from the worse ones.",
            "",
        ]

    if not non_empty_tiers:
        return [
            "## Analysis mode",
            "- No scored attempts are available. If this happens, return no memories rather than fabricating evidence.",
            "",
        ]

    only_tier = non_empty_tiers[0]
    label = _PROMPT_TIER_LABELS.get(only_tier, only_tier.replace("_", " ").title())
    guidance = [
        "## Analysis mode",
        f"- Only one outcome tier is available in this batch: {label}.",
        "- Do not say the task requires contrast. Extract reusable lessons from the repeated patterns in these attempts.",
    ]

    if only_tier in {"correct", "full"}:
        guidance.extend(
            [
                "- Distill the shared moves that repeatedly worked: representation choices, decomposition, validation steps, or decision rules.",
                "- Focus on what made the successful reasoning robust, not on restating the final algorithm for this one problem.",
            ]
        )
    elif only_tier == "partial":
        guidance.extend(
            [
                "- Preserve what the attempts got right, then explain what missing step, state, or validation kept them from full completion.",
                "- Rewrite the failure mode as positive, reusable guidance for how to finish similar problems correctly.",
            ]
        )
    else:
        guidance.extend(
            [
                "- Diagnose the recurring bottlenecks, omissions, or false assumptions behind the failed attempts.",
                "- Rewrite those failure patterns as positive, reusable guidance rather than problem-specific criticism.",
            ]
        )

    guidance.append("")
    return guidance


def _describe_solution_pool(non_empty_tiers: list[str]) -> str:
    if not non_empty_tiers:
        return "none"

    labels = [
        _PROMPT_TIER_LABELS.get(tier, tier.replace("_", " ").title())
        for tier in non_empty_tiers
    ]
    return ", ".join(labels)


def _domain_specific_guidance(domain: str) -> list[str]:
    guidance_map = {
        "math": [
            "## Math-specific guidance",
            "- Name the reasoning move, not the theorem or topic.",
            "- Prefer representation, invariant, completeness, and validation moves that transfer beyond one math setting.",
            "",
        ],
        "coding": [
            "## Code-specific guidance",
            "- Name the design move, not the exact algorithm or API.",
            "- Prefer state, transition, boundary, and contract checks that transfer across implementations.",
            "",
        ],
        "science": [
            "## Science-specific guidance",
            "- Name the reasoning move, not the scientific topic or fact.",
            "- Prefer mechanism, evidence, and unit/scale checks that transfer across topics.",
            "",
        ],
        "logic": [
            "## Logic-specific guidance",
            "- Name the inference pattern, not the story or entities.",
            "- Prefer explicit constraints, consistency checks, and clean separation of forced moves from branches.",
            "",
        ],
        "simulation": [
            "## Simulation-specific guidance",
            "- Name the modeling move, not the scenario.",
            "- Prefer state, update-order, boundary, and fidelity checks that transfer across simulations.",
            "",
        ],
        "table": [
            "## Table-specific guidance",
            "- Name the data reasoning move, not the schema fields.",
            "- Prefer slice, scope, denominator, and aggregation checks that transfer across tables.",
            "",
        ],
        "generic": [
            "## Cross-domain guidance",
            "- Name a transferable reasoning move: representation choice, validation, decomposition, completeness, or scope control.",
            "- If the domain is unfamiliar or mixed, stay abstract and avoid domain-local jargon.",
            "",
        ],
    }
    return guidance_map[domain]


def build_memory_refinement_prompt(
    problem: Problem,
    grouped_solutions: dict[str, list[str]],
    previous_memory: Memory,
    iteration: int,
) -> str:
    """Build a refinement prompt that wraps the base creation prompt with feedback context."""
    base_prompt = build_memory_creation_prompt(problem, grouped_solutions)
    previous_items_text = _format_previous_memories(previous_memory)

    refinement_preamble = (
        f"## Refinement Context (Iteration {iteration})\n"
        "You previously produced the following set of memories for this problem, "
        "but they did not sufficiently improve problem-solving performance when applied. "
        "The solution pool below contains attempts that were generated USING those "
        "previous memories — analyze how the model applied (or failed to apply) them. "
        "If the pool collapses to a single outcome tier, mine the repeated patterns within "
        "that tier instead of refusing due to lack of contrast.\n\n"
        "### Previous Memories\n"
        f"{previous_items_text}\n\n"
        "### Instructions for Refinement\n"
        "- Analyze why the previous memories may not have helped, based on the solutions below.\n"
        "- Produce an IMPROVED set of memories. You may keep, revise, or discard any previous items.\n"
        "- Focus on what was MISSING or MISLEADING in the previous set.\n"
        "- The same rules apply: every memory must be generalizable and transferable.\n\n"
    )
    return refinement_preamble + base_prompt


def _format_previous_memories(memory: Memory) -> str:
    lines = []
    for i, item in enumerate(memory.items, 1):
        lines.append(f"{i}. **{item.title}**: {item.description}")
        if item.content and item.content != item.description:
            lines.append(f"   {item.content}")
    return "\n".join(lines)
