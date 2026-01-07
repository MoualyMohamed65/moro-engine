from __future__ import annotations

from abc import ABC, abstractmethod

from ..core.rng import RNG


class MortalityModel(ABC):
    @abstractmethod
    def sample_excess_deaths(self, event_types: list[str], rng: RNG) -> int:
        raise NotImplementedError
