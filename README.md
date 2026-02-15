# QUANT

QUANT is a local-first **Quant Apprenticeship OS** for deliberate quant practice, research output, and career execution.

## Quickstart
1. `python -m venv .venv && source .venv/bin/activate`
2. `pip install -e .[dev]`
3. `streamlit run app/Home.py`

## How to run
- App: `streamlit run app/Home.py`
- Tests: `pytest`
- Lint: `ruff check .`
- Type check: `mypy quant_core app`

## Reset demo data
- Click **Settings → Reset demo data**, or run: `python -m quant_core.db.db --reset`

## Add new questions
- Add rows to `drill_questions` table or extend generators in `quant_core/drills/generators.py` and run reset.

## Create a sprint
- Go to **Sprints** page.
- Select template + hypothesis + dataset.
- Creates `artifacts/sprint_<id>/memo.md`, `metadata.json`, and `reproduce.py`.

## Add your own datasets
- CSV with columns: `date,open,high,low,close,volume`.
- Place under `data/sample_prices/` or choose your path.

## Export memos
- Artifact page supports Markdown→HTML export.
- If Quarto is installed locally, you can render memo documents to PDF/HTML externally.

## How to use QUANT during uni
- Daily: 10 min mental math, 15 min probability, 20 min coding.
- Weekly: one sprint milestone + one memo update.
- Monthly: one portfolio-quality artifact with robustness checks.

## Architecture
- `app/`: Streamlit multipage UI
- `quant_core/`: core domain logic (db, drills, backtests, sprints, interview, career, university planner)
- `data/`: local DB + sample datasets + subject config
- `artifacts/`: generated research outputs
