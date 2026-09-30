import json
import logging
from datetime import datetime, timezone
from typing import Dict, Any, Optional
from pathlib import Path

class AuditLogger:
    def __init__(self, log_file_path: str = "logs/audit.jsonl"):
        self.log_path = Path(log_file_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        
    def log_event(
        self,
        event_type: str,
        agent_name: str,
        user_id: str,
        action: str,
        details: Dict[str, Any],
        status: str = "SUCCESS",
        error: Optional[str] = None
    ):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "event_type": event_type,
            "agent_name": agent_name,
            "user_id": user_id,
            "action": action,
            "status": status,
            "details": details,
            "error": error
        }

        log_line = json.dumps(event)
        
        # Write to JSONL log file
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(log_line + "\n")

audit_logger = AuditLogger()
