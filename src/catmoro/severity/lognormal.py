from __future__ import annotations

from dataclasses import dataclass

from ..core.rng import RNG
from .base import SeverityModel


@dataclass(frozen=True)
class LognormalSeverity(SeverityModel):
    mu: float
    sigma: float

    def sample(self, rng: RNG, count: int) -> list[float]:
        return [rng.lognormal(self.mu, self.sigma) for _ in range(count)]
