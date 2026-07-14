from app.services.ai_provider import AIProvider


class MockAIProvider(AIProvider):
    def generate_coaching_questions(self, scenario: dict, user_response: str) -> list[str]:
        cognitive_skill = scenario.get("cognitive_skill", "problem reframing")

        return [
            f"This challenge is practicing {cognitive_skill}. What assumption might be shaping your first response?",
            "What part of the situation are you treating as fixed that might actually be changeable?",
            "What is the real goal you are trying to accomplish?",
            "What is one simpler solution you might consider before adding complexity?"
        ]