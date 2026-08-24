from datetime import datetime
from uuid import UUID

from app.schemas.common import APIModel


class InvitationCreate(APIModel):
    family_id: UUID
    expires_at: datetime | None = None


class InvitationRead(APIModel):
    id: UUID
    code: str
    invite_url: str
    expires_at: datetime | None
