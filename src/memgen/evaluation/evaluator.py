from __future__ import annotations

import asyncio
from dataclasses import dataclass

from memgen.config import EvaluationConfig, GenerationConfig, LLMConfig
from memgen.data.base import Problem
from memgen.evaluation.prompts import get_augmented_prompt_fn, get_baseline_prompt_fn
from memgen.memory.prompts import Memory
from memgen.request_limiter import RequestLimiter
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
    def __init__(
        self,
        config: EvaluationConfig,
        scorer,
        llm_config: LLMConfig | None = None,
        request_limiter: RequestLimiter | None = None,
    ):
        self.config = config
        self.scorer = scorer
        self.llm_config = llm_config or LLMConfig()
        self.request_limiter = request_limiter
        concurrent_requests = config.concurrent_requests or config.k
        self.generator_config = GenerationConfig(
            model=config.model,
            k=config.k,
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            extra_body=config.extra_body.copy(),
            concurrent_requests=concurrent_requests,
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
        baseline_results = await self._score_generations(problem, baseline_solutions)
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
            augmented_results = await self._score_generations(problem, augmented_solutions)
            augmented_scores = [result.score for result in augmented_results]
            used_baseline_for_augmented = False

        baseline_pass_rate = self._avg_at_k(baseline_results)
        augmented_pass_rate = self._avg_at_k(augmented_results)

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
            self._generator = Generator(
                self.generator_config,
                self.llm_config,
                request_limiter=self.request_limiter,
            )
        return self._generator

    async def _score_generations(self, problem: Problem, generations: list[str]) -> list[ScoreResult]:
        if hasattr(self.scorer, "score_batch"):
            return await asyncio.to_thread(self.scorer.score_batch, problem, generations)

        def _score_one_by_one() -> list[ScoreResult]:
            return [
                self.scorer.score(problem, generation_text, index)
                for index, generation_text in enumerate(generations)
            ]

        return await asyncio.to_thread(_score_one_by_one)

    @staticmethod
    def _avg_at_k(results: list[ScoreResult]) -> float:
        if not results:
            return 0.0
        # avg@k is the average of binarized per-sample correctness:
        # full credit counts as 1.0, everything else counts as 0.0.
        return sum(1.0 for result in results if result.score == 1.0) / len(results)
