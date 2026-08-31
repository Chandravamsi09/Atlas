from typing import Dict, Type, Optional
from backend.app.gateway.base import BaseLLMProvider
from backend.app.gateway.providers.mock_provider import MockLLMProvider
from backend.app.gateway.providers.openai_provider import OpenAIProvider
from backend.app.gateway.providers.anthropic_provider import AnthropicProvider


class ProviderRegistry:
    """Central registry for LLM provider instances and model-to-provider mappings."""

    def __init__(self):
        self._providers: Dict[str, BaseLLMProvider] = {
            "mock": MockLLMProvider(),
            "openai": OpenAIProvider(),
            "anthropic": AnthropicProvider(),
        }
        self._model_to_provider: Dict[str, str] = {
            "mock-gpt-4o": "mock",
            "mock-fast": "mock",
            "gpt-4o": "openai",
            "gpt-4o-mini": "openai",
            "gpt-4-turbo": "openai",
            "gpt-3.5-turbo": "openai",
            "claude-3-5-sonnet-20240620": "anthropic",
            "claude-3-haiku-20240307": "anthropic",
            "claude-3-opus-20240229": "anthropic",
        }

    def get_provider_for_model(self, model_name: str) -> BaseLLMProvider:
        provider_key = self._model_to_provider.get(model_name.lower(), "mock")
        return self._providers.get(provider_key, self._providers["mock"])

    def get_provider(self, provider_name: str) -> Optional[BaseLLMProvider]:
        return self._providers.get(provider_name.lower())


provider_registry = ProviderRegistry()
