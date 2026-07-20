from app.instruction.prompt_builder import PromptBuilder
from app.scenarios import get_scenario_by_id


scenario = get_scenario_by_id("tv_delivery")

if scenario is None:
    raise ValueError("TV delivery scenario was not found.")

builder = PromptBuilder()

prompt = builder.build_coaching_prompt(
    scenario=scenario,
    user_response="I would use a crane to move the television."
)

print(prompt)