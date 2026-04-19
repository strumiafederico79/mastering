import json
from pathlib import Path
from app.core.paths import JOBS_DIR

def job_path(job_id: str) -> Path:
    return JOBS_DIR / f"{job_id}.json"

def write_job(job_id: str, payload: dict) -> None:
    job_path(job_id).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

def read_job(job_id: str) -> dict:
    path = job_path(job_id)
    if not path.exists():
        raise FileNotFoundError(job_id)
    return json.loads(path.read_text(encoding="utf-8"))
