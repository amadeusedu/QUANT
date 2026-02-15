from __future__ import annotations

try:
    import vectorbt as vbt
except Exception:  # noqa: BLE001
    vbt = None


def is_available() -> bool:
    return vbt is not None
