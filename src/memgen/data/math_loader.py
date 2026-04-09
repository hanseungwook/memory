import re

from datasets import load_dataset

from memgen.config import DatasetConfig
from memgen.data.base import Problem


def _get_first_present(row: dict, *keys: str, required: bool = True):
    for key in keys:
        if key in row and row[key] is not None:
            return row[key]

    if required:
        joined = ", ".join(keys)
        raise KeyError(f"None of the expected keys were found: {joined}")

    return None


def _parse_problem_metadata(problem_id: str) -> tuple[int | None, int | None]:
    year_match = re.match(r"(?P<year>\d{4})", problem_id)
    number_match = re.search(r"(?P<number>\d+)$", problem_id)

    year = int(year_match.group("year")) if year_match else None
    problem_number = int(number_match.group("number")) if number_match else None
    return year, problem_number


def load_math_problems(config: DatasetConfig | None = None) -> list[Problem]:
    """Load AIME problems from HuggingFace.

    Supports multiple AIME-style schemas, including:
    - gneubig/aime-1983-2024
    - Maxwell-Jia/AIME_2024
    """
    name = "gneubig/aime-1983-2024"
    split = "train"
    max_problems = None

    if config is not None:
        name = config.name
        split = config.split
        max_problems = config.max_problems

    ds = load_dataset(name, split=split)

    problems = []
    for row in ds:
        problem_id = str(_get_first_present(row, "ID", "id"))
        year, inferred_problem_number = _parse_problem_metadata(problem_id)

        problem = Problem(
            id=problem_id,
            domain="math",
            statement=_get_first_present(row, "Question", "Problem"),
            answer=str(_get_first_present(row, "Answer")),
            metadata={
                "year": _get_first_present(row, "Year", required=False) or year,
                "problem_number": _get_first_present(
                    row, "Problem_Number", "Problem Number", required=False
                ) or inferred_problem_number,
            },
        )
        problems.append(problem)

    if max_problems is not None:
        problems = problems[:max_problems]

    return problems
