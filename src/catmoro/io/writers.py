from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from ..core.types import YearResult


def summarize_results(items: Iterable[YearResult]) -> str:
    """Return CSV text for a list of per-year results."""
    lines = ["year,event_count,gross_loss,net_loss"]
    for item in items:
        lines.append(
            f"{item.year},{item.event_count},{item.gross_loss:.6f},{item.net_loss:.6f}"
        )
    return "\n".join(lines)


def write_csv(path: Path, items: Iterable[YearResult]) -> None:
    """Write results as CSV to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summarize_results(items), encoding="utf-8")
