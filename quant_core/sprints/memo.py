from __future__ import annotations
from markdown import markdown

def memo_to_html(md_text: str) -> str:
    return markdown(md_text, extensions=["tables", "fenced_code"])
