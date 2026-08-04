from datetime import datetime

from app.storage.attempt import LearningAttempt
from app.storage.sqlite_repository import SQLiteAttemptRepository


def test_sqlite_repository_saves_and_loads_attempt(tmp_path):
    repository = SQLiteAttemptRepository()

    repository.database_path = tmp_path / "test_learning_history.db"
    repository._initialize_database()

    attempt = LearningAttempt(
        timestamp=datetime(2026, 8, 4, 15, 30),
        scenario_id="tv_delivery",
        initial_response="I would rent a crane.",
        revised_response=(
            "I would remove the television from the box "
            "and focus on getting the television into the room."
        ),
        overall_score=4.2,
        rubric=[
            {
                "name": "Problem Framing",
                "score": 5,
                "feedback": "The response focuses on the actual goal.",
            }
        ],
        key_takeaway="Question the frame before adding complexity.",
    )

    repository.save_attempt(attempt)

    saved_attempts = repository.load_attempts()

    assert len(saved_attempts) == 1

    saved_attempt = saved_attempts[0]

    assert saved_attempt.scenario_id == "tv_delivery"
    assert saved_attempt.initial_response == "I would rent a crane."
    assert saved_attempt.overall_score == 4.2
    assert saved_attempt.rubric[0]["name"] == "Problem Framing"
    assert saved_attempt.key_takeaway == (
        "Question the frame before adding complexity."
    )