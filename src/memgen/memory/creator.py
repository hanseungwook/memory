from __future__ import annotations

from collections import OrderedDict

from dotenv import load_dotenv
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from memgen.config import MemoryConfig
from memgen.data.base import Problem
from memgen.memory.prompts import (
    MEMORY_SYSTEM_PROMPT,
    Memory,
    build_memory_creation_prompt,
    parse_memory_response,
)
from memgen.scoring.base import ScoreResult

load_dotenv()

_TIER_ORDER = ("correct", "incorrect", "full", "partial", "fail")


class MemoryCreator:
    def __init__(self, config: MemoryConfig):
        self.client = AsyncOpenAI()
        self.config = config

    async def create_memory(
        self,
        problem: Problem,
        grouped_solutions: dict[str, list[str]],
        scores: list[ScoreResult],
    ) -> Memory | None:
        del scores

        non_empty_tiers = [tier for tier, items in grouped_solutions.items() if items]
        if len(non_empty_tiers) < 2:
            return None

        prompt = build_memory_creation_prompt(problem, grouped_solutions)
        raw_response = await self._request_memory(prompt)
        return parse_memory_response(problem.id, raw_response)

    @staticmethod
    def group_solutions(
        solutions: list[str], scores: list[ScoreResult]
    ) -> dict[str, list[str]]:
        grouped: OrderedDict[str, list[str]] = OrderedDict()
        indexed_scores = sorted(scores, key=lambda score: score.generation_index)

        for score in indexed_scores:
            if score.generation_index < 0 or score.generation_index >= len(solutions):
                continue
            grouped.setdefault(score.tier, []).append(solutions[score.generation_index])

        ordered: OrderedDict[str, list[str]] = OrderedDict()
        for tier in _TIER_ORDER:
            if tier in grouped:
                ordered[tier] = grouped[tier]

        for tier, tier_solutions in grouped.items():
            if tier not in ordered:
                ordered[tier] = tier_solutions

        return dict(ordered)

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=8),
        reraise=True,
    )
    async def _request_memory(self, prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=self.config.model,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
            messages=[
                {"role": "system", "content": MEMORY_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
        )
        content = response.choices[0].message.content
        return content.strip() if content else ""
