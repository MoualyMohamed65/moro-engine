from __future__ import annotations

import math
import random
from typing import Iterable


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
        l = math.exp(-rate)
        k = 0
        p = 1.0
        while p > l:
            k += 1
            p *= self._rng.random()
        return k - 1

    def lognormal(self, mu: float, sigma: float) -> float:
        return math.exp(self.gauss(mu, sigma))

    def choice(self, values: Iterable[int]) -> int:
        vals = list(values)
        return vals[self._rng.randrange(len(vals))]
