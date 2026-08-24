from fastapi import APIRouter, Depends

from app.integrations.llm.base import LLMClient
from app.integrations.llm.factory import get_llm_client
from app.schemas.ai import TaskExtractionRequest, TaskExtractionResult
from app.services.task_extraction import TaskExtractionService

router = APIRouter()


@router.post("/extract-task", response_model=TaskExtractionResult)
async def extract_task(
    payload: TaskExtractionRequest,
    llm_client: LLMClient = Depends(get_llm_client),
) -> TaskExtractionResult:
    """Turns text transcriptions, emails or OCR text into a task draft."""
    return await TaskExtractionService(llm_client).extract(payload)
