from app.instruction.prompt_builder import PromptBuilder


def test_prompt_builder_returns_instructions_and_input():
    builder = PromptBuilder(
        system_prompt="You are a cognitive coach."
    )

    scenario = {
        "title": "The Large TV Problem",
        "scenario": (
            "A large television appears too big to move into an "
            "room."
        ),
        "cognitive_skill": "Problem reframing",
    }

    result = builder.build(
        scenario=scenario,
        learner_response="I would rent a crane.",
    )

    assert isinstance(result, dict)

    assert "instructions" in result
    assert "input" in result

    assert (
        "You are a cognitive coach."
        in result["instructions"]
    )

    assert (
        "The Large TV Problem"
        in result["input"]
    )

    assert (
        "I would rent a crane."
        in result["input"]
    )

    assert (
        "Problem reframing"
        in result["input"]
    )