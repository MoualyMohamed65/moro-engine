from __future__ import annotations

from ..config.loader import (
    build_cat_process,
    build_mapping,
    build_mortality,
    build_program,
    build_severity,
)
from ..config.schema import SimulationConfig
from ..core.rng import RNG
from ..core.types import YearResult
from .simulate_year import simulate_year


def run_simulation(cfg: SimulationConfig) -> list[YearResult]:
    rng = RNG(cfg.seed)
    cat_process = build_cat_process(cfg)
    severity = build_severity(cfg)
    mortality = build_mortality(cfg)
    mapping = build_mapping(cfg)
    program = build_program(cfg)

    results: list[YearResult] = []
    for year in range(1, cfg.years + 1):
        results.append(
            simulate_year(
                year,
                rng,
                cat_process,
                severity,
                mortality,
                mapping,
                program,
            )
        )
    return results


def run_tiny_simulation() -> list[YearResult]:
    cfg = SimulationConfig(years=3, seed=7)
    return run_simulation(cfg)
