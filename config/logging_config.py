import sys
import logging

def setup_logging(level: str = "INFO"):
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    # Audit logger specific logger
    audit_logger = logging.getLogger("audit")
    audit_logger.setLevel(logging.INFO)

    return logging.getLogger("app")

logger = setup_logging()
