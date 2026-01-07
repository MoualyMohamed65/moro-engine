from __future__ import annotations

from collections.abc import Callable, Iterable


def grid_search(values: Iterable[float], objective: Callable[[float], float]) -> float:
    best_value = None
    best_score = None
    for value in values:
        score = objective(value)
        if best_score is None or score < best_score:
            best_score = score
            best_value = value
    if best_value is None:
        raise ValueError("grid_search received no values")
    return best_value
