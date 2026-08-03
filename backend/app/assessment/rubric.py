from dataclasses import dataclass


@dataclass
class RubricDimension:
    """
    Represents one dimension of cognitive performance.
    """

    name: str
    score: int
    feedback: str


@dataclass
class CognitiveRubric:
    """
    Represents the learner's overall cognitive assessment.
    """

    dimensions: list[RubricDimension]

    @property
    def overall_score(self) -> float:
        if not self.dimensions:
            return 0.0

        total = sum(d.score for d in self.dimensions)
        return round(total / len(self.dimensions), 1)