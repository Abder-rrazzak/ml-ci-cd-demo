from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict

app = FastAPI()

class IrisInput(BaseModel):
    features: list[float]

@app.post("/predict")
def make_prediction(input_data: IrisInput):
    prediction = predict(input_data.features)
    return {"prediction": prediction}
