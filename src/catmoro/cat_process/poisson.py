from __future__ import annotations

from dataclasses import dataclass

from ..core.rng import RNG
from .base import CatProcess


@dataclass(frozen=True)
class PoissonProcess(CatProcess):
    rate: float

    def sample_count(self, rng: RNG, year: int) -> int:
        _ = year
        return rng.poisson(self.rate)
