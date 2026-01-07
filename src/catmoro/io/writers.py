from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from ..core.types import YearResult


def summarize_results(items: Iterable[YearResult]) -> str:
    """Return CSV text for a list of per-year results."""
    lines = [
        "year,event_count,gross_cat_loss,gross_mortality_loss,"
        "gross_total_loss,ceded_loss,net_loss"
    ]
    for item in items:
        lines.append(
            f"{item.year},{item.event_count},"
            f"{item.gross_cat_loss:.6f},"
            f"{item.gross_mortality_loss:.6f},"
            f"{item.gross_total_loss:.6f},"
            f"{item.ceded_loss:.6f},"
            f"{item.net_loss:.6f}"
        )
    return "\n".join(lines)


def write_csv(path: Path, items: Iterable[YearResult]) -> None:
    """Write results as CSV to disk."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summarize_results(items), encoding="utf-8")
