from __future__ import annotations

from .metrics import quantile


def capital_requirement(losses: list[float], p: float = 0.99) -> float:
    return quantile(losses, p)
