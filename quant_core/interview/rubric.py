from __future__ import annotations

def score_rubric(clarity: int, honesty: int, tradeoffs: int) -> float:
    return round((clarity + honesty + tradeoffs) / 3, 2)
