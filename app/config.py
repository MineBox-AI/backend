from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "MineBoxAI"
    VERSION: str = "0.0.1"
    LOG_LEVEL: str = "INFO"
    AUTH0_DOMAIN: str
    AUTH0_API_AUDIENCE: str
    AUTH0_ISSUER: str
    AUTH0_ALGORITHMS: str = "RS256"
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
