from __future__ import annotations

import json

from quant_core.drills.generators import gen_coding, gen_mental_math, gen_probability, gen_stats


def seed_questions() -> list[tuple[str, str, str, float, str, str]]:
    rows: list[tuple[str, str, str, float, str, str]] = []
    generators = [
        ("mental_math", gen_mental_math, '["in1"]'),
        ("probability", gen_probability, '["ma3"]'),
        ("stats", gen_stats, '["ma4"]'),
        ("coding", gen_coding, '["cs1"]'),
    ]
    for domain, fn, skill in generators:
        for _ in range(15):
            q = fn()
            rows.append(
                (
                    domain,
                    str(q["prompt"]),
                    str(q["answer"]),
                    float(q["difficulty"]),
                    json.dumps(q["tags"]),
                    skill,
                )
            )
    return rows
