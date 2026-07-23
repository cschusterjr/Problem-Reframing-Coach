import logging
import os

from app.services.ai_provider import AIProvider
from app.services.mock_provider import MockAIProvider
from app.services.openai_provider import OpenAIProvider


logger = logging.getLogger(__name__)


def create_ai_provider() -> AIProvider:
    """Create the AI provider selected through environment configuration."""

    provider_name = os.getenv("AI_PROVIDER", "openai").strip().lower()

    if provider_name == "mock":
        provider = MockAIProvider()

    elif provider_name == "openai":
        provider = OpenAIProvider()

    else:
        raise ValueError(
            f"Unsupported AI_PROVIDER value: '{provider_name}'. "
            "Supported values are 'openai' and 'mock'."
        )

    logger.info(
        "Using AI provider: %s",
        provider.__class__.__name__,
    )

    return provider