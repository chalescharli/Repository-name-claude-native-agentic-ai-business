from fastapi import APIRouter, HTTPException
from backend.app.schemas.agent_schemas import UserQueryRequest, AgentExecutionResult
from backend.app.services.orchestrator_service import orchestrator_service
from config.logging_config import logger

router = APIRouter()

@router.post("/query", response_model=AgentExecutionResult)
def process_query(request: UserQueryRequest):
    """Process user prompt through Orchestrator service."""
    try:
        result = orchestrator_service.execute_query(request.query)
        return AgentExecutionResult(status="success", data=result)
    except Exception as e:
        logger.error(f"[Agents API] Query execution error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
