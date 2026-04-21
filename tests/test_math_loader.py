from memgen.config import DatasetConfig, Domain
from memgen.data.math_loader import load_math_problems


def test_load_math_problems_supports_default_aime_schema(monkeypatch):
    rows = [
        {
            "ID": "1983-1",
            "Year": 1983,
            "Problem Number": 1,
            "Question": "Question text",
            "Answer": "60",
        }
    ]

    monkeypatch.setattr("memgen.data.math_loader.load_dataset", lambda *args, **kwargs: rows)

    problems = load_math_problems(
        DatasetConfig(domain=Domain.MATH, name="dummy/default-aime", split="train")
    )

    assert len(problems) == 1
    assert problems[0].id == "1983-1"
    assert problems[0].statement == "Question text"
    assert problems[0].answer == "60"
    assert problems[0].metadata == {"year": 1983, "problem_number": 1}


def test_load_math_problems_supports_problem_only_schema(monkeypatch):
    rows = [
        {
            "ID": "2024-II-4",
            "Problem": "Problem text",
            "Solution": "Solution text",
            "Answer": 33,
        }
    ]

    monkeypatch.setattr("memgen.data.math_loader.load_dataset", lambda *args, **kwargs: rows)

    problems = load_math_problems(
        DatasetConfig(domain=Domain.MATH, name="dummy/problem-only-aime", split="train")
    )

    assert len(problems) == 1
    assert problems[0].id == "2024-II-4"
    assert problems[0].statement == "Problem text"
    assert problems[0].answer == "33"
    assert problems[0].metadata == {"year": 2024, "problem_number": 4}


def test_load_math_problems_supports_stable_sharding_and_per_shard_caps(monkeypatch):
    rows = [
        {
            "ID": f"1983-{index}",
            "Year": 1983,
            "Problem Number": index,
            "Question": f"Question {index}",
            "Answer": str(index),
        }
        for index in range(20)
    ]

    monkeypatch.setattr("memgen.data.math_loader.load_dataset", lambda *args, **kwargs: rows)

    shard0 = load_math_problems(
        DatasetConfig(
            domain=Domain.MATH,
            name="dummy/default-aime",
            split="train",
            num_shards=2,
            shard_index=0,
        )
    )
    shard1 = load_math_problems(
        DatasetConfig(
            domain=Domain.MATH,
            name="dummy/default-aime",
            split="train",
            num_shards=2,
            shard_index=1,
        )
    )

    shard0_ids = {problem.id for problem in shard0}
    shard1_ids = {problem.id for problem in shard1}
    all_ids = {row["ID"] for row in rows}

    assert shard0_ids.isdisjoint(shard1_ids)
    assert shard0_ids | shard1_ids == all_ids

    capped = load_math_problems(
        DatasetConfig(
            domain=Domain.MATH,
            name="dummy/default-aime",
            split="train",
            max_problems=3,
            num_shards=2,
            shard_index=0,
        )
    )

    assert len(capped) == 3
