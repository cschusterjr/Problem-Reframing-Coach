from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_feedback_endpoint_returns_cognitive_rubric():
    response = client.post(
        "/feedback",
        json={
            "scenario_id": "tv_delivery",
            "initial_response": "I would rent a crane.",
            "revised_response": (
                "I would question whether the box must remain fixed, "
                "remove the television from the box, and focus on the "
                "actual goal of moving the television into the room."
            ),
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "overall_rubric_score" in body
    assert "rubric_dimensions" in body
    assert len(body["rubric_dimensions"]) == 5

    dimension_names = [
        dimension["name"]
        for dimension in body["rubric_dimensions"]
    ]

    assert dimension_names == [
        "Assumption Awareness",
        "Constraint Flexibility",
        "Problem Framing",
        "Simplification",
        "Reflection",
    ]

    assert 1.0 <= body["overall_rubric_score"] <= 5.0

    assert all(
        1 <= dimension["score"] <= 5
        for dimension in body["rubric_dimensions"]
    )