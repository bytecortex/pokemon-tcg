from pathlib import Path
from dotenv import load_dotenv
import os

if os.getenv("APP_ENV") != "production":
    env_path = Path(__file__).resolve().parents[2] / ".env"
    load_dotenv(env_path)

class Settings:
    APP_ENV = os.getenv("APP_ENV", "development")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

settings = Settings()
