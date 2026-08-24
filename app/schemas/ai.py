from datetime import datetime
from typing import Literal
from uuid import UUID

from pydantic import Field

from app.schemas.common import APIModel


class TaskExtractionRequest(APIModel):
    family_id: UUID
    content: str = Field(min_length=1, description="Transcript, email text or OCR result")
    source: Literal["voice", "email", "image", "chat"]
    known_members: list[str] = Field(default_factory=list)


class TaskExtractionResult(APIModel):
    title: str
    description: str | None = None
    due_at: datetime | None = None
    suggested_assignee_name: str | None = None
    confidence: float = Field(ge=0, le=1)
    needs_clarification: bool = False
    clarification_question: str | None = None
