import joblib
import numpy as np

model = joblib.load("model.joblib")

def predict(data):
    return model.predict(np.array(data).reshape(1, -1)).tolist()
