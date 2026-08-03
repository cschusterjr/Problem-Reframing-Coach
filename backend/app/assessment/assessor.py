from app.assessment.rubric import CognitiveRubric, RubricDimension


class CognitiveAssessor:
    """
    Produces a lightweight rule-based assessment of a revised response.

    This version is intentionally deterministic.
    It can later be replaced or extended with AI-based evaluation.
    """

    def assess(
        self,
        initial_response: str,
        revised_response: str,
    ) -> CognitiveRubric:
        revised = revised_response.lower().strip()

        dimensions = [
            self._assess_assumption_awareness(revised),
            self._assess_constraint_flexibility(revised),
            self._assess_problem_framing(revised),
            self._assess_simplification(revised),
            self._assess_reflection(
                initial_response=initial_response,
                revised_response=revised_response,
            ),
        ]

        return CognitiveRubric(dimensions=dimensions)

    def _assess_assumption_awareness(
        self,
        revised_response: str,
    ) -> RubricDimension:
        keywords = [
            "assumption",
            "assume",
            "question",
            "fixed",
            "necessary",
        ]

        score = self._score_keywords(
            revised_response,
            keywords,
        )

        return RubricDimension(
            name="Assumption Awareness",
            score=score,
            feedback=(
                "The response shows awareness of assumptions and whether "
                "they should be treated as fixed."
                if score >= 4
                else
                "The response could more clearly identify or question "
                "the assumptions shaping the original solution."
            ),
        )

    def _assess_constraint_flexibility(
        self,
        revised_response: str,
    ) -> RubricDimension:
        keywords = [
            "constraint",
            "change",
            "adjust",
            "flexible",
            "alternative",
            "different",
        ]

        score = self._score_keywords(
            revised_response,
            keywords,
        )

        return RubricDimension(
            name="Constraint Flexibility",
            score=score,
            feedback=(
                "The response reconsidered whether the original constraints "
                "were truly fixed."
                if score >= 4
                else
                "The response could examine which constraints are real and "
                "which may be changed."
            ),
        )

    def _assess_problem_framing(
        self,
        revised_response: str,
    ) -> RubricDimension:
        keywords = [
            "goal",
            "outcome",
            "actual problem",
            "real problem",
            "reframe",
            "need",
        ]

        score = self._score_keywords(
            revised_response,
            keywords,
        )

        return RubricDimension(
            name="Problem Framing",
            score=score,
            feedback=(
                "The response focuses on the desired outcome rather than "
                "only optimizing the original method."
                if score >= 4
                else
                "The response could restate the actual goal more clearly "
                "before selecting a solution."
            ),
        )

    def _assess_simplification(
        self,
        revised_response: str,
    ) -> RubricDimension:
        keywords = [
            "remove",
            "reduce",
            "separate",
            "simplify",
            "smaller",
            "unbox",
            "deflate",
        ]

        score = self._score_keywords(
            revised_response,
            keywords,
        )

        return RubricDimension(
            name="Simplification",
            score=score,
            feedback=(
                "The response considers simplifying the situation before "
                "adding more resources or complexity."
                if score >= 4
                else
                "The response could explore what might be removed, reduced, "
                "or simplified first."
            ),
        )

    def _assess_reflection(
        self,
        initial_response: str,
        revised_response: str,
    ) -> RubricDimension:
        initial = initial_response.strip().lower()
        revised = revised_response.strip().lower()

        if not revised:
            score = 1
        elif revised == initial:
            score = 2
        elif len(revised) > len(initial):
            score = 5
        else:
            score = 4

        return RubricDimension(
            name="Reflection",
            score=score,
            feedback=(
                "The revised response demonstrates a meaningful change "
                "from the learner's initial thinking."
                if score >= 4
                else
                "The revised response should show a clearer change in "
                "reasoning from the initial answer."
            ),
        )

    @staticmethod
    def _score_keywords(
        response: str,
        keywords: list[str],
    ) -> int:
        matches = sum(
            1
            for keyword in keywords
            if keyword in response
        )

        if matches >= 3:
            return 5

        if matches == 2:
            return 4

        if matches == 1:
            return 3

        return 2