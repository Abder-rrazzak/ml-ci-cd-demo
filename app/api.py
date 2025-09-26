from fastapi import FastAPI
from pydantic import BaseModel
from app.predict import predict

# Configuration de l'application FastAPI
app = FastAPI(
    title="ML CI/CD Demo API",
    description="Une API de prédiction pour les fleurs Iris 🌸, avec pipeline CI/CD et déploiement automatique.",
    version="1.0.0",
    docs_url="/docs",    # Swagger UI
    redoc_url="/redoc"   # Documentation ReDoc
)

# 🔹 Route racine (GET /)
@app.get("/")
def root():
    return {
        "message": "Bienvenue sur l'API de prédiction Iris 🌸. Rendez-vous sur /docs pour essayer l'API."
    }

# 🔹 Schéma de la requête pour /predict
class PredictionRequest(BaseModel):
    features: list[float]

# 🔹 Route de prédiction (POST /predict)
@app.post("/predict", tags=["Prédiction"])
def make_prediction(request: PredictionRequest):
    result = predict(request.features)
    return {"prediction": result}

@app.get("/health", tags=["Monitoring"])
def health_check():
    return {"status": "ok", "model_version": "v1"}
