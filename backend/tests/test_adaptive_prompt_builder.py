from app.instruction.learner_context import LearnerContext
from app.instruction.prompt_builder import PromptBuilder


def test_prompt_builder_includes_learner_context():
    builder = PromptBuilder(
        system_prompt="You are a cognitive coach."
    )

    scenario = {
        "title": "The Large TV Problem",
        "scenario": (
            "A large television needs to be moved "
            "into an eighth-floor room."
        ),
        "cognitive_skill": "Problem reframing",
    }

    learner_context = LearnerContext(
        strongest_skill="Problem Framing",
        growth_area="Reflection",
        challenges_completed=4,
        average_score=4.1,
    )

    result = builder.build(
        scenario=scenario,
        learner_response="I would rent a crane.",
        learner_context=learner_context,
    )

    instructions = result["instructions"]

    assert "LEARNER CONTEXT" in instructions
    assert "Challenges completed:" in instructions
    assert "4" in instructions
    assert "4.1/5" in instructions
    assert "Problem Framing" in instructions
    assert "Reflection" in instructions
    assert "ADAPTIVE COACHING INSTRUCTION" in instructions


def test_prompt_builder_uses_standard_coaching_without_history():
    builder = PromptBuilder(
        system_prompt="You are a cognitive coach."
    )

    scenario = {
        "title": "The Large TV Problem",
        "scenario": "A large television needs to be moved.",
        "cognitive_skill": "Problem reframing",
    }

    learner_context = LearnerContext(
        strongest_skill=None,
        growth_area=None,
        challenges_completed=0,
        average_score=0.0,
    )

    result = builder.build(
        scenario=scenario,
        learner_response="I would rent a crane.",
        learner_context=learner_context,
    )

    instructions = result["instructions"]

    assert "No prior learner history is available." in instructions
    assert "Use the standard coaching sequence." in instructions


def test_prompt_builder_remains_backward_compatible():
    builder = PromptBuilder(
        system_prompt="You are a cognitive coach."
    )

    scenario = {
        "title": "The Large TV Problem",
        "scenario": "A large television needs to be moved.",
        "cognitive_skill": "Problem reframing",
    }

    result = builder.build(
        scenario=scenario,
        learner_response="I would rent a crane.",
    )

    assert "instructions" in result
    assert "input" in result
    assert "No prior learner history is available." in result["instructions"]