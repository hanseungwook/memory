from memgen.openai_compat import build_chat_completion_request


def test_build_chat_completion_request_uses_max_completion_tokens():
    request = build_chat_completion_request(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
    )

    assert request["max_completion_tokens"] == 128
    assert "max_tokens" not in request


def test_build_chat_completion_request_omits_temperature_for_gpt5_models():
    request = build_chat_completion_request(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
        temperature=0.7,
    )

    assert request["max_completion_tokens"] == 128
    assert "temperature" not in request


def test_build_chat_completion_request_keeps_temperature_for_non_gpt5_models():
    request = build_chat_completion_request(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=128,
        temperature=0.7,
    )

    assert request["max_completion_tokens"] == 128
    assert request["temperature"] == 0.7
