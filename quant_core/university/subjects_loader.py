from __future__ import annotations
import json
from pathlib import Path

def load_subjects(path: Path) -> list[dict[str, object]]:
    return json.loads(path.read_text())
