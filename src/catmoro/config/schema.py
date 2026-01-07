from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class CatProcessConfig(BaseModel):
    kind: Literal["poisson"] = "poisson"
    rate: float = Field(ge=0.0, default=1.0)


class SeverityConfig(BaseModel):
    kind: Literal["lognormal"] = "lognormal"
    mu: float = 0.0
    sigma: float = Field(gt=0.0, default=1.0)


class MortalityConfig(BaseModel):
    kind: Literal["event_linked_jump"] = "event_linked_jump"
    jump_prob: float = Field(ge=0.0, le=1.0, default=0.0)


class MappingConfig(BaseModel):
    kind: Literal["linear"] = "linear"
    factor: float = 1.0
    intercept: float = 0.0


class InsuranceContractConfig(BaseModel):
    limit: float = Field(gt=0.0)
    attachment: float = Field(ge=0.0)


class InsuranceConfig(BaseModel):
    contracts: list[InsuranceContractConfig] = Field(default_factory=list)


class SimulationConfig(BaseModel):
    years: int = Field(ge=1, default=3)
    seed: int = 123
    cat_process: CatProcessConfig = Field(default_factory=CatProcessConfig)
    severity: SeverityConfig = Field(default_factory=SeverityConfig)
    mortality: MortalityConfig = Field(default_factory=MortalityConfig)
    mapping: MappingConfig = Field(default_factory=MappingConfig)
    insurance: InsuranceConfig = Field(default_factory=InsuranceConfig)
