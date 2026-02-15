import pandas as pd
import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo
from quant_core.backtest.engine import run_backtest
from quant_core.backtest.robustness import run_parameter_sweep, leakage_check, regime_split

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Backtest Harness")
path = st.selectbox("Sample data", ["data/sample_prices/SPY.csv","data/sample_prices/AAPL.csv","data/sample_prices/MSFT.csv"])
df = pd.read_csv(path, parse_dates=["date"]).set_index("date")
window = st.slider("MA window", 5, 80, 20)
sig = (df["close"] > df["close"].rolling(window).mean()).astype(float)
out,m = run_backtest(df,sig, float(repo.get_setting("fee_bps","1.0")), float(repo.get_setting("slippage_bps","1.0")))
st.line_chart(out["equity"])
st.line_chart(out["drawdown"])
st.json(m)
if st.button("Run robustness checks"):
    sweep = run_parameter_sweep(df,[10,20,40,60])
    regimes = regime_split(df,sig)
    passed = leakage_check(sig) and m["sharpe"] > 0
    st.write({"passed": passed, "sweep": sweep, "regimes": regimes})
