from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from quant_core.sprints.templates import MEMO_TEMPLATE


def create_artifact(base_dir: Path, sprint_id: int, hypothesis: str, dataset_ref: str) -> Path:
    folder = base_dir / f"sprint_{sprint_id}"
    folder.mkdir(parents=True, exist_ok=True)
    memo = MEMO_TEMPLATE.format(
        sprint_id=sprint_id,
        hypothesis=hypothesis,
        data=dataset_ref,
        method="Baseline walkthrough",
        results="Pending",
        robustness="Pending",
        failures="Pending",
        next_steps="Iterate.",
    )
    (folder / "memo.md").write_text(memo)
    (folder / "reproduce.py").write_text("print('Reproduce sprint results here')\n")
    (folder / "metadata.json").write_text(
        json.dumps(
            {
                "sprint_id": sprint_id,
                "created_at": datetime.now(timezone.utc).isoformat(),
                "dataset_ref": dataset_ref,
            },
            indent=2,
        )
    )
    return folder
