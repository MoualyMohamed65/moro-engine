from __future__ import annotations

from dataclasses import dataclass

from .contracts import Contract


@dataclass(frozen=True)
class Program:
    contracts: list[Contract]

    def apply_total(self, gross_loss: float) -> float:
        recovery = sum(c.recovery(gross_loss) for c in self.contracts)
        return max(gross_loss - recovery, 0.0)
