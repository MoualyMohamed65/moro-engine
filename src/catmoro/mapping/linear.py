from __future__ import annotations

from dataclasses import dataclass

from .base import MappingModel


@dataclass(frozen=True)
class LinearMapping(MappingModel):
    cost_per_excess_death: float

    def map_excess_deaths(self, excess_deaths: int) -> float:
        return float(excess_deaths) * self.cost_per_excess_death
