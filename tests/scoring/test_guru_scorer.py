import json
from contextlib import contextmanager

from memgen.config import LLMConfig, ScoringConfig
from memgen.data.base import Problem
from memgen.scoring.guru_scorer import GuruScorer


def make_problem(problem_id: str, domain: str, statement: str, metadata: dict) -> Problem:
    return Problem(id=problem_id, domain=domain, statement=statement, metadata=metadata)


def test_scores_scalar_math_answers_from_boxed_output():
    scorer = GuruScorer(ScoringConfig())
    problem = make_problem(
        "m1",
        "math",
        "Solve it.",
        {"data_source": "math__deepscaler_preview", "ground_truth": "10^{-x}"},
    )

    result = scorer.score(problem, "Reasoning\n\\boxed{10^{-x}}", 0)

    assert result.score == 1.0
    assert result.tier == "correct"


def test_scores_codeio_json_reconstruction():
    scorer = GuruScorer(ScoringConfig())
    problem = make_problem(
        "s1",
        "simulation",
        "Predict the input.",
        {"data_source": "simulation__codeio", "ground_truth": '"input": {"start_value": 808}'},
    )

    result = scorer.score(problem, '```json\n{"input": {"start_value": 808}}\n```', 0)

    assert result.score == 1.0
    assert result.tier == "correct"


def test_scores_zebra_with_partial_credit():
    scorer = GuruScorer(ScoringConfig())
    problem = make_problem(
        "l1",
        "logic",
        "Solve the zebra puzzle.",
        {
            "data_source": "logic__zebra_puzzle_dataset",
            "ground_truth": {
                "header": ["Position", "Color"],
                "rows": [["1", "red"], ["2", "blue"]],
            },
        },
    )

    generation = """
<answer>
{"header": ["Position", "Color"], "rows": [["1", "red"], ["2", "green"]]}
</answer>
"""
    result = scorer.score(problem, generation, 0)

    assert result.score == 0.75
    assert result.tier == "partial"


def test_scores_zebra_rejects_placeholder_rows_without_crashing():
    scorer = GuruScorer(ScoringConfig())
    problem = make_problem(
        "l2",
        "logic",
        "Solve the zebra puzzle.",
        {
            "data_source": "logic__zebra_puzzle_dataset",
            "ground_truth": {
                "header": ["Position", "Color"],
                "rows": [["1", "red"], ["2", "blue"]],
            },
        },
    )

    generation = """
<answer>
{"header": ["Position", "Color"], "rows": [...]}
</answer>
"""
    result = scorer.score(problem, generation, 0)

    assert result.score == 0.0
    assert result.tier == "fail"
    assert result.details["predicted"] is None


def test_scores_arc_grids_with_partial_credit():
    scorer = GuruScorer(ScoringConfig())
    problem = make_problem(
        "a1",
        "logic",
        "Predict the output grid.",
        {
            "data_source": "simulation__arcagi1",
            "ground_truth": [[1, 2], [3, 4]],
        },
    )

    generation = "<answer>[[1, 2], [3, 0]]</answer>"
    result = scorer.score(problem, generation, 0)

    assert result.score == 0.75
    assert result.tier == "partial"


def test_scores_functional_codegen_via_assertion_harness():
    scorer = GuruScorer(ScoringConfig(timeout_seconds=5))
    problem = make_problem(
        "c1",
        "coding",
        "Double the input.",
        {
            "data_source": "codegen__leetcode2k",
            "ground_truth": json.dumps(
                {
                    "functional": (
                        "def check(candidate):\n"
                        "    assert candidate(2) == 4\n"
                        "    assert candidate(7) == 14\n\n"
                        "check(Solution().double)"
                    )
                }
            ),
            "extra_info": {},
        },
    )

    generation = """```python
class Solution:
    def double(self, x: int) -> int:
        return x * 2
```"""
    result = scorer.score(problem, generation, 0)

    assert result.score == 1.0
    assert result.tier == "full"


def test_science_fallback_uses_configured_judge_model(monkeypatch):
    calls = {}

    class DummyCompletions:
        def create(self, **kwargs):
            calls["request"] = kwargs
            message = type("Message", (), {"content": "Final Decision: Yes"})()
            choice = type("Choice", (), {"message": message})()
            return type("Response", (), {"choices": [choice]})()

    class DummyChat:
        def __init__(self):
            self.completions = DummyCompletions()

    class DummyClient:
        def __init__(self):
            self.chat = DummyChat()

    def fake_create_openai_client(config):
        calls["client_config"] = config
        return DummyClient()

    monkeypatch.setattr("memgen.scoring.guru_scorer.create_openai_client", fake_create_openai_client)

    class DummyLimiter:
        def __init__(self):
            self.acquisitions = 0

        @contextmanager
        def sync_slot(self):
            self.acquisitions += 1
            yield

    limiter = DummyLimiter()

    scorer = GuruScorer(
        ScoringConfig(),
        llm_config=LLMConfig(base_url="http://localhost:8000/v1"),
        judge_model="solver-model",
        request_limiter=limiter,
    )
    problem = make_problem(
        "sci1",
        "science",
        "Physics question.",
        {
            "data_source": "stem_web",
            "ground_truth": "F = \\frac{432m}{4913}",
            "extra_info": {"question": "What is the force?"},
        },
    )

    result = scorer.score(problem, "The force is approximately equivalent to the reference answer.", 0)

    assert result.score == 1.0
    assert result.details["judge"] == "llm"
    assert calls["client_config"].base_url == "http://localhost:8000/v1"
    assert calls["request"]["model"] == "solver-model"
    assert limiter.acquisitions == 1
