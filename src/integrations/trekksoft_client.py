from typing import List, Dict, Any, Optional
import httpx
from config.settings import settings
from config.logging_config import logger

class TrekkSoftClient:
    """Client for TrekkSoft Tour/Booking Management API."""
    def __init__(self, api_url: Optional[str] = None, api_key: Optional[str] = None):
        self.api_url = api_url or settings.TREKKSOFT_API_URL
        self.api_key = api_key or settings.TREKKSOFT_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_bookings(self, booking_date: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Retrieve recent bookings, filtered by date if provided."""
        if not self.api_key:
            logger.info("[TrekkSoft Mock Mode] Returning simulated booking data.")
            return self._mock_bookings(booking_date, limit)

        params = {"limit": limit}
        if booking_date:
            params["date"] = booking_date

        try:
            with httpx.Client(timeout=10.0) as client:
                resp = client.get(f"{self.api_url}/bookings", headers=self.headers, params=params)
                resp.raise_for_status()
                return resp.json().get("bookings", [])
        except Exception as e:
            logger.error(f"Error fetching TrekkSoft bookings: {e}")
            return self._mock_bookings(booking_date, limit)

    def get_booking_details(self, booking_id: str) -> Dict[str, Any]:
        """Retrieve full details for a specific booking."""
        if not self.api_key:
            return self._mock_booking_detail(booking_id)

        try:
            with httpx.Client(timeout=10.0) as client:
                resp = client.get(f"{self.api_url}/bookings/{booking_id}", headers=self.headers)
                resp.raise_for_status()
                return resp.json()
        except Exception as e:
            logger.error(f"Error fetching booking {booking_id}: {e}")
            return self._mock_booking_detail(booking_id)

    def search_customer_bookings(self, customer_email: str) -> List[Dict[str, Any]]:
        """Search bookings associated with a customer email."""
        all_bookings = self.get_bookings(limit=50)
        return [b for b in all_bookings if b.get("customer_email", "").lower() == customer_email.lower()]

    def _mock_bookings(self, booking_date: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """Simulated TrekkSoft booking dataset for testing/MVP demonstration."""
        mock_data = [
            {
                "booking_id": "TS-1001",
                "customer_name": "Hans Müller",
                "customer_email": "hans.mueller@swissmail.ch",
                "activity": "Interlaken Paragliding Experience",
                "date": booking_date or "2026-09-28",
                "participants": 2,
                "total_price_chf": 380.00,
                "status": "CONFIRMED"
            },
            {
                "booking_id": "TS-1002",
                "customer_name": "Sarah Jenkins",
                "customer_email": "sarah.j@traveler.com",
                "activity": "Jungfraujoch Top of Europe Day Tour",
                "date": booking_date or "2026-09-28",
                "participants": 4,
                "total_price_chf": 940.00,
                "status": "CONFIRMED"
            },
            {
                "booking_id": "TS-1003",
                "customer_name": "Marco Rossi",
                "customer_email": "marco.rossi@ticino.ch",
                "activity": "Lake Thun Kayak Guided Tour",
                "date": booking_date or "2026-09-29",
                "participants": 1,
                "total_price_chf": 110.00,
                "status": "PENDING_PAYMENT"
            }
        ]
        return mock_data[:limit]

    def _mock_booking_detail(self, booking_id: str) -> Dict[str, Any]:
        bookings = self._mock_bookings(limit=10)
        for b in bookings:
            if b["booking_id"] == booking_id:
                b_copy = b.copy()
                b_copy["notes"] = "Customer requested hotel pick-up at 08:30 AM."
                b_copy["payment_method"] = "Credit Card (Visa)"
                return b_copy
        return {
            "booking_id": booking_id,
            "status": "NOT_FOUND",
            "message": f"Booking ID {booking_id} does not exist."
        }

trekksoft_client = TrekkSoftClient()
