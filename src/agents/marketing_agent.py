from src.agents.base_agent import BaseAgent
from src.hitl.approval_engine import hitl_gateway, RiskLevel

def mcp_prepare_brevo_campaign(campaign_name: str, target_segment: str, email_body: str):
    """MCP Tool: Create Brevo Email Campaign Draft."""
    return hitl_gateway.evaluate_action(
        agent_name="MarketingAgent",
        tool_name="prepare_brevo_campaign",
        parameters={"campaign_name": campaign_name, "target_segment": target_segment, "email_body": email_body},
        risk_level=RiskLevel.MEDIUM,
        description=f"Create Brevo Email Campaign draft '{campaign_name}' targeting '{target_segment}'"
    )

class MarketingAgent(BaseAgent):
    """
    Marketing Agent: Responsible for Brevo marketing integration, campaign drafts,
    customer segmentation, and promotional messages.
    """
    def __init__(self):
        system_prompt = (
            "You are the specialized Marketing Agent for a Swiss tourism SME. "
            "Your role is to assist with preparing email marketing campaigns in Brevo, "
            "segmenting customers, and generating promotional copy."
        )
        super().__init__(
            name="MarketingAgent",
            role_description="Manages Brevo marketing campaigns and customer outreach.",
            system_prompt=system_prompt
        )

        self.register_tool(
            name="prepare_brevo_campaign",
            description="Prepare a Brevo marketing campaign draft (Requires Approval).",
            input_schema={
                "type": "object",
                "properties": {
                    "campaign_name": {"type": "string"},
                    "target_segment": {"type": "string"},
                    "email_body": {"type": "string"}
                },
                "required": ["campaign_name", "target_segment", "email_body"]
            },
            handler=mcp_prepare_brevo_campaign
        )

marketing_agent = MarketingAgent()
