from abc import ABC, abstractmethod


class AIProvider(ABC):
    @abstractmethod
    def generate_coaching_questions(self, scenario: dict, user_response: str) -> list[str]:
        pass