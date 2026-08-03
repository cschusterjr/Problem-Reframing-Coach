from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_coach_endpoint_returns_questions():
    response = client.post(
        "/coach",
        json={
            "scenario_id": "tv_delivery",
            "user_response": "I would rent a crane."
        },
    )

    assert response.status_code == 200

    body = response.json()

    assert "coaching_questions" in body
    assert len(body["coaching_questions"]) == 4