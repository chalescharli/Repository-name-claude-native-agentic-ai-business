import os
from pathlib import Path
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # System Settings
    ENVIRONMENT: str = Field(default="development")
    LOG_LEVEL: str = Field(default="INFO")
    SECRET_KEY: str = Field(default="dev_secret_key_change_in_prod")
    
    # Anthropic Claude API Settings
    ANTHROPIC_API_KEY: str = Field(default="")
    DEFAULT_CLAUDE_MODEL: str = Field(default="claude-3-5-sonnet-20241022")
    
    # Microsoft Graph API Credentials
    MS_GRAPH_CLIENT_ID: str = Field(default="")
    MS_GRAPH_CLIENT_SECRET: str = Field(default="")
    MS_GRAPH_TENANT_ID: str = Field(default="")
    MS_GRAPH_SHAREPOINT_SITE_ID: str = Field(default="")
    
    # TrekkSoft API
    TREKKSOFT_API_URL: str = Field(default="https://api.trekksoft.com/v1")
    TREKKSOFT_API_KEY: str = Field(default="")
    TREKKSOFT_MERCHANT_ID: str = Field(default="")
    
    # bexio API
    BEXIO_API_URL: str = Field(default="https://api.bexio.com/2.0")
    BEXIO_API_TOKEN: str = Field(default="")
    
    # Brevo API
    BREVO_API_URL: str = Field(default="https://api.brevo.com/v3")
    BREVO_API_KEY: str = Field(default="")
    
    # Vector DB / Persistence
    CHROMA_PERSIST_DIR: str = Field(default="./data/chroma_db")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()
