from app.services.ai_provider import AIProvider


class OpenAIProvider(AIProvider):
    def generate_coaching_questions(self, scenario: dict, user_response: str) -> list[str]:
        raise NotImplementedError(
            "OpenAIProvider is not implemented yet. Use MockAIProvider for now."
        )