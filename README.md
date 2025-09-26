Here is your **final, professional, and complete `README.md`** for your Machine Learning CI/CD project.
It’s production-grade and ready to showcase in a portfolio, GitHub profile, or even for interviews. ✅

---

```markdown
# 🌸 ML CI/CD Demo — Iris Classification Project

[![CI](https://github.com/<YOUR-GITHUB-USERNAME>/ml-ci-cd-demo/actions/workflows/ci.yml/badge.svg)](https://github.com/<YOUR-GITHUB-USERNAME>/ml-ci-cd-demo/actions)
[![API Live](https://img.shields.io/badge/api-live-success)](https://ml-ci-cd-demo-2.onrender.com)
[![Streamlit App](https://img.shields.io/badge/demo-streamlit-blue)](https://<YOUR-STREAMLIT-URL>.streamlit.app/)

> End-to-end Machine Learning project: training, versioning, CI/CD, API deployment (FastAPI), UI (Streamlit), containerization (Docker), and testing.

---

## 🚀 Project Overview

This project demonstrates a full ML lifecycle with modern DevOps best practices:

- 🧠 Train a model on the **Iris** dataset using scikit-learn
- 🐳 Deploy a REST API using **FastAPI** (served with Uvicorn)
- 🎈 Build an interactive **Streamlit** web app
- 🧪 Write unit/integration tests with `pytest`
- 🔁 Automate testing with **GitHub Actions** CI
- 📦 Containerize everything using **Docker & docker-compose**
- 📈 Track training runs with **MLflow**

---

## 🗂️ Folder Structure

```

ml-ci-cd-demo/
│
├── app/                     # FastAPI application
│   ├── api.py               # API routes
│   ├── model.py             # ML training utilities
│   └── predict.py           # Prediction logic
│
├── models/                  # Saved trained models
│   └── model_v1.joblib
│
├── tests/                   # Unit and integration tests
│   ├── test_api.py
│   └── test_predict.py
│
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions workflow
│
├── streamlit_app.py         # Streamlit frontend
├── train.py                 # Model training script (MLflow integrated)
├── requirements.txt         # Python dependencies
├── Dockerfile               # API Docker container
├── Dockerfile.streamlit     # Streamlit UI Docker container
├── docker-compose.yml       # Multi-container setup
└── README.md                # Project documentation

````

---

## ⚙️ How to Use

### 🔧 Step 1 — Install Dependencies

```bash
pip install -r requirements.txt
````

### 🧠 Step 2 — Train the Model

This will train a Random Forest model and save it as `model_v1.joblib` in the `models/` directory.
Also logs the run using **MLflow**.

```bash
python train.py
```

### 🧪 Step 3 — Run Tests

```bash
pytest
```

---

## 🐳 Run with Docker

### 📦 Build and Run Locally with `docker-compose`

```bash
docker-compose up --build
```

* FastAPI API available at → [http://localhost:8000](http://localhost:8000)
* Swagger UI at → [http://localhost:8000/docs](http://localhost:8000/docs)
* Streamlit App at → [http://localhost:8501](http://localhost:8501)

---

## 🔁 CI/CD with GitHub Actions

This project includes a full **CI pipeline** that runs on every push:

* ✅ Installs dependencies
* 🧪 Runs unit & integration tests
* 🧼 Validates code and ML pipeline

Config file: `.github/workflows/ci.yml`

---

## 📊 Model Tracking with MLflow

Each training run is tracked using **MLflow**:

* Metrics (accuracy, etc.)
* Parameters (version, model type)
* Model artifacts (serialized joblib file)

To launch the MLflow UI locally:

```bash
mlflow ui
```

Access at: [http://localhost:5000](http://localhost:5000)

---

## 🔌 API Endpoints (FastAPI)

| Endpoint   | Method | Description                       |
| ---------- | ------ | --------------------------------- |
| `/`        | GET    | Welcome message                   |
| `/health`  | GET    | Health check (status & version)   |
| `/predict` | POST   | Predict flower type from features |

### 🔎 Example API Usage

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

**Response:**

```json
{
  "prediction": [0],
  "label": "Iris-setosa"
}
```

---

## 🖥️ Streamlit Interface

The Streamlit frontend connects to the API and allows users to:

* Input flower measurements
* Get predictions in real-time
* See the classification label (e.g., "Iris-setosa")

Run locally:

```bash
streamlit run streamlit_app.py
```

---

## ✅ Features Recap

* [x] Model training + versioning
* [x] REST API with FastAPI
* [x] Dockerized backend + frontend
* [x] CI pipeline with GitHub Actions
* [x] MLflow tracking
* [x] Streamlit UI
* [x] Unit + integration testing
* [x] `/health` and `/predict` endpoints
* [x] Docker Compose for orchestration

---

## 🔜 Roadmap

* [ ] Auto versioning model on each train run
* [ ] Deploy MLflow server on remote storage (e.g., S3)
* [ ] Add Prometheus / Grafana monitoring
* [ ] Deploy on Hugging Face Spaces or Azure

---

## 📄 License

MIT License © [Abderazzak_ZERROUKI]

```

---

## 🧩 Replace placeholders before publishing:

- `<YOUR-GITHUB-USERNAME>` → your GitHub username
- `<YOUR-STREAMLIT-URL>` → your Streamlit app URL (if deployed)
- `[Your Name]` → your actual name or GitHub handle


