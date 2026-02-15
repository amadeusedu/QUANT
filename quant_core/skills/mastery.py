from __future__ import annotations

def update_mastery(current: float, correct: bool, response_time: float, confidence: float) -> float:
    signal = (1.0 if correct else -0.6) * (1.2 if response_time < 25 else 0.9)
    alpha = 0.12 * max(0.2, min(confidence, 1.0))
    proposed = current + alpha * (signal * 10)
    daily_cap = 4.0
    return max(0.0, min(100.0, max(current - daily_cap, min(current + daily_cap, proposed))))
