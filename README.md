# ML CI/CD Demo

A minimal machine learning project using CI/CD with GitHub Actions.

## Features

- Train a logistic regression model on the Iris dataset
- Expose predictions via a FastAPI API
- Run unit tests with pytest
- GitHub Actions pipeline: install, train, test

## Getting Started

```bash
# Clone the repo
git clone https://github.com/ton-pseudo/ml-ci-cd-demo.git
cd ml-ci-cd-demo

# Install dependencies
pip install -r requirements.txt

# Train the model
python app/model.py

# Run the API
uvicorn app.api:app --reload
