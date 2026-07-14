from app.services.cognitive_coach import CognitiveCoach

coach = CognitiveCoach()


def generate_coaching_questions(scenario, user_response):
    return coach.generate_questions(
        scenario=scenario,
        user_response=user_response
    )


def generate_feedback(scenario, initial_response, revised_response):
    return coach.generate_feedback(
        scenario=scenario,
        initial_response=initial_response,
        revised_response=revised_response
    )