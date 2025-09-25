from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict

app = FastAPI(
    title="ML CI/CD Demo API",
    description="Une API de prédiction pour Iris avec CI/CD et déploiement via Render.",
    version="1.0.0",
    docs_url="/docs",  # URL de Swagger UI
    redoc_url="/redoc"  # URL alternative (ReDoc)
)

@app.get("/")
def root():
    return {
        "message": "Bienvenue sur l'API de prédiction Iris 🌸. Rendez-vous sur /docs pour essayer l'API."
    }

class PredictionRequest(BaseModel):
    features: list[float]

@app.post("/predict")
def make_prediction(request: PredictionRequest):
    result = predict(request.features)
    return {"prediction": result}

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
