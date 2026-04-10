"""Async OpenAI generation engine."""

import asyncio

from tenacity import retry, stop_after_attempt, wait_exponential

from memgen.config import GenerationConfig, LLMConfig
from memgen.data.base import Problem
from memgen.llm import create_async_openai_client
from memgen.openai_compat import build_chat_completion_request


class Generator:
    def __init__(self, config: GenerationConfig, llm_config: LLMConfig | None = None):
        self.config = config
        self.llm_config = llm_config or LLMConfig()
        self._client = None
        self.semaphore = asyncio.Semaphore(config.concurrent_requests)

    @property
    def client(self):
        if self._client is None:
            self._client = create_async_openai_client(self.llm_config)
        return self._client

    @retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=30))
    async def generate_one(self, messages: list[dict]) -> str:
        """Single API call with retry and concurrency control."""
        async with self.semaphore:
            response = await self.client.chat.completions.create(
                **build_chat_completion_request(
                    provider=self.llm_config.provider,
                    model=self.config.model,
                    messages=messages,
                    temperature=self.config.temperature,
                    max_tokens=self.config.max_tokens,
                    extra_body=self.config.extra_body,
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
