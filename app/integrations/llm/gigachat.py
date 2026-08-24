import uuid

import httpx

from app.integrations.llm.base import LLMClient


class GigaChatLLMClient(LLMClient):
    """GigaChat adapter with token retrieval isolated from product services."""

    oauth_url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
    completions_url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    def __init__(self, auth_key: str, model: str, scope: str) -> None:
        self._auth_key = auth_key
        self._model = model
        self._scope = scope

    async def _access_token(self, client: httpx.AsyncClient) -> str:
        response = await client.post(
            self.oauth_url,
            headers={"RqUID": str(uuid.uuid4()), "Authorization": f"Basic {self._auth_key}"},
            data={"scope": self._scope},
        )
        response.raise_for_status()
        return response.json()["access_token"]

    async def complete_json(self, *, system_prompt: str, user_prompt: str) -> str:
        async with httpx.AsyncClient(timeout=30) as client:
            token = await self._access_token(client)
            response = await client.post(
                self.completions_url,
                headers={"Authorization": f"Bearer {token}"},
                json={
                    "model": self._model,
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt},
                    ],
                    "response_format": {"type": "json_object"},
                },
            )
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]
