from typing import Dict, Any
from src.orchestrator.router import orchestrator

class OrchestratorService:
    def execute_query(self, user_query: str) -> Dict[str, Any]:
        """Delegate intent routing and agent execution to the core orchestrator."""
        return orchestrator.route_and_execute(user_query)

orchestrator_service = OrchestratorService()
