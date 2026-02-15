import pandas as pd

from quant_core.backtest.robustness import leakage_check, run_parameter_sweep


def test_robustness_tools() -> None:
    idx = pd.date_range('2024-01-01', periods=120)
    df = pd.DataFrame({'close': range(100, 220)}, index=idx)
    sig = (df['close'] > df['close'].rolling(5).mean()).astype(float)
    assert leakage_check(sig)
    sweep = run_parameter_sweep(df, [5, 10])
    assert len(sweep) == 2
