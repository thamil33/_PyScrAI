"""
LLM Service for handling AI model interactions
Integrates with existing model_client_adapters
"""
import asyncio
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

from app.core.config import settings

# Import the existing model client adapters
try:
    from model_client_adapters import get_model_client
    from model_client_adapters.base_adapter import ChatMessage, ChatResponse
except ImportError:
    # Fallback if adapters not available
    get_model_client = None
    ChatMessage = None
    ChatResponse = None

@dataclass
class LLMResponse:
    """Standardized response format"""
    content: str
    model: str
    provider: str
    tokens_used: Optional[int] = None
    metadata: Optional[Dict[str, Any]] = None

class LLMService:
    """Service for handling LLM interactions"""

    def __init__(self):
        self._adapter = None

    async def get_adapter(self, provider: Optional[str] = None, model: Optional[str] = None):
        """Get or create adapter instance"""
        if self._adapter is None and get_model_client:
            provider = provider or settings.LLM_API_PROVIDER
            model = model or settings.DEFAULT_MODEL
            self._adapter = get_model_client(provider=provider, model=model)
        return self._adapter

    async def generate_response(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        provider: Optional[str] = None,
        tulpa_provider: Optional[str] = None,
        tulpa_model: Optional[str] = None,
        **kwargs
    ) -> LLMResponse:
        """Generate a response from the LLM"""
        # Prioritize tulpa-specific settings, fall back to global settings
        effective_provider = tulpa_provider or provider or settings.LLM_API_PROVIDER
        effective_model = tulpa_model or model or settings.DEFAULT_MODEL

        adapter = await self.get_adapter(effective_provider, effective_model)

        if adapter is None:
            raise Exception("No LLM adapter available. Please check model_client_adapters installation.")

        try:
            # Convert messages to ChatMessage format
            chat_messages = []
            for msg in messages:
                if ChatMessage:
                    chat_messages.append(ChatMessage(role=msg["role"], content=msg["content"]))
                else:
                    # Fallback if ChatMessage not available
                    chat_messages.append({"role": msg["role"], "content": msg["content"]})

            # Generate response
            if hasattr(adapter, 'unified_call'):
                # Use unified interface if available
                response_text, usage = adapter.unified_call(
                    system_message=next((m["content"] for m in messages if m["role"] == "system"), None),
                    user_message=next((m["content"] for m in messages if m["role"] == "user"), ""),
                    **kwargs
                )
                return LLMResponse(
                    content=response_text,
                    model=effective_model,
                    provider=effective_provider,
                    metadata=usage
                )
            else:
                # Use standard interface
                response = await adapter.generate_response(chat_messages, **kwargs)
                return LLMResponse(
                    content=response.content,
                    model=effective_model,
                    provider=effective_provider,
                    tokens_used=getattr(response, 'tokens_used', None),
                    metadata=getattr(response, 'metadata', None)
                )

        except Exception as e:
            raise Exception(f"LLM service error: {str(e)}")

    async def validate_connection(self, provider: Optional[str] = None) -> bool:
        """Validate connection to LLM provider"""
        adapter = await self.get_adapter(provider)
        if adapter and hasattr(adapter, 'validate_connection'):
            return adapter.validate_connection()
        return False

    async def get_available_models(self, provider: Optional[str] = None) -> List[str]:
        """Get list of available models"""
        adapter = await self.get_adapter(provider)
        if adapter and hasattr(adapter, 'get_available_models'):
            return adapter.get_available_models()
        return []

    async def get_model_info(self, provider: Optional[str] = None) -> Dict[str, Any]:
        """Get model information"""
        adapter = await self.get_adapter(provider)
        if adapter and hasattr(adapter, 'get_model_info'):
            return adapter.get_model_info()
        return {}
