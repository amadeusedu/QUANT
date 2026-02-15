from __future__ import annotations
import json
import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo
from quant_core.drills.scheduler import schedule_next
from quant_core.drills.scoring import confidence_from_reviews
from quant_core.skills.mastery import update_mastery

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Daily Drills")
qdf = repo.due_questions()
if qdf.empty:
    st.info("No questions available")
else:
    row = qdf.iloc[0]
    st.write(f"**Prompt:** {row['prompt']}")
    show = st.checkbox("Reveal answer")
    if show:
        st.write(f"Answer: {row['answer']}")
    correct = st.toggle("I got it correct", value=True)
    resp = st.number_input("Response time (s)", min_value=1.0, value=20.0)
    tags = st.multiselect("Error tags", ["concept_gap","careless","speed","didnt_know_tool"])
    quality = st.slider("Review quality (0-5)", 0, 5, 4)
    if st.button("Submit review"):
        repo.insert_review(int(row["id"]), correct, float(resp), tags)
        ns = schedule_next(quality, float(row["easiness"]), int(row["interval"]), int(row["repetitions"]))
        repo.update_question_schedule(int(row["id"]), ns.easiness, ns.interval, ns.repetitions, ns.next_due.isoformat())
        for sid in json.loads(row["skill_ids_json"]):
            sdf = repo.list_skills()
            current = float(sdf.loc[sdf["id"] == sid, "mastery_score"].iloc[0])
            conf = confidence_from_reviews(int(ns.repetitions))
            repo.update_skill_mastery(sid, update_mastery(current, bool(correct), float(resp), conf))
        st.success("Review saved and mastery updated")
