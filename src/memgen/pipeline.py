"""Orchestrator for the Memory from Generations experiment pipeline."""

from __future__ import annotations

import asyncio
import dataclasses
import logging

from tqdm import tqdm

from memgen.config import Domain, PipelineConfig
from memgen.data.base import Problem
from memgen.evaluation.evaluator import Evaluator
from memgen.generation.generator import Generator
from memgen.generation.prompts import get_prompt_fn
from memgen.memory.creator import MemoryCreator
from memgen.memory.prompts import Memory, MemoryItem, build_memory_creation_prompt
from memgen.persistence.store import ResultStore
from memgen.scoring.base import ScoreResult
from memgen.scoring.coding_scorer import get_scorer

logger = logging.getLogger(__name__)


class Pipeline:
    def __init__(self, config: PipelineConfig):
        self.config = config
        self.store = ResultStore(config.results_dir, config.dataset.domain.value)
        self.scorer = get_scorer(config.dataset.domain.value, config.scoring)
        self.generator = Generator(config.generation)
        self.creator = MemoryCreator(config.memory)
        self.evaluator = Evaluator(config.evaluation, self.scorer)
        self.problems: list[Problem] = []

    def _load_problems(self) -> list[Problem]:
        if self.problems:
            return self.problems

        if self.config.dataset.domain == Domain.MATH:
            from memgen.data.math_loader import load_math_problems
            self.problems = load_math_problems(self.config.dataset)
        else:
            from memgen.data.coding_loader import load_coding_problems
            self.problems = load_coding_problems(self.config.dataset)

        return self.problems

    def _problems_by_id(self) -> dict[str, Problem]:
        return {p.id: p for p in self._load_problems()}

    async def run(self):
        """Full pipeline: load -> generate -> score -> create memories -> evaluate -> report."""
        await self.run_generate()
        await self.run_score()
        await self.run_memory()
        await self.run_evaluate()
        self.print_report()

    async def run_generate(self):
        """Run only the generation stage."""
        problems = self._load_problems()
        prompt_fn = get_prompt_fn(self.config.dataset.domain.value)
        completed = self.store.get_completed_ids("generation") if self.config.resume else set()

        todo = [p for p in problems if p.id not in completed]
        if not todo:
            logger.info("Generation: all %d problems already completed", len(problems))
            return

        logger.info("Generation: %d/%d problems to process", len(todo), len(problems))
        for problem in tqdm(todo, desc="Generating"):
            system_prompt, user_prompt = prompt_fn(problem)
            solutions = await self.generator.generate_k(problem, system_prompt, user_prompt)
            self.store.save_generation(problem.id, solutions)
            self.store.save_problem_artifact(
                problem,
                "generation",
                {
                    "system_prompt": system_prompt,
                    "user_prompt": user_prompt,
                    "solutions": solutions,
                },
            )

    async def run_score(self):
        """Run only the scoring stage."""
        problems_by_id = self._problems_by_id()
        generations = self.store.load_generations()
        completed = self.store.get_completed_ids("scoring") if self.config.resume else set()

        todo = {pid: gens for pid, gens in generations.items() if pid not in completed}
        if not todo:
            logger.info("Scoring: all problems already scored")
            return

        logger.info("Scoring: %d problems to score", len(todo))
        for pid, solutions in tqdm(todo.items(), desc="Scoring"):
            problem = problems_by_id[pid]
            results = self.scorer.score_batch(problem, solutions)
            score_dicts = [dataclasses.asdict(r) for r in results]
            self.store.save_scores(pid, score_dicts)
            self.store.save_problem_artifact(
                problem,
                "scoring",
                {"scores": score_dicts},
            )

    async def run_memory(self):
        """Run only the memory creation stage."""
        problems_by_id = self._problems_by_id()
        generations = self.store.load_generations()
        all_scores = self.store.load_scores()
        completed = self.store.get_completed_ids("memory") if self.config.resume else set()

        todo_ids = [pid for pid in generations if pid in all_scores and pid not in completed]
        if not todo_ids:
            logger.info("Memory: all problems already processed")
            return

        logger.info("Memory: %d problems to process", len(todo_ids))
        for pid in tqdm(todo_ids, desc="Creating memories"):
            problem = problems_by_id[pid]
            solutions = generations[pid]
            score_dicts = all_scores[pid]
            scores = [ScoreResult(**d) for d in score_dicts]

            grouped = MemoryCreator.group_solutions(solutions, scores)
            non_empty_tiers = [tier for tier, items in grouped.items() if items]
            memory_prompt = (
                build_memory_creation_prompt(problem, grouped)
                if len(non_empty_tiers) >= 2
                else None
            )
            memory = await self.creator.create_memory(problem, grouped, scores)

            if memory is None:
                self.store.save_memory(pid, {"skipped": True})
                artifact_payload = {
                    "grouped_solutions": grouped,
                    "prompt": memory_prompt,
                    "skipped": True,
                    "skip_reason": "insufficient_tiers",
                    "items": [],
                    "raw_response": None,
                }
            else:
                self.store.save_memory(pid, dataclasses.asdict(memory))
                artifact_payload = {
                    "grouped_solutions": grouped,
                    "prompt": memory_prompt,
                    "skipped": False,
                    "items": [
                        dataclasses.asdict(item)
                        for item in memory.items
                    ],
                    "raw_response": memory.raw_response,
                }
            self.store.save_problem_artifact(problem, "memory", artifact_payload)

    async def run_evaluate(self):
        """Run only the evaluation stage."""
        problems_by_id = self._problems_by_id()
        memories = self.store.load_memories()
        completed = self.store.get_completed_ids("evaluation") if self.config.resume else set()

        todo = {pid: mem for pid, mem in memories.items() if pid not in completed}
        if not todo:
            logger.info("Evaluation: all problems already evaluated")
            return

        logger.info("Evaluation: %d problems to evaluate", len(todo))
        for pid, mem_dict in tqdm(todo.items(), desc="Evaluating"):
            problem = problems_by_id[pid]

            if mem_dict.get("skipped"):
                memory = None
            else:
                items = [
                    MemoryItem(**item) if isinstance(item, dict) else item
                    for item in mem_dict.get("items", [])
                ]
                memory = Memory(
                    problem_id=mem_dict.get("problem_id", pid),
                    items=items,
                    raw_response=mem_dict.get("raw_response", ""),
                )

            evaluation_run = await self.evaluator.evaluate_problem(problem, memory)
            self.store.save_evaluation(pid, dataclasses.asdict(evaluation_run.result))
            evaluation_artifact = dataclasses.asdict(evaluation_run.artifact)
            evaluation_artifact.update(
                {
                    "baseline_pass_rate": evaluation_run.result.baseline_pass_rate,
                    "augmented_pass_rate": evaluation_run.result.augmented_pass_rate,
                    "improvement": evaluation_run.result.improvement,
                }
            )
            self.store.save_problem_artifact(problem, "evaluation", evaluation_artifact)

    def print_report(self):
        """Print aggregate statistics from completed evaluations."""
        evaluations = self.store.load_evaluations()
        if not evaluations:
            print("No evaluation results found.")
            return

        baseline_rates = []
        augmented_rates = []
        improvements = []
        helped = 0
        hurt = 0
        no_change = 0

        for result in evaluations.values():
            baseline_rates.append(result["baseline_pass_rate"])
            augmented_rates.append(result["augmented_pass_rate"])
            improvements.append(result["improvement"])
            if result["improvement"] > 0:
                helped += 1
            elif result["improvement"] < 0:
                hurt += 1
            else:
                no_change += 1

        n = len(evaluations)
        print(f"\n{'='*50}")
        print("  Memory from Generations - Results")
        print(f"{'='*50}")
        print(f"  Problems evaluated:       {n}")
        print(f"  Mean baseline pass@1:     {sum(baseline_rates)/n:.4f}")
        print(f"  Mean augmented pass@1:    {sum(augmented_rates)/n:.4f}")
        print(f"  Mean improvement:         {sum(improvements)/n:+.4f}")
        print(f"  Memory helped:            {helped} ({helped/n*100:.1f}%)")
        print(f"  Memory hurt:              {hurt} ({hurt/n*100:.1f}%)")
        print(f"  No change:                {no_change} ({no_change/n*100:.1f}%)")
        print(f"{'='*50}\n")
