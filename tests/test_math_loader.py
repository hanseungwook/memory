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
