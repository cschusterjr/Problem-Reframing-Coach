from datetime import datetime

from app.analytics.service import LearningAnalyticsService
from app.storage.attempt import LearningAttempt


def test_score_trend_returns_attempts_in_chronological_order():
    service = LearningAnalyticsService()

    attempts = [
        LearningAttempt(
            timestamp=datetime(2026, 8, 12, 10, 0),
            scenario_id="second",
            initial_response="Initial",
            revised_response="Revised",
            overall_score=4.5,
            rubric=[],
            key_takeaway="Takeaway",
        ),
        LearningAttempt(
            timestamp=datetime(2026, 8, 10, 10, 0),
            scenario_id="first",
            initial_response="Initial",
            revised_response="Revised",
            overall_score=3.8,
            rubric=[],
            key_takeaway="Takeaway",
        ),
    ]

    trend = service.score_trend(attempts)

    assert len(trend) == 2

    assert trend[0]["scenario_id"] == "first"
    assert trend[0]["overall_score"] == 3.8

    assert trend[1]["scenario_id"] == "second"
    assert trend[1]["overall_score"] == 4.5


def test_score_trend_returns_empty_list_for_no_attempts():
    service = LearningAnalyticsService()

    assert service.score_trend([]) == []