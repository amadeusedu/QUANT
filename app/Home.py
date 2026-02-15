from __future__ import annotations
import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo
from quant_core.backtest.vectorbt_adapter import is_available
from app.ui.theme import apply_theme

apply_theme()
init_db()
repo = Repo(init_db.__globals__["DB_PATH"])

st.title("QUANT — Personal Quant Apprenticeship OS")
col1,col2,col3=st.columns(3)
skills = repo.list_skills()
arts = repo.list_artifacts()
apps = repo.list_applications()
col1.metric("Avg Mastery", f"{skills['mastery_score'].mean():.1f}")
col2.metric("Artifacts this month", int(len(arts)))
col3.metric("Career actions", int(len(apps)))
st.caption(f"vectorbt installed: {is_available()}")
