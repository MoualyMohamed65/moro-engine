from __future__ import annotations

from abc import ABC, abstractmethod

from ..core.rng import RNG


class MortalityModel(ABC):
    @abstractmethod
    def apply(self, event_count: int, rng: RNG) -> int:
        raise NotImplementedError
