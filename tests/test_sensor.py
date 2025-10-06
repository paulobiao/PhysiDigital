from fastapi.testclient import TestClient
from src.physidigital.main import app

def test_sensor_analyze():
    c = TestClient(app)
    r = c.post("/api/v1/sensor", json={"sensor_id":"s","temperature":70.0,"vibration":1.0})
    assert r.status_code == 200
    j = r.json()
    assert "anomaly" in j and "score" in j
