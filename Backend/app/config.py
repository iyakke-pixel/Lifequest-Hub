import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

class Settings:
    PROJECT_NAME: str = os.getenv("APP_NAME", "LifeQuest Hub")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./lifequest.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default-secret-key")

settings = Settings()