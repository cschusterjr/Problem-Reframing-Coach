from app.assessment.assessor import CognitiveAssessor


def test_stronger_revision_scores_higher_than_weak_revision():
    assessor = CognitiveAssessor()

    initial_response = "I would rent a crane."

    weak_rubric = assessor.assess(
        initial_response=initial_response,
        revised_response="I would still rent a crane.",
    )

    strong_rubric = assessor.assess(
        initial_response=initial_response,
        revised_response=(
            "I would question whether the box must remain fixed, "
            "remove the television from the box, simplify the task, "
            "and focus on the actual goal of moving the television "
            "into the room."
        ),
    )

    assert strong_rubric.overall_score > weak_rubric.overall_score


def test_unchanged_response_receives_low_reflection_score():
    assessor = CognitiveAssessor()

    rubric = assessor.assess(
        initial_response="I would rent a crane.",
        revised_response="I would rent a crane.",
    )

    reflection = next(
        dimension
        for dimension in rubric.dimensions
        if dimension.name == "Reflection"
    )

    assert reflection.score <= 2