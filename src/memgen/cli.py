"""CLI for the Memory from Generations experiment system."""

import asyncio
import logging

import click

from memgen.config import load_config
from memgen.persistence.store import ResultStore


@click.group()
def main():
    """Memory from Generations experiment system."""


@main.command()
@click.option("--config", "-c", type=click.Path(exists=True), required=True, help="Path to YAML config")
@click.option("--stage", type=click.Choice(["all", "generate", "score", "memory", "evaluate"]), default="all", help="Pipeline stage to run")
@click.option("--max-problems", type=int, default=None, help="Override max problems (for testing)")
def run(config, stage, max_problems):
    """Run the experiment pipeline."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    cfg = load_config(config)
    if max_problems is not None:
        cfg.dataset.max_problems = max_problems

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
def report(config):
    """Print summary statistics from completed evaluation."""
    cfg = load_config(config)

    from memgen.pipeline import Pipeline
    pipeline = Pipeline(cfg)
    pipeline.print_report()


if __name__ == "__main__":
    main()
