from typing import Any

from app.integrations.llm.base import LLMClient


class OpenAILLMClient(LLMClient):
    def __init__(self, api_key: str, model: str) -> None:
        # Keep the web application bootable even when an LLM SDK is not installed
        # yet (for example, before optional local dependencies are installed).
        try:
            from openai import AsyncOpenAI
        except ImportError as exc:  # pragma: no cover - dependency is declared in pyproject
            raise RuntimeError("Install the openai package to use the OpenAI provider") from exc

        self._client: Any = AsyncOpenAI(api_key=api_key)
        self._model = model

    async def complete_json(self, *, system_prompt: str, user_prompt: str) -> str:
        response = await self._client.responses.create(
            model=self._model,
            instructions=system_prompt,
            input=user_prompt,
            text={"format": {"type": "json_object"}},
        )
        return response.output_text
