from app.instruction.diagnosis import CognitiveDiagnosis


class CoachingStrategySelector:
    """Chooses an instructional coaching strategy based on the diagnosis."""

    def select(self, diagnosis: CognitiveDiagnosis) -> str:
        pattern = diagnosis.reasoning_pattern.lower()

        if "assumption" in pattern:
            return (
                "Spend additional time helping the learner uncover hidden "
                "assumptions before discussing solutions."
            )

        if "constraint" in pattern:
            return (
                "Guide the learner to question which constraints are real "
                "and which are self-imposed."
            )

        if "complexity" in pattern:
            return (
                "Encourage the learner to simplify the problem before adding "
                "resources, tools, or steps."
            )

        if "goal" in pattern:
            return (
                "Help the learner distinguish the desired outcome from the "
                "method they initially selected."
            )

        return (
            "Follow the standard four-stage coaching framework while "
            "encouraging reflection."
        )