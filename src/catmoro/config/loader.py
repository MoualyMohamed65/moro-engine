from __future__ import annotations

from pathlib import Path

import yaml

from ..cat_process.poisson import PoissonProcess
from ..insurance.contracts import Contract
from ..insurance.program import Program
from ..mapping.linear import LinearMapping
from ..mortality.event_linked_jump import EventLinkedJump
from ..severity.lognormal import LognormalSeverity
from .schema import SimulationConfig


def load_config(path: Path) -> SimulationConfig:
    data = yaml.safe_load(path.read_text(encoding="ascii"))
    return SimulationConfig.model_validate(data)


def build_cat_process(cfg: SimulationConfig) -> PoissonProcess:
    return PoissonProcess(rate=cfg.cat_process.rate)


def build_severity(cfg: SimulationConfig) -> LognormalSeverity:
    return LognormalSeverity(mu=cfg.severity.mu, sigma=cfg.severity.sigma)


def build_mortality(cfg: SimulationConfig) -> EventLinkedJump:
    return EventLinkedJump(jump_prob=cfg.mortality.jump_prob)


def build_mapping(cfg: SimulationConfig) -> LinearMapping:
    return LinearMapping(factor=cfg.mapping.factor, intercept=cfg.mapping.intercept)


def build_program(cfg: SimulationConfig) -> Program:
    contracts = [
        Contract(limit=c.limit, attachment=c.attachment)
        for c in cfg.insurance.contracts
    ]
    return Program(contracts=contracts)
