from fastapi import FastAPI
from app.config import get_settings

app = FastAPI()
settings = get_settings()

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "gcs_bucket": settings.gcs_target_bucket
    }
