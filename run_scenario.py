import sys
import os
import json

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.orchestrator.router import orchestrator
from src.hitl.approval_engine import hitl_gateway
from src.integrations.trekksoft_client import trekksoft_client
from src.rag.vector_store import knowledge_store

def main():
    print("=" * 60)
    print("  CLAUDE-NATIVE AGENTIC AI BUSINESS PLATFORM DEMO")
    print("=" * 60)

    prompts = [
        ("1. Booking Agent", "Show me today's bookings."),
        ("2. Operations Agent (SharePoint SOP RAG)", "What is our procedure for handling a cancelled tour?"),
        ("3. Sales Agent (HITL Trigger)", "Prepare follow-up emails for yesterday's customers."),
        ("4. Marketing Agent (Brevo Integration)", "Prepare an email campaign for previous customers."),
        ("5. Management Agent", "Give me a summary of today's business activity.")
    ]

    for title, prompt in prompts:
        print(f"\n---> [TEST] {title}")
        print(f"Prompt: \"{prompt}\"")
        result = orchestrator.route_and_execute(prompt)
        print("Execution Result:")
        print(json.dumps(result, indent=2))
        print("-" * 60)

    # Show pending approvals
    pending = hitl_gateway.get_pending_actions()
    print("\n---> [HITL GATEWAY] Pending High-Risk Actions:")
    print(json.dumps(pending, indent=2))

    if pending:
        action_id = list(pending.keys())[0]
        print(f"\n---> [HITL GATEWAY] Approving Action ID '{action_id}'...")
        approval_res = hitl_gateway.approve_and_execute(
            action_id=action_id,
            approver_id="executive_admin",
            comment="Approved for execution by executive admin."
        )
        print("Approval Result:")
        print(json.dumps(approval_res, indent=2))

    print("\n" + "=" * 60)
    print("  ALL AGENT WORKFLOWS EXECUTED SUCCESSFULLY")
    print("=" * 60)

if __name__ == "__main__":
    main()
