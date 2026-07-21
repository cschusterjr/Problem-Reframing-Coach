from dataclasses import dataclass


@dataclass
class CognitiveDiagnosis:
    """
    Represents the coach's internal assessment of the learner's reasoning.

    This object is never shown directly to the learner.
    It informs how the AI generates coaching.
    """

    reasoning_pattern: str
    likely_assumption: str
    instructional_move: str
    confidence: float