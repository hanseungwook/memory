"""Orchestrator for the Memory from Generations experiment pipeline."""

from __future__ import annotations

import asyncio
import dataclasses
import logging

from tqdm import tqdm

from memgen.config import Domain, MemoryMode, PipelineConfig
from memgen.data.base import Problem
from memgen.evaluation.evaluator import EvaluationResult, Evaluator
from memgen.generation.generator import Generator
from memgen.generation.prompts import get_prompt_fn
from memgen.memory.creator import MemoryCreator
from memgen.evaluation.prompts import get_augmented_prompt_fn
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
        self.generator = Generator(config.generation, config.llm)
        self.creator = MemoryCreator(config.memory, config.llm)
        self.evaluator = Evaluator(config.evaluation, self.scorer, config.llm)
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
        if self.config.memory_mode == MemoryMode.FEEDBACK_LOOP:
            await self.run_feedback_loop()
        else:
            await self.run_generate()
            await self.run_score()
            await self.run_memory()
            await self.run_evaluate()
        self.print_report()

    async def _run_problem_batch(self, items, desc: str, worker, save_result) -> None:
        if not items:
            return

        concurrency = self.config.concurrent_problems
        if concurrency == 1:
            for item in tqdm(items, desc=desc):
                save_result(await worker(item))
            return

        semaphore = asyncio.Semaphore(concurrency)

        async def bounded(item):
            async with semaphore:
                return await worker(item)

        tasks = [asyncio.create_task(bounded(item)) for item in items]
        try:
            for future in tqdm(
                asyncio.as_completed(tasks),
                total=len(tasks),
                desc=desc,
            ):
                save_result(await future)
        except Exception:
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            raise

    async def run_generate(self):
        """Run only the generation stage."""
        problems = self._load_problems()
        prompt_fn = get_prompt_fn(self.config.dataset.domain.value)
        completed = self.store.get_completed_ids("generation") if self.config.resume else set()

        todo = [p for p in problems if p.id not in completed]
        if not todo:
            logger.info("Generation: all %d problems already completed", len(problems))
            return

        logger.info(
            "Generation: %d/%d problems to process (%d concurrent)",
            len(todo),
            len(problems),
            self.config.concurrent_problems,
        )

        async def generate_problem(problem):
            system_prompt, user_prompt = prompt_fn(problem)
            solutions = await self.generator.generate_k(problem, system_prompt, user_prompt)
            return problem, system_prompt, user_prompt, solutions

        def save_generation(result):
            problem, system_prompt, user_prompt, solutions = result
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

        await self._run_problem_batch(todo, "Generating", generate_problem, save_generation)

    async def run_score(self):
        """Run only the scoring stage."""
        problems_by_id = self._problems_by_id()
        generations = self.store.load_generations()
        completed = self.store.get_completed_ids("scoring") if self.config.resume else set()

        todo = {pid: gens for pid, gens in generations.items() if pid not in completed}
        if not todo:
            logger.info("Scoring: all problems already scored")
            return

        logger.info(
            "Scoring: %d problems to score (%d concurrent)",
            len(todo),
            self.config.concurrent_problems,
        )

        async def score_problem(item):
            pid, solutions = item
            problem = problems_by_id[pid]
            results = await asyncio.to_thread(self.scorer.score_batch, problem, solutions)
            score_dicts = [dataclasses.asdict(r) for r in results]
            return problem, pid, score_dicts

        def save_scores(result):
            problem, pid, score_dicts = result
            self.store.save_scores(pid, score_dicts)
            self.store.save_problem_artifact(
                problem,
                "scoring",
                {"scores": score_dicts},
            )

        await self._run_problem_batch(
            list(todo.items()),
            "Scoring",
            score_problem,
            save_scores,
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

        logger.info(
            "Memory: %d problems to process (%d concurrent)",
            len(todo_ids),
            self.config.concurrent_problems,
        )

        async def create_memory_for_problem(pid):
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
                memory_payload = {"skipped": True}
                artifact_payload = {
                    "grouped_solutions": grouped,
                    "prompt": memory_prompt,
                    "skipped": True,
                    "skip_reason": "insufficient_tiers",
                    "items": [],
                    "raw_response": None,
                }
            else:
                memory_payload = dataclasses.asdict(memory)
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
            return problem, pid, memory_payload, artifact_payload

        def save_memory_result(result):
            problem, pid, memory_payload, artifact_payload = result
            self.store.save_memory(pid, memory_payload)
            self.store.save_problem_artifact(problem, "memory", artifact_payload)

        await self._run_problem_batch(
            todo_ids,
            "Creating memories",
            create_memory_for_problem,
            save_memory_result,
        )

    async def run_evaluate(self):
        """Run only the evaluation stage."""
        problems_by_id = self._problems_by_id()
        memories = self.store.load_memories()
        completed = self.store.get_completed_ids("evaluation") if self.config.resume else set()

        todo = {pid: mem for pid, mem in memories.items() if pid not in completed}
        if not todo:
            logger.info("Evaluation: all problems already evaluated")
            return

        logger.info(
            "Evaluation: %d problems to evaluate (%d concurrent)",
            len(todo),
            self.config.concurrent_problems,
        )

        async def evaluate_problem_item(item):
            pid, mem_dict = item
            problem = problems_by_id[pid]

            if mem_dict.get("skipped"):
                memory = None
            else:
                items = [
                    MemoryItem.from_dict(item) if isinstance(item, dict) else item
                    for item in mem_dict.get("items", [])
                ]
                memory = Memory(
                    problem_id=mem_dict.get("problem_id", pid),
                    items=items,
                    raw_response=mem_dict.get("raw_response", ""),
                )

            evaluation_run = await self.evaluator.evaluate_problem(problem, memory)
            evaluation_result = dataclasses.asdict(evaluation_run.result)
            evaluation_artifact = dataclasses.asdict(evaluation_run.artifact)
            evaluation_artifact.update(
                {
                    "baseline_pass_rate": evaluation_run.result.baseline_pass_rate,
                    "augmented_pass_rate": evaluation_run.result.augmented_pass_rate,
                    "improvement": evaluation_run.result.improvement,
                }
            )
            return problem, pid, evaluation_result, evaluation_artifact

        def save_evaluation_result(result):
            problem, pid, evaluation_result, evaluation_artifact = result
            self.store.save_evaluation(pid, evaluation_result)
            self.store.save_problem_artifact(problem, "evaluation", evaluation_artifact)

        await self._run_problem_batch(
            list(todo.items()),
            "Evaluating",
            evaluate_problem_item,
            save_evaluation_result,
        )

    async def run_feedback_loop(self):
        """Feedback loop mode: per-problem generate -> score -> [memory -> evaluate -> refine]."""
        problems = self._load_problems()
        completed = self.store.get_completed_ids("evaluation") if self.config.resume else set()
        todo = [p for p in problems if p.id not in completed]

        if not todo:
            logger.info("Feedback loop: all %d problems already completed", len(problems))
            return

        feedback_cfg = self.config.feedback
        logger.info(
            "Feedback loop: %d/%d problems to process (max %d iterations, %d concurrent)",
            len(todo), len(problems), feedback_cfg.max_iterations, feedback_cfg.concurrent_problems,
        )

        sem = asyncio.Semaphore(feedback_cfg.concurrent_problems)
        done_count = 0

        async def bounded(problem):
            nonlocal done_count
            async with sem:
                await self._run_single_problem_loop(problem)
            done_count += 1
            logger.info("Feedback loop: completed %d/%d problems", done_count, len(todo))

        await asyncio.gather(*[bounded(p) for p in todo])

    async def _run_single_problem_loop(self, problem):
        """Run the full feedback loop for a single problem."""
        feedback_cfg = self.config.feedback
        max_iter = feedback_cfg.max_iterations
        threshold = feedback_cfg.improvement_threshold
        prompt_fn = get_prompt_fn(self.config.dataset.domain.value)

        # Step 1: Generate K initial solutions
        system_prompt, user_prompt = prompt_fn(problem)
        solutions = await self.generator.generate_k(problem, system_prompt, user_prompt)
        self.store.save_generation(problem.id, solutions)

        # Step 2: Score initial solutions
        score_results = self.scorer.score_batch(problem, solutions)
        score_dicts = [dataclasses.asdict(r) for r in score_results]
        self.store.save_scores(problem.id, score_dicts)

        # Step 3: Create initial memory from tier groupings
        grouped = MemoryCreator.group_solutions(solutions, score_results)
        memory = await self.creator.create_memory(problem, grouped, score_results)

        if memory is None:
            self.store.save_memory(problem.id, {"skipped": True})
            self.store.save_evaluation(problem.id, {
                "problem_id": problem.id,
                "baseline_pass_rate": 0.0, "augmented_pass_rate": 0.0,
                "improvement": 0.0, "baseline_scores": [], "augmented_scores": [],
            })
            return

        # Step 4: Evaluate iteration 1 — get both baseline and augmented
        eval_run = await self.evaluator.evaluate_problem(problem, memory)
        baseline_pass_rate = eval_run.result.baseline_pass_rate

        iterations = [{
            "iteration": 1,
            "baseline_pass_rate": baseline_pass_rate,
            "augmented_pass_rate": eval_run.result.augmented_pass_rate,
            "improvement": eval_run.result.improvement,
            "accepted": eval_run.result.augmented_pass_rate > baseline_pass_rate + threshold,
            "memory_items": [dataclasses.asdict(item) for item in memory.items],
        }]

        best_memory = memory
        best_augmented_rate = eval_run.result.augmented_pass_rate
        best_iteration = 1
        best_eval_result = eval_run.result

        # Check if already good enough
        if eval_run.result.augmented_pass_rate > baseline_pass_rate + threshold:
            logger.debug("Problem %s: accepted at iteration 1", problem.id)
        else:
            # Refine loop (iterations 2..max_iter)
            prev_augmented_solutions = eval_run.artifact.augmented_solutions
            prev_augmented_results = eval_run.artifact.augmented_results
            prev_memory = memory

            eval_generator = self.evaluator._get_generator()
            augmented_prompt_fn = get_augmented_prompt_fn(problem.domain)

            for iteration in range(2, max_iter + 1):
                # Build tier pool from ONLY the previous augmented solutions
                aug_score_results = [
                    ScoreResult(
                        problem_id=r.problem_id,
                        generation_index=i,
                        score=r.score,
                        tier=r.tier,
                        details=r.details,
                    )
                    for i, r in enumerate(prev_augmented_results)
                ]
                aug_grouped = MemoryCreator.group_solutions(
                    prev_augmented_solutions, aug_score_results
                )

                # Create refined memory
                refined = await self.creator.create_refined_memory(
                    problem, aug_grouped, prev_memory, iteration
                )
                if refined is None:
                    logger.debug("Problem %s: refinement returned None at iteration %d", problem.id, iteration)
                    break

                # Generate augmented-only solutions with refined memory
                aug_sys, aug_user = augmented_prompt_fn(problem, refined)
                aug_solutions = await eval_generator.generate_k(
                    problem, aug_sys, aug_user, k=self.config.evaluation.k
                )
                aug_results = [
                    self.scorer.score(problem, gen, i)
                    for i, gen in enumerate(aug_solutions)
                ]
                aug_scores = [r.score for r in aug_results]
                augmented_pass_rate = self.evaluator._avg_at_k(aug_results)
                improvement = augmented_pass_rate - baseline_pass_rate
                accepted = augmented_pass_rate > baseline_pass_rate + threshold

                iterations.append({
                    "iteration": iteration,
                    "baseline_pass_rate": baseline_pass_rate,
                    "augmented_pass_rate": augmented_pass_rate,
                    "improvement": improvement,
                    "accepted": accepted,
                    "memory_items": [dataclasses.asdict(item) for item in refined.items],
                })

                # Track best
                if augmented_pass_rate > best_augmented_rate:
                    best_memory = refined
                    best_augmented_rate = augmented_pass_rate
                    best_iteration = iteration
                    best_eval_result = EvaluationResult(
                        problem_id=problem.id,
                        baseline_pass_rate=baseline_pass_rate,
                        augmented_pass_rate=augmented_pass_rate,
                        improvement=improvement,
                        baseline_scores=eval_run.result.baseline_scores,
                        augmented_scores=aug_scores,
                    )

                if accepted:
                    logger.debug("Problem %s: accepted at iteration %d", problem.id, iteration)
                    break

                # Prepare for next iteration
                prev_augmented_solutions = aug_solutions
                prev_augmented_results = aug_results
                prev_memory = refined

        # Save final results — use the best memory across iterations
        self.store.save_memory(problem.id, dataclasses.asdict(best_memory))
        self.store.save_evaluation(problem.id, dataclasses.asdict(best_eval_result))

        # Save artifacts with iteration history
        feedback_loop_data = {
            "iterations": iterations,
            "total_iterations": len(iterations),
            "best_iteration": best_iteration,
        }
        self.store.save_problem_artifact(problem, "generation", {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "solutions": solutions,
        })
        self.store.save_problem_artifact(problem, "scoring", {"scores": score_dicts})
        self.store.save_problem_artifact(problem, "memory", {
            "grouped_solutions": grouped,
            "skipped": False,
            "items": [dataclasses.asdict(item) for item in best_memory.items],
            "raw_response": best_memory.raw_response,
            "feedback_loop": feedback_loop_data,
        })
        self.store.save_problem_artifact(problem, "evaluation", {
            "baseline_pass_rate": best_eval_result.baseline_pass_rate,
            "augmented_pass_rate": best_eval_result.augmented_pass_rate,
            "improvement": best_eval_result.improvement,
            "feedback_loop": feedback_loop_data,
        })

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
        print(f"  Mean baseline avg@k:     {sum(baseline_rates)/n:.4f}")
        print(f"  Mean augmented avg@k:    {sum(augmented_rates)/n:.4f}")
        print(f"  Mean improvement:         {sum(improvements)/n:+.4f}")
        print(f"  Memory helped:            {helped} ({helped/n*100:.1f}%)")
        print(f"  Memory hurt:              {hurt} ({hurt/n*100:.1f}%)")
        print(f"  No change:                {no_change} ({no_change/n*100:.1f}%)")
        print(f"{'='*50}\n")
