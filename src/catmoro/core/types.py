from dataclasses import dataclass


@dataclass(frozen=True)
class YearResult:
    year: int
    event_count: int
    gross_loss: float
    net_loss: float
