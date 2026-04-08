from __future__ import annotations

import json

from memgen.data.base import Problem
from memgen.persistence.store import ResultStore


def test_save_problem_artifact_writes_json_markdown_and_index(tmp_path):
    store = ResultStore(str(tmp_path), "math")
    problem = Problem(id="problem/1", domain="math", statement="What is 2 + 2?", answer="4")

    store.save_problem_artifact(
        problem,
        "generation",
        {
            "system_prompt": "system prompt",
            "user_prompt": "user prompt",
            "solutions": ["ANSWER: 4", "ANSWER: 5"],
        },
    )
    store.save_problem_artifact(
        problem,
        "scoring",
        {
            "scores": [
                {
                    "problem_id": "problem/1",
                    "generation_index": 0,
                    "score": 1.0,
                    "tier": "correct",
                    "details": {"expected": "4", "extracted": "4"},
                },
                {
                    "problem_id": "problem/1",
                    "generation_index": 1,
                    "score": 0.0,
                    "tier": "incorrect",
                    "details": {"expected": "4", "extracted": "5"},
                },
            ]
        },
    )
    store.save_problem_artifact(
        problem,
        "memory",
        {
            "grouped_solutions": {
                "correct": ["ANSWER: 4"],
                "incorrect": ["ANSWER: 5"],
            },
            "prompt": "Compare the successful and unsuccessful attempts.",
            "skipped": False,
            "raw_response": (
                "<reasoning>Successful attempts verified the arithmetic.</reasoning>"
                "<memories><memory>Verify simple computations before finalizing.</memory></memories>"
            ),
            "items": [
                {
                    "insight": "Verify simple computations before finalizing.",
                    "reasoning": "Successful attempts verified the arithmetic.",
                }
            ],
        },
    )
    store.save_problem_artifact(
        problem,
        "evaluation",
        {
            "baseline_pass_rate": 0.5,
            "augmented_pass_rate": 1.0,
            "improvement": 0.5,
            "baseline_prompt": {
                "system_prompt": "baseline system",
                "user_prompt": "baseline user",
            },
            "baseline_solutions": ["baseline good", "baseline bad"],
            "baseline_results": [
                {"generation_index": 0, "score": 1.0, "tier": "correct", "details": {}},
                {"generation_index": 1, "score": 0.0, "tier": "incorrect", "details": {}},
            ],
            "augmented_prompt": {
                "system_prompt": "augmented system",
                "user_prompt": "augmented user",
            },
            "augmented_solutions": ["augmented good", "augmented good"],
            "augmented_results": [
                {"generation_index": 0, "score": 1.0, "tier": "correct", "details": {}},
                {"generation_index": 1, "score": 1.0, "tier": "correct", "details": {}},
            ],
        },
    )

    artifact_json = next((tmp_path / "math" / "artifacts").rglob("artifact.json"))
    artifact_md = artifact_json.with_name("artifact.md")
    index_md = tmp_path / "math" / "artifacts" / "index.md"

    data = json.loads(artifact_json.read_text())
    markdown = artifact_md.read_text()
    index = index_md.read_text()

    assert data["problem"]["id"] == "problem/1"
    assert data["stages"]["generation"]["solutions"][0] == "ANSWER: 4"
    assert data["stages"]["evaluation"]["improvement"] == 0.5
    assert "# Problem problem/1" in markdown
    assert "## Generation" in markdown
    assert "## Memory" in markdown
    assert "## Evaluation" in markdown
    assert "problem/1" in index
    assert "+0.5000" in index
