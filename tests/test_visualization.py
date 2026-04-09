from __future__ import annotations

import json

from click.testing import CliRunner

from memgen.cli import main
from memgen.visualization import build_visualization_data, render_visualization_html


def test_build_visualization_data_merges_artifacts_and_stage_jsonl(tmp_path):
    result_root = tmp_path / "math"
    _write_jsonl(
        result_root / "scores" / "scores.jsonl",
        [
            {
                "problem_id": "1983-1",
                "scores": [
                    {
                        "generation_index": 0,
                        "score": 1.0,
                        "tier": "correct",
                        "details": {"expected": "42", "extracted": "42"},
                    },
                    {
                        "generation_index": 1,
                        "score": 0.0,
                        "tier": "incorrect",
                        "details": {"expected": "42", "extracted": "0"},
                    },
                ],
            }
        ],
    )
    _write_jsonl(
        result_root / "generations" / "generations.jsonl",
        [{"problem_id": "1983-2", "solutions": ["ANSWER: 7"]}],
    )

    artifact_dir = result_root / "artifacts" / "1983-1-example"
    artifact_dir.mkdir(parents=True)
    artifact = {
        "problem_id": "1983-1",
        "domain": "math",
        "problem": {
            "id": "1983-1",
            "domain": "math",
            "statement": "Find x.",
            "answer": "42",
        },
        "stages": {
            "generation": {
                "system_prompt": "system",
                "user_prompt": "user",
                "solutions": ["ANSWER: 42", "ANSWER: 0"],
            },
            "memory": {
                "skipped": False,
                "prompt": "compare solutions",
                "items": [
                    {
                        "title": "Validate Final Arithmetic",
                        "description": "Check the last arithmetic step before finalizing.",
                        "content": "The correct branch verified the last step instead of assuming the simplification was right.",
                        "reasoning": "The correct branch verified the last step.",
                    }
                ],
                "grouped_solutions": {
                    "correct": ["ANSWER: 42"],
                    "incorrect": ["ANSWER: 0"],
                },
                "raw_response": (
                    "<memory><title>Validate Final Arithmetic</title>"
                    "<description>Check the last arithmetic step before finalizing.</description>"
                    "<content>The correct branch verified the last step instead of assuming the simplification was right.</content></memory>"
                ),
            },
            "evaluation": {
                "baseline_pass_rate": 0.25,
                "augmented_pass_rate": 0.75,
                "improvement": 0.5,
                "baseline_solutions": ["ANSWER: 0"],
                "baseline_results": [
                    {"generation_index": 0, "score": 0.0, "tier": "incorrect"}
                ],
                "augmented_solutions": ["ANSWER: 42"],
                "augmented_results": [
                    {"generation_index": 0, "score": 1.0, "tier": "correct"}
                ],
            },
        },
    }
    (artifact_dir / "artifact.json").write_text(json.dumps(artifact), encoding="utf-8")
    (artifact_dir / "artifact.md").write_text("# Artifact\n", encoding="utf-8")

    data = build_visualization_data(result_root)
    problems = {problem["problem_id"]: problem for problem in data["problems"]}

    assert data["problem_count"] == 2
    assert data["summary"]["stage_counts"] == {
        "generation": 2,
        "scoring": 1,
        "memory": 1,
        "evaluation": 1,
    }
    assert data["summary"]["mean_improvement"] == 0.5
    assert problems["1983-1"]["available_stages"] == [
        "generation",
        "scoring",
        "memory",
        "evaluation",
    ]
    assert problems["1983-1"]["score_summary"]["count"] == 2
    assert problems["1983-1"]["memory_item_count"] == 1
    assert problems["1983-1"]["links"]["artifact_json_path"].endswith("artifact.json")
    assert problems["1983-2"]["available_stages"] == ["generation"]


def test_render_visualization_html_embeds_problem_data(tmp_path):
    result_root = tmp_path / "math"
    _write_jsonl(
        result_root / "generations" / "generations.jsonl",
        [{"problem_id": "1983-7", "solutions": ["ANSWER: 13"]}],
    )

    html = render_visualization_html(build_visualization_data(result_root))

    assert "Memgen Results Viewer" in html
    assert "1983-7" in html
    assert "Generation" in html
    assert "Evaluation" in html


def test_visualize_cli_writes_html_for_specific_result_path(tmp_path):
    result_root = tmp_path / "math"
    _write_jsonl(
        result_root / "generations" / "generations.jsonl",
        [{"problem_id": "1983-9", "solutions": ["ANSWER: 9"]}],
    )
    output_path = tmp_path / "viewer.html"

    runner = CliRunner()
    result = runner.invoke(main, ["visualize", str(result_root), "--output", str(output_path)])

    assert result.exit_code == 0, result.output
    assert output_path.exists()
    html = output_path.read_text(encoding="utf-8")
    assert "1983-9" in html
    assert "Problem Table" in html
    assert "Wrote visualization to" in result.output


def _write_jsonl(path, records):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record) + "\n")
