from pydantic import BaseSettings


class Settings(BaseSettings):
    """App settings."""

    PROJECT_NAME: str = "debug_hell"
    DEBUG: bool = False
    ENVIRONMENT: str = "local"

    # API
    RATE_LIMIT: int = 10
    CORS_ALLOW_ORIGINS: list[str] = []
    API_PREFIX: str = "/dbg"

    # Database
    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
