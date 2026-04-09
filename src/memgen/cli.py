"""CLI for the Memory from Generations experiment system."""

import asyncio
import logging
import webbrowser
from pathlib import Path

import click

from memgen.config import load_config
from memgen.visualization import write_visualization


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


if __name__ == "__main__":
    main()
