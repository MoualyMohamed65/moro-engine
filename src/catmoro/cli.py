from pathlib import Path

import typer

from .config.loader import load_config
from .engine.runner import run_simulation
from .io.writers import summarize_results
from .risk.metrics import cvar, mean, var

app = typer.Typer(add_completion=False)


CONFIG_OPTION = typer.Option(..., exists=True, dir_okay=False)


@app.command()
def run(config: Path = CONFIG_OPTION) -> None:
    """Run a simulation using a YAML config."""
    cfg = load_config(config)
    results = run_simulation(cfg)
    typer.echo(summarize_results(results))
    net_losses = [item.net_loss for item in results]
    mean_loss = mean(net_losses)
    p99 = var(net_losses, 0.99)
    cvar99 = cvar(net_losses, 0.99)
    typer.echo(
        f"summary_mean_net_loss={mean_loss:.6f},p99_net_loss={p99:.6f},cvar99_net_loss={cvar99:.6f}"
    )
