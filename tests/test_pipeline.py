import asyncio

import memgen.pipeline as pipeline_module
from memgen.config import DatasetConfig, Domain, MemoryMode, PipelineConfig
from memgen.data.base import Problem
from memgen.evaluation.evaluator import (
    EvaluationArtifact,
    EvaluationResult,
    EvaluationRun,
    PromptArtifact,
)
from memgen.pipeline import Pipeline
from memgen.scoring.base import ScoreResult


def test_run_generate_processes_multiple_problems_concurrently_in_single_mode(
    tmp_path, monkeypatch
):
    cfg = PipelineConfig(
        dataset=DatasetConfig(domain=Domain.CODING, name="dummy", max_problems=3),
        concurrent_problems=2,
        results_dir=str(tmp_path),
        resume=False,
    )
    pipeline = Pipeline(cfg)
    problems = [
        Problem(
            id=f"p{i}",
            domain="coding",
            statement=f"problem {i}",
            answer="",
            test_cases=[{"input": "1 2\n", "output": "3\n"}],
        )
        for i in range(3)
    ]
    state = {"active": 0, "max_active": 0}

    monkeypatch.setattr(pipeline, "_load_problems", lambda: problems)
    monkeypatch.setattr(
        pipeline_module,
        "get_prompt_fn",
        lambda domain: (lambda problem: ("system", problem.statement)),
    )
    monkeypatch.setattr(pipeline_module, "tqdm", lambda iterable, **kwargs: iterable)

    async def fake_generate_k(problem, system_prompt, user_prompt, k=None):
        del system_prompt, user_prompt, k
        state["active"] += 1
        state["max_active"] = max(state["max_active"], state["active"])
        try:
            await asyncio.sleep(0.01)
            return [f"solution-{problem.id}"]
        finally:
            state["active"] -= 1

    monkeypatch.setattr(pipeline.generator, "generate_k", fake_generate_k)

    asyncio.run(pipeline.run_generate())

    assert state["max_active"] == 2
    assert pipeline.store.load_generations() == {
        "p0": ["solution-p0"],
        "p1": ["solution-p1"],
        "p2": ["solution-p2"],
    }


def test_feedback_loop_uses_real_evaluation_when_memory_creation_returns_none(
    tmp_path, monkeypatch
):
    cfg = PipelineConfig(
        dataset=DatasetConfig(domain=Domain.MATH, name="dummy", max_problems=1),
        memory_mode=MemoryMode.FEEDBACK_LOOP,
        results_dir=str(tmp_path),
        resume=False,
    )
    pipeline = Pipeline(cfg)
    problem = Problem(id="p1", domain="math", statement="Compute 6*7.", answer="42")

    async def fake_generate_k(problem, system_prompt, user_prompt, k=None):
        del problem, system_prompt, user_prompt, k
        return ["ANSWER: 42", "ANSWER: 0"]

    class FakeScorer:
        def score_batch(self, problem, solutions):
            del solutions
            return [
                ScoreResult(
                    problem_id=problem.id,
                    generation_index=0,
                    score=1.0,
                    tier="correct",
                    details={},
                ),
                ScoreResult(
                    problem_id=problem.id,
                    generation_index=1,
                    score=0.0,
                    tier="incorrect",
                    details={},
                ),
            ]

    captured = {}

    async def fake_evaluate_problem(problem_arg, memory):
        assert problem_arg is problem
        captured["memory"] = memory
        return EvaluationRun(
            result=EvaluationResult(
                problem_id=problem.id,
                baseline_pass_rate=0.5,
                augmented_pass_rate=0.5,
                improvement=0.0,
                baseline_scores=[1.0, 0.0],
                augmented_scores=[1.0, 0.0],
            ),
            artifact=EvaluationArtifact(
                baseline_prompt=PromptArtifact(
                    system_prompt="baseline system",
                    user_prompt="baseline user",
                ),
                baseline_solutions=["baseline good", "baseline bad"],
                baseline_results=[
                    ScoreResult(
                        problem_id=problem.id,
                        generation_index=0,
                        score=1.0,
                        tier="correct",
                        details={},
                    ),
                    ScoreResult(
                        problem_id=problem.id,
                        generation_index=1,
                        score=0.0,
                        tier="incorrect",
                        details={},
                    ),
                ],
                augmented_prompt=None,
                augmented_solutions=["baseline good", "baseline bad"],
                augmented_results=[
                    ScoreResult(
                        problem_id=problem.id,
                        generation_index=0,
                        score=1.0,
                        tier="correct",
                        details={},
                    ),
                    ScoreResult(
                        problem_id=problem.id,
                        generation_index=1,
                        score=0.0,
                        tier="incorrect",
                        details={},
                    ),
                ],
                used_baseline_for_augmented=True,
            ),
        )

    monkeypatch.setattr(pipeline.generator, "generate_k", fake_generate_k)
    pipeline.scorer = FakeScorer()
    async def fake_create_memory(*args, **kwargs):
        del args, kwargs
        return None

    monkeypatch.setattr(pipeline.creator, "create_memory", fake_create_memory)
    monkeypatch.setattr(pipeline.evaluator, "evaluate_problem", fake_evaluate_problem)

    asyncio.run(pipeline._run_single_problem_loop(problem))

    assert captured["memory"] is None
    assert pipeline.store.load_memories() == {
        "p1": {"skipped": True, "skip_reason": "no_scored_solutions"}
    }
    assert pipeline.store.load_evaluations() == {
        "p1": {
            "baseline_pass_rate": 0.5,
            "augmented_pass_rate": 0.5,
            "improvement": 0.0,
            "baseline_scores": [1.0, 0.0],
            "augmented_scores": [1.0, 0.0],
        }
    }


def test_pipeline_uses_shard_specific_result_store_namespace(tmp_path):
    cfg = PipelineConfig(
        dataset=DatasetConfig(
            domain=Domain.GURU,
            name="dummy",
            num_shards=8,
            shard_index=3,
        ),
        results_dir=str(tmp_path),
        resume=False,
    )

    pipeline = Pipeline(cfg)

    assert pipeline.store.base_dir == tmp_path / "guru" / "shard_3_of_8"
