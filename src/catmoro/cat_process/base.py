from __future__ import annotations

from abc import ABC, abstractmethod

from ..core.rng import RNG


class CatProcess(ABC):
    @abstractmethod
    def sample_events(self, rng: RNG, year: int) -> list[str]:
        raise NotImplementedError
