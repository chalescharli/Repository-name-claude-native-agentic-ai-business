from fastapi import APIRouter
from backend.app.api.v1.routes import agents, hitl, health

api_router = APIRouter()
api_router.include_router(health.router, tags=["Health"])
api_router.include_router(agents.router, tags=["Agents"])
api_router.include_router(hitl.router, prefix="/hitl", tags=["HITL Safety"])
