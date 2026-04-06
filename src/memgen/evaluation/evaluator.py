from __future__ import annotations

from dataclasses import dataclass

from memgen.config import EvaluationConfig, GenerationConfig
from memgen.data.base import Problem
from memgen.evaluation.prompts import get_augmented_prompt_fn, get_baseline_prompt_fn
from memgen.memory.prompts import Memory


@dataclass
class EvaluationResult:
    problem_id: str
    baseline_pass_rate: float
    augmented_pass_rate: float
    improvement: float
    baseline_scores: list[float]
    augmented_scores: list[float]


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
    ) -> EvaluationResult:
        baseline_prompt_fn = get_baseline_prompt_fn(problem.domain)
        baseline_system_prompt, baseline_user_prompt = baseline_prompt_fn(problem)

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
            augmented_scores = baseline_scores.copy()
        else:
            augmented_prompt_fn = get_augmented_prompt_fn(problem.domain)
            augmented_system_prompt, augmented_user_prompt = augmented_prompt_fn(
                problem, memory
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

        baseline_pass_rate = self._pass_at_1(baseline_scores)
        augmented_pass_rate = self._pass_at_1(augmented_scores)

        return EvaluationResult(
            problem_id=problem.id,
            baseline_pass_rate=baseline_pass_rate,
            augmented_pass_rate=augmented_pass_rate,
            improvement=augmented_pass_rate - baseline_pass_rate,
            baseline_scores=baseline_scores,
            augmented_scores=augmented_scores,
        )

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
