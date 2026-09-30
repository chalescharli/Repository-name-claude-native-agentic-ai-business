from pydantic import BaseModel, Field
from typing import Dict, Any, Optional

class UserQueryRequest(BaseModel):
    query: str = Field(..., min_length=1, description="Prompt or instructions for the AI Workforce")
    user_id: Optional[str] = Field("admin_user", description="User identifier")
    provider: Optional[str] = Field("anthropic", description="LLM Provider override (anthropic, openai, gemini)")

class AgentExecutionResult(BaseModel):
    status: str
    data: Dict[str, Any]
