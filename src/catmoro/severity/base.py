from __future__ import annotations

from abc import ABC, abstractmethod

from ..core.rng import RNG


class SeverityModel(ABC):
    @abstractmethod
    def sample(self, rng: RNG, event_types: list[str]) -> list[float]:
        raise NotImplementedError
