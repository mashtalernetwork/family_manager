from fastapi import APIRouter, HTTPException, status

from app.schemas.invitation import InvitationCreate, InvitationRead

router = APIRouter()


@router.post("", response_model=InvitationRead, status_code=status.HTTP_201_CREATED)
async def create_invitation(payload: InvitationCreate) -> InvitationRead:
    """Creates an invitation link/code for joining a family."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Coming soon")
