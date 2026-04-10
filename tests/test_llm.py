from unittest.mock import patch

from memgen.config import LLMConfig, LLMProvider
from memgen.llm import create_async_openai_client


def test_create_async_openai_client_passes_explicit_settings():
    with patch("memgen.llm.AsyncOpenAI") as mock_client:
        config = LLMConfig(
            provider=LLMProvider.VLLM,
            base_url="http://localhost:8000/v1",
            api_key="token",
            timeout_seconds=30,
            max_retries=5,
        )

        create_async_openai_client(config)

    mock_client.assert_called_once_with(
        api_key="token",
        base_url="http://localhost:8000/v1",
        timeout=30,
        max_retries=5,
    )


def test_create_async_openai_client_omits_unset_optional_settings():
    with patch("memgen.llm.AsyncOpenAI") as mock_client:
        create_async_openai_client(LLMConfig())

    mock_client.assert_called_once_with(max_retries=2)
