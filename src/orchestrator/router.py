from typing import Dict, Any
from src.agents.booking_agent import booking_agent
from src.agents.operations_agent import operations_agent
from src.agents.sales_agent import sales_agent
from src.agents.marketing_agent import marketing_agent
from src.agents.management_agent import management_agent
from config.logging_config import logger

class AgentOrchestrator:
    """
    Central AI Router & Orchestrator.
    Analyzes user intent and routes queries to the appropriate specialized AI Agent.
    """
    def __init__(self):
        self.agents = {
            "booking": booking_agent,
            "operations": operations_agent,
            "sales": sales_agent,
            "marketing": marketing_agent,
            "management": management_agent
        }

    def route_and_execute(self, user_query: str) -> Dict[str, Any]:
        """Classify user intent and route to the target agent."""
        query_lower = user_query.lower()
        
        # Intent classification heuristics
        if any(w in query_lower for w in ["booking", "book", "trekksoft", "tour reservation", "ts-"]):
            target_agent = self.agents["booking"]
        elif any(w in query_lower for w in ["sharepoint", "sop", "procedure", "policy", "cancellation policy", "weather refund"]):
            target_agent = self.agents["operations"]
        elif any(w in query_lower for w in ["sales", "follow-up", "follow up", "email draft", "customer email"]):
            target_agent = self.agents["sales"]
        elif any(w in query_lower for w in ["marketing", "brevo", "campaign", "newsletter", "segment"]):
            target_agent = self.agents["marketing"]
        elif any(w in query_lower for w in ["summary", "report", "business activity", "executive", "daily summary"]):
            target_agent = self.agents["management"]
        else:
            # Default to Operations Agent for general company queries
            target_agent = self.agents["operations"]

        logger.info(f"[Orchestrator Router] Routing query to '{target_agent.name}'")
        execution_result = target_agent.execute(user_query)
        
        return {
            "query": user_query,
            "routed_to": target_agent.name,
            "execution": execution_result
        }

orchestrator = AgentOrchestrator()
