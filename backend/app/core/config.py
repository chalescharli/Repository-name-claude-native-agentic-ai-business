import os
from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Rishan AI Agents Platform"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # LLM Provider Keys
    DEFAULT_LLM_PROVIDER: str = "anthropic"
    ANTHROPIC_API_KEY: str = ""
    OPENAI_API_KEY: str = ""
    GEMINI_API_KEY: str = ""
    DEFAULT_CLAUDE_MODEL: str = "claude-3-5-sonnet-20241022"
    DEFAULT_OPENAI_MODEL: str = "gpt-4o"
    DEFAULT_GEMINI_MODEL: str = "gemini-1.5-pro"
    
    # CORS
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173", "http://127.0.0.1:8000", "http://127.0.0.1:5173", "*"]
    
    # Security & Execution
    ENVIRONMENT: str = "development"
    SECRET_KEY: str = "super-secret-key-change-in-production"

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
