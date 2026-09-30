import unittest
from src.orchestrator.router import orchestrator
from src.hitl.approval_engine import hitl_gateway, RiskLevel
from src.mcp_servers.trekksoft_mcp import mcp_get_daily_bookings, mcp_cancel_booking
from src.mcp_servers.ms_graph_mcp import mcp_search_sharepoint_sop, mcp_send_email

class TestPlatform(unittest.TestCase):

    def test_booking_agent_daily_bookings(self):
        """Verify Booking Agent retrieves bookings from TrekkSoft MCP tool."""
        res = mcp_get_daily_bookings(booking_date="2026-09-28")
        self.assertEqual(res["status"], "success")
        self.assertGreater(res["count"], 0)
        self.assertIn("bookings", res)

    def test_operations_agent_sharepoint_sop_rag(self):
        """Verify Operations Agent performs vector search for SharePoint SOPs."""
        res = mcp_search_sharepoint_sop(query="cancellation weather refund policy")
        self.assertEqual(res["status"], "success")
        self.assertGreater(len(res["results"]), 0)
        self.assertIn("Cancellation", res["results"][0]["doc_title"])

    def test_hitl_high_risk_action_blocking(self):
        """Verify HIGH risk action (sending email) is held for Human-in-the-Loop approval."""
        eval_res = mcp_send_email(
            recipient="client@swissdomain.ch",
            subject="Booking Confirmation",
            body="Your paragliding trip is confirmed."
        )
        self.assertTrue(eval_res["requires_approval"])
        self.assertIn("action_id", eval_res)
        
        action_id = eval_res["action_id"]
        pending = hitl_gateway.get_pending_actions()
        self.assertIn(action_id, pending)

    def test_hitl_approval_execution_flow(self):
        """Verify approving a pending action executes the underlying handler."""
        eval_res = mcp_send_email(
            recipient="approved_test@swissdomain.ch",
            subject="Important Notice",
            body="Test content"
        )
        action_id = eval_res["action_id"]
        
        # Register execution handler for test
        hitl_gateway.register_execution_handler("send_email", lambda recipient, subject, body: {"status": "SENT_OK"})

        approval_res = hitl_gateway.approve_and_execute(
            action_id=action_id,
            approver_id="manager_user_1",
            comment="Approved by manager"
        )
        self.assertTrue(approval_res["success"])
        self.assertEqual(approval_res["result"]["status"], "SENT_OK")

    def test_orchestrator_routing_cases(self):
        """Test Orchestrator routes prompts to correct specialized agents."""
        q1 = orchestrator.route_and_execute("Show me today's bookings.")
        self.assertEqual(q1["routed_to"], "BookingAgent")

        q2 = orchestrator.route_and_execute("What is our procedure for handling a cancelled tour?")
        self.assertEqual(q2["routed_to"], "OperationsAgent")

        q3 = orchestrator.route_and_execute("Prepare follow-up emails for yesterday's customers.")
        self.assertEqual(q3["routed_to"], "SalesAgent")

        q4 = orchestrator.route_and_execute("Prepare an email campaign for previous customers.")
        self.assertEqual(q4["routed_to"], "MarketingAgent")

        q5 = orchestrator.route_and_execute("Give me a summary of today's business activity.")
        self.assertEqual(q5["routed_to"], "ManagementAgent")

if __name__ == "__main__":
    unittest.main()
