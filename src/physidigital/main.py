from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from collections import deque

app = FastAPI(title="PhysiDigital API", version="0.2.0")

class SensorData(BaseModel):
    sensor_id: str
    temperature: float
    vibration: float

WINDOW = 50
temp_hist = deque(maxlen=WINDOW)
vib_hist  = deque(maxlen=WINDOW)

@app.get("/health")
def health():
    return {"status": "ok", "service": "PhysiDigital"}

def zscore(value, history):
    if len(history) < 10:  # warmup
        return 0.0
    mu = np.mean(history)
    sd = np.std(history) or 1.0
    return (value - mu) / sd

@app.post("/api/v1/sensor")
def process_sensor(data: SensorData):
    temp_hist.append(data.temperature)
    vib_hist.append(data.vibration)
    zt = abs(zscore(data.temperature, temp_hist))
    zv = abs(zscore(data.vibration, vib_hist))
    anomaly = (zt > 3.0) or (zv > 3.0)
    score = min(100, int((zt + zv) * 25))  # escala simples
    return {"sensor_id": data.sensor_id, "z_temp": round(zt,2), "z_vib": round(zv,2), "anomaly": anomaly, "score": score}
