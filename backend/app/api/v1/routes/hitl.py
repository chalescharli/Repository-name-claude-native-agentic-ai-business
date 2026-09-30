from fastapi import APIRouter, HTTPException
from backend.app.schemas.hitl_schemas import HITLApprovalRequest, HITLRejectionRequest
from backend.app.services.hitl_service import hitl_service

router = APIRouter()

@router.get("/pending")
def get_pending_approvals():
    """Retrieve all high-risk actions pending human approval."""
    return {"pending_actions": hitl_service.get_pending_actions()}

@router.post("/approve")
def approve_action(request: HITLApprovalRequest):
    """Approve and execute a pending high-risk action."""
    res = hitl_service.approve_action(
        action_id=request.action_id,
        approver_id=request.approver_id,
        comment=request.comment
    )
    if not res.get("success"):
        raise HTTPException(status_code=400, detail=res.get("error"))
    return res

@router.post("/reject")
def reject_action(request: HITLRejectionRequest):
    """Reject a pending action."""
    res = hitl_service.reject_action(
        action_id=request.action_id,
        approver_id=request.approver_id,
        reason=request.reason
    )
    return res
