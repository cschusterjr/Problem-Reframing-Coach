from app.instruction.learner_context import LearnerContext
from app.services.ai_provider import AIProvider


class MockAIProvider(AIProvider):
    """Returns deterministic coaching questions without using an API."""

    def generate_coaching_questions(
        self,
        scenario: dict,
        learner_response: str,
        learner_context: LearnerContext | None = None,
    ) -> list[str]:
        cognitive_skill = scenario.get(
            "cognitive_skill",
            "problem reframing",
        )

        return [
            (
                f"This challenge is practicing {cognitive_skill}. "
                "What assumption might be shaping your first response?"
            ),
            (
                "What part of the situation are you treating as fixed "
                "that might actually be changeable?"
            ),
            (
                "What could be simplified before adding more resources "
                "or steps?"
            ),
            (
                "How could you restate the real goal without including "
                "the method you first selected?"
            ),
        ]