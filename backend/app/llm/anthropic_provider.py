from typing import List, Dict, Any, Optional
import anthropic
from backend.app.llm.base_provider import BaseLLMProvider
from backend.app.core.config import settings
from config.logging_config import logger

class AnthropicLLMProvider(BaseLLMProvider):
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or settings.ANTHROPIC_API_KEY
        self.client = anthropic.Anthropic(api_key=key) if key else None

    def generate_completion(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        tools: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        if not self.client:
            return {"status": "fallback", "response": f"Anthropic Provider: Echoing '{prompt}'"}

        try:
            response = self.client.messages.create(
                model=settings.DEFAULT_CLAUDE_MODEL,
                max_tokens=1024,
                system=system_prompt or "You are an AI assistant.",
                messages=[{"role": "user", "content": prompt}],
                tools=tools if tools else None
            )

            if response.stop_reason == "tool_use":
                tool_use = next(block for block in response.content if block.type == "tool_use")
                return {
                    "status": "tool_use",
                    "tool_name": tool_use.name,
                    "tool_input": tool_use.input
                }

            text_content = next(block.text for block in response.content if block.type == "text")
            return {"status": "success", "response": text_content}
        except Exception as e:
            logger.error(f"[AnthropicLLMProvider] Error: {e}")
            return {"status": "error", "error": str(e)}
