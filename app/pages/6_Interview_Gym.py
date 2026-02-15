import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo
from quant_core.interview.mock_interview import weekly_mock
from quant_core.interview.rubric import score_rubric

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Interview Gym")
qids = repo.due_questions()["id"].tolist()
st.json(weekly_mock(qids))
resp = st.text_area("Explain sprint X in 90 seconds")
clarity = st.slider("Clarity",1,5,3)
honesty = st.slider("Honesty",1,5,3)
trade = st.slider("Tradeoffs",1,5,3)
st.metric("Rubric score", score_rubric(clarity,honesty,trade))
