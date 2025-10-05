
# PhysiDigital™ – Smart Infrastructure Security Monitor

Simulated IoT/OT monitoring for buildings/energy/transport. Edge agents publish sensor events; central FastAPI aggregates, scores risk, and exposes a real-time view.

## Features
- MQTT-like ingestion (HTTP emulation) with agent token
- Simple anomaly flags (thresholds & sudden drift)
- Batch CSV scoring for demo
- Docker & CI ready

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn physidigital.main:app --reload --port 8000
# http://localhost:8000/docs
```
