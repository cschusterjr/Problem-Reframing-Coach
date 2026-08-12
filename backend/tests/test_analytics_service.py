from datetime import datetime

from app.analytics.service import LearningAnalyticsService
from app.storage.attempt import LearningAttempt


def test_learning_analytics_summary():
    service = LearningAnalyticsService()

    attempts = [
        LearningAttempt(
            timestamp=datetime(2026, 8, 1, 10, 0),
            scenario_id="tv_delivery",
            initial_response="I would rent a crane.",
            revised_response="I would remove the TV from the box.",
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
            timestamp=datetime(2026, 8, 2, 10, 0),
            scenario_id="bridge_problem",
            initial_response="I would raise the bridge.",
            revised_response="I would simplify the constraint first.",
            overall_score=4.6,
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
            key_takeaway="Reframe before adding complexity.",
        ),
    ]

    summary = service.summarize(attempts)

    assert summary["challenges_completed"] == 2
    assert summary["average_score"] == 4.3
    assert summary["strongest_skill"] == "Problem Framing"
    assert summary["growth_area"] == "Reflection"


def test_learning_analytics_empty_history():
    service = LearningAnalyticsService()

    summary = service.summarize([])

    assert summary["challenges_completed"] == 0
    assert summary["average_score"] == 0.0
    assert summary["strongest_skill"] is None
    assert summary["growth_area"] is None