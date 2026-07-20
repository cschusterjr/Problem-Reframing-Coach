import os

from openai import OpenAI

from app.instruction.prompt_builder import PromptBuilder
from app.services.ai_provider import AIProvider


class OpenAIProvider(AIProvider):
    """
    Generates personalized coaching questions with the OpenAI API.

    The provider is only used when AI_PROVIDER=openai.
    """

    def __init__(self):
        self.model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
        self.api_key = os.getenv("OPENAI_API_KEY", "")
        self.prompt_builder = PromptBuilder()

    def generate_coaching_questions(
        self,
        scenario: dict,
        user_response: str,
    ) -> list[str]:
        if not self.api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. "
                "Add it to backend/.env or use AI_PROVIDER=mock."
            )

        prompt = self.prompt_builder.build_coaching_prompt(
            scenario=scenario,
            user_response=user_response,
        )

        client = OpenAI(api_key=self.api_key)

        response = client.responses.create(
            model=self.model,
            input=prompt,
        )

        questions = self._parse_questions(response.output_text)

        if len(questions) != 4:
            raise ValueError(
                "OpenAIProvider expected exactly four coaching questions, "
                f"but received {len(questions)}."
            )

        return questions

    def _parse_questions(self, output_text: str) -> list[str]:
        questions = []

        for line in output_text.splitlines():
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            cleaned_line = cleaned_line.lstrip("-• ")
            cleaned_line = self._remove_numbering(cleaned_line)

            if cleaned_line:
                questions.append(cleaned_line)

        return questions

    def _remove_numbering(self, text: str) -> str:
        for prefix in ("1. ", "2. ", "3. ", "4. "):
            if text.startswith(prefix):
                return text[len(prefix):].strip()

        return text