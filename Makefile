# Makefile for ML CI/CD Demo

# Variables
PYTHON=python
APP_DIR=app
MODEL_DIR=models
MODEL_FILE=model_v1.joblib

# =========================
# ENVIRONNEMENT
# =========================

venv:
	$(PYTHON) -m venv venv
	source venv/Scripts/activate && pip install -r requirements.txt

install:
	pip install -r requirements.txt

# =========================
# TRAINING
# =========================

train:
	$(PYTHON) train.py

# =========================
# API & Streamlit
# =========================

run-api:
	uvicorn app.api:app --reload --host 0.0.0.0 --port 8000

run-streamlit:
	streamlit run streamlit_app.py

# =========================
# TESTS
# =========================

test:
	PYTHONPATH=. pytest

# =========================
# DOCKER
# =========================

build-docker:
	docker build -t ml-api .

run-docker:
	docker run -p 8000:8000 ml-api

# =========================
# CLEANUP
# =========================

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

clean-models:
	rm -rf $(MODEL_DIR)/*.joblib

# =========================
# CI UTIL
# =========================

check:
	PYTHONPATH=. pytest --disable-warnings -v

