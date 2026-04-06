from datasets import load_dataset

from memgen.config import DatasetConfig
from memgen.data.base import Problem


def load_math_problems(config: DatasetConfig | None = None) -> list[Problem]:
    """Load AIME problems from HuggingFace.

    Dataset: gneubig/aime-1983-2024
    Columns: ID (str), Year (int), Problem_Number (int), Question (str), Answer (str)
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
        problem = Problem(
            id=str(row["ID"]),
            domain="math",
            statement=row["Question"],
            answer=str(row["Answer"]),
            metadata={
                "year": row["Year"],
                "problem_number": row["Problem_Number"],
            },
        )
        problems.append(problem)

    if max_problems is not None:
        problems = problems[:max_problems]

    return problems
