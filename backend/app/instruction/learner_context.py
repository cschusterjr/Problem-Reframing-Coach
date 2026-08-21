from dataclasses import dataclass


@dataclass
class LearnerContext:
    """
    Represents learner-level context used to personalize coaching.
    """

    strongest_skill: str | None
    growth_area: str | None
    challenges_completed: int
    average_score: float