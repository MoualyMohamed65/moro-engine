from __future__ import annotations

from dataclasses import dataclass

from .base import MappingModel


@dataclass(frozen=True)
class LinearMapping(MappingModel):
    factor: float
    intercept: float

    def map_severity(self, losses: list[float]) -> list[float]:
        return [self.factor * loss + self.intercept for loss in losses]
