from typing import Optional
from backend.app.llm.base_provider import BaseLLMProvider
from backend.app.llm.anthropic_provider import AnthropicLLMProvider
from backend.app.llm.openai_provider import OpenAILLMProvider
from backend.app.llm.gemini_provider import GeminiLLMProvider
from backend.app.core.config import settings

class LLMProviderFactory:
    @staticmethod
    def get_provider(provider_name: Optional[str] = None, api_key: Optional[str] = None) -> BaseLLMProvider:
        target_provider = (provider_name or settings.DEFAULT_LLM_PROVIDER).lower()

        if target_provider in ["anthropic", "claude"]:
            return AnthropicLLMProvider(api_key=api_key)
        elif target_provider in ["openai", "gpt"]:
            return OpenAILLMProvider(api_key=api_key)
        elif target_provider in ["gemini", "google"]:
            return GeminiLLMProvider(api_key=api_key)
        else:
            return AnthropicLLMProvider(api_key=api_key)
