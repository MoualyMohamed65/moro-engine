from __future__ import annotations

from abc import ABC, abstractmethod


class MappingModel(ABC):
    @abstractmethod
    def map_severity(self, losses: list[float]) -> list[float]:
        raise NotImplementedError
