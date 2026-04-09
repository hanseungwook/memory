from __future__ import annotations

import dataclasses
import hashlib
import html
import json
import re
from pathlib import Path

from memgen.memory.prompts import MemoryItem

_STAGE_ORDER = ("generation", "scoring", "memory", "evaluation")


class ResultStore:
    """JSONL-based persistence with per-problem granularity."""

    def __init__(self, base_dir: str, domain: str):
        self.base_dir = Path(base_dir) / domain
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _ensure_dir(self, subdir: str) -> Path:
        path = self.base_dir / subdir
        path.mkdir(parents=True, exist_ok=True)
        return path

    def _append_jsonl(self, subdir: str, filename: str, data: dict) -> None:
        dir_path = self._ensure_dir(subdir)
        filepath = dir_path / filename
        with open(filepath, "a") as f:
            f.write(json.dumps(data) + "\n")

    def _load_jsonl(self, subdir: str, filename: str) -> list[dict]:
        filepath = self.base_dir / subdir / filename
        if not filepath.exists():
            return []
        records = []
        with open(filepath) as f:
            for line in f:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        return records

    def _write_json(self, filepath: Path, data: dict | list) -> None:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.write("\n")

    def _write_text(self, filepath: Path, content: str) -> None:
        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(content)

    def _artifact_root(self) -> Path:
        return self._ensure_dir("artifacts")

    def _problem_slug(self, problem_id: str) -> str:
        normalized = re.sub(r"[^A-Za-z0-9._-]+", "-", problem_id).strip("-")
        if not normalized:
            normalized = "problem"
        digest = hashlib.sha1(problem_id.encode("utf-8")).hexdigest()[:8]
        return f"{normalized}-{digest}"

    def _artifact_dir(self, problem_id: str) -> Path:
        return self._artifact_root() / self._problem_slug(problem_id)

    def _artifact_json_path(self, problem_id: str) -> Path:
        return self._artifact_dir(problem_id) / "artifact.json"

    def _artifact_markdown_path(self, problem_id: str) -> Path:
        return self._artifact_dir(problem_id) / "artifact.md"

    def _normalize_value(self, value):
        if dataclasses.is_dataclass(value):
            return dataclasses.asdict(value)
        if isinstance(value, dict):
            return {str(k): self._normalize_value(v) for k, v in value.items()}
        if isinstance(value, list):
            return [self._normalize_value(item) for item in value]
        if isinstance(value, tuple):
            return [self._normalize_value(item) for item in value]
        return value

    def _load_problem_artifact(self, problem_id: str) -> dict:
        filepath = self._artifact_json_path(problem_id)
        if not filepath.exists():
            return {}
        with open(filepath) as f:
            return json.load(f)

    def save_problem_artifact(self, problem, stage: str, data: dict) -> None:
        artifact = self._load_problem_artifact(problem.id)
        artifact["problem_id"] = problem.id
        artifact["domain"] = problem.domain
        artifact["problem"] = self._normalize_value(problem)

        stages = artifact.setdefault("stages", {})
        stages[stage] = self._normalize_value(data)

        json_path = self._artifact_json_path(problem.id)
        markdown_path = self._artifact_markdown_path(problem.id)

        self._write_json(json_path, artifact)
        self._write_text(markdown_path, self._render_problem_artifact_markdown(artifact))
        self._write_artifact_index()

    def _write_artifact_index(self) -> None:
        records = []
        for artifact_path in sorted(self._artifact_root().glob("*/artifact.json")):
            with open(artifact_path) as f:
                artifact = json.load(f)
            records.append(
                {
                    "problem_id": artifact.get("problem_id", ""),
                    "domain": artifact.get("domain", ""),
                    "stages": [
                        stage
                        for stage in _STAGE_ORDER
                        if stage in artifact.get("stages", {})
                    ],
                    "improvement": artifact.get("stages", {})
                    .get("evaluation", {})
                    .get("improvement"),
                    "path": str(artifact_path.parent),
                }
            )

        index_root = self._artifact_root()
        self._write_json(index_root / "index.json", records)
        self._write_text(index_root / "index.md", self._render_artifact_index_markdown(records))

    def _render_problem_artifact_markdown(self, artifact: dict) -> str:
        problem = artifact.get("problem", {})
        stages = artifact.get("stages", {})
        lines = [f"# Problem {artifact.get('problem_id', '')}", ""]
        lines.extend(
            [
                f"- Domain: `{artifact.get('domain', '')}`",
                "",
                "## Problem",
                "",
            ]
        )

        statement = str(problem.get("statement", "")).strip()
        if statement:
            lines.extend(["```text", statement, "```", ""])

        answer = problem.get("answer")
        if answer is not None:
            lines.extend([f"- Expected answer: `{answer}`", ""])

        starter_code = str(problem.get("starter_code") or "").strip()
        if starter_code:
            lines.extend(["### Starter Code", "", "```python", starter_code, "```", ""])

        test_cases = problem.get("test_cases") or []
        if test_cases:
            lines.extend(
                [
                    "### Test Cases",
                    "",
                    "```json",
                    json.dumps(test_cases, indent=2, ensure_ascii=False),
                    "```",
                    "",
                ]
            )

        generation = stages.get("generation")
        if generation:
            lines.extend(["## Generation", ""])
            lines.extend(self._render_prompt_section(generation))
            solutions = generation.get("solutions", [])
            if solutions:
                lines.extend(["### Outputs", ""])
                for index, solution in enumerate(solutions, start=1):
                    lines.extend(
                        self._render_details_block(
                            f"Generation {index}", str(solution).strip(), language="text"
                        )
                    )

        scoring = stages.get("scoring")
        if scoring:
            lines.extend(["## Scoring", ""])
            lines.extend(self._render_score_table(scoring.get("scores", [])))

        memory = stages.get("memory")
        if memory:
            lines.extend(["## Memory", ""])
            if memory.get("skipped"):
                reason = memory.get("skip_reason", "unspecified")
                lines.extend([f"- Skipped: `true`", f"- Reason: `{reason}`", ""])
            else:
                lines.extend(["- Skipped: `false`", ""])
            prompt = memory.get("prompt")
            if prompt:
                lines.extend(["### Prompt", ""])
                lines.extend(self._render_text_block(str(prompt), language="text"))
            grouped = memory.get("grouped_solutions") or {}
            if grouped:
                lines.extend(["### Grouped Solutions", ""])
                for tier, tier_solutions in grouped.items():
                    lines.append(f"#### Tier: `{tier}`")
                    lines.append("")
                    for index, solution in enumerate(tier_solutions, start=1):
                        lines.extend(
                            self._render_details_block(
                                f"{tier} attempt {index}",
                                str(solution).strip(),
                                language="text",
                            )
                        )
            items = memory.get("items") or []
            if items:
                lines.extend(["### Parsed Memory Items", ""])
                for index, item in enumerate(items, start=1):
                    normalized = MemoryItem.from_dict(item)
                    lines.append(f"{index}. {normalized.title}")
                    if normalized.description:
                        lines.append(f"Description: {normalized.description}")
                    if normalized.content:
                        lines.extend(
                            self._render_details_block(
                                f"Content {index}",
                                normalized.content,
                            )
                        )
                    if normalized.reasoning:
                        lines.extend(
                            self._render_details_block(
                                f"Reasoning {index}",
                                normalized.reasoning,
                            )
                        )
            raw_response = memory.get("raw_response")
            if raw_response:
                lines.extend(["### Raw Response", ""])
                lines.extend(self._render_details_block("Memory model output", str(raw_response)))

        evaluation = stages.get("evaluation")
        if evaluation:
            lines.extend(["## Evaluation", ""])
            lines.extend(
                [
                    f"- Baseline pass@1: `{evaluation.get('baseline_pass_rate', 0.0):.4f}`",
                    f"- Augmented pass@1: `{evaluation.get('augmented_pass_rate', 0.0):.4f}`",
                    f"- Improvement: `{evaluation.get('improvement', 0.0):+.4f}`",
                    "",
                ]
            )
            if evaluation.get("used_baseline_for_augmented"):
                lines.extend(
                    [
                        "- Augmented outputs reused baseline generations because no memory was available.",
                        "",
                    ]
                )
            lines.extend(["### Baseline", ""])
            lines.extend(self._render_prompt_section(evaluation.get("baseline_prompt") or {}))
            lines.extend(self._render_generation_results_section("Baseline", evaluation))

            if evaluation.get("augmented_prompt") or evaluation.get("augmented_solutions"):
                lines.extend(["### Augmented", ""])
                if evaluation.get("augmented_prompt"):
                    lines.extend(
                        self._render_prompt_section(evaluation.get("augmented_prompt") or {})
                    )
                lines.extend(self._render_generation_results_section("Augmented", evaluation))

        return "\n".join(lines).rstrip() + "\n"

    def _render_artifact_index_markdown(self, records: list[dict]) -> str:
        lines = ["# Artifact Index", "", "| Problem ID | Stages | Improvement | Path |", "| --- | --- | ---: | --- |"]
        for record in records:
            improvement = record.get("improvement")
            improvement_text = f"{improvement:+.4f}" if improvement is not None else ""
            lines.append(
                "| {problem_id} | {stages} | {improvement} | `{path}` |".format(
                    problem_id=record.get("problem_id", ""),
                    stages=", ".join(record.get("stages", [])),
                    improvement=improvement_text,
                    path=record.get("path", ""),
                )
            )
        return "\n".join(lines).rstrip() + "\n"

    def _render_prompt_section(self, prompt: dict) -> list[str]:
        lines: list[str] = []
        system_prompt = str(prompt.get("system_prompt", "")).strip()
        user_prompt = str(prompt.get("user_prompt", "")).strip()
        if system_prompt:
            lines.extend(["### System Prompt", ""])
            lines.extend(self._render_text_block(system_prompt))
        if user_prompt:
            lines.extend(["### User Prompt", ""])
            lines.extend(self._render_text_block(user_prompt))
        return lines

    def _render_generation_results_section(self, prefix: str, evaluation: dict) -> list[str]:
        lines: list[str] = []
        solutions = evaluation.get(f"{prefix.lower()}_solutions", [])
        results = evaluation.get(f"{prefix.lower()}_results", [])
        if solutions:
            lines.extend(["#### Outputs", ""])
            for index, solution in enumerate(solutions, start=1):
                lines.extend(
                    self._render_details_block(
                        f"{prefix} generation {index}",
                        str(solution).strip(),
                        language="text",
                    )
                )
        if results:
            lines.extend([f"#### {prefix} Scores", ""])
            lines.extend(self._render_score_table(results))
        return lines

    def _render_score_table(self, scores: list[dict]) -> list[str]:
        if not scores:
            return []

        lines = ["| Generation | Score | Tier |", "| --- | ---: | --- |"]
        for score in scores:
            index = score.get("generation_index", 0)
            numeric_score = float(score.get("score", 0.0))
            tier = score.get("tier", "")
            lines.append(f"| {index} | {numeric_score:.4f} | `{tier}` |")
        lines.append("")

        for score in scores:
            details = score.get("details")
            if details:
                index = score.get("generation_index", 0)
                lines.extend(
                    self._render_details_block(
                        f"Score details for generation {index}",
                        json.dumps(details, indent=2, ensure_ascii=False),
                        language="json",
                    )
                )
        return lines

    def _render_text_block(self, text: str, language: str = "text") -> list[str]:
        return [f"```{language}", text.strip(), "```", ""]

    def _render_details_block(
        self, summary: str, content: str, language: str = "text"
    ) -> list[str]:
        safe_summary = html.escape(summary, quote=True)
        return [
            "<details>",
            f"<summary>{safe_summary}</summary>",
            "",
            f"```{language}",
            content.strip(),
            "```",
            "",
            "</details>",
            "",
        ]

    def save_generation(self, problem_id: str, solutions: list[str]) -> None:
        self._append_jsonl(
            "generations",
            "generations.jsonl",
            {"problem_id": problem_id, "solutions": solutions},
        )

    def load_generations(self) -> dict[str, list[str]]:
        records = self._load_jsonl("generations", "generations.jsonl")
        result = {}
        for rec in records:
            result[rec["problem_id"]] = rec["solutions"]
        return result

    def save_scores(self, problem_id: str, scores: list[dict]) -> None:
        self._append_jsonl(
            "scores",
            "scores.jsonl",
            {"problem_id": problem_id, "scores": scores},
        )

    def load_scores(self) -> dict[str, list[dict]]:
        records = self._load_jsonl("scores", "scores.jsonl")
        result = {}
        for rec in records:
            result[rec["problem_id"]] = rec["scores"]
        return result

    def save_memory(self, problem_id: str, memory: dict) -> None:
        self._append_jsonl(
            "memories",
            "memories.jsonl",
            {"problem_id": problem_id, **memory},
        )

    def load_memories(self) -> dict[str, dict]:
        records = self._load_jsonl("memories", "memories.jsonl")
        result = {}
        for rec in records:
            pid = rec["problem_id"]
            result[pid] = {k: v for k, v in rec.items() if k != "problem_id"}
        return result

    def save_evaluation(self, problem_id: str, result: dict) -> None:
        self._append_jsonl(
            "evaluations",
            "evaluations.jsonl",
            {"problem_id": problem_id, **result},
        )

    def load_evaluations(self) -> dict[str, dict]:
        records = self._load_jsonl("evaluations", "evaluations.jsonl")
        result = {}
        for rec in records:
            pid = rec["problem_id"]
            result[pid] = {k: v for k, v in rec.items() if k != "problem_id"}
        return result

    def get_completed_ids(self, stage: str) -> set[str]:
        """Return problem IDs already processed for a given stage."""
        stage_map = {
            "generation": ("generations", "generations.jsonl"),
            "scoring": ("scores", "scores.jsonl"),
            "memory": ("memories", "memories.jsonl"),
            "evaluation": ("evaluations", "evaluations.jsonl"),
        }
        if stage not in stage_map:
            return set()
        subdir, filename = stage_map[stage]
        records = self._load_jsonl(subdir, filename)
        return {rec["problem_id"] for rec in records}
