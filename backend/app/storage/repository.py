from abc import ABC, abstractmethod

from app.storage.attempt import LearningAttempt


class AttemptRepository(ABC):
    """
    Defines how learner attempts are stored.

    Different implementations may use:

    - SQLite
    - PostgreSQL
    - Cloud storage
    - In-memory testing
    """

    @abstractmethod
    def save_attempt(
        self,
        attempt: LearningAttempt,
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def load_attempts(self) -> list[LearningAttempt]:
        raise NotImplementedError