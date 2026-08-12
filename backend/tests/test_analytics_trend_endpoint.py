from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app, attempt_repository
from app.storage.attempt import LearningAttempt


client = TestClient(app)


def test_analytics_trend_endpoint_returns_chronological_scores(
    tmp_path,
):
    attempt_repository.database_path = (
        tmp_path / "test_learning_history.db"
    )

    attempt_repository._initialize_database()

    attempt_repository.save_attempt(
        LearningAttempt(
            timestamp=datetime(2026, 8, 12, 10, 0),
            scenario_id="second",
            initial_response="Initial",
            revised_response="Revised",
            overall_score=4.5,
            rubric=[],
            key_takeaway="Takeaway",
        )
    )

    attempt_repository.save_attempt(
        LearningAttempt(
            timestamp=datetime(2026, 8, 10, 10, 0),
            scenario_id="first",
            initial_response="Initial",
            revised_response="Revised",
            overall_score=3.8,
            rubric=[],
            key_takeaway="Takeaway",
        )
    )

    response = client.get("/analytics/trend")

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 2

    assert body[0]["scenario_id"] == "first"
    assert body[0]["overall_score"] == 3.8

    assert body[1]["scenario_id"] == "second"
    assert body[1]["overall_score"] == 4.5