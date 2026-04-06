from enum import Enum
from pathlib import Path

import yaml
from pydantic import BaseModel


class Domain(str, Enum):
    MATH = "math"
    CODING = "coding"


class DatasetConfig(BaseModel):
    domain: Domain
    name: str  # HuggingFace path
    split: str = "train"
    max_problems: int | None = None


class GenerationConfig(BaseModel):
    model: str = "gpt-5-mini"
    k: int = 16
    temperature: float = 0.7
    max_tokens: int = 4096
    concurrent_requests: int = 16


class ScoringConfig(BaseModel):
    timeout_seconds: int = 30
    max_output_length: int = 10000


class MemoryConfig(BaseModel):
    model: str = "gpt-5-mini"
    temperature: float = 0.3
    max_tokens: int = 2048


class EvaluationConfig(BaseModel):
    model: str = "gpt-5-mini"
    k: int = 16
    temperature: float = 0.7
    max_tokens: int = 4096


class PipelineConfig(BaseModel):
    dataset: DatasetConfig
    generation: GenerationConfig = GenerationConfig()
    scoring: ScoringConfig = ScoringConfig()
    memory: MemoryConfig = MemoryConfig()
    evaluation: EvaluationConfig = EvaluationConfig()
    results_dir: str = "results"
    resume: bool = True


def load_config(path: str) -> PipelineConfig:
    """Load a YAML config file and merge with defaults."""
    config_path = Path(path)
    with open(config_path) as f:
        raw = yaml.safe_load(f)

    # If the YAML doesn't contain all sections, fill in defaults
    if raw is None:
        raw = {}

    return PipelineConfig(**raw)
