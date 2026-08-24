from uuid import UUID

from app.schemas.common import APIModel


class MemberContribution(APIModel):
    member_id: UUID
    member_name: str
    completed_tasks: int
    workload_points: int


class FamilyStatistics(APIModel):
    family_id: UUID
    period_start: str
    period_end: str
    contributions: list[MemberContribution]
