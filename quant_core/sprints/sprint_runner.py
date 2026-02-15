from __future__ import annotations
from pathlib import Path
from quant_core.sprints.artifact_manager import create_artifact


def run_sprint(base_dir: Path, sprint_id: int, hypothesis: str, dataset_ref: str) -> Path:
    return create_artifact(base_dir, sprint_id, hypothesis, dataset_ref)
