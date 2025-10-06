from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="PhysiDigital API",
    version="0.1.0",
    description="Open-source physiotherapy digital assessment system — part of EB2-NIW applied cybersecurity portfolio."
)

# Modelo de dados simulado
class SessionData(BaseModel):
    patient_id: str
    movement: str
    angle: float
    pain_level: int

class ScoreResponse(BaseModel):
    score: float
    recommendation: str

@app.get("/health")
def health():
    return {"status": "ok", "system": "PhysiDigital"}

@app.post("/api/v1/analyze", response_model=ScoreResponse)
def analyze_session(data: SessionData):
    # Exemplo simples de análise
    score = max(0, 100 - data.pain_level * 10 + (data.angle / 2))
    recommendation = "Continue exercise" if score > 70 else "Review with physiotherapist"
    return {"score": round(score, 2), "recommendation": recommendation}
