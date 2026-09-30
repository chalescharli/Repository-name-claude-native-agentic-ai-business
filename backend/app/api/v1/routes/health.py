from fastapi import APIRouter
from backend.app.core.config import settings

router = APIRouter()

@router.get("/health")
def health_check():
    return {
        "status": "online",
        "platform": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "active_agents": ["SalesAgent", "BookingAgent", "OperationsAgent", "MarketingAgent", "ManagementAgent"]
    }
