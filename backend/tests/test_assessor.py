from app.assessment.assessor import CognitiveAssessor


def test_assessor_returns_five_rubric_dimensions():
    assessor = CognitiveAssessor()

    rubric = assessor.assess(
        initial_response="I would rent a crane.",
        revised_response=(
            "I would question whether the box must remain fixed, "
            "remove the television from the box, and focus on the "
            "actual goal of moving the television into the room."
        ),
    )

    assert len(rubric.dimensions) == 5

    dimension_names = [
        dimension.name
        for dimension in rubric.dimensions
    ]

    assert dimension_names == [
        "Assumption Awareness",
        "Constraint Flexibility",
        "Problem Framing",
        "Simplification",
        "Reflection",
    ]


def test_assessor_scores_remain_within_rubric_range():
    assessor = CognitiveAssessor()

    rubric = assessor.assess(
        initial_response="I would rent a crane.",
        revised_response=(
            "I would question the fixed assumptions, change the "
            "constraint, simplify the task, and focus on the real goal."
        ),
    )

    assert all(
        1 <= dimension.score <= 5
        for dimension in rubric.dimensions
    )

    assert 1.0 <= rubric.overall_score <= 5.0


def test_assessor_rewards_meaningful_revision():
    assessor = CognitiveAssessor()

    rubric = assessor.assess(
        initial_response="I would rent a crane.",
        revised_response=(
            "Instead of adding equipment, I would question whether "
            "the packaging is necessary and simplify the problem first."
        ),
    )

    reflection = next(
        dimension
        for dimension in rubric.dimensions
        if dimension.name == "Reflection"
    )

    assert reflection.score >= 4