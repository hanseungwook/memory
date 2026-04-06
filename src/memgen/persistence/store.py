import json
from pathlib import Path


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
