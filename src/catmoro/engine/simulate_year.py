from __future__ import annotations

from ..cat_process.base import CatProcess
from ..core.rng import RNG
from ..core.types import YearResult
from ..insurance.program import Program
from ..mapping.base import MappingModel
from ..mortality.base import MortalityModel
from ..severity.base import SeverityModel


def simulate_year(
    year: int,
    rng: RNG,
    cat_process: CatProcess,
    severity: SeverityModel,
    mortality: MortalityModel,
    mapping: MappingModel,
    program: Program,
) -> YearResult:
    event_count = cat_process.sample_count(rng, year)
    event_count = mortality.apply(event_count, rng)
    severities = severity.sample(rng, event_count)
    mapped = mapping.map_severity(severities)
    gross = sum(mapped)
    net = program.apply_total(gross)
    return YearResult(
        year=year,
        event_count=event_count,
        gross_loss=gross,
        net_loss=net,
    )
