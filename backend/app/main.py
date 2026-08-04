import logging
from datetime import datetime

from fastapi import FastAPI, HTTPException

from app.coach import generate_coaching_questions, generate_feedback
from app.models import (
    CoachingResponse,
    FeedbackResponse,
    InitialResponse,
    RevisedResponse,
)
from app.scenarios import get_scenario_by_id, load_scenarios
from app.storage.attempt import LearningAttempt
from app.storage.sqlite_repository import SQLiteAttemptRepository


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(name)s: %(message)s",
)

app = FastAPI(
    title="Problem Reframing Coach",
    description="API for the AI-powered Problem Reframing Coach.",
    version="0.8.0",
)

# Repository used to persist completed learner attempts
attempt_repository = SQLiteAttemptRepository()


@app.get("/")
def root():
    return {
        "message": "Problem Reframing Coach API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.get("/scenarios")
def get_scenarios():
    return load_scenarios()


@app.get("/scenarios/{scenario_id}")
def get_scenario(scenario_id: str):
    scenario = get_scenario_by_id(scenario_id)

    if not scenario:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found",
        )

    return scenario


@app.post("/coach", response_model=CoachingResponse)
def coach_response(response: InitialResponse):
    scenario = get_scenario_by_id(response.scenario_id)

    if not scenario:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found",
        )

    coaching_questions = generate_coaching_questions(
        scenario=scenario,
        user_response=response.user_response,
    )

    return CoachingResponse(
        scenario_id=response.scenario_id,
        initial_response=response.user_response,
        coaching_questions=coaching_questions,
    )


@app.post("/feedback", response_model=FeedbackResponse)
def feedback_response(response: RevisedResponse):
    scenario = get_scenario_by_id(response.scenario_id)

    if not scenario:
        raise HTTPException(
            status_code=404,
            detail="Scenario not found",
        )

    feedback = generate_feedback(
        scenario=scenario,
        initial_response=response.initial_response,
        revised_response=response.revised_response,
    )

    attempt = LearningAttempt(
        timestamp=datetime.now(),
        scenario_id=response.scenario_id,
        initial_response=response.initial_response,
        revised_response=response.revised_response,
        overall_score=feedback["overall_rubric_score"],
        rubric=feedback["rubric_dimensions"],
        key_takeaway=feedback["key_takeaway"],
    )

    attempt_repository.save_attempt(attempt)

    return FeedbackResponse(**feedback)