from __future__ import annotations

from dataclasses import dataclass

from ..core.rng import RNG
from .base import MortalityModel


@dataclass(frozen=True)
class EventLinkedJump(MortalityModel):
    jump_prob: float

    def apply(self, event_count: int, rng: RNG) -> int:
        if event_count <= 0:
            return 0
        if rng.random() < self.jump_prob:
            return event_count + 1
        return event_count
