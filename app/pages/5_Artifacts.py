from pathlib import Path
import zipfile
import streamlit as st
from quant_core.db.db import init_db
from quant_core.db.repositories import Repo
from quant_core.sprints.memo import memo_to_html

init_db(); repo = Repo(init_db.__globals__["DB_PATH"])
st.title("Artifact Vault")
df = repo.list_artifacts()
st.dataframe(df, use_container_width=True)
folder = st.text_input("Artifact folder to export", "artifacts")
if st.button("Export zip"):
    p=Path(folder)
    zip_path=Path("artifacts_export.zip")
    with zipfile.ZipFile(zip_path, "w") as z:
        for f in p.rglob("*"):
            if f.is_file(): z.write(f, f.relative_to(p.parent))
    st.success(f"Wrote {zip_path}")
md_path = st.text_input("Memo markdown path", "artifacts/sprint_1/memo.md")
if st.button("Export HTML"):
    md = Path(md_path).read_text()
    html = memo_to_html(md)
    out = Path(md_path).with_suffix('.html')
    out.write_text(html)
    st.success(f"Exported {out}")
