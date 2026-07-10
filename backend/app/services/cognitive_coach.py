class CognitiveCoach:
    """
    Core coaching engine.

    This class contains the instructional logic that guides learners
    through identifying assumptions, reframing problems, and reflecting
    on their thinking.

    Later, individual methods will call GPT instead of returning
    hardcoded responses.
    """

    def analyze_response(self, user_response: str):
        """
        Placeholder for future AI analysis.
        """
        return {
            "response_length": len(user_response),
            "contains_solution": True
        }

    def generate_questions(self, scenario):
        return [
            "What assumptions are you making about the object, the space, or the process?",
            "What part of the situation are you treating as fixed that might actually be changeable?",
            "What is the real goal you are trying to accomplish?",
            "What could be removed, reduced, or changed before choosing a complex solution?"
        ]

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
            "problem"
        ]

        for keyword in keywords:
            if keyword in revised:
                return 10

        return 7

    def generate_feedback(self, scenario, initial_response, revised_response):

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