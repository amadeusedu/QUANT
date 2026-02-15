from __future__ import annotations
import numpy as np
import pandas as pd


def compute_metrics(equity: pd.Series, returns: pd.Series, turnover: pd.Series) -> dict[str, float]:
    ann = 252
    total = equity.iloc[-1] / equity.iloc[0] - 1
    years = max(len(equity) / ann, 1 / ann)
    cagr = (1 + total) ** (1 / years) - 1
    vol = returns.std() * np.sqrt(ann)
    sharpe = (returns.mean() * ann) / vol if vol else 0.0
    neg = returns[returns < 0]
    sortino = (returns.mean() * ann) / (neg.std() * np.sqrt(ann)) if len(neg) > 1 else 0.0
    dd = equity / equity.cummax() - 1
    mdd = dd.min()
    calmar = cagr / abs(mdd) if mdd else 0.0
    hit = float((returns > 0).mean())
    worst_63d = returns.rolling(63).sum().min()
    tail = float(np.percentile(returns, 5))
    return {"cagr": float(cagr), "ann_vol": float(vol), "sharpe": float(sharpe), "sortino": float(sortino), "max_drawdown": float(mdd), "calmar": float(calmar), "turnover": float(turnover.mean()), "hit_rate": hit, "worst_rolling_63d": float(worst_63d), "tail_loss_p5": tail}
