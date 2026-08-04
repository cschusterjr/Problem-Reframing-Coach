import json
import sqlite3
from datetime import datetime
from pathlib import Path

from app.storage.attempt import LearningAttempt
from app.storage.repository import AttemptRepository


class SQLiteAttemptRepository(AttemptRepository):
    """
    Stores learner attempts in a local SQLite database.
    """

    def __init__(self):
        self.database_path = (
            Path(__file__).resolve().parents[2]
            / "learning_history.db"
        )

        self._initialize_database()

    def _initialize_database(self):
        connection = sqlite3.connect(self.database_path)

        cursor = connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS attempts (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                timestamp TEXT,

                scenario_id TEXT,

                initial_response TEXT,

                revised_response TEXT,

                overall_score REAL,

                rubric TEXT,

                key_takeaway TEXT
            )
            """
        )

        connection.commit()
        connection.close()

    def save_attempt(
        self,
        attempt: LearningAttempt,
    ) -> None:

        connection = sqlite3.connect(self.database_path)

        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO attempts (

                timestamp,

                scenario_id,

                initial_response,

                revised_response,

                overall_score,

                rubric,

                key_takeaway

            )

            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                attempt.timestamp.isoformat(),
                attempt.scenario_id,
                attempt.initial_response,
                attempt.revised_response,
                attempt.overall_score,
                json.dumps(attempt.rubric),
                attempt.key_takeaway,
            ),
        )

        connection.commit()
        connection.close()

    def load_attempts(self) -> list[LearningAttempt]:

        connection = sqlite3.connect(self.database_path)

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT
                timestamp,
                scenario_id,
                initial_response,
                revised_response,
                overall_score,
                rubric,
                key_takeaway
            FROM attempts
            ORDER BY timestamp DESC
            """
        )

        rows = cursor.fetchall()

        connection.close()

        attempts = []

        for row in rows:

            attempts.append(
                LearningAttempt(
                    timestamp=datetime.fromisoformat(row[0]),
                    scenario_id=row[1],
                    initial_response=row[2],
                    revised_response=row[3],
                    overall_score=row[4],
                    rubric=json.loads(row[5]),
                    key_takeaway=row[6],
                )
            )

        return attempts