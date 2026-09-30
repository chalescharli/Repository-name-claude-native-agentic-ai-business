from typing import Dict, Any, Optional
from src.integrations.ms_graph_client import ms_graph_client
from src.rag.vector_store import knowledge_store
from src.hitl.approval_engine import hitl_gateway, RiskLevel
from src.hitl.audit_logger import audit_logger

def mcp_search_sharepoint_sop(query: str) -> Dict[str, Any]:
    """
    MCP Tool: Search SharePoint company documents and SOP procedures using RAG vector search.
    Risk Level: LOW
    """
    results = knowledge_store.search_knowledge(query=query, top_k=3)
    
    audit_logger.log_event(
        event_type="MCP_TOOL_EXECUTION",
        agent_name="OperationsAgent",
        user_id="claude_user",
        action="search_sharepoint_sop",
        details={"query": query, "results_found": len(results)}
    )

    return {
        "status": "success",
        "query": query,
        "results": results
    }

def mcp_search_outlook(query: str) -> Dict[str, Any]:
    """
    MCP Tool: Search Outlook email messages.
    Risk Level: LOW
    """
    messages = ms_graph_client.search_outlook_messages(query)
    return {
        "status": "success",
        "count": len(messages),
        "messages": messages
    }

def mcp_create_email_draft(recipient: str, subject: str, body: str) -> Dict[str, Any]:
    """
    MCP Tool: Create an email draft in Outlook.
    Risk Level: MEDIUM
    """
    eval_result = hitl_gateway.evaluate_action(
        agent_name="SalesAgent",
        tool_name="create_email_draft",
        parameters={"recipient": recipient, "subject": subject, "body": body},
        risk_level=RiskLevel.MEDIUM,
        description=f"Create email draft for {recipient} with subject '{subject}'"
    )

    if eval_result.get("requires_approval"):
        return eval_result

    res = ms_graph_client.create_email_draft(recipient, subject, body)
    return {"status": "success", "result": res}

def mcp_send_email(recipient: str, subject: str, body: str) -> Dict[str, Any]:
    """
    MCP Tool: Send an email directly via Outlook.
    Risk Level: HIGH (Requires Human-in-the-Loop Approval)
    """
    eval_result = hitl_gateway.evaluate_action(
        agent_name="SalesAgent",
        tool_name="send_email",
        parameters={"recipient": recipient, "subject": subject, "body": body},
        risk_level=RiskLevel.HIGH,
        description=f"Send email directly to {recipient} with subject '{subject}'"
    )

    return eval_result
