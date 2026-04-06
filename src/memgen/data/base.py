from dataclasses import dataclass, field


@dataclass
class Problem:
    id: str
    domain: str  # "math" or "coding"
    statement: str
    answer: str | None = None  # Ground truth for math
    test_cases: list[dict] | None = None  # For coding: [{"input": ..., "output": ...}]
    starter_code: str | None = None
    metadata: dict = field(default_factory=dict)
