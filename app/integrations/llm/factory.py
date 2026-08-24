from functools import lru_cache

from fastapi import HTTPException, status

from app.core.config import settings
from app.integrations.llm.base import LLMClient
from app.integrations.llm.gigachat import GigaChatLLMClient
from app.integrations.llm.openai import OpenAILLMClient


@lru_cache
def get_llm_client() -> LLMClient:
    if settings.llm_provider == "openai" and settings.openai_api_key:
        return OpenAILLMClient(settings.openai_api_key, settings.openai_model)
    if settings.llm_provider == "gigachat" and settings.gigachat_auth_key:
        return GigaChatLLMClient(
            settings.gigachat_auth_key, settings.gigachat_model, settings.gigachat_scope
        )
    raise HTTPException(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        detail="LLM provider is not configured",
    )
