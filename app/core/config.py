import os

from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Settings(BaseSettings):
    class Config:
        env_file = ".env"
        case_sensitive = True

    APP_NAME: str = "99Shops"
    DEBUG: bool = False
    DATABASE_NAME: str
    DATABASE_NAME_TEST: str = "TEST_99Shops"
    DATABASE_ID: str
    DATABASE_PASSWORD: str
    TESTING: bool = False

    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        databasename = self.DATABASE_NAME
        if self.TESTING:
            databasename = self.DATABASE_NAME_TEST

        return (
            f"postgresql://{settings.DATABASE_ID}:{settings.DATABASE_PASSWORD}"
            f"@localhost/{databasename}"
        )


settings = Settings()
