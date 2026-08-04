from app.assessment.assessor import CognitiveAssessor
from app.services.provider_factory import create_ai_provider


class CognitiveCoach:
    """
    Core coaching engine.

    The coach owns the instructional and assessment logic.
    The AI provider owns how coaching questions are generated.
    """

    def __init__(self, ai_provider=None):
        self.ai_provider = ai_provider or create_ai_provider()
        self.assessor = CognitiveAssessor()

    def analyze_response(self, user_response: str) -> dict:
        return {
            "response_length": len(user_response),
            "contains_solution": bool(user_response.strip()),
        }

    def generate_questions(
        self,
        scenario: dict,
        user_response: str,
    ) -> list[str]:
        self.analyze_response(user_response)

        return self.ai_provider.generate_coaching_questions(
            scenario=scenario,
            learner_response=user_response,
        )

    def score_response(self, revised_response: str) -> int:
        """
        Legacy score retained temporarily for UI compatibility.

        This will be removed after the Streamlit feedback screen is fully
        migrated to the cognitive rubric.
        """

        revised = revised_response.lower()

        keywords = [
            "box",
            "remove",
            "unbox",
            "air",
            "tire",
            "meeting",
            "customer",
            "problem",
            "simplify",
            "constraint",
        ]

        for keyword in keywords:
            if keyword in revised:
                return 10

        return 7

    def generate_feedback(
        self,
        scenario: dict,
        initial_response: str,
        revised_response: str,
    ) -> dict:
        rubric = self.assessor.assess(
            initial_response=initial_response,
            revised_response=revised_response,
        )

        legacy_score = self.score_response(revised_response)

        rubric_dimensions = [
            {
                "name": dimension.name,
                "score": dimension.score,
                "feedback": dimension.feedback,
            }
            for dimension in rubric.dimensions
        ]

        return {
            "scenario_id": scenario["id"],
            "original_frame": scenario["original_frame"],
            "better_frame": scenario["better_frame"],
            "hidden_assumption": scenario["hidden_assumption"],
            "simple_solution": scenario["simple_solution"],
            "feedback": (
                "Your revised response shows stronger problem reframing. "
                "The rubric below explains how your reasoning changed across "
                "several cognitive dimensions."
            ),
            "score": legacy_score,
            "overall_rubric_score": rubric.overall_score,
            "rubric_dimensions": rubric_dimensions,
            "key_takeaway": scenario["key_takeaway"],
            "reflection_prompt": scenario["reflection_prompt"],
            "real_world_applications": scenario[
                "real_world_applications"
            ],
        }