from src.agents.base_agent import BaseAgent
from src.mcp_servers.trekksoft_mcp import mcp_get_daily_bookings
from src.mcp_servers.ms_graph_mcp import mcp_search_outlook

class ManagementAgent(BaseAgent):
    """
    Management Agent: Responsible for generating consolidated daily business summaries,
    booking reports, revenue performance metrics, and operational overviews for executive leadership.
    """
    def __init__(self):
        system_prompt = (
            "You are the central Management Agent for executive leadership of a Swiss tourism SME. "
            "Your role is to aggregate information across Sales, Booking, Operations, Marketing, and Accounting "
            "to provide concise, actionable business intelligence reports."
        )
        super().__init__(
            name="ManagementAgent",
            role_description="Generates executive business intelligence reports and activity summaries.",
            system_prompt=system_prompt
        )

        self.register_tool(
            name="get_daily_bookings",
            description="Retrieve booking metrics and daily activity from TrekkSoft.",
            input_schema={
                "type": "object",
                "properties": {
                    "booking_date": {"type": "string"}
                }
            },
            handler=mcp_get_daily_bookings
        )

        self.register_tool(
            name="search_outlook",
            description="Retrieve executive communications from Outlook.",
            input_schema={
                "type": "object",
                "properties": {
                    "query": {"type": "string"}
                },
                "required": ["query"]
            },
            handler=mcp_search_outlook
        )

management_agent = ManagementAgent()
