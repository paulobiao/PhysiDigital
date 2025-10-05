
from pydantic import BaseModel
from typing import Optional

class SensorEvent(BaseModel):
    node_id: str
    metric: str  # temperature, power, flow
    value: float
    ts: Optional[str] = None
    token: Optional[str] = None

class ScoreResponse(BaseModel):
    score: int
    reasons: list[str]
    flags: dict
