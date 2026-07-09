import json
from pathlib import Path

DATA_PATH = Path(__file__).parent / "data" / "scenarios.json"


def load_scenarios():
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def get_scenario_by_id(scenario_id: str):
    scenarios = load_scenarios()

    for scenario in scenarios:
        if scenario["id"] == scenario_id:
            return scenario

    return None