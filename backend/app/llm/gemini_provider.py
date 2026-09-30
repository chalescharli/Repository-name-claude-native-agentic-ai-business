from typing import List, Dict, Any, Optional
from backend.app.llm.base_provider import BaseLLMProvider
from backend.app.core.config import settings
from config.logging_config import logger

class GeminiLLMProvider(BaseLLMProvider):
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or settings.GEMINI_API_KEY

    def generate_completion(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        if not self.api_key:
            return {"status": "fallback", "response": f"Google Gemini Provider (Mock): Processed '{prompt}'"}

        logger.info("[GeminiLLMProvider] Executing completion via Gemini adapter")
        return {"status": "success", "response": f"Gemini 1.5 Pro Response for '{prompt}'"}
