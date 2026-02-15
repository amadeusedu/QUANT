from __future__ import annotations
import pandas as pd

def transaction_costs(position: pd.Series, fee_bps: float, slippage_bps: float) -> pd.Series:
    turnover = position.diff().abs().fillna(position.abs())
    total_bps = (fee_bps + slippage_bps) / 10000
    return turnover * total_bps
