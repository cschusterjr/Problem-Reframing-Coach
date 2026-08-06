from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app, attempt_repository
from app.storage.attempt import LearningAttempt


client = TestClient(app)


def test_attempts_endpoint_returns_saved_attempt(
    tmp_path,
):
    attempt_repository.database_path = (
        tmp_path
        / "test_learning_history.db"
    )

    attempt_repository._initialize_database()

    attempt_repository.save_attempt(
        LearningAttempt(
            timestamp=datetime(
                2026,
                8,
                6,
                14,
                30,
            ),
            scenario_id="tv_delivery",
            initial_response=(
                "I would rent a crane."
            ),
            revised_response=(
                "I would remove the television "
                "from the box."
            ),
            overall_score=4.2,
            rubric=[
                {
                    "name": "Problem Framing",
                    "score": 5,
                    "feedback": (
                        "Strong reframing."
                    ),
                }
            ],
            key_takeaway=(
                "Question the frame before "
                "adding complexity."
            ),
        )
    )

    response = client.get("/attempts")

    assert response.status_code == 200

    body = response.json()

    assert len(body) == 1

    assert (
        body[0]["scenario_id"]
        == "tv_delivery"
    )

    assert (
        body[0]["overall_score"]
        == 4.2
    )