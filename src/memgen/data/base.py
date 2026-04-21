from dataclasses import dataclass, field


@dataclass
class Problem:
    id: str
    domain: str  # e.g. "math", "coding", "science", "logic", "simulation", "table"
    statement: str
    answer: str | None = None  # Ground truth answer for simple scalar tasks
    test_cases: list[dict] | None = None  # Optional coding tests: [{"input": ..., "output": ...}]
    starter_code: str | None = None
    metadata: dict = field(default_factory=dict)
