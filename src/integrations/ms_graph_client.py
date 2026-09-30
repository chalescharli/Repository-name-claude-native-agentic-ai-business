from typing import List, Dict, Any, Optional
import httpx
from config.settings import settings
from config.logging_config import logger

class MSGraphClient:
    """Client for Microsoft Graph API (SharePoint & Outlook integration)."""
    def __init__(self):
        self.client_id = settings.MS_GRAPH_CLIENT_ID
        self.client_secret = settings.MS_GRAPH_CLIENT_SECRET
        self.tenant_id = settings.MS_GRAPH_TENANT_ID
        self.site_id = settings.MS_GRAPH_SHAREPOINT_SITE_ID
        self.base_url = "https://graph.microsoft.com/v1.0"
        self._access_token: Optional[str] = None

    def search_sharepoint_documents(self, query: str) -> List[Dict[str, Any]]:
        """Search company documents in SharePoint."""
        if not self.client_id:
            logger.info("[MS Graph Mock Mode] Searching SharePoint mock documents.")
            return self._mock_sharepoint_search(query)
            
        # Graph API call implementation
        return self._mock_sharepoint_search(query)

    def search_outlook_messages(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Search emails in Outlook."""
        if not self.client_id:
            logger.info("[MS Graph Mock Mode] Searching Outlook mock emails.")
            return self._mock_outlook_search(query, limit)
            
        return self._mock_outlook_search(query, limit)

    def create_email_draft(self, recipient: str, subject: str, body: str) -> Dict[str, Any]:
        """Create an email draft in Outlook."""
        logger.info(f"[MS Graph] Created email draft for {recipient} with subject '{subject}'")
        return {
            "draft_id": "draft_msg_99812",
            "recipient": recipient,
            "subject": subject,
            "body": body,
            "status": "DRAFT_CREATED"
        }

    def send_email(self, recipient: str, subject: str, body: str) -> Dict[str, Any]:
        """Send an email directly via Outlook (Requires HITL Approval)."""
        logger.info(f"[MS Graph] Email sent to {recipient}")
        return {
            "recipient": recipient,
            "subject": subject,
            "status": "SENT"
        }

    def _mock_sharepoint_search(self, query: str) -> List[Dict[str, Any]]:
        docs = [
            {
                "doc_id": "sp_doc_001",
                "title": "Tour Cancellation & Weather Refund Standard Operating Procedure (SOP)",
                "category": "Operations",
                "content": (
                    "Cancellation Policy: If a tour is cancelled due to severe weather (e.g. high winds during paragliding), "
                    "customers are entitled to a 100% full refund or reschedule within 12 months. "
                    "Cancellations requested by the customer more than 48 hours in advance receive a full refund minus a 10 CHF admin fee. "
                    "Cancellations under 24 hours are non-refundable unless accompanied by a medical certificate."
                ),
                "url": "https://company.sharepoint.com/sop/cancellation_policy.pdf"
            },
            {
                "doc_id": "sp_doc_002",
                "title": "Customer Service & Booking Guidelines",
                "category": "Customer Support",
                "content": (
                    "Standard response time for customer inquiries is 4 business hours. "
                    "For group bookings over 10 participants, offer a 15% corporate discount. "
                    "Follow-up emails should be sent within 24 hours post-activity."
                ),
                "url": "https://company.sharepoint.com/sop/customer_guidelines.docx"
            }
        ]
        query_lower = query.lower()
        results = [d for d in docs if any(q in d["title"].lower() or q in d["content"].lower() for q in query_lower.split())]
        return results if results else docs

    def _mock_outlook_search(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        emails = [
            {
                "email_id": "msg_001",
                "sender": "hans.mueller@swissmail.ch",
                "subject": "Inquiry regarding paragliding weather refund",
                "date": "2026-09-27T14:30:00Z",
                "snippet": "Hello, I booked a tour for yesterday but was told it might rain. What is your cancellation procedure?"
            },
            {
                "email_id": "msg_002",
                "sender": "sarah.j@traveler.com",
                "subject": "Confirmation for Jungfraujoch tour",
                "date": "2026-09-26T10:15:00Z",
                "snippet": "Thank you for the booking details. Can we add 1 more participant to TS-1002?"
            }
        ]
        return emails[:limit]

ms_graph_client = MSGraphClient()
