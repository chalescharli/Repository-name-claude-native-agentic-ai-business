from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class HITLApprovalRequest(BaseModel):
    action_id: str = Field(..., description="Unique Action UUID pending approval")
    approver_id: str = Field(..., description="ID or email of the human approver")
    comment: Optional[str] = Field(None, description="Optional approval notes")

class HITLRejectionRequest(BaseModel):
    action_id: str = Field(..., description="Unique Action UUID pending approval")
    approver_id: str = Field(..., description="ID or email of the rejecting user")
    reason: str = Field(..., min_length=1, description="Reason for action rejection")
