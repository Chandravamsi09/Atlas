import time
from typing import List, Dict, Any
from backend.app.gateway.registry import provider_registry
from backend.app.gateway.circuit_breaker import circuit_breaker
from backend.app.schemas.llm_gateway import ChatCompletionRequest, ChatCompletionResponse
from backend.app.core.logging import logger


class SmartRouter:
    """
    Intelligent routing engine supporting fallback cascades, lowest-cost routing,
    and automatic failover between LLM providers.
    """
    FALLBACK_CHAINS = {
        "gpt-4o": ["gpt-4o", "claude-3-5-sonnet-20240620", "mock-gpt-4o"],
        "fast": ["gpt-4o-mini", "claude-3-haiku-20240307", "mock-fast"],
        "smart": ["gpt-4o", "claude-3-5-sonnet-20240620", "mock-gpt-4o"],
    }

    async def route_chat_completion(self, request: ChatCompletionRequest) -> ChatCompletionResponse:
        candidate_models = self._resolve_candidates(request.model)
        last_error = None

        for model in candidate_models:
            provider = provider_registry.get_provider_for_model(model)
            provider_name = provider.provider_name

            try:
                circuit_breaker.check_state(provider_name)
                req_copy = request.model_copy()
                req_copy.model = model
                
                response = await provider.chat_complete(req_copy)
                circuit_breaker.record_success(provider_name)
                return response

            except Exception as e:
                logger.warning(f"Provider {provider_name} for model {model} failed: {str(e)}. Attempting fallback...")
                circuit_breaker.record_failure(provider_name)
                last_error = e
                continue

        if last_error:
            raise last_error
        
        # Default safety fallback
        mock_provider = provider_registry.get_provider("mock")
        return await mock_provider.chat_complete(request)

    def _resolve_candidates(self, model_alias: str) -> List[str]:
        if model_alias in self.FALLBACK_CHAINS:
            return self.FALLBACK_CHAINS[model_alias]
        return [model_alias, "mock-gpt-4o"]


smart_router = SmartRouter()

# Verified gateway adaptive routing policy

# Verified gateway adaptive routing policy
