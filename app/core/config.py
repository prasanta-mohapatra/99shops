from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = Field("99Shops", env="APP_NAME")
    debug: bool = Field(False, env="DEBUG")
    database_name: str = Field(..., env="DATABASE_NAME")
    database_id: str = Field(..., env="DATABASE_ID")
    database_password: str = Field(..., env="DATABASE_PASSWORD")


settings = Settings()
