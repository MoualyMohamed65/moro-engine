from __future__ import annotations

from dataclasses import dataclass

from ..core.rng import RNG
from .base import CatProcess


@dataclass(frozen=True)
class PoissonProcess(CatProcess):
    annual_rate: float
    event_type_mix: dict[str, float]

    def sample_events(self, rng: RNG, year: int) -> list[str]:
        _ = year
        count = rng.poisson(self.annual_rate)
        if count <= 0:
            return []
        if not self.event_type_mix:
            return ["generic"] * count
        event_types = list(self.event_type_mix.keys())
        weights = list(self.event_type_mix.values())
        return [rng.choice_weighted(event_types, weights) for _ in range(count)]
