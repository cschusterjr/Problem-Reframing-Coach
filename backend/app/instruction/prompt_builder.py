class PromptBuilder:
    """Builds structured instructions and learner input for the AI coach."""

    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def build(
        self,
        scenario: dict,
        learner_response: str,
    ) -> dict:
        scenario_title = scenario.get("title", "Untitled scenario")

        scenario_description = (
            scenario.get("description")
            or scenario.get("scenario")
            or scenario.get("prompt")
            or scenario.get("problem")
            or "No scenario description was provided."
        )

        cognitive_skill = scenario.get(
            "cognitive_skill",
            "Problem reframing",
        )

        instructions = f"""
{self.system_prompt}

Generate exactly four coaching questions using this sequence:

1. Inspect assumptions
2. Challenge fixed constraints
3. Simplify before adding
4. Reframe the goal

Do not answer the scenario.
Do not reveal the solution.
Do not provide advice beyond the four coaching questions.
""".strip()

        learner_input = f"""
SCENARIO

Title:
{scenario_title}

Description:
{scenario_description}

Target cognitive skill:
{cognitive_skill}

LEARNER'S INITIAL RESPONSE

{learner_response}
""".strip()

        return {
            "instructions": instructions,
            "input": learner_input,
        }