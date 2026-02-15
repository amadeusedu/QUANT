import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo
from quant_core.career.pipeline import STATUSES

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Career Pipeline")
with st.form("app"):
    company = st.text_input("Company")
    role = st.text_input("Role")
    status = st.selectbox("Status", STATUSES)
    next_action = st.text_input("Next action")
    notes = st.text_area("Notes")
    if st.form_submit_button("Add application") and company and role:
        repo.add_application(company, role, status, next_action, notes)
with st.form("contact"):
    name=st.text_input("Contact name")
    org=st.text_input("Org")
    follow=st.text_input("Next follow-up")
    notes2=st.text_area("Contact notes")
    if st.form_submit_button("Add contact") and name:
        repo.add_contact(name,org,follow,notes2)
st.subheader("Applications")
st.dataframe(repo.list_applications(), use_container_width=True)
st.subheader("Contacts")
st.dataframe(repo.list_contacts(), use_container_width=True)
