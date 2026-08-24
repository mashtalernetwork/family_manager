import uuid

from app.schemas.ai import TaskExtractionRequest
from app.services.task_extraction import TaskExtractionService


class FakeLLMClient:
    async def complete_json(self, *, system_prompt: str, user_prompt: str) -> str:
        return """{
            "title": "Забрать Мишу с плавания",
            "description": null,
            "due_at": "2026-08-25T18:00:00+03:00",
            "suggested_assignee_name": "Анна",
            "confidence": 0.91,
            "needs_clarification": false,
            "clarification_question": null
        }"""


async def test_extract_task_is_provider_independent() -> None:
    request = TaskExtractionRequest(
        family_id=uuid.uuid4(),
        source="voice",
        content="Аня, завтра в шесть забери Мишу с плавания",
        known_members=["Анна", "Миша"],
    )

    result = await TaskExtractionService(FakeLLMClient()).extract(request)

    assert result.title == "Забрать Мишу с плавания"
    assert result.suggested_assignee_name == "Анна"
    assert result.confidence == 0.91
