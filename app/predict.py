import joblib
import os

MODEL_VERSION = "v1"
MODEL_PATH = f"models/model_{MODEL_VERSION}.joblib"

if not os.path.exists(MODEL_PATH):
    from train import train_and_save_model
    print("🔁 Modèle non trouvé. Entraînement...")
    train_and_save_model()

model = joblib.load(MODEL_PATH)

def predict(features):
    return model.predict([features]).tolist()
