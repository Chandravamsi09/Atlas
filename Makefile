.PHONY: install build run test lint clean

install:
	python -m pip install --upgrade pip
	pip install -r requirements.txt
	pip install -e .[dev]
	cd frontend && npm install

build:
	docker build -t atlas-enterprise-backend .
	cd frontend && npm run build

run:
	uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest tests/ -v

lint:
	ruff check .
	mypy backend/app/ --ignore-missing-imports

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov .mypy_cache .ruff_cache frontend/.next
