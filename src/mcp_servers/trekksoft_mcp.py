from typing import Dict, Any, List, Optional
from src.integrations.trekksoft_client import trekksoft_client
from src.hitl.approval_engine import hitl_gateway, RiskLevel
from src.hitl.audit_logger import audit_logger

def mcp_get_daily_bookings(booking_date: Optional[str] = None) -> Dict[str, Any]:
    """
    MCP Tool: Retrieve list of bookings for a specific date (defaults to today).
    Risk Level: LOW
    """
    eval_result = hitl_gateway.evaluate_action(
        agent_name="BookingAgent",
        tool_name="get_daily_bookings",
        parameters={"booking_date": booking_date},
        risk_level=RiskLevel.LOW,
        description=f"Fetch daily bookings for date {booking_date or 'today'}"
    )

    bookings = trekksoft_client.get_bookings(booking_date=booking_date)
    
    audit_logger.log_event(
        event_type="MCP_TOOL_EXECUTION",
        agent_name="BookingAgent",
        user_id="claude_user",
        action="get_daily_bookings",
        details={"booking_date": booking_date, "count": len(bookings)}
    )

    return {
        "status": "success",
        "count": len(bookings),
        "bookings": bookings
    }

def mcp_get_booking_details(booking_id: str) -> Dict[str, Any]:
    """
    MCP Tool: Retrieve detailed information for a specific booking ID.
    Risk Level: LOW
    """
    hitl_gateway.evaluate_action(
        agent_name="BookingAgent",
        tool_name="get_booking_details",
        parameters={"booking_id": booking_id},
        risk_level=RiskLevel.LOW,
        description=f"Fetch details for booking ID {booking_id}"
    )

    details = trekksoft_client.get_booking_details(booking_id)
    return {
        "status": "success",
        "booking_details": details
    }

def mcp_cancel_booking(booking_id: str, reason: str) -> Dict[str, Any]:
    """
    MCP Tool: Cancel a customer booking.
    Risk Level: HIGH (Requires Human-in-the-Loop Approval)
    """
    eval_result = hitl_gateway.evaluate_action(
        agent_name="BookingAgent",
        tool_name="cancel_booking",
        parameters={"booking_id": booking_id, "reason": reason},
        risk_level=RiskLevel.HIGH,
        description=f"Cancel booking {booking_id}. Reason: {reason}"
    )

    # High-risk action triggers HITL gate
    return eval_result
