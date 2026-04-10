import asyncio

import memgen.pipeline as pipeline_module
from memgen.config import DatasetConfig, Domain, PipelineConfig
from memgen.data.base import Problem
from memgen.pipeline import Pipeline


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
