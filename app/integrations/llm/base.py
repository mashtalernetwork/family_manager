from typing import Protocol


class LLMClient(Protocol):
    async def complete_json(self, *, system_prompt: str, user_prompt: str) -> str:
        """Return a JSON object as text, without any persistence concerns."""
