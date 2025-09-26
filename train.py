# train.py
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import os
import mlflow
import mlflow.sklearn

MODEL_DIR = "models"
MODEL_VERSION = "v1"
MODEL_PATH = os.path.join(MODEL_DIR, f"model_{MODEL_VERSION}.joblib")

def train_and_save_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", RandomForestClassifier(n_estimators=100, random_state=42))
    ])

    with mlflow.start_run():
        pipeline.fit(X_train, y_train)
        joblib.dump(pipeline, MODEL_PATH)
        print(f"✅ Modèle sauvegardé : {MODEL_PATH}")

        mlflow.log_param("model_version", MODEL_VERSION)
        mlflow.log_metric("accuracy", pipeline.score(X_test, y_test))
        mlflow.sklearn.log_model(pipeline, "model")

if __name__ == "__main__":
    train_and_save_model()
    
