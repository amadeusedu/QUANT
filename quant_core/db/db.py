from __future__ import annotations

import sqlite3
from pathlib import Path
from quant_core.drills.question_bank import seed_questions
from quant_core.skills.skill_tree import SKILL_SEED

ROOT = Path(__file__).resolve().parents[2]
DB_PATH = ROOT / "data" / "quant.db"


def init_db(reset: bool = False) -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    if reset and DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    schema = (Path(__file__).with_name("schema.sql")).read_text()
    con.executescript(schema)
    if con.execute("select count(*) from skills").fetchone()[0] == 0:
        con.executemany("insert into skills(id,name,domain,description,prereqs_json,mastery_score,last_practiced,target_mastery) values (?,?,?,?,?,0,NULL,80)", SKILL_SEED)
    if con.execute("select count(*) from drill_questions").fetchone()[0] == 0:
        con.executemany("insert into drill_questions(domain,prompt,answer,difficulty,tags_json,skill_ids_json,next_due) values (?,?,?,?,?,?,datetime('now'))", seed_questions())
    if con.execute("select count(*) from settings").fetchone()[0] == 0:
        con.executemany("insert into settings(key,value) values (?,?)", [("weekly_drill_minutes","315"),("weekly_drills","21"),("fee_bps","1.0"),("slippage_bps","1.0"),("timezone","Australia/Brisbane"),("enable_vectorbt","false")])
    con.commit()
    con.close()


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--reset", action="store_true")
    args = p.parse_args()
    init_db(reset=args.reset)
