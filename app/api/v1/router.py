from fastapi import APIRouter

from app.api.v1.endpoints import ai, families, health, invitations, statistics, tasks

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(families.router, prefix="/families", tags=["families"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(statistics.router, prefix="/statistics", tags=["statistics"])
api_router.include_router(invitations.router, prefix="/invitations", tags=["invitations"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
