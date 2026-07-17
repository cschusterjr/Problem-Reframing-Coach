from pathlib import Path

from app.services.ai_provider import AIProvider


class OpenAIProvider(AIProvider):
    def __init__(self):
        self.system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        prompt_path = (
            Path(__file__).resolve().parents[2]
            / "prompts"
            / "cognitive_coach.md"
        )

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Cognitive coach prompt was not found at: {prompt_path}"
            )

        return prompt_path.read_text(encoding="utf-8")

    def generate_coaching_questions(
        self,
        scenario: dict,
        user_response: str
    ) -> list[str]:
        raise NotImplementedError(
            "OpenAI API integration is not enabled yet. "
            "The system prompt loaded successfully."
        )