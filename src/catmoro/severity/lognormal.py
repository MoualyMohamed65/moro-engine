from __future__ import annotations

from dataclasses import dataclass

from ..core.rng import RNG
from .base import SeverityModel


@dataclass(frozen=True)
class LognormalParams:
    mu: float
    sigma: float


@dataclass(frozen=True)
class LognormalSeverity(SeverityModel):
    mu: float
    sigma: float
    event_type_params: dict[str, LognormalParams]

    def sample(self, rng: RNG, event_types: list[str]) -> list[float]:
        losses: list[float] = []
        for event_type in event_types:
            params = self.event_type_params.get(
                event_type,
                LognormalParams(mu=self.mu, sigma=self.sigma),
            )
            losses.append(rng.lognormal(params.mu, params.sigma))
        return losses
