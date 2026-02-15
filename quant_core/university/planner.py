from __future__ import annotations

def weekly_quotas(load_weight: float, exam_mode: bool) -> dict[str, int]:
    base = {"drill_minutes": 315, "sprint_hours": 6}
    if load_weight > 1.2:
        base["sprint_hours"] = 4
    if exam_mode:
        base["drill_minutes"] += 90
        base["sprint_hours"] = max(2, base["sprint_hours"] - 2)
    return base
