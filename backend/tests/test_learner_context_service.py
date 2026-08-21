from datetime import datetime

from app.instruction.learner_context_service import (
    LearnerContextService,
)
from app.storage.attempt import LearningAttempt


def test_learner_context_service_builds_context():
    service = LearnerContextService()

    attempts = [
        LearningAttempt(
            timestamp=datetime(2026, 8, 20, 10, 0),
            scenario_id="tv_delivery",
            initial_response="I would rent a crane.",
            revised_response="I would simplify the problem.",
            overall_score=4.0,
            rubric=[
                {
                    "name": "Problem Framing",
                    "score": 5,
                    "feedback": "Strong framing.",
                },
                {
                    "name": "Reflection",
                    "score": 3,
                    "feedback": "Some reflection.",
                },
            ],
            key_takeaway="Question assumptions.",
        ),
        LearningAttempt(
            timestamp=datetime(2026, 8, 21, 10, 0),
            scenario_id="bridge_problem",
            initial_response="I would raise the bridge.",
            revised_response="I would reconsider the constraint.",
            overall_score=4.4,
            rubric=[
                {
                    "name": "Problem Framing",
                    "score": 4,
                    "feedback": "Good framing.",
                },
                {
                    "name": "Reflection",
                    "score": 2,
                    "feedback": "Needs more reflection.",
                },
            ],
            key_takeaway="Reframe first.",
        ),
    ]

    context = service.build(attempts)

    assert context.challenges_completed == 2
    assert context.average_score == 4.2
    assert context.strongest_skill == "Problem Framing"
    assert context.growth_area == "Reflection"


def test_learner_context_service_handles_no_history():
    service = LearnerContextService()

    context = service.build([])

    assert context.challenges_completed == 0
    assert context.average_score == 0.0
    assert context.strongest_skill is None
    assert context.growth_area is None