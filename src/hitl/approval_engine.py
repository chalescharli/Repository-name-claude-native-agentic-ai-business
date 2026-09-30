from typing import Dict, Any, Optional, Callable
from enum import Enum
from pydantic import BaseModel, Field
import uuid
from datetime import datetime, timezone
from config.logging_config import logger
from src.integrations.ms_graph_client import ms_graph_client
from src.integrations.trekksoft_client import trekksoft_client

class RiskLevel(str, Enum):
    LOW = "low"         # Read-only queries (e.g. search bookings, get docs)
    MEDIUM = "medium"   # Creating email drafts, staging data
    HIGH = "high"       # Sending emails, cancelling bookings, creating invoices

class ActionStatus(str, Enum):
    PENDING_APPROVAL = "pending_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXECUTED = "executed"
    FAILED = "failed"

class ProposedAction(BaseModel):
    action_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    agent_name: str
    tool_name: str
    risk_level: RiskLevel
    description: str
    parameters: Dict[str, Any]
    created_at: str = Field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    status: ActionStatus = ActionStatus.PENDING_APPROVAL
    approval_comment: Optional[str] = None

class HumanInTheLoopGateway:
    def __init__(self):
        self._pending_actions: Dict[str, ProposedAction] = {}
        self._execution_handlers: Dict[str, Callable] = {}
        self._register_default_handlers()

    def _register_default_handlers(self):
        """Register default API client callbacks for executable tools."""
        self.register_execution_handler("create_email_draft", ms_graph_client.create_email_draft)
        self.register_execution_handler("send_email", ms_graph_client.send_email)
        self.register_execution_handler("cancel_booking", lambda booking_id, reason: {"status": "CANCELLED", "booking_id": booking_id, "reason": reason})
        self.register_execution_handler("prepare_brevo_campaign", lambda campaign_name, target_segment, email_body: {"status": "CAMPAIGN_STAGED", "campaign_name": campaign_name})

    def register_execution_handler(self, tool_name: str, handler: Callable):
        """Register the actual API execution callback for a tool."""
        self._execution_handlers[tool_name] = handler

    def evaluate_action(
        self,
        agent_name: str,
        tool_name: str,
        parameters: Dict[str, Any],
        risk_level: RiskLevel,
        description: str
    ) -> Dict[str, Any]:
        action = ProposedAction(
            agent_name=agent_name,
            tool_name=tool_name,
            risk_level=risk_level,
            description=description,
            parameters=parameters
        )

        if risk_level == RiskLevel.LOW:
            action.status = ActionStatus.APPROVED
            logger.info(f"[HITL Auto-Approved] Agent: {agent_name}, Tool: {tool_name}")
            return {
                "requires_approval": False,
                "action": action.model_dump(),
                "message": "Action auto-approved due to LOW risk classification."
            }

        # Store for approval
        self._pending_actions[action.action_id] = action
        logger.warning(
            f"[HITL Approval Required] Action ID: {action.action_id}, "
            f"Agent: {agent_name}, Tool: {tool_name}, Risk: {risk_level.value}"
        )
        return {
            "requires_approval": True,
            "action_id": action.action_id,
            "action": action.model_dump(),
            "message": f"Action requires Human-in-the-Loop approval before execution. Pending ID: {action.action_id}"
        }

    def approve_and_execute(self, action_id: str, approver_id: str, comment: Optional[str] = None) -> Dict[str, Any]:
        """Approve and execute a pending high-risk action."""
        if action_id not in self._pending_actions:
            return {"success": False, "error": f"Action ID {action_id} not found or already processed."}

        action = self._pending_actions[action_id]
        action.status = ActionStatus.APPROVED
        action.approval_comment = f"Approved by {approver_id}. Comment: {comment or 'N/A'}"

        tool_name = action.tool_name
        if tool_name not in self._execution_handlers:
            action.status = ActionStatus.FAILED
            return {"success": False, "error": f"No execution handler registered for tool '{tool_name}'."}

        try:
            handler = self._execution_handlers[tool_name]
            result = handler(**action.parameters)
            action.status = ActionStatus.EXECUTED
            logger.info(f"[HITL Executed Successfully] Action ID: {action_id}")
            return {
                "success": True,
                "action_id": action_id,
                "result": result
            }
        except Exception as e:
            action.status = ActionStatus.FAILED
            logger.error(f"[HITL Execution Error] Action ID: {action_id}, Error: {str(e)}")
            return {"success": False, "action_id": action_id, "error": str(e)}

    def reject_action(self, action_id: str, approver_id: str, reason: str) -> Dict[str, Any]:
        """Reject a pending action."""
        if action_id not in self._pending_actions:
            return {"success": False, "error": f"Action ID {action_id} not found."}

        action = self._pending_actions[action_id]
        action.status = ActionStatus.REJECTED
        action.approval_comment = f"Rejected by {approver_id}. Reason: {reason}"
        logger.info(f"[HITL Action Rejected] Action ID: {action_id} by {approver_id}")
        return {"success": True, "action_id": action_id, "status": "rejected"}

    def get_pending_actions(self) -> Dict[str, Dict[str, Any]]:
        return {k: v.model_dump() for k, v in self._pending_actions.items() if v.status == ActionStatus.PENDING_APPROVAL}

# Global singleton HITL Gateway
hitl_gateway = HumanInTheLoopGateway()
