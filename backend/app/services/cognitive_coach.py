from app.services.provider_factory import create_ai_provider


class CognitiveCoach:
    """
    Core coaching engine.

    The coach owns the instructional logic.
    The AI provider owns how coaching text is generated.
    """

    def __init__(self, ai_provider=None):
        self.ai_provider = ai_provider or create_ai_provider()

    def analyze_response(self, user_response: str):
        return {
            "response_length": len(user_response),
            "contains_solution": bool(user_response.strip())
        }

    def generate_questions(self, scenario: dict, user_response: str):
        self.analyze_response(user_response)

        return self.ai_provider.generate_coaching_questions(
            scenario=scenario,
            user_response=user_response
        )

    def score_response(self, revised_response: str):
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
            "constraint"
        ]

        for keyword in keywords:
            if keyword in revised:
                return 10

        return 7

    def generate_feedback(
        self,
        scenario: dict,
        initial_response: str,
        revised_response: str
    ):
        score = self.score_response(revised_response)

        return {
            "scenario_id": scenario["id"],
            "original_frame": scenario["original_frame"],
            "better_frame": scenario["better_frame"],
            "hidden_assumption": scenario["hidden_assumption"],
            "simple_solution": scenario["simple_solution"],
            "feedback": (
                "Your revised response shows stronger problem reframing. "
                "The key move is shifting away from the first obvious solution "
                "and questioning whether the original frame was too narrow."
            ),
            "score": score,
            "key_takeaway": scenario["key_takeaway"],
            "reflection_prompt": scenario["reflection_prompt"],
            "real_world_applications": scenario["real_world_applications"]
        }