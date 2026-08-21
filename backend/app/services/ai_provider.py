from abc import ABC, abstractmethod

from app.instruction.learner_context import LearnerContext


class AIProvider(ABC):
    """Contract implemented by every coaching provider."""

    @abstractmethod
    def generate_coaching_questions(
        self,
        scenario: dict,
        learner_response: str,
        learner_context: LearnerContext | None = None,
    ) -> list[str]:
        """Generate coaching questions for a learner response."""
        raise NotImplementedError