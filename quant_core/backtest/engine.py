from __future__ import annotations
import pandas as pd
from quant_core.backtest.costs import transaction_costs
from quant_core.backtest.metrics import compute_metrics


def run_backtest(df: pd.DataFrame, signal: pd.Series, fee_bps: float = 1.0, slippage_bps: float = 1.0) -> tuple[pd.DataFrame, dict[str, float]]:
    px = df["close"].astype(float)
    ret = px.pct_change().fillna(0.0)
    position = signal.reindex(df.index).fillna(0.0).shift(1).fillna(0.0)
    costs = transaction_costs(position, fee_bps, slippage_bps)
    strat_ret = position * ret - costs
    equity = (1 + strat_ret).cumprod()
    out = pd.DataFrame({"returns": strat_ret, "equity": equity, "position": position, "drawdown": equity / equity.cummax() - 1})
    return out, compute_metrics(equity, strat_ret, position.diff().abs().fillna(0.0))
