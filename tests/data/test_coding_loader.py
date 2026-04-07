import base64
import importlib
import json
import pickle
import sys
import types
import zlib
from dataclasses import dataclass

import pytest


def _import_coding_loader(monkeypatch, load_dataset=None):
    config_stub = types.ModuleType("memgen.config")

    @dataclass
    class DatasetConfig:
        name: str = ""
        split: str = "train"
        max_problems: int | None = None

    config_stub.DatasetConfig = DatasetConfig

    datasets_stub = types.ModuleType("datasets")
    datasets_stub.load_dataset = load_dataset or (lambda *args, **kwargs: [])

    monkeypatch.setitem(sys.modules, "memgen.config", config_stub)
    monkeypatch.setitem(sys.modules, "datasets", datasets_stub)
    sys.modules.pop("memgen.data.coding_loader", None)

    return importlib.import_module("memgen.data.coding_loader")


def _encode_private_test_cases(test_cases: list[dict]) -> str:
    payload = pickle.dumps(json.dumps(test_cases))
    compressed = zlib.compress(payload)
    return base64.b64encode(compressed).decode("utf-8")


@pytest.fixture
def sample_test_cases():
    return [{"input": "1 2\n", "output": "3\n", "testtype": "stdin"}]


def test_decode_test_cases_from_plain_json(monkeypatch, sample_test_cases):
    coding_loader = _import_coding_loader(monkeypatch)

    assert coding_loader._decode_test_cases(json.dumps(sample_test_cases)) == sample_test_cases


def test_decode_test_cases_from_encoded_json_string(monkeypatch, sample_test_cases):
    coding_loader = _import_coding_loader(monkeypatch)
    encoded = _encode_private_test_cases(sample_test_cases)

    assert coding_loader._decode_test_cases(encoded) == sample_test_cases


@pytest.mark.parametrize("raw", ["", None])
def test_decode_test_cases_empty_or_missing_returns_empty_list(monkeypatch, raw):
    coding_loader = _import_coding_loader(monkeypatch)

    assert coding_loader._decode_test_cases(raw) == []


def test_load_coding_problems_preserves_func_name_and_testtype(monkeypatch):
    public_test_cases = [{"input": "2\n", "output": "4\n", "testtype": "stdin"}]
    private_test_cases = [{"input": "[1, 2, 3]", "output": "6", "testtype": "functional"}]

    row = {
        "question_id": 42,
        "question_content": "Double the number.",
        "question_title": "Double",
        "platform": "leetcode",
        "difficulty": "easy",
        "starter_code": "def solve(nums):\n    pass\n",
        "public_test_cases": json.dumps(public_test_cases),
        "private_test_cases": _encode_private_test_cases(private_test_cases),
        "metadata": json.dumps({"func_name": "solve"}),
    }

    def fake_load_dataset(*args, **kwargs):
        return [row]

    coding_loader = _import_coding_loader(monkeypatch, load_dataset=fake_load_dataset)
    problems = coding_loader.load_coding_problems()

    assert len(problems) == 1
    assert problems[0].metadata["func_name"] == "solve"
    assert problems[0].test_cases == public_test_cases + private_test_cases
