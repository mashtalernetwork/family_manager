from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.statistics import FamilyStatistics

router = APIRouter()


@router.get("/workload", response_model=FamilyStatistics)
async def get_workload(family_id: UUID = Query()) -> FamilyStatistics:
    """Data source for the 'Who did how much' screen."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Coming soon")
