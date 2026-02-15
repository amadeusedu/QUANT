import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo
from quant_core.sprints.templates import TEMPLATES
from quant_core.sprints.sprint_runner import run_sprint

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Research Sprints")
template = st.selectbox("Template", list(TEMPLATES.keys()))
hypothesis = st.text_input("Hypothesis", "Momentum outperforms buy-and-hold after costs")
dataset = st.text_input("Dataset reference", "data/sample_prices/SPY.csv")
if st.button("Create sprint artifact"):
    sid = repo.add_sprint(template, hypothesis, dataset)
    folder = run_sprint(init_db.__globals__["DB_PATH"].parents[1] / "artifacts", sid, hypothesis, dataset)
    repo.add_artifact(sid, str(folder), "sprint_bundle", {"template": template})
    st.success(f"Created {folder}")
