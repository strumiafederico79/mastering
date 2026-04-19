from pathlib import Path
from app.core.config import settings

DATA_DIR = Path(settings.data_dir)
UPLOAD_DIR = Path(settings.upload_dir)
OUTPUT_DIR = Path(settings.output_dir)
JOBS_DIR = Path(settings.jobs_dir)
LEARNING_DIR = Path(settings.learning_dir)

for p in [DATA_DIR, UPLOAD_DIR, OUTPUT_DIR, JOBS_DIR, LEARNING_DIR]:
    p.mkdir(parents=True, exist_ok=True)
