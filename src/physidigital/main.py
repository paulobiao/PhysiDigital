
from fastapi import FastAPI, UploadFile, File, HTTPException
from .models import SensorEvent, ScoreResponse
from .rules import score_event
import pandas as pd, io, csv

app = FastAPI(title="PhysiDigital API", version="0.1.0")

@app.get("/health")
def health(): return {"status": "ok"}

@app.post("/api/v1/ingest", response_model=ScoreResponse)
def ingest(ev: SensorEvent):
    s, r, f = score_event(ev.model_dump())
    return ScoreResponse(score=s, reasons=r, flags=f)

@app.post("/api/v1/ingest/batch")
async def ingest_batch(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(400, "Upload a CSV")
    content = await file.read()
    df = pd.read_csv(io.BytesIO(content))
    out = []
    for _, row in df.iterrows():
        s, r, f = score_event(row.to_dict())
        out.append({"node_id": row.get("node_id"), "score": s, "reasons": r, "flags": f})
    return {"count": len(out), "results": out}
