from __future__ import annotations

from pathlib import Path

import yaml

from ..cat_process.poisson import PoissonProcess
from ..insurance.contracts import QuotaShareContract, XoLContract
from ..insurance.program import Program
from ..mapping.linear import LinearMapping
from ..mortality.event_linked_jump import EventLinkedJump
from ..severity.lognormal import LognormalParams, LognormalSeverity
from .schema import SimulationConfig


def load_config(path: Path) -> SimulationConfig:
    data = yaml.safe_load(path.read_text(encoding="ascii"))
    return SimulationConfig.model_validate(data)


def build_cat_process(cfg: SimulationConfig) -> PoissonProcess:
    return PoissonProcess(
        annual_rate=cfg.cat_process.annual_rate,
        event_type_mix=cfg.cat_process.event_type_mix,
    )


def build_severity(cfg: SimulationConfig) -> LognormalSeverity:
    event_type_params = {
        key: LognormalParams(mu=value.mu, sigma=value.sigma)
        for key, value in cfg.severity.event_type_params.items()
    }
    return LognormalSeverity(
        mu=cfg.severity.mu,
        sigma=cfg.severity.sigma,
        event_type_params=event_type_params,
    )


def build_mortality(cfg: SimulationConfig) -> EventLinkedJump:
    return EventLinkedJump(
        base_lambda=cfg.mortality.base_lambda,
        jump_prob=cfg.mortality.jump_prob,
        jump_lambda=cfg.mortality.jump_lambda,
    )


def build_mapping(cfg: SimulationConfig) -> LinearMapping:
    return LinearMapping(cost_per_excess_death=cfg.loss_mapping.cost_per_excess_death)


def build_program(cfg: SimulationConfig) -> Program:
    contracts = []
    for contract in cfg.reinsurance.program:
        if contract.kind == "xol":
            contracts.append(
                XoLContract(
                    attachment=contract.attachment,
                    limit=contract.limit,
                )
            )
        elif contract.kind == "quota_share":
            contracts.append(QuotaShareContract(share=contract.share))
    return Program(contracts=contracts)
