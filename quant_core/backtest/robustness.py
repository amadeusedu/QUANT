from __future__ import annotations
import pandas as pd
from quant_core.backtest.engine import run_backtest


def leakage_check(signal: pd.Series) -> bool:
    return signal.index.is_monotonic_increasing


def run_parameter_sweep(df: pd.DataFrame, windows: list[int]) -> dict[int, float]:
    res: dict[int, float] = {}
    for w in windows:
        ma = df["close"].rolling(w).mean()
        sig = (df["close"] > ma).astype(float)
        _, m = run_backtest(df, sig)
        res[w] = m["sharpe"]
    return res


def regime_split(df: pd.DataFrame, signal: pd.Series) -> dict[str, float]:
    vol = df["close"].pct_change().rolling(20).std().fillna(0.0)
    med = vol.median()
    low = df[vol <= med]
    hi = df[vol > med]
    _, m1 = run_backtest(low, signal.reindex(low.index).fillna(0))
    _, m2 = run_backtest(hi, signal.reindex(hi.index).fillna(0))
    return {"low_vol_sharpe": m1["sharpe"], "high_vol_sharpe": m2["sharpe"]}
