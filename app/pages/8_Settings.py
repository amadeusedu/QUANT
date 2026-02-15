import json
from pathlib import Path
import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Settings")
weekly = st.number_input("Weekly drill minutes", value=int(repo.get_setting("weekly_drill_minutes", "315")))
fee = st.number_input("Fee bps", value=float(repo.get_setting("fee_bps", "1.0")))
slip = st.number_input("Slippage bps", value=float(repo.get_setting("slippage_bps", "1.0")))
tz = st.text_input("Timezone", repo.get_setting("timezone", "Australia/Brisbane"))
vec = st.checkbox("Enable vectorbt if installed", value=repo.get_setting("enable_vectorbt", "false")=="true")
if st.button("Save settings"):
    repo.save_setting("weekly_drill_minutes", str(int(weekly)))
    repo.save_setting("fee_bps", str(float(fee)))
    repo.save_setting("slippage_bps", str(float(slip)))
    repo.save_setting("timezone", tz)
    repo.save_setting("enable_vectorbt", "true" if vec else "false")
    st.success("Saved")
if st.button("Reset demo data"):
    init_db(reset=True)
    st.success("Reset complete")
subjects_path = Path("data/university/subjects.json")
if subjects_path.exists():
    st.json(json.loads(subjects_path.read_text()))
