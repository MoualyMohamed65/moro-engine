from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Callable


class Optimizer(ABC):
    @abstractmethod
    def optimize(self, objective: Callable[[float], float]) -> float:
        raise NotImplementedError
