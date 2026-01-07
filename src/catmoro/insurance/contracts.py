from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


class Contract(ABC):
    @abstractmethod
    def ceded(self, loss: float) -> float:
        raise NotImplementedError


@dataclass(frozen=True)
class XoLContract(Contract):
    attachment: float
    limit: float

    def ceded(self, loss: float) -> float:
        if loss <= self.attachment:
            return 0.0
        return min(loss - self.attachment, self.limit)


@dataclass(frozen=True)
class QuotaShareContract(Contract):
    share: float

    def ceded(self, loss: float) -> float:
        if self.share <= 0.0:
            return 0.0
        return loss * self.share
