from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Any

from datasets import load_dataset
from huggingface_hub import hf_hub_url, list_repo_files

from memgen.config import DatasetConfig
from memgen.data.base import Problem
from memgen.data.sharding import is_problem_in_shard


def load_guru_problems(config: DatasetConfig | None = None) -> list[Problem]:
    """Load Guru problems from HuggingFace with source-aware question parsing."""
    name = "LLM360/guru-RL-92k"
    split = "train"
    max_problems = None

    if config is not None:
        name = config.name
        split = config.split
        max_problems = config.max_problems

    rows = _iter_guru_rows(name, split)

    problems: list[Problem] = []
    for index, row in enumerate(rows):
        problem = _row_to_problem(row, index)
        if not is_problem_in_shard(problem.id, config):
            continue
        problems.append(problem)
        if max_problems is not None and len(problems) >= max_problems:
            break
    return problems


def _iter_guru_rows(name: str, split: str):
    if _should_fallback_to_shards(name, split):
        yield from _iter_rows_from_train_shards(name)
        return

    try:
        ds = load_dataset(name, split=split)
        yield from ds
        return
    except Exception:
        if not _should_fallback_to_shards(name, split):
            raise

    yield from _iter_rows_from_train_shards(name)


def _should_fallback_to_shards(name: str, split: str) -> bool:
    normalized_name = str(name).strip().lower()
    return normalized_name == "llm360/guru-rl-92k" and str(split).startswith("train")


def _iter_rows_from_train_shards(repo_id: str):
    parquet_files = sorted(
        file
        for file in list_repo_files(repo_id, repo_type="dataset")
        if file.startswith("train/") and file.endswith(".parquet")
    )

    for parquet_file in parquet_files:
        shard_url = hf_hub_url(repo_id=repo_id, repo_type="dataset", filename=parquet_file)
        shard = load_dataset("parquet", data_files=shard_url, split="train", streaming=True)
        yield from shard


def _row_to_problem(row: dict[str, Any], fallback_index: int) -> Problem:
    data_source = str(row.get("data_source") or "").strip()
    domain = _infer_domain(row)
    extra_info = _to_jsonable(row.get("extra_info") or {})
    meta = _to_jsonable(row.get("meta") or {})
    reward_model = _to_jsonable(row.get("reward_model") or {})
    prompt_messages = _to_jsonable(row.get("prompt") or [])
    query = row.get("query")
    prompt_content = _extract_prompt_content(prompt_messages)
    statement = _extract_statement(
        data_source=data_source,
        domain=domain,
        query=query,
        prompt_content=prompt_content,
        extra_info=extra_info,
        meta=meta,
    )

    source_key = (
        extra_info.get("index")
        or extra_info.get("id")
        or extra_info.get("idx")
        or meta.get("question_id")
        or meta.get("id")
        or row.get("task_id")
        or fallback_index
    )
    problem_id = str(row.get("task_id") or f"{data_source}:{source_key}")

    metadata = {
        "data_source": data_source,
        "ability": str(row.get("ability") or "").strip().lower(),
        "apply_chat_template": bool(row.get("apply_chat_template")),
        "entry_point": _to_jsonable(row.get("entry_point")),
        "test": _to_jsonable(row.get("test")),
        "input_output": _to_jsonable(row.get("input_output")),
        "query": _to_jsonable(query),
        "prompt_messages": prompt_messages,
        "source_prompt": prompt_content,
        "source_meta": meta,
        "extra_info": extra_info,
        "reward_model": reward_model,
        "ground_truth": reward_model.get("ground_truth"),
    }

    starter_code = _extract_starter_code(data_source, meta)
    func_name = _extract_func_name(data_source, metadata)
    if func_name:
        metadata["func_name"] = func_name
    if starter_code:
        metadata["starter_code_source"] = "meta.lang_code"

    return Problem(
        id=problem_id,
        domain=domain,
        statement=statement,
        starter_code=starter_code,
        metadata=metadata,
    )


def _infer_domain(row: dict[str, Any]) -> str:
    data_source = str(row.get("data_source") or "").strip().lower()
    ability = str(row.get("ability") or "").strip().lower()

    if data_source.startswith("codegen__"):
        return "coding"
    if data_source.startswith("math__"):
        return "math"
    if data_source.startswith("table__"):
        return "table"
    if data_source.startswith("stem__") or data_source.startswith("stem_"):
        return "science"
    if data_source.startswith("simulation__codeio"):
        return "simulation"
    if data_source.startswith("logic__"):
        return "logic"
    if data_source.startswith(("simulation__arcagi", "simulation__barc")):
        return "logic"

    if ability in {"codegen"}:
        return "coding"
    if ability in {"math"}:
        return "math"
    if ability in {"qa"}:
        return "science"
    if ability in {"table"}:
        return "table"
    if ability in {"coding-inference"}:
        return "simulation"
    if ability in {"logical_reasoning", "reasoning"}:
        return "logic"

    return "generic"


def _extract_statement(
    *,
    data_source: str,
    domain: str,
    query: Any,
    prompt_content: str,
    extra_info: dict[str, Any],
    meta: dict[str, Any],
) -> str:
    if domain == "coding":
        return _extract_coding_statement(data_source, query, prompt_content, extra_info, meta)

    if isinstance(query, str) and query.strip():
        return query.strip()

    if prompt_content:
        return prompt_content.strip()

    if domain == "math" and extra_info.get("original_question"):
        return str(extra_info["original_question"]).strip()
    if domain == "science" and extra_info.get("question"):
        return str(extra_info["question"]).strip()

    return ""


def _extract_coding_statement(
    data_source: str,
    query: Any,
    prompt_content: str,
    extra_info: dict[str, Any],
    meta: dict[str, Any],
) -> str:
    question_title = (
        extra_info.get("question_title")
        or meta.get("question_title")
        or meta.get("question")
    )
    if data_source.startswith("codegen__leetcode") and question_title:
        return str(question_title).strip()

    raw = ""
    if isinstance(query, str) and query.strip():
        raw = query.strip()
    elif prompt_content:
        raw = prompt_content.strip()
    elif extra_info.get("original_prompt"):
        raw = str(extra_info["original_prompt"]).strip()

    if not raw:
        return ""

    if "### Question:\n" in raw:
        raw = raw.split("### Question:\n", 1)[1]
    elif "Below is the question:\n\n" in raw:
        raw = raw.split("Below is the question:\n\n", 1)[1]
    elif raw.startswith("Solve the following coding problem using the programming language python:\n\n"):
        raw = raw.split(
            "Solve the following coding problem using the programming language python:\n\n",
            1,
        )[1]
    elif raw.startswith("Solve the programming task below in a Python markdown code block.\n"):
        raw = raw.split(
            "Solve the programming task below in a Python markdown code block.\n",
            1,
        )[1]

    for marker in (
        "\n\n### Format:",
        "\n\nRead the inputs from stdin solve the problem and write the answer to stdout",
        "\n\nThe input will be stdin and you should print your solution to stdout",
        "\n\nNow solve the problem and return the code.",
    ):
        if marker in raw:
            raw = raw.split(marker, 1)[0]

    return raw.strip()


def _extract_starter_code(data_source: str, meta: dict[str, Any]) -> str | None:
    if not data_source.startswith("codegen__"):
        return None
    lang_code = meta.get("lang_code")
    if isinstance(lang_code, str) and lang_code.strip():
        return lang_code.rstrip()
    return None


def _extract_func_name(data_source: str, metadata: dict[str, Any]) -> str | None:
    if not data_source.startswith("codegen__"):
        return None

    entry_point = metadata.get("entry_point")
    if isinstance(entry_point, str) and entry_point.strip():
        raw = entry_point.strip()
        if raw.endswith(")"):
            raw = raw[:-1]
        if "." in raw:
            raw = raw.rsplit(".", 1)[-1]
        return raw.strip() or None

    function_name = metadata.get("extra_info", {}).get("function_name")
    if isinstance(function_name, str) and function_name.strip():
        return function_name.strip()
    return None


def _extract_prompt_content(prompt_messages: list[dict[str, Any]]) -> str:
    for message in prompt_messages:
        if isinstance(message, dict) and message.get("role") == "user":
            content = message.get("content")
            if isinstance(content, str) and content.strip():
                return content
    return ""


def _to_jsonable(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _to_jsonable(inner) for key, inner in value.items()}
    if isinstance(value, list):
        return [_to_jsonable(inner) for inner in value]
    if isinstance(value, tuple):
        return [_to_jsonable(inner) for inner in value]
    if isinstance(value, (datetime, date)):
        return value.isoformat()
    if isinstance(value, Decimal):
        return str(value)
    return value
