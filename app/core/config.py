import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True

    APP_NAME: str = "99Shops"
    APP_VERSION: float = 1.0
    DEBUG: bool = False
    DATABASE_HOST: str = "127.0.0.1"
    DATABASE_NAME: str
    DATABASE_NAME_TEST: str = "test_99shops"
    DATABASE_ID: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int = 5432
    TESTING: bool = False
    NOMINATION_URL: str = "https://nominatim.openstreetmap.org"
    CONTACT: str = "mohapatraprasant98@gmail.com"
    BASE_URL: str = "127.0.0.1:8000"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    ALLOWED_ORIGINS: str
    DATABASE_URL: Optional[str]

    @property
    def ALLOWED_ORIGINS_LIST(self) -> list:
        return self.ALLOWED_ORIGINS.split(",")

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        if not self.TESTING and self.DATABASE_URL:
            return self.DATABASE_URL
        databasename = self.DATABASE_NAME
        if self.TESTING:
            databasename = self.DATABASE_NAME_TEST

        return f"postgresql://{self.DATABASE_ID}:{self.DATABASE_PASSWORD}@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{databasename}"


settings = Settings()  # type: ignore
