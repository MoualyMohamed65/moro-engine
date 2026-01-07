from __future__ import annotations

from dataclasses import dataclass

from .contracts import Contract


@dataclass(frozen=True)
class Program:
    contracts: list[Contract]

    def apply_total(self, gross_loss: float) -> tuple[float, float]:
        remaining = gross_loss
        ceded_total = 0.0
        for contract in self.contracts:
            ceded = contract.ceded(remaining)
            ceded_total += ceded
            remaining = max(remaining - ceded, 0.0)
        return remaining, ceded_total
