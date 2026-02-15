from __future__ import annotations

def confidence_from_reviews(total_reviews: int) -> float:
    return min(1.0, 0.2 + total_reviews / 20)
