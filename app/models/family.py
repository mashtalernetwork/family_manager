import uuid
from enum import StrEnum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin


class MemberRole(StrEnum):
    PARENT = "parent"
    CHILD = "child"


class Family(TimestampMixin, Base):
    __tablename__ = "families"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(120))
    timezone: Mapped[str] = mapped_column(String(64), default="Europe/Moscow")
    members: Mapped[list["FamilyMember"]] = relationship(back_populates="family")


class FamilyMember(TimestampMixin, Base):
    __tablename__ = "family_members"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    family_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("families.id", ondelete="CASCADE"))
    name: Mapped[str] = mapped_column(String(120))
    role: Mapped[MemberRole] = mapped_column(
        SAEnum(
            MemberRole,
            native_enum=False,
            create_constraint=True,
            values_callable=lambda roles: [role.value for role in roles],
        ),
        default=MemberRole.PARENT,
    )
    timezone: Mapped[str | None] = mapped_column(String(64), nullable=True)
    family: Mapped[Family] = relationship(back_populates="members")
