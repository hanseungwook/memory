import logging
from typing import Any

from memgen.config import LLMProvider

logger = logging.getLogger(__name__)
_WARNED_TEMPERATURE_MODELS: set[str] = set()


def build_chat_completion_request(
    *,
    provider: LLMProvider | str = LLMProvider.OPENAI,
    model: str,
    messages: list[dict[str, Any]],
    max_tokens: int | None = None,
    temperature: float | None = None,
    extra_body: dict[str, Any] | None = None,
    **extra: Any,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "model": model,
        "messages": messages,
        **extra,
    }
    normalized_provider = LLMProvider(provider)

    if max_tokens is not None:
        token_field = (
            "max_completion_tokens"
            if normalized_provider == LLMProvider.OPENAI
            else "max_tokens"
        )
        request[token_field] = max_tokens

    if normalized_provider != LLMProvider.OPENAI or _supports_custom_temperature(model):
        if temperature is not None:
            request["temperature"] = temperature
    elif temperature not in (None, 1, 1.0):
        normalized_model = model.lower()
        if normalized_model not in _WARNED_TEMPERATURE_MODELS:
            logger.warning(
                "Ignoring temperature=%s for model %s because Chat Completions only "
                "supports the default temperature for this GPT-5 model.",
                temperature,
                model,
            )
            _WARNED_TEMPERATURE_MODELS.add(normalized_model)

    if extra_body:
        request["extra_body"] = extra_body

    return request


def _supports_custom_temperature(model: str) -> bool:
    return not model.lower().startswith("gpt-5")
