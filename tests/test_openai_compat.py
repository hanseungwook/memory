from memgen.config import LLMProvider
from memgen.openai_compat import build_chat_completion_request


def test_build_chat_completion_request_uses_max_completion_tokens():
    request = build_chat_completion_request(
        provider=LLMProvider.OPENAI,
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
    )

    assert request["max_completion_tokens"] == 128
    assert "max_tokens" not in request


def test_build_chat_completion_request_omits_temperature_for_gpt5_models():
    request = build_chat_completion_request(
        provider=LLMProvider.OPENAI,
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
        temperature=0.7,
    )

    assert request["max_completion_tokens"] == 128
    assert "temperature" not in request


def test_build_chat_completion_request_keeps_temperature_for_non_gpt5_models():
    request = build_chat_completion_request(
        provider=LLMProvider.OPENAI,
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
        temperature=0.7,
    )

    assert request["max_completion_tokens"] == 128
    assert request["temperature"] == 0.7


def test_build_chat_completion_request_uses_max_tokens_for_vllm():
    request = build_chat_completion_request(
        provider=LLMProvider.VLLM,
        model="Qwen/Qwen3-32B",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
    )

    assert request["max_tokens"] == 128
    assert "max_completion_tokens" not in request


def test_build_chat_completion_request_keeps_temperature_for_vllm_models():
    request = build_chat_completion_request(
        provider=LLMProvider.VLLM,
        model="gpt-5-compatible-local-model",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
        temperature=0.7,
    )

    assert request["max_tokens"] == 128
    assert request["temperature"] == 0.7


def test_build_chat_completion_request_passes_extra_body_through():
    request = build_chat_completion_request(
        provider=LLMProvider.VLLM,
        model="Qwen/Qwen3-32B",
        messages=[{"role": "user", "content": "Hi"}],
        extra_body={"top_k": 20},
    )

    assert request["extra_body"] == {"top_k": 20}
