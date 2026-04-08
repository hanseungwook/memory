from __future__ import annotations

from dataclasses import dataclass

from memgen.config import EvaluationConfig, GenerationConfig
from memgen.data.base import Problem
from memgen.evaluation.prompts import get_augmented_prompt_fn, get_baseline_prompt_fn
from memgen.memory.prompts import Memory
from memgen.scoring.base import ScoreResult


@dataclass
class EvaluationResult:
    problem_id: str
    baseline_pass_rate: float
    augmented_pass_rate: float
    improvement: float
    baseline_scores: list[float]
    augmented_scores: list[float]


@dataclass
class PromptArtifact:
    system_prompt: str
    user_prompt: str


@dataclass
class EvaluationArtifact:
    baseline_prompt: PromptArtifact
    baseline_solutions: list[str]
    baseline_results: list[ScoreResult]
    augmented_prompt: PromptArtifact | None
    augmented_solutions: list[str]
    augmented_results: list[ScoreResult]
    used_baseline_for_augmented: bool = False


@dataclass
class EvaluationRun:
    result: EvaluationResult
    artifact: EvaluationArtifact


class Evaluator:
    def __init__(self, config: EvaluationConfig, scorer):
        self.config = config
        self.scorer = scorer
        self.generator_config = GenerationConfig(
            model=config.model,
            k=config.k,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            concurrent_requests=config.k,
        )
        self._generator = None

    async def evaluate_problem(
        self, problem: Problem, memory: Memory | None
    ) -> EvaluationRun:
        baseline_prompt_fn = get_baseline_prompt_fn(problem.domain)
        baseline_system_prompt, baseline_user_prompt = baseline_prompt_fn(problem)
        baseline_prompt = PromptArtifact(
            system_prompt=baseline_system_prompt,
            user_prompt=baseline_user_prompt,
        )

        generator = self._get_generator()
        baseline_solutions = await generator.generate_k(
            problem,
            baseline_system_prompt,
            baseline_user_prompt,
            k=self.config.k,
        )
        baseline_results = [
            self.scorer.score(problem, generation_text, index)
            for index, generation_text in enumerate(baseline_solutions)
        ]
        baseline_scores = [result.score for result in baseline_results]

        if memory is None:
            augmented_prompt = None
            augmented_solutions = baseline_solutions.copy()
            augmented_results = baseline_results.copy()
            augmented_scores = baseline_scores.copy()
            used_baseline_for_augmented = True
        else:
            augmented_prompt_fn = get_augmented_prompt_fn(problem.domain)
            augmented_system_prompt, augmented_user_prompt = augmented_prompt_fn(
                problem, memory
            )
            augmented_prompt = PromptArtifact(
                system_prompt=augmented_system_prompt,
                user_prompt=augmented_user_prompt,
            )
            augmented_solutions = await generator.generate_k(
                problem,
                augmented_system_prompt,
                augmented_user_prompt,
                k=self.config.k,
            )
            augmented_results = [
                self.scorer.score(problem, generation_text, index)
                for index, generation_text in enumerate(augmented_solutions)
            ]
            augmented_scores = [result.score for result in augmented_results]
            used_baseline_for_augmented = False

        baseline_pass_rate = self._pass_at_1(baseline_scores)
        augmented_pass_rate = self._pass_at_1(augmented_scores)

        result = EvaluationResult(
            problem_id=problem.id,
            baseline_pass_rate=baseline_pass_rate,
            augmented_pass_rate=augmented_pass_rate,
            improvement=augmented_pass_rate - baseline_pass_rate,
            baseline_scores=baseline_scores,
            augmented_scores=augmented_scores,
        )
        artifact = EvaluationArtifact(
            baseline_prompt=baseline_prompt,
            baseline_solutions=baseline_solutions,
            baseline_results=baseline_results,
            augmented_prompt=augmented_prompt,
            augmented_solutions=augmented_solutions,
            augmented_results=augmented_results,
            used_baseline_for_augmented=used_baseline_for_augmented,
        )
        return EvaluationRun(result=result, artifact=artifact)

    def _get_generator(self):
        if self._generator is None:
            try:
                from memgen.generation.generator import Generator
            except ImportError as exc:
                raise ImportError(
                    "memgen.generation.generator.Generator is required for evaluation"
                ) from exc
            self._generator = Generator(self.generator_config)
        return self._generator

    @staticmethod
    def _pass_at_1(scores: list[float]) -> float:
        if not scores:
            return 0.0
        return sum(1.0 for score in scores if score == 1.0) / len(scores)
