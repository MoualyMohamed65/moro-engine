from pathlib import Path

import typer

from .config.loader import load_config
from .engine.runner import run_simulation
from .io.writers import summarize_results

app = typer.Typer(add_completion=False)


CONFIG_OPTION = typer.Option(..., exists=True, dir_okay=False)


@app.command()
def run(config: Path = CONFIG_OPTION) -> None:
    """Run a simulation using a YAML config."""
    cfg = load_config(config)
    results = run_simulation(cfg)
    typer.echo(summarize_results(results))
