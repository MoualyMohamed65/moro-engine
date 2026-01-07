from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Contract:
    limit: float
    attachment: float

    def recovery(self, loss: float) -> float:
        if loss <= self.attachment:
            return 0.0
        return min(loss - self.attachment, self.limit)
