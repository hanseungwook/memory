import json

from memgen.config import DatasetConfig, Domain
from memgen.data.guru_loader import load_guru_problems


def test_load_guru_problems_parses_mixed_sources(monkeypatch):
    rows = [
        {
            "data_source": "math__deepscaler_preview",
            "ability": "math",
            "prompt": [
                {
                    "role": "user",
                    "content": "Window problem. Please output the final answer within \\boxed{}.",
                }
            ],
            "query": None,
            "extra_info": {"index": 1, "original_question": "Window problem."},
            "reward_model": {"ground_truth": "26", "style": "rule"},
            "meta": {},
            "entry_point": None,
            "test": None,
            "input_output": None,
            "apply_chat_template": True,
        },
        {
            "data_source": "codegen__livecodebench",
            "ability": "codegen",
            "prompt": [
                {
                    "role": "user",
                    "content": (
                        "You are an expert Python programmer.\n\nBelow is the question:\n\n"
                        "Add two integers.\n\nRead the inputs from stdin solve the problem "
                        "and write the answer to stdout."
                    ),
                }
            ],
            "query": None,
            "extra_info": {"index": 0, "original_prompt": "ignored"},
            "reward_model": {
                "ground_truth": json.dumps({"inputs": ["1 2\n"], "outputs": ["3\n"]}),
                "style": "rule",
            },
            "meta": {},
            "entry_point": None,
            "test": None,
            "input_output": None,
            "apply_chat_template": True,
        },
        {
            "data_source": "codegen__leetcode2k",
            "ability": "codegen",
            "prompt": [{"role": "user", "content": "ignored"}],
            "query": None,
            "extra_info": {"index": 9, "question_title": "Implement isMatch."},
            "reward_model": {
                "ground_truth": json.dumps(
                    {
                        "functional": "def check(candidate):\n    assert candidate(2) == 4\ncheck(Solution().double)"
                    }
                ),
                "style": "rule",
            },
            "meta": {"lang_code": "class Solution:\n    def double(self, x: int) -> int:\n        "},
            "entry_point": "Solution().double",
            "test": None,
            "input_output": None,
            "apply_chat_template": True,
        },
        {
            "data_source": "logic__zebra_puzzle_dataset",
            "ability": "logical_reasoning",
            "prompt": [{"role": "user", "content": "Solve the puzzle and answer in <answer> tags."}],
            "query": None,
            "extra_info": {"id": "2767"},
            "reward_model": {"ground_truth": {"header": ["Position"], "rows": [["1"]]}, "style": "rule"},
            "meta": {},
            "entry_point": None,
            "test": None,
            "input_output": None,
            "apply_chat_template": True,
        },
    ]

    monkeypatch.setattr("memgen.data.guru_loader.load_dataset", lambda *args, **kwargs: rows)

    problems = load_guru_problems(
        DatasetConfig(domain=Domain.GURU, name="dummy/guru-fixture", split="train")
    )

    assert [problem.domain for problem in problems] == ["math", "coding", "coding", "logic"]

    assert problems[0].id == "math__deepscaler_preview:1"
    assert problems[0].statement == "Window problem. Please output the final answer within \\boxed{}."
    assert problems[0].metadata["ground_truth"] == "26"

    assert problems[1].statement == "Add two integers."
    assert "Read the inputs from stdin" not in problems[1].statement

    assert problems[2].statement == "Implement isMatch."
    assert problems[2].starter_code == "class Solution:\n    def double(self, x: int) -> int:"
    assert problems[2].metadata["func_name"] == "double"

    assert problems[3].statement == "Solve the puzzle and answer in <answer> tags."
    assert problems[3].id == "logic__zebra_puzzle_dataset:2767"


def test_load_guru_problems_falls_back_to_train_shards_on_schema_mismatch(monkeypatch):
    calls = []

    def fake_load_dataset(name, *args, **kwargs):
        calls.append((name, kwargs))
        if name == "LLM360/guru-RL-92k":
            raise RuntimeError("schema mismatch")
        assert name == "parquet"
        return [
            {
                "data_source": "math__deepscaler_preview",
                "ability": "math",
                "prompt": [{"role": "user", "content": "Shard question."}],
                "query": None,
                "extra_info": {"index": 7},
                "reward_model": {"ground_truth": "5", "style": "rule"},
                "meta": {},
                "entry_point": None,
                "test": None,
                "input_output": None,
                "apply_chat_template": True,
            }
        ]

    monkeypatch.setattr("memgen.data.guru_loader.load_dataset", fake_load_dataset)
    monkeypatch.setattr(
        "memgen.data.guru_loader.list_repo_files",
        lambda *args, **kwargs: ["train/math__combined_54.4k.parquet"],
    )
    monkeypatch.setattr(
        "memgen.data.guru_loader.hf_hub_url",
        lambda **kwargs: f"https://example.com/{kwargs['filename']}",
    )

    problems = load_guru_problems(
        DatasetConfig(domain=Domain.GURU, name="LLM360/guru-RL-92k", split="train")
    )

    assert len(problems) == 1
    assert problems[0].statement == "Shard question."
    assert problems[0].id == "math__deepscaler_preview:7"
    assert calls[0][0] == "parquet"


def test_load_guru_problems_supports_stable_sharding(monkeypatch):
    rows = [
        {
            "data_source": "math__deepscaler_preview",
            "ability": "math",
            "prompt": [{"role": "user", "content": f"Question {index}"}],
            "query": None,
            "extra_info": {"index": index},
            "reward_model": {"ground_truth": str(index), "style": "rule"},
            "meta": {},
            "entry_point": None,
            "test": None,
            "input_output": None,
            "apply_chat_template": True,
        }
        for index in range(12)
    ]

    monkeypatch.setattr("memgen.data.guru_loader.load_dataset", lambda *args, **kwargs: rows)

    shard0 = load_guru_problems(
        DatasetConfig(
            domain=Domain.GURU,
            name="dummy/guru-fixture",
            split="train",
            num_shards=2,
            shard_index=0,
        )
    )
    shard1 = load_guru_problems(
        DatasetConfig(
            domain=Domain.GURU,
            name="dummy/guru-fixture",
            split="train",
            num_shards=2,
            shard_index=1,
        )
    )

    shard0_ids = {problem.id for problem in shard0}
    shard1_ids = {problem.id for problem in shard1}
    all_ids = {f"math__deepscaler_preview:{index}" for index in range(12)}

    assert shard0_ids.isdisjoint(shard1_ids)
    assert shard0_ids | shard1_ids == all_ids
