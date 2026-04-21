#!/usr/bin/env python3

from __future__ import annotations

import argparse
import asyncio
import json
import logging
from collections.abc import Iterable
from pathlib import Path

from datasets import load_dataset
from huggingface_hub import hf_hub_url, list_repo_files

from memgen.config import (
    DatasetConfig,
    Domain,
    EvaluationConfig,
    GenerationConfig,
    LLMConfig,
    LLMProvider,
    MemoryConfig,
    MemoryMode,
    PipelineConfig,
    ScoringConfig,
)
from memgen.data.base import Problem
from memgen.data.guru_loader import _row_to_problem
from memgen.pipeline import Pipeline

DEFAULT_DOMAIN_SOURCE_PREFIXES = {
    "math": "train/math__",
    "coding": "train/codegen__leetcode2k_",
    "science": "train/stem__web_",
    "logic": "train/logic__zebra_puzzle_",
    "simulation": "train/simulation__codeio_",
    "table": "train/table__hitab_",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a small Guru smoke test with 10 problems per domain."
    )
    parser.add_argument(
        "--dataset",
        default="LLM360/guru-RL-92k",
        help="Hugging Face dataset repo id.",
    )
    parser.add_argument(
        "--split",
        default="train",
        help="Dataset split to sample from.",
    )
    parser.add_argument(
        "--base-url",
        default="http://fs-mbz-gpu-574:8000/v1",
        help="OpenAI-compatible base URL for the vLLM server.",
    )
    parser.add_argument(
        "--model",
        default="MiniMaxAI/MiniMax-M2.7",
        help="Model name exposed by the vLLM server.",
    )
    parser.add_argument(
        "--api-key",
        default="token",
        help="API key sent to the OpenAI-compatible endpoint.",
    )
    parser.add_argument(
        "--per-domain",
        type=int,
        default=10,
        help="Problems to sample for each domain.",
    )
    parser.add_argument(
        "--generation-k",
        type=int,
        default=2,
        help="Initial generations per problem.",
    )
    parser.add_argument(
        "--evaluation-k",
        type=int,
        default=2,
        help="Baseline and augmented generations per problem during evaluation.",
    )
    parser.add_argument(
        "--results-root",
        default="results/guru_domain_smoke_minimax_m27",
        help="Root directory for run outputs.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from any existing per-domain results under results-root.",
    )
    return parser.parse_args()


def _resolve_repo_files(repo_id: str) -> list[str]:
    return sorted(list_repo_files(repo_id, repo_type="dataset"))


def _resolve_source_file(repo_files: Iterable[str], prefix: str) -> str:
    matches = [path for path in repo_files if path.startswith(prefix) and path.endswith(".parquet")]
    if not matches:
        raise ValueError(f"No dataset file found for prefix: {prefix}")
    return matches[0]


def _load_domain_problems(
    *,
    repo_id: str,
    source_file: str,
    expected_domain: str,
    per_domain: int,
) -> list[Problem]:
    shard_url = hf_hub_url(repo_id=repo_id, repo_type="dataset", filename=source_file)
    rows = load_dataset("parquet", data_files=shard_url, split="train", streaming=True)

    problems: list[Problem] = []
    for row_index, row in enumerate(rows):
        problem = _row_to_problem(row, row_index)
        if problem.domain != expected_domain:
            continue
        if not problem.statement.strip():
            continue
        problems.append(problem)
        if len(problems) >= per_domain:
            break

    if len(problems) < per_domain:
        raise ValueError(
            f"Only found {len(problems)} {expected_domain} problems in {source_file}; "
            f"needed {per_domain}"
        )

    return problems


def _build_config(
    *,
    dataset_name: str,
    split: str,
    base_url: str,
    model: str,
    api_key: str,
    generation_k: int,
    evaluation_k: int,
    results_dir: Path,
    resume: bool,
) -> PipelineConfig:
    return PipelineConfig(
        dataset=DatasetConfig(
            domain=Domain.GURU,
            name=dataset_name,
            split=split,
        ),
        llm=LLMConfig(
            provider=LLMProvider.VLLM,
            base_url=base_url,
            api_key=api_key,
            timeout_seconds=300,
            max_retries=2,
        ),
        generation=GenerationConfig(
            model=model,
            k=generation_k,
            temperature=1.0,
            max_tokens=4096,
            extra_body={},
            concurrent_requests=min(generation_k, 4),
        ),
        scoring=ScoringConfig(
            timeout_seconds=30,
            max_output_length=10000,
        ),
        memory=MemoryConfig(
            model=model,
            temperature=0.3,
            max_tokens=2048,
            extra_body={},
        ),
        evaluation=EvaluationConfig(
            model=model,
            k=evaluation_k,
            temperature=1.0,
            max_tokens=4096,
            extra_body={},
        ),
        memory_mode=MemoryMode.SINGLE,
        concurrent_problems=1,
        results_dir=str(results_dir),
        resume=resume,
    )


def _compute_summary(pipeline: Pipeline) -> dict[str, object]:
    evaluations = pipeline.store.load_evaluations()
    if not evaluations:
        return {
            "problems_evaluated": 0,
            "mean_baseline_avg_at_k": 0.0,
            "mean_augmented_avg_at_k": 0.0,
            "mean_improvement": 0.0,
            "helped": 0,
            "hurt": 0,
            "no_change": 0,
        }

    baseline_rates = [result["baseline_pass_rate"] for result in evaluations.values()]
    augmented_rates = [result["augmented_pass_rate"] for result in evaluations.values()]
    improvements = [result["improvement"] for result in evaluations.values()]

    helped = sum(1 for value in improvements if value > 0)
    hurt = sum(1 for value in improvements if value < 0)
    no_change = sum(1 for value in improvements if value == 0)
    total = len(evaluations)

    return {
        "problems_evaluated": total,
        "mean_baseline_avg_at_k": sum(baseline_rates) / total,
        "mean_augmented_avg_at_k": sum(augmented_rates) / total,
        "mean_improvement": sum(improvements) / total,
        "helped": helped,
        "hurt": hurt,
        "no_change": no_change,
    }


async def run_domain(
    *,
    domain: str,
    problems: list[Problem],
    source_file: str,
    args: argparse.Namespace,
    results_root: Path,
) -> dict[str, object]:
    run_dir = results_root / domain
    config = _build_config(
        dataset_name=args.dataset,
        split=args.split,
        base_url=args.base_url,
        model=args.model,
        api_key=args.api_key,
        generation_k=args.generation_k,
        evaluation_k=args.evaluation_k,
        results_dir=run_dir,
        resume=args.resume,
    )
    pipeline = Pipeline(config)
    pipeline.problems = problems

    manifest = {
        "domain": domain,
        "source_file": source_file,
        "problem_ids": [problem.id for problem in problems],
        "sources": [problem.metadata.get("data_source", "") for problem in problems],
    }
    run_dir.mkdir(parents=True, exist_ok=True)
    with open(run_dir / "selection_manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")

    logging.info("Running %s domain with %d problems", domain, len(problems))
    await pipeline.run()
    summary = _compute_summary(pipeline)
    summary["results_path"] = str(run_dir / "guru")
    return summary


async def main() -> None:
    args = parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    repo_files = _resolve_repo_files(args.dataset)
    selected: dict[str, list[Problem]] = {}
    source_files: dict[str, str] = {}

    for domain, prefix in DEFAULT_DOMAIN_SOURCE_PREFIXES.items():
        source_file = _resolve_source_file(repo_files, prefix)
        source_files[domain] = source_file
        selected[domain] = _load_domain_problems(
            repo_id=args.dataset,
            source_file=source_file,
            expected_domain=domain,
            per_domain=args.per_domain,
        )

    results_root = Path(args.results_root)
    results_root.mkdir(parents=True, exist_ok=True)

    selection_summary = {
        domain: {
            "source_file": source_files[domain],
            "count": len(problems),
            "problem_ids": [problem.id for problem in problems],
            "data_sources": [problem.metadata.get("data_source", "") for problem in problems],
        }
        for domain, problems in selected.items()
    }
    with open(results_root / "selection_summary.json", "w") as f:
        json.dump(selection_summary, f, indent=2)
        f.write("\n")

    overall_summary: dict[str, dict[str, object]] = {}
    for domain, problems in selected.items():
        summary = await run_domain(
            domain=domain,
            problems=problems,
            source_file=source_files[domain],
            args=args,
            results_root=results_root,
        )
        overall_summary[domain] = summary
        logging.info(
            "%s summary: baseline=%.4f augmented=%.4f improvement=%+.4f",
            domain,
            summary["mean_baseline_avg_at_k"],
            summary["mean_augmented_avg_at_k"],
            summary["mean_improvement"],
        )

    with open(results_root / "run_summary.json", "w") as f:
        json.dump(overall_summary, f, indent=2)
        f.write("\n")

    print(json.dumps(overall_summary, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
