from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="ignore")

    app_name: str = "Family Manager API"
    environment: str = "local"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"
    database_url: str = "postgresql+asyncpg://family_manager:family_manager@localhost:5432/family_manager"

    llm_provider: Literal["openai", "gigachat", "disabled"] = "disabled"
    openai_api_key: str | None = None
    openai_model: str = "gpt-5-mini"
    gigachat_auth_key: str | None = None
    gigachat_model: str = "GigaChat-2-Max"
    gigachat_scope: str = "GIGACHAT_API_PERS"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
