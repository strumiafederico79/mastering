from typing import Any
from pydantic import BaseModel

class JobCreateResponse(BaseModel):
    job_id: str
    task_id: str
    status: str

class JobStatusResponse(BaseModel):
    job_id: str
    task_id: str | None = None
    status: str
    progress: int = 0
    message: str | None = None
    mode: str | None = None
    profile: str | None = None
    analysis: dict[str, Any] = {}
    decision: dict[str, Any] = {}
    chain: dict[str, Any] = {}
    metrics: dict[str, Any] = {}
    outputs: dict[str, Any] = {}
    issues: list[str] = []
    error: str | None = None
