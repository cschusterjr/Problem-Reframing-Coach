from app.instruction.prompt_builder import PromptBuilder
from app.scenarios import get_scenario_by_id


scenario = get_scenario_by_id("tv_delivery")

if scenario is None:
    raise ValueError("TV delivery scenario was not found.")

builder = PromptBuilder()

request = builder.build_request(
    scenario=scenario,
    user_response="I would use a crane to move the television.",
)

print("=== INSTRUCTIONS ===")
print(request["instructions"])

print()
print("=== INPUT ===")
print(request["input"])