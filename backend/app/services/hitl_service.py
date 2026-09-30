from typing import Dict, Any, Optional
from src.hitl.approval_engine import hitl_gateway

class HITLService:
    def get_pending_actions(self) -> Dict[str, Any]:
        return hitl_gateway.get_pending_actions()

    def approve_action(self, action_id: str, approver_id: str, comment: Optional[str] = None) -> Dict[str, Any]:
        return hitl_gateway.approve_and_execute(action_id=action_id, approver_id=approver_id, comment=comment)

    def reject_action(self, action_id: str, approver_id: str, reason: str) -> Dict[str, Any]:
        return hitl_gateway.reject_action(action_id=action_id, approver_id=approver_id, reason=reason)

hitl_service = HITLService()
