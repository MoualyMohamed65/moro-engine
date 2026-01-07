    from __future__ import annotations

    from ..core.types import YearResult


    def summarize_results(results: list[YearResult]) -> str:
        lines = ["year,event_count,gross_loss,net_loss"]
        for item in results:
            lines.append(
                f"{item.year},{item.event_count},{item.gross_loss:.4f},{item.net_loss:.4f}"
            )
        return "
".join(lines)
