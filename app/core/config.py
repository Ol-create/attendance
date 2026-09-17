from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App
    APP_NAME: str = "Student Attendance API"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str

    # JWT / Auth
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()