from datetime import datetime

from app.services.cognitive_coach import CognitiveCoach
from app.storage.attempt import LearningAttempt


class FakeAIProvider:
    def generate_coaching_questions(
        self,
        scenario: dict,
        learner_response: str,
    ) -> list[str]:
        return [
            "Question 1?",
            "Question 2?",
            "Question 3?",
            "Question 4?",
        ]


def test_cognitive_coach_builds_learner_context():
    coach = CognitiveCoach(
        ai_provider=FakeAIProvider()
    )

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

    context = coach.build_learner_context(
        attempts
    )

    assert context.challenges_completed == 2
    assert context.average_score == 4.2
    assert context.strongest_skill == "Problem Framing"
    assert context.growth_area == "Reflection"