from pathlib import Path

from app.instruction.scenario_strategy import get_instructional_strategy


class PromptBuilder:
    """
    Builds structured instructions and learner context for AI coaching.
    """

    def __init__(self):
        self.base_system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        prompt_path = (
            Path(__file__).resolve().parents[2]
            / "prompts"
            / "cognitive_coach.md"
        )

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Cognitive coach prompt not found at: {prompt_path}"
            )

        return prompt_path.read_text(encoding="utf-8")

    def build_instructions(self, scenario: dict) -> str:
        strategy = get_instructional_strategy(scenario)

        principles = "\n".join(
            f"- {principle}"
            for principle in strategy.coaching_principles
        )

        return f"""
{self.base_system_prompt}

## Current Instructional Strategy

Strategy name:
{strategy.name}

Coaching goal:
{strategy.coaching_goal}

Coaching principles:
{principles}
""".strip()

    def build_input(
        self,
        scenario: dict,
        user_response: str,
    ) -> str:
        return f"""
## Scenario Context

Scenario title:
{scenario["title"]}

Scenario:
{scenario["scenario"]}

Target cognitive skill:
{scenario["cognitive_skill"]}

## Learner Response

{user_response}

## Task

Generate exactly four concise coaching questions that are specific to the learner's response.

Do not reveal:

- The hidden assumption
- The better framing
- The simple solution
- The final answer
""".strip()

    def build_request(
        self,
        scenario: dict,
        user_response: str,
    ) -> dict:
        return {
            "instructions": self.build_instructions(scenario),
            "input": self.build_input(
                scenario=scenario,
                user_response=user_response,
            ),
        }