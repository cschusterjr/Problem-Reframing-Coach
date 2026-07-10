from app.services.cognitive_coach import CognitiveCoach

coach = CognitiveCoach()


def generate_coaching_questions(scenario, user_response):
    coach.analyze_response(user_response)
    return coach.generate_questions(scenario)


def generate_feedback(scenario, initial_response, revised_response):
    return coach.generate_feedback(
        scenario,
        initial_response,
        revised_response
    )