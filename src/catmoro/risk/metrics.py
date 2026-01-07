from __future__ import annotations


def mean(values: list[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def quantile(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    idx = int(round((len(ordered) - 1) * p))
    return ordered[idx]


def var(values: list[float], p: float) -> float:
    return quantile(values, p)


def cvar(values: list[float], p: float) -> float:
    if not values:
        return 0.0
    threshold = var(values, p)
    tail = [value for value in values if value >= threshold]
    if not tail:
        return 0.0
    return sum(tail) / len(tail)
