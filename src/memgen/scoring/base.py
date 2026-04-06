from dataclasses import dataclass, field


@dataclass
class ScoreResult:
    problem_id: str
    generation_index: int
    score: float  # 0.0 or 1.0 for math; 0.0-1.0 for coding
    tier: str  # "correct"/"incorrect" for math; "fail"/"partial"/"full" for coding
    details: dict = field(default_factory=dict)
