from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app, attempt_repository
from app.storage.attempt import LearningAttempt


client = TestClient(app)


def test_analytics_summary_endpoint(tmp_path):
    attempt_repository.database_path = (
        tmp_path / "test_learning_history.db"
    )

    attempt_repository._initialize_database()

    attempt_repository.save_attempt(
        LearningAttempt(
            timestamp=datetime(2026, 8, 10, 10, 0),
            scenario_id="tv_delivery",
            initial_response="I would rent a crane.",
            revised_response=(
                "I would question the assumption and simplify "
                "the problem before adding complexity."
            ),
            overall_score=4.4,
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
            key_takeaway="Question assumptions before adding complexity.",
        )
    )

    attempt_repository.save_attempt(
        LearningAttempt(
            timestamp=datetime(2026, 8, 11, 10, 0),
            scenario_id="bridge_problem",
            initial_response="I would raise the bridge.",
            revised_response=(
                "I would reconsider which constraint is actually fixed."
            ),
            overall_score=4.0,
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
            key_takeaway="Reframe the constraint first.",
        )
    )

    response = client.get("/analytics/summary")

    assert response.status_code == 200

    body = response.json()

    assert body["challenges_completed"] == 2
    assert body["average_score"] == 4.2
    assert body["strongest_skill"] == "Problem Framing"
    assert body["growth_area"] == "Reflection"