from uuid import UUID

from pydantic import Field

from app.schemas.common import APIModel


class FamilyCreate(APIModel):
    name: str = Field(min_length=1, max_length=120, examples=["Семья Ивановых"])
    timezone: str = Field(default="Europe/Moscow", max_length=64)
    owner_name: str = Field(min_length=1, max_length=120, examples=["Анна"])


class FamilyRead(APIModel):
    id: UUID
    name: str
    timezone: str
