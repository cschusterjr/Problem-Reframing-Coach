from app.instruction.diagnosis import CognitiveDiagnosis


class CognitiveDiagnoser:
    """
    Performs a lightweight diagnosis of the learner's response.

    Today this uses simple rules.

    Later GPT can produce this diagnosis.
    """

    def diagnose(
        self,
        scenario: dict,
        learner_response: str
    ) -> CognitiveDiagnosis:

        response = learner_response.lower()

        if any(word in response for word in [
            "crane",
            "hire",
            "buy",
            "add",
            "new",
            "equipment"
        ]):

            return CognitiveDiagnosis(
                reasoning_pattern="Adding complexity too early",
                likely_assumption="The current object or process cannot change.",
                instructional_move="Question assumptions before introducing resources.",
                confidence=0.92
            )

        return CognitiveDiagnosis(
            reasoning_pattern="Unknown",
            likely_assumption="Unknown",
            instructional_move="Encourage reflection.",
            confidence=0.50
        )