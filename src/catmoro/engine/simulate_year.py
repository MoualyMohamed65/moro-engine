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
    event_types = cat_process.sample_events(rng, year)
    severities = severity.sample(rng, event_types)
    gross_cat_loss = sum(severities)
    excess_deaths = mortality.sample_excess_deaths(event_types, rng)
    gross_mortality_loss = mapping.map_excess_deaths(excess_deaths)
    gross_total_loss = gross_cat_loss + gross_mortality_loss
    net_loss, ceded_loss = program.apply_total(gross_total_loss)
    return YearResult(
        year=year,
        event_count=len(event_types),
        gross_cat_loss=gross_cat_loss,
        gross_mortality_loss=gross_mortality_loss,
        gross_total_loss=gross_total_loss,
        ceded_loss=ceded_loss,
        net_loss=net_loss,
    )
