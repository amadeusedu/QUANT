from __future__ import annotations
import random

def weekly_mock(question_ids: list[int]) -> dict[str, list[int] | str]:
    random.shuffle(question_ids)
    return {
        "mental_math": question_ids[:5],
        "probability": question_ids[5:8],
        "coding": question_ids[8:9],
        "project_prompt": "Explain sprint X in 90 seconds with tradeoffs.",
    }
