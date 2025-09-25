import os
import joblib
import numpy as np
from app.model import train_and_save_model
from app.predict import predict

def test_prediction_output():
    sample = [5.1, 3.5, 1.4, 0.2]
    result = predict(sample)
    assert isinstance(result, list)
    assert len(result) == 1

MODEL_PATH = "model.joblib"

# Vérifie si le modèle existe, sinon le crée
if not os.path.exists(MODEL_PATH):
    print("✅ Modèle non trouvé. Entraînement en cours...")
    train_and_save_model()
else:
    print("✅ Modèle chargé depuis le disque.")

# Charge le modèle une fois qu’il existe
model = joblib.load(MODEL_PATH)

def predict(data):
    return model.predict(np.array(data).reshape(1, -1)).tolist()
