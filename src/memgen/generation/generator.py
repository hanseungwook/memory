"""Async OpenAI generation engine."""

import asyncio

from dotenv import load_dotenv
from openai import AsyncOpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

from memgen.config import GenerationConfig
from memgen.data.base import Problem
from memgen.openai_compat import build_chat_completion_request

load_dotenv()


class Generator:
    def __init__(self, config: GenerationConfig):
        self.config = config
        self.client = AsyncOpenAI()
        self.semaphore = asyncio.Semaphore(config.concurrent_requests)

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=30))
    async def generate_one(self, messages: list[dict]) -> str:
        """Single API call with retry and concurrency control."""
        async with self.semaphore:
            response = await self.client.chat.completions.create(
                **build_chat_completion_request(
                    model=self.config.model,
                    messages=messages,
                    temperature=self.config.temperature,
                    max_tokens=self.config.max_tokens,
                )
            )
            return response.choices[0].message.content

    async def generate_k(
        self,
        problem: Problem,
        system_prompt: str,
        user_prompt: str,
        k: int | None = None,
    ) -> list[str]:
        """Generate K solutions concurrently."""
        k = k or self.config.k
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        tasks = [self.generate_one(messages) for _ in range(k)]
        return await asyncio.gather(*tasks)
