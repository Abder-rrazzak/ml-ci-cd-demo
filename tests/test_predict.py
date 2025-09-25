import os
import joblib
import numpy as np
from app.model import train_and_save_model

MODEL_PATH = "model.joblib"

# Si le modèle n'existe pas, on le crée
if not os.path.exists(MODEL_PATH):
    train_and_save_model()

model = joblib.load(MODEL_PATH)

def predict(data):
    return model.predict(np.array(data).reshape(1, -1)).tolist()
