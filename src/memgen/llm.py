from __future__ import annotations

from dotenv import load_dotenv
from openai import AsyncOpenAI

from memgen.config import LLMConfig

load_dotenv()


def create_async_openai_client(config: LLMConfig) -> AsyncOpenAI:
    client_kwargs: dict[str, object] = {
        "max_retries": config.max_retries,
    }

    if config.api_key is not None:
        client_kwargs["api_key"] = config.api_key
    if config.base_url is not None:
        client_kwargs["base_url"] = config.base_url
    if config.timeout_seconds is not None:
        client_kwargs["timeout"] = config.timeout_seconds

    return AsyncOpenAI(**client_kwargs)
