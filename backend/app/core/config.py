from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

# .env fica na raiz do projeto (cortex/), três níveis acima deste arquivo
ENV_FILE = Path(__file__).resolve().parents[3] / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    database_url: str


settings = Settings()
