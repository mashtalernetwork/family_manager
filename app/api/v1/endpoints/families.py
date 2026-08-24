from fastapi import APIRouter, HTTPException, status

from app.schemas.family import FamilyCreate, FamilyRead

router = APIRouter()


@router.post("", response_model=FamilyRead, status_code=status.HTTP_201_CREATED)
async def create_family(payload: FamilyCreate) -> FamilyRead:
    """Contract for onboarding; persistence is added through FamilyService."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Coming soon")
