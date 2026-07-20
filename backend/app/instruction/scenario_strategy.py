from app.instruction.strategy import InstructionalStrategy


QUESTION_ASSUMPTIONS = InstructionalStrategy(
    name="Question Assumptions",
    coaching_goal=(
        "Help the learner recognize hidden assumptions before attempting "
        "to solve the problem."
    ),
    coaching_principles=[
        "Ask about hidden assumptions.",
        "Challenge fixed constraints.",
        "Encourage simpler alternatives.",
        "Do not reveal the solution.",
    ],
)


CHALLENGE_CONSTRAINTS = InstructionalStrategy(
    name="Challenge Constraints",
    coaching_goal=(
        "Help the learner determine whether the perceived constraints "
        "are actually fixed."
    ),
    coaching_principles=[
        "Question physical or procedural constraints.",
        "Encourage reversible changes.",
        "Prefer low-cost experiments.",
        "Do not reveal the solution.",
    ],
)


REMOVE_BEFORE_ADD = InstructionalStrategy(
    name="Remove Before Add",
    coaching_goal=(
        "Encourage removing unnecessary complexity before adding resources."
    ),
    coaching_principles=[
        "Remove before adding.",
        "Question existing work.",
        "Simplify first.",
        "Do not reveal the solution.",
    ],
)


STRATEGY_MAP = {
    "Questioning Assumptions": QUESTION_ASSUMPTIONS,
    "Changing Constraints": CHALLENGE_CONSTRAINTS,
    "Remove Before Add": REMOVE_BEFORE_ADD,
}


def get_instructional_strategy(
    scenario: dict
) -> InstructionalStrategy:
    skill = scenario.get("cognitive_skill")

    return STRATEGY_MAP.get(
        skill,
        QUESTION_ASSUMPTIONS,
    )