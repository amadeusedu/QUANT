import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Skill Tree")
df = repo.list_skills()
st.dataframe(df[["id","name","domain","mastery_score","target_mastery","last_practiced"]], use_container_width=True)
st.bar_chart(df.groupby("domain")["mastery_score"].mean())
