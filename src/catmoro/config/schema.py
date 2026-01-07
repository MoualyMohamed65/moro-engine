from __future__ import annotations

from typing import Annotated, Literal

from pydantic import BaseModel, Field


class SimulationSettings(BaseModel):
    n_years: int = Field(ge=1, default=3)
    seed: int = 123


class CatProcessConfig(BaseModel):
    kind: Literal["poisson"] = "poisson"
    annual_rate: float = Field(ge=0.0, default=1.0)
    event_type_mix: dict[str, float] = Field(default_factory=lambda: {"generic": 1.0})


class LognormalParamConfig(BaseModel):
    mu: float
    sigma: float = Field(gt=0.0)


class SeverityConfig(BaseModel):
    kind: Literal["lognormal"] = "lognormal"
    mu: float = 0.0
    sigma: float = Field(gt=0.0, default=1.0)
    event_type_params: dict[str, LognormalParamConfig] = Field(default_factory=dict)


class MortalityConfig(BaseModel):
    kind: Literal["event_linked_jump"] = "event_linked_jump"
    base_lambda: float = Field(ge=0.0, default=0.0)
    jump_prob: float = Field(ge=0.0, le=1.0, default=0.0)
    jump_lambda: float = Field(ge=0.0, default=0.0)


class MappingConfig(BaseModel):
    kind: Literal["linear"] = "linear"
    cost_per_excess_death: float = Field(ge=0.0, default=1.0)


class XoLContractConfig(BaseModel):
    kind: Literal["xol"] = "xol"
    attachment: float = Field(ge=0.0)
    limit: float = Field(gt=0.0)


class QuotaShareContractConfig(BaseModel):
    kind: Literal["quota_share"] = "quota_share"
    share: float = Field(ge=0.0, le=1.0)


ContractConfig = Annotated[
    XoLContractConfig | QuotaShareContractConfig,
    Field(discriminator="kind"),
]


class ReinsuranceConfig(BaseModel):
    program: list[ContractConfig] = Field(default_factory=list)


class SimulationConfig(BaseModel):
    simulation: SimulationSettings = Field(default_factory=SimulationSettings)
    cat_process: CatProcessConfig = Field(default_factory=CatProcessConfig)
    severity: SeverityConfig = Field(default_factory=SeverityConfig)
    mortality: MortalityConfig = Field(default_factory=MortalityConfig)
    loss_mapping: MappingConfig = Field(default_factory=MappingConfig)
    reinsurance: ReinsuranceConfig = Field(default_factory=ReinsuranceConfig)
