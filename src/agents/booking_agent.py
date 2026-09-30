from src.agents.base_agent import BaseAgent
from src.mcp_servers.trekksoft_mcp import (
    mcp_get_daily_bookings,
    mcp_get_booking_details,
    mcp_cancel_booking
)

class BookingAgent(BaseAgent):
    """
    Booking Agent: Responsible for TrekkSoft API integration, retrieving bookings,
    checking tour status, and providing human-readable booking summaries.
    """
    def __init__(self):
        system_prompt = (
            "You are the specialized Booking Agent for a Swiss tourism and activity SME. "
            "Your responsibility is to assist management and staff with retrieving customer bookings, "
            "checking tour availability, looking up booking details in TrekkSoft, and summarizing booking data clearly."
        )
        super().__init__(
            name="BookingAgent",
            role_description="Manages TrekkSoft tour & activity bookings.",
            system_prompt=system_prompt
        )
        
        # Register MCP tools
        self.register_tool(
            name="get_daily_bookings",
            description="Retrieve bookings for a given date from TrekkSoft.",
            input_schema={
                "type": "object",
                "properties": {
                    "booking_date": {"type": "string", "description": "Date in YYYY-MM-DD format."}
                }
            },
            handler=mcp_get_daily_bookings
        )
        
        self.register_tool(
            name="get_booking_details",
            description="Fetch detailed information for a specific booking ID from TrekkSoft.",
            input_schema={
                "type": "object",
                "properties": {
                    "booking_id": {"type": "string", "description": "TrekkSoft Booking ID, e.g., TS-1001"}
                },
                "required": ["booking_id"]
            },
            handler=mcp_get_booking_details
        )
        
        self.register_tool(
            name="cancel_booking",
            description="Cancel a customer booking (Requires Human Approval).",
            input_schema={
                "type": "object",
                "properties": {
                    "booking_id": {"type": "string"},
                    "reason": {"type": "string"}
                },
                "required": ["booking_id", "reason"]
            },
            handler=mcp_cancel_booking
        )

booking_agent = BookingAgent()
