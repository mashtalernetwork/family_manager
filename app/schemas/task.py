from datetime import datetime
from uuid import UUID

from pydantic import Field

from app.models.task import TaskSource, TaskStatus
from app.schemas.common import APIModel


class TaskCreate(APIModel):
    family_id: UUID
    title: str = Field(min_length=1, max_length=255, examples=["Забрать Мишу с плавания"])
    description: str | None = None
    assignee_id: UUID | None = None
    due_at: datetime | None = None
    priority: int = Field(default=3, ge=1, le=5)


class TaskRead(APIModel):
    id: UUID
    family_id: UUID
    title: str
    description: str | None
    assignee_id: UUID | None
    due_at: datetime | None
    status: TaskStatus
    source: TaskSource
    priority: int
