import base64
import json
import pickle
import zlib

from datasets import load_dataset

from memgen.config import DatasetConfig
from memgen.data.base import Problem


def _decode_test_cases(raw: str) -> list[dict]:
    """Parse test cases from JSON string.

    Handles two formats:
    1. Plain JSON string
    2. Base64+zlib+pickle encoded JSON string (for large test cases)
    """
    if not raw:
        return []

    # Try plain JSON first
    try:
        return json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        pass

    # Fall back to base64+zlib+pickle
    try:
        decoded = base64.b64decode(raw.encode("utf-8"))
        decompressed = zlib.decompress(decoded)
        return json.loads(pickle.loads(decompressed))
    except Exception:
        return []


def load_coding_problems(config: DatasetConfig | None = None) -> list[Problem]:
    """Load coding problems from HuggingFace.

    Dataset: hanseungwook/code_generation_lite
    Columns: question_id, question_content, question_title, platform,
             difficulty, starter_code, public_test_cases (JSON),
             private_test_cases (JSON), metadata (JSON)
    """
    name = "hanseungwook/code_generation_lite"
    split = "train"
    max_problems = None

    if config is not None:
        name = config.name
        split = config.split
        max_problems = config.max_problems

    ds = load_dataset(name, split=split)

    problems = []
    for row in ds:
        public_tests = _decode_test_cases(row.get("public_test_cases", ""))
        private_tests = _decode_test_cases(row.get("private_test_cases", ""))

        # Parse metadata JSON
        meta = {}
        if row.get("metadata"):
            try:
                meta = json.loads(row["metadata"])
            except (json.JSONDecodeError, TypeError):
                pass

        meta["func_name"] = meta.get("func_name")

        # Add extra fields to metadata
        meta["question_title"] = row.get("question_title", "")
        meta["platform"] = row.get("platform", "")
        meta["difficulty"] = row.get("difficulty", "")

        problem = Problem(
            id=str(row["question_id"]),
            domain="coding",
            statement=row["question_content"],
            test_cases=public_tests + private_tests,
            starter_code=row.get("starter_code") or None,
            metadata=meta,
        )
        problems.append(problem)

    if max_problems is not None:
        problems = problems[:max_problems]

    return problems
