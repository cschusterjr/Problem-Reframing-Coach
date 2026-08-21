import os
import re
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from app.instruction.learner_context import LearnerContext
from app.instruction.prompt_builder import PromptBuilder
from app.services.ai_provider import AIProvider


class OpenAIProvider(AIProvider):
    """Generates cognitive coaching questions using the OpenAI API."""

    def __init__(self) -> None:
        load_dotenv()

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY is missing. "
                "Add it to the backend/.env file."
            )

        self.model = os.getenv(
            "OPENAI_MODEL",
            "gpt-5-mini",
        )

        self.client = OpenAI(
            api_key=api_key
        )

        prompt_path = (
            Path(__file__).resolve().parents[2]
            / "prompts"
            / "cognitive_coach.md"
        )

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"System prompt file was not found: {prompt_path}"
            )

        system_prompt = prompt_path.read_text(
            encoding="utf-8"
        )

        self.prompt_builder = PromptBuilder(
            system_prompt
        )

    def generate_coaching_questions(
        self,
        scenario: dict,
        learner_response: str,
        learner_context: LearnerContext | None = None,
    ) -> list[str]:
        prompt = self.prompt_builder.build(
            scenario=scenario,
            learner_response=learner_response,
            learner_context=learner_context,
        )

        response = self.client.responses.create(
            model=self.model,
            instructions=prompt["instructions"],
            input=prompt["input"],
        )

        questions = self._parse_questions(
            response.output_text
        )

        if len(questions) < 4:
            raise ValueError(
                "The OpenAI response did not contain "
                "four coaching questions."
            )

        return questions[:4]

    @staticmethod
    def _parse_questions(
        response_text: str,
    ) -> list[str]:
        if (
            not response_text
            or not response_text.strip()
        ):
            return []

        questions = []

        for line in response_text.strip().splitlines():
            cleaned_line = line.strip()

            if not cleaned_line:
                continue

            cleaned_line = re.sub(
                r"^(?:\d+[.)]|[-*])\s*",
                "",
                cleaned_line,
            ).strip()

            if cleaned_line:
                questions.append(
                    cleaned_line
                )

        return questions