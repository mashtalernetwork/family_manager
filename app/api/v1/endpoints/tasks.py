from uuid import UUID

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.task import TaskCreate, TaskRead

router = APIRouter()


@router.get("/today", response_model=list[TaskRead])
async def get_today_tasks(family_id: UUID = Query()) -> list[TaskRead]:
    """Data source for the Today's tasks screen."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Coming soon")


@router.post("", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(payload: TaskCreate) -> TaskRead:
    """Contract for manual task creation: who, what, when."""
    raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="Coming soon")
