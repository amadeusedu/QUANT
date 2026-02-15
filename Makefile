.PHONY: install run test lint typecheck reset

install:
	python -m pip install -e .[dev]

run:
	streamlit run app/Home.py

test:
	pytest

lint:
	ruff check .

typecheck:
	mypy quant_core app

reset:
	python -m quant_core.db.db --reset
