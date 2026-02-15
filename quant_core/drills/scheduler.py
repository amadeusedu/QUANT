from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

@dataclass(slots=True)
class ScheduleState:
    easiness: float
    interval: int
    repetitions: int
    next_due: datetime


def schedule_next(review_quality: int, easiness: float, interval: int, repetitions: int) -> ScheduleState:
    q = max(0, min(5, review_quality))
    new_ease = max(1.3, easiness + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)))
    if q < 3:
        repetitions = 0
        interval = 1
    else:
        repetitions += 1
        if repetitions == 1:
            interval = 1
        elif repetitions == 2:
            interval = 6
        else:
            interval = int(round(interval * new_ease))
    return ScheduleState(new_ease, interval, repetitions, datetime.now(timezone.utc) + timedelta(days=interval))
