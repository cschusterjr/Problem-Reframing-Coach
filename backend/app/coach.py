def generate_coaching_questions(user_response: str):
    return [
        "What assumptions are you making about the object, the space, or the process?",
        "What part of the situation are you treating as fixed that might actually be changeable?",
        "What is the real goal: moving the box, or moving the TV safely into the room?",
        "What could be removed, reduced, or changed before choosing a complex solution?"
    ]


def generate_feedback(scenario, initial_response: str, revised_response: str):
    score = 7

    if "box" in revised_response.lower() or "unbox" in revised_response.lower():
        score = 10

    return {
        "scenario_id": scenario["id"],
        "original_frame": "How do we move a large boxed TV to the 8th floor?",
        "better_frame": scenario["better_frame"],
        "hidden_assumption": scenario["hidden_assumption"],
        "simple_solution": scenario["simple_solution"],
        "feedback": "Your revised response shows stronger problem reframing. The key move is shifting from moving the boxed object to safely moving the actual TV.",
        "score": score
    }