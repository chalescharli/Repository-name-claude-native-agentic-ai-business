def mask_api_key(key: str) -> str:
    """Safely mask API key for display/logging."""
    if not key or len(key) < 8:
        return "********"
    return f"{key[:4]}...{key[-4:]}"

def sanitize_input(user_input: str) -> str:
    """Sanitize prompt inputs against basic injection attempts."""
    return user_input.strip()
