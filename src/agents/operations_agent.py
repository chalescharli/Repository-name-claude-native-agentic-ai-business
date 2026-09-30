from src.agents.base_agent import BaseAgent
from src.mcp_servers.ms_graph_mcp import (
    mcp_search_sharepoint_sop,
    mcp_search_outlook
)

class OperationsAgent(BaseAgent):
    """
    Operations Agent: Responsible for searching SharePoint documents, retrieving
    internal company SOPs, procedures, policies, and checking operational Outlook messages.
    """
    def __init__(self):
        system_prompt = (
            "You are the specialized Operations Agent for a Swiss tourism and activity SME. "
            "Your role is to help employees and management access company procedures, SOPs, "
            "weather cancellation rules, and internal SharePoint documents."
        )
        super().__init__(
            name="OperationsAgent",
            role_description="Searches SharePoint documents and retrieves operational SOPs.",
            system_prompt=system_prompt
        )
        
        self.register_tool(
            name="search_sharepoint_sop",
            description="Search SharePoint company documents and SOP procedures via RAG vector search.",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query for SOP or document"}
                },
                "required": ["query"]
            },
            handler=mcp_search_sharepoint_sop
        )

        self.register_tool(
            name="search_outlook",
            description="Search Outlook email messages for operational inquiries.",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search keyword for Outlook emails"}
                },
                "required": ["query"]
            },
            handler=mcp_search_outlook
        )

operations_agent = OperationsAgent()
