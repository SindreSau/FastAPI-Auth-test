# Handles loading of environment variables and configuration settings
from pydantic import BaseSettings


class Settings(BaseSettings):
    API_KEY: str

    class Config:
        env_file = ".env"


def get_settings():
    return Settings()
