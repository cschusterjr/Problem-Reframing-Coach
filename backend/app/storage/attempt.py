from dataclasses import dataclass
from datetime import datetime


@dataclass
class LearningAttempt:
    """
    Represents one completed learner attempt.
    """

    timestamp: datetime

    scenario_id: str

    initial_response: str

    revised_response: str

    overall_score: float

    rubric: list

    key_takeaway: str