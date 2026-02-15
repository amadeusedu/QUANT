import pandas as pd

from quant_core.backtest.engine import run_backtest


def test_backtest_outputs_metrics() -> None:
    idx = pd.date_range('2024-01-01', periods=50)
    df = pd.DataFrame({'close': range(100, 150)}, index=idx)
    signal = pd.Series(1, index=idx)
    _, m = run_backtest(df, signal)
    assert 'sharpe' in m
