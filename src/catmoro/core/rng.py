from __future__ import annotations

import math
import random
from collections.abc import Iterable


class RNG:
    """Small RNG wrapper to keep deterministic behavior centralized."""

    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)

    def random(self) -> float:
        return self._rng.random()

    def gauss(self, mu: float, sigma: float) -> float:
        return self._rng.gauss(mu, sigma)

    def poisson(self, rate: float) -> int:
        if rate <= 0.0:
            return 0
        threshold = math.exp(-rate)
        k = 0
        p = 1.0
        while p > threshold:
            k += 1
            p *= self._rng.random()
        return k - 1

    def lognormal(self, mu: float, sigma: float) -> float:
        return math.exp(self.gauss(mu, sigma))

    def choice(self, values: Iterable[int]) -> int:
        vals = list(values)
        return vals[self._rng.randrange(len(vals))]

    def choice_weighted(self, values: Iterable[str], weights: Iterable[float]) -> str:
        vals = list(values)
        wts = list(weights)
        if not vals:
            raise ValueError("values must be non-empty")
        if len(vals) != len(wts):
            raise ValueError("values and weights must have the same length")
        total = sum(wts)
        if total <= 0.0:
            raise ValueError("weights must sum to a positive number")
        threshold = self._rng.random() * total
        cumulative = 0.0
        for value, weight in zip(vals, wts, strict=True):
            cumulative += weight
            if threshold <= cumulative:
                return value
        return vals[-1]
