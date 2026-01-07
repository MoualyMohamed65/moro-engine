from dataclasses import dataclass


@dataclass(frozen=True)
class YearResult:
    year: int
    event_count: int
    gross_cat_loss: float
    gross_mortality_loss: float
    gross_total_loss: float
    ceded_loss: float
    net_loss: float
