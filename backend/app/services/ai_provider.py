from abc import ABC, abstractmethod


class AIProvider(ABC):
    """Contract implemented by every coaching provider."""

    @abstractmethod
    def generate_coaching_questions(
        self,
        scenario: dict,
        learner_response: str,
    ) -> list[str]:
        """Generate coaching questions for a learner response."""
        raise NotImplementedError