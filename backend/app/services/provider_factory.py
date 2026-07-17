import os

from dotenv import load_dotenv

from app.services.mock_provider import MockAIProvider
from app.services.openai_provider import OpenAIProvider

load_dotenv()


def create_ai_provider():
    provider_name = os.getenv("AI_PROVIDER", "mock").lower()

    if provider_name == "openai":
        return OpenAIProvider()

    if provider_name == "mock":
        return MockAIProvider()

    raise ValueError(
        f"Unsupported AI provider: {provider_name}. "
        "Use 'mock' or 'openai'."
    )