from __future__ import annotations

from abc import ABC, abstractmethod


class MappingModel(ABC):
    @abstractmethod
    def map_excess_deaths(self, excess_deaths: int) -> float:
        raise NotImplementedError
