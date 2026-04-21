from enum import Enum
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class Domain(str, Enum):
    MATH = "math"
    CODING = "coding"
    SCIENCE = "science"
    LOGIC = "logic"
    SIMULATION = "simulation"
    TABLE = "table"
    GURU = "guru"


class LLMProvider(str, Enum):
    OPENAI = "openai"
    VLLM = "vllm"


class DatasetConfig(BaseModel):
    domain: Domain
    name: str  # HuggingFace path
    split: str = "train"
    max_problems: int | None = None
    num_shards: int | None = None
    shard_index: int | None = None

    def model_post_init(self, __context: Any) -> None:
        del __context

        if self.num_shards is None and self.shard_index is None:
            return

        if self.num_shards is None or self.shard_index is None:
            raise ValueError("dataset.num_shards and dataset.shard_index must be set together")
        if self.num_shards < 1:
            raise ValueError("dataset.num_shards must be at least 1")
        if not 0 <= self.shard_index < self.num_shards:
            raise ValueError("dataset.shard_index must be in [0, dataset.num_shards)")

    @property
    def is_sharded(self) -> bool:
        return self.num_shards not in (None, 1)

    @property
    def shard_slug(self) -> str | None:
        if not self.is_sharded:
            return None
        return f"shard_{self.shard_index}_of_{self.num_shards}"


class LLMConfig(BaseModel):
    provider: LLMProvider = LLMProvider.OPENAI
    base_url: str | None = None
    api_key: str | None = None
    timeout_seconds: float | None = None
    max_retries: int = 2


class ChatCompletionConfig(BaseModel):
    model: str = "gpt-5-mini"
    temperature: float = 0.7
    max_tokens: int = 4096
    extra_body: dict[str, Any] = Field(default_factory=dict)


class GenerationConfig(ChatCompletionConfig):
    k: int = 16
    concurrent_requests: int = 16


class ScoringConfig(BaseModel):
    timeout_seconds: int = 30
    max_output_length: int = 10000


class MemoryConfig(ChatCompletionConfig):
    temperature: float = 0.3
    max_tokens: int = 2048


class EvaluationConfig(ChatCompletionConfig):
    k: int = 16
    concurrent_requests: int | None = None


class MemoryMode(str, Enum):
    SINGLE = "single"
    FEEDBACK_LOOP = "feedback_loop"


class FeedbackConfig(BaseModel):
    max_iterations: int = 5
    improvement_threshold: float = 0.0
    concurrent_problems: int = 1


class PipelineConfig(BaseModel):
    dataset: DatasetConfig
    llm: LLMConfig = Field(default_factory=LLMConfig)
    generation: GenerationConfig = Field(default_factory=GenerationConfig)
    scoring: ScoringConfig = Field(default_factory=ScoringConfig)
    memory: MemoryConfig = Field(default_factory=MemoryConfig)
    evaluation: EvaluationConfig = Field(default_factory=EvaluationConfig)
    memory_mode: MemoryMode = MemoryMode.SINGLE
    feedback: FeedbackConfig = Field(default_factory=FeedbackConfig)
    concurrent_problems: int = Field(default=1, ge=1)
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
