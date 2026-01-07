from __future__ import annotations

from abc import ABC, abstractmethod

from ..core.rng import RNG


class SeverityModel(ABC):
    @abstractmethod
    def sample(self, rng: RNG, count: int) -> list[float]:
        raise NotImplementedError
