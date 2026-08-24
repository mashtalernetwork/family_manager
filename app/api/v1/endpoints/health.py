from fastapi import APIRouter

router = APIRouter()


@router.get("/health", summary="Service readiness check")
async def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
