from __future__ import annotations

from dataclasses import dataclass

from ..core.rng import RNG
from .base import MortalityModel


@dataclass(frozen=True)
class EventLinkedJump(MortalityModel):
    base_lambda: float
    jump_prob: float
    jump_lambda: float

    def sample_excess_deaths(self, event_types: list[str], rng: RNG) -> int:
        if not event_types:
            return 0
        total = 0
        for _ in event_types:
            total += rng.poisson(self.base_lambda)
            if rng.random() < self.jump_prob:
                total += rng.poisson(self.jump_lambda)
        return total
