# Makefile for the FastAPI REST API

# Variables
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Create virtual environment
venv:
	python -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run the application
run:
	$(PYTHON) -m uvicorn app.main:app --reload

# Run tests
.PHONY: test

test:
	$(PYTHON) -m pytest --cov=app tests/

# Format code using black and isort
.PHONY: format

format:
	$(PYTHON) -m black .
	$(PYTHON) -m isort .

# Linting with flake8
.PHONY: lint

lint:
	$(PYTHON) -m flake8 .

# Run all checks (lint, format, test)
.PHONY: check

check: format lint test
