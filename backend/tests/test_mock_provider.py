from app.services.mock_provider import MockAIProvider


def test_mock_provider_returns_four_questions():
    provider = MockAIProvider()

    scenario = {
        "title": "The Large TV Problem",
        "cognitive_skill": "Problem reframing",
    }

    questions = provider.generate_coaching_questions(
        scenario=scenario,
        learner_response="I would rent a crane.",
    )

    assert isinstance(questions, list)
    assert len(questions) == 4
    assert all(isinstance(question, str) for question in questions)
    assert all(question.strip() for question in questions)