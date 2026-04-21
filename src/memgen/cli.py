"""CLI for the Memory from Generations experiment system."""

import asyncio
import logging
import webbrowser
from pathlib import Path

import click

from memgen.config import DatasetConfig, load_config
from memgen.visualization import write_guru_domain_plots, write_visualization


@click.group()
def main():
    """Memory from Generations experiment system."""


@main.command()
@click.option("--config", "-c", type=click.Path(exists=True), required=True, help="Path to YAML config")
@click.option("--stage", type=click.Choice(["all", "generate", "score", "memory", "evaluate"]), default="all", help="Pipeline stage to run")
@click.option("--max-problems", type=int, default=None, help="Override max problems (for testing)")
@click.option("--memory-mode", type=click.Choice(["single", "feedback_loop"]), default=None, help="Override memory mode from config")
@click.option("--num-shards", type=int, default=None, help="Override dataset shard count")
@click.option("--shard-index", type=int, default=None, help="Override dataset shard index")
@click.option(
    "--llm-provider",
    type=click.Choice(["openai", "vllm"]),
    default=None,
    help="Override llm.provider",
)
@click.option("--llm-base-url", type=str, default=None, help="Override llm.base_url")
@click.option("--llm-api-key", type=str, default=None, help="Override llm.api_key")
@click.option(
    "--model",
    type=str,
    default=None,
    help="Override generation/memory/evaluation model names together",
)
@click.option(
    "--generation-concurrent-requests",
    type=int,
    default=None,
    help="Override generation.concurrent_requests",
)
@click.option(
    "--concurrent-problems",
    type=int,
    default=None,
    help="Override pipeline concurrent_problems",
)
def run(
    config,
    stage,
    max_problems,
    memory_mode,
    num_shards,
    shard_index,
    llm_provider,
    llm_base_url,
    llm_api_key,
    model,
    generation_concurrent_requests,
    concurrent_problems,
):
    """Run the experiment pipeline."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    cfg = load_config(config)
    if max_problems is not None:
        cfg.dataset.max_problems = max_problems
    if memory_mode is not None:
        from memgen.config import MemoryMode
        cfg.memory_mode = MemoryMode(memory_mode)
    cfg.dataset = _override_dataset_sharding(cfg.dataset, num_shards, shard_index)
    cfg = _override_runtime_config(
        cfg,
        llm_provider=llm_provider,
        llm_base_url=llm_base_url,
        llm_api_key=llm_api_key,
        model=model,
        generation_concurrent_requests=generation_concurrent_requests,
        concurrent_problems=concurrent_problems,
    )

    from memgen.pipeline import Pipeline
    pipeline = Pipeline(cfg)

    stage_methods = {
        "all": pipeline.run,
        "generate": pipeline.run_generate,
        "score": pipeline.run_score,
        "memory": pipeline.run_memory,
        "evaluate": pipeline.run_evaluate,
    }
    asyncio.run(stage_methods[stage]())


@main.command()
@click.option("--config", "-c", type=click.Path(exists=True), required=True, help="Path to YAML config")
@click.option("--num-shards", type=int, default=None, help="Override dataset shard count")
@click.option("--shard-index", type=int, default=None, help="Override dataset shard index")
def report(config, num_shards, shard_index):
    """Print summary statistics from completed evaluation."""
    cfg = load_config(config)
    cfg.dataset = _override_dataset_sharding(cfg.dataset, num_shards, shard_index)

    from memgen.pipeline import Pipeline
    pipeline = Pipeline(cfg)
    pipeline.print_report()


@main.command()
@click.argument("results_path", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option(
    "--output",
    "-o",
    type=click.Path(dir_okay=False, path_type=Path),
    default=None,
    help="Where to write the HTML viewer. Defaults to <results_path>/visualization.html.",
)
@click.option(
    "--open/--no-open",
    "open_browser",
    default=False,
    help="Open the generated viewer in the default browser.",
)
def visualize(results_path: Path, output: Path | None, open_browser: bool):
    """Build a browser-based viewer for one result-set directory."""
    try:
        output_path = write_visualization(results_path, output)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc

    click.echo(f"Wrote visualization to {output_path}")
    if open_browser:
        webbrowser.open(output_path.resolve().as_uri())


@main.command("plot-domains")
@click.argument("results_path", type=click.Path(exists=True, file_okay=False, path_type=Path))
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(file_okay=False, path_type=Path),
    default=None,
    help="Where to write the domain plot assets. Defaults to <results_path>/plots/domain_summary.",
)
@click.option(
    "--open/--no-open",
    "open_browser",
    default=False,
    help="Open the generated HTML report in the default browser.",
)
def plot_domains(results_path: Path, output_dir: Path | None, open_browser: bool):
    """Build Guru domain summary plots from completed evaluation results."""
    try:
        outputs = write_guru_domain_plots(results_path, output_dir)
    except ValueError as exc:
        raise click.ClickException(str(exc)) from exc

    click.echo(f"Wrote domain plots to {outputs['html']}")
    if open_browser:
        webbrowser.open(outputs["html"].resolve().as_uri())


def _override_dataset_sharding(
    dataset: DatasetConfig,
    num_shards: int | None,
    shard_index: int | None,
) -> DatasetConfig:
    if num_shards is None and shard_index is None:
        return dataset
    if num_shards is None or shard_index is None:
        raise click.ClickException("--num-shards and --shard-index must be set together")
    data = dataset.model_dump()
    data["num_shards"] = num_shards
    data["shard_index"] = shard_index
    return DatasetConfig(**data)


def _override_runtime_config(
    cfg,
    *,
    llm_provider: str | None,
    llm_base_url: str | None,
    llm_api_key: str | None,
    model: str | None,
    generation_concurrent_requests: int | None,
    concurrent_problems: int | None,
):
    if llm_provider is not None:
        cfg.llm.provider = llm_provider
    if llm_base_url is not None:
        cfg.llm.base_url = llm_base_url
    if llm_api_key is not None:
        cfg.llm.api_key = llm_api_key
    if model is not None:
        cfg.generation.model = model
        cfg.memory.model = model
        cfg.evaluation.model = model
    if generation_concurrent_requests is not None:
        cfg.generation.concurrent_requests = generation_concurrent_requests
    if concurrent_problems is not None:
        cfg.concurrent_problems = concurrent_problems
    return cfg


if __name__ == "__main__":
    main()
