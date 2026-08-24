import json

from pydantic import ValidationError

from app.integrations.llm.base import LLMClient
from app.schemas.ai import TaskExtractionRequest, TaskExtractionResult


class TaskExtractionService:
    """Product logic independent of a particular model provider."""

    system_prompt = """
Ты семейный диспетчер. Извлеки из сообщения одну наиболее важную семейную задачу.
Верни только JSON с ключами: title, description, due_at, suggested_assignee_name,
confidence, needs_clarification, clarification_question. due_at используй в ISO 8601
с часовым поясом или null. Не выдумывай дату и исполнителя: при недостатке данных
укажи needs_clarification=true и задай короткий нейтральный вопрос.
""".strip()

    def __init__(self, llm_client: LLMClient) -> None:
        self._llm_client = llm_client

    async def extract(self, request: TaskExtractionRequest) -> TaskExtractionResult:
        members = ", ".join(request.known_members) or "не указаны"
        user_prompt = (
            f"Источник: {request.source}. Известные члены семьи: {members}.\n"
            f"Сообщение:\n{request.content}"
        )
        raw_result = await self._llm_client.complete_json(
            system_prompt=self.system_prompt, user_prompt=user_prompt
        )
        try:
            return TaskExtractionResult.model_validate(json.loads(raw_result))
        except (json.JSONDecodeError, ValidationError) as exc:
            raise ValueError("LLM returned an invalid task extraction payload") from exc
