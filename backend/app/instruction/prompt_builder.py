from pathlib import Path

from app.instruction.scenario_strategy import get_instructional_strategy


class PromptBuilder:
    """
    Builds the full coaching prompt from:

    - the base system prompt
    - the scenario
    - the learner's response
    - the selected instructional strategy
    """

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
                f"Cognitive coach prompt not found at: {prompt_path}"
            )

        return prompt_path.read_text(encoding="utf-8")

    def build_coaching_prompt(
        self,
        scenario: dict,
        user_response: str
    ) -> str:
        strategy = get_instructional_strategy(scenario)

        principles = "\n".join(
            f"- {principle}"
            for principle in strategy.coaching_principles
        )

        return f"""
{self.system_prompt}

## Current Instructional Strategy

Strategy name:
{strategy.name}

Coaching goal:
{strategy.coaching_goal}

Coaching principles:
{principles}

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