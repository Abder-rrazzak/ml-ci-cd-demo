from setuptools import setup, find_packages

setup(
    name="ml_cicd_demo",
    version="0.1.0",
    description="ML CI/CD demo project with FastAPI, Streamlit, and Docker",
    author="Ton Nom",
    author_email="ton.email@example.com",
    packages=find_packages(),  # va trouver app/, tests/, etc.
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "joblib",
        "scikit-learn",
        "pydantic",
        "streamlit",
        "mlflow",
        "httpx",            # pour les tests API
        "pytest",
        "python-multipart", # si tu acceptes des fichiers un jour
    ],
    entry_points={
        "console_scripts": [
            "train-model=app.model:train_and_save_model",
        ],
    },
    python_requires=">=3.7",
)
