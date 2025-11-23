import os
from functools import lru_cache
from dotenv import load_dotenv

# Load .env when running locally
load_dotenv()

class Settings:
    def __init__(self):
        # AWS Configuration
        self.aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        self.aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        self.aws_region = os.getenv("AWS_REGION", "us-east-1")

        # GCP Configuration
        # Path to service account JSON
        self.gcp_credentials_json = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
        self.gcs_target_bucket = os.getenv("GCS_TARGET_BUCKET")

        # Other
        self.max_retries = int(os.getenv("MAX_RETRIES", "3"))

        # Basic validation
        if not self.gcs_target_bucket:
            raise ValueError("GCS_TARGET_BUCKET environment variable is required")

@lru_cache
def get_settings():
    return Settings()
