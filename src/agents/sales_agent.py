from src.agents.base_agent import BaseAgent
from src.mcp_servers.ms_graph_mcp import (
    mcp_create_email_draft,
    mcp_send_email
)
from src.mcp_servers.trekksoft_mcp import mcp_get_daily_bookings

class SalesAgent(BaseAgent):
    """
    Sales Agent: Responsible for retrieving customer booking info, preparing sales follow-ups,
    generating email drafts, and handling sales questions.
    """
    def __init__(self):
        system_prompt = (
            "You are the specialized Sales Agent for a Swiss tourism SME. "
            "Your role is to assist with sales queries, customer follow-up emails, "
            "sales summaries, and preparing email drafts for human approval."
        )
        super().__init__(
            name="SalesAgent",
            role_description="Handles sales queries, customer follow-ups, and email drafts.",
            system_prompt=system_prompt
        )

        self.register_tool(
            name="get_daily_bookings",
            description="Retrieve recent customer bookings for sales follow-ups.",
            input_schema={
                "type": "object",
                "properties": {
                    "booking_date": {"type": "string"}
                }
            },
            handler=mcp_get_daily_bookings
        )

        self.register_tool(
            name="create_email_draft",
            description="Create an email draft in Outlook (Requires approval).",
            input_schema={
                "type": "object",
                "properties": {
                    "recipient": {"type": "string"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["recipient", "subject", "body"]
            },
            handler=mcp_create_email_draft
        )

        self.register_tool(
            name="send_email",
            description="Send an email directly via Outlook (Requires HITL Approval).",
            input_schema={
                "type": "object",
                "properties": {
                    "recipient": {"type": "string"},
                    "subject": {"type": "string"},
                    "body": {"type": "string"}
                },
                "required": ["recipient", "subject", "body"]
            },
            handler=mcp_send_email
        )

sales_agent = SalesAgent()
