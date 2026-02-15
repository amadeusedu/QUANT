from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

class Repo:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def conn(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def list_skills(self) -> pd.DataFrame:
        with self.conn() as c:
            return pd.read_sql_query("select * from skills", c)

    def due_questions(self) -> pd.DataFrame:
        with self.conn() as c:
            return pd.read_sql_query("select * from drill_questions order by coalesce(next_due,'1970-01-01') asc limit 20", c)

    def insert_review(self, question_id: int, correct: bool, response_time: float, error_tags: list[str]) -> None:
        with self.conn() as c:
            c.execute(
                "insert into drill_reviews(question_id,ts,correct,response_time,error_tags_json) values (?,?,?,?,?)",
                (question_id, datetime.now(timezone.utc).isoformat(), int(correct), response_time, json.dumps(error_tags)),
            )
            c.commit()

    def update_question_schedule(self, question_id: int, easiness: float, interval: int, repetitions: int, next_due: str) -> None:
        with self.conn() as c:
            c.execute("update drill_questions set easiness=?, interval=?, repetitions=?, next_due=? where id=?",(easiness, interval, repetitions, next_due, question_id))
            c.commit()

    def update_skill_mastery(self, skill_id: str, score: float) -> None:
        with self.conn() as c:
            c.execute("update skills set mastery_score=?, last_practiced=? where id=?", (score, datetime.now(timezone.utc).isoformat(), skill_id))
            c.commit()

    def add_sprint(self, template: str, hypothesis: str, dataset_ref: str) -> int:
        now = datetime.now(timezone.utc).isoformat()
        with self.conn() as c:
            cur = c.execute("insert into sprints(template,hypothesis,dataset_ref,status,created_at,updated_at) values (?,?,?,?,?,?)",(template,hypothesis,dataset_ref,"created",now,now))
            c.commit()
            return int(cur.lastrowid)

    def add_artifact(self, sprint_id: int, path: str, kind: str, metadata: dict[str, object]) -> None:
        with self.conn() as c:
            c.execute("insert into artifacts(sprint_id,path,created_at,kind,metadata_json) values (?,?,?,?,?)",(sprint_id,path,datetime.now(timezone.utc).isoformat(),kind,json.dumps(metadata)))
            c.commit()

    def list_artifacts(self) -> pd.DataFrame:
        with self.conn() as c:
            return pd.read_sql_query("select * from artifacts order by created_at desc", c)

    def add_application(self, company: str, role: str, status: str, next_action: str, notes: str) -> None:
        with self.conn() as c:
            c.execute("insert into career_applications(company,role,status,date_applied,next_action,notes) values (?,?,?,?,?,?)",(company,role,status,datetime.now(timezone.utc).date().isoformat(),next_action,notes))
            c.commit()

    def list_applications(self) -> pd.DataFrame:
        with self.conn() as c:
            return pd.read_sql_query("select * from career_applications", c)

    def add_contact(self, name: str, org: str, next_followup: str, notes: str) -> None:
        with self.conn() as c:
            c.execute("insert into career_contacts(name,org,last_contact,next_followup,notes) values (?,?,?,?,?)",(name,org,datetime.now(timezone.utc).date().isoformat(),next_followup,notes))
            c.commit()

    def list_contacts(self) -> pd.DataFrame:
        with self.conn() as c:
            return pd.read_sql_query("select * from career_contacts", c)

    def save_setting(self, key: str, value: str) -> None:
        with self.conn() as c:
            c.execute("insert into settings(key,value) values (?,?) on conflict(key) do update set value=excluded.value",(key,value))
            c.commit()

    def get_setting(self, key: str, default: str) -> str:
        with self.conn() as c:
            row = c.execute("select value from settings where key=?",(key,)).fetchone()
            return row[0] if row else default
