from fastapi import FastAPI, HTTPException
from app.models import InitialResponse, CoachingResponse, RevisedResponse, FeedbackResponse
from app.scenarios import load_scenarios, get_scenario_by_id
from app.coach import generate_coaching_questions, generate_feedback

app = FastAPI(title="Problem Reframing Coach")


@app.get("/")
def root():
    return {"message": "Problem Reframing Coach API is running."}


@app.get("/scenarios")
def get_scenarios():
    return load_scenarios()


@app.get("/scenarios/{scenario_id}")
def get_scenario(scenario_id: str):
    scenario = get_scenario_by_id(scenario_id)

    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")

    return scenario


@app.post("/coach", response_model=CoachingResponse)
def coach_response(response: InitialResponse):
    scenario = get_scenario_by_id(response.scenario_id)

    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")

    coaching_questions = generate_coaching_questions(response.user_response)

    return CoachingResponse(
        scenario_id=response.scenario_id,
        initial_response=response.user_response,
        coaching_questions=coaching_questions
    )


@app.post("/feedback", response_model=FeedbackResponse)
def feedback_response(response: RevisedResponse):
    scenario = get_scenario_by_id(response.scenario_id)

    if not scenario:
        raise HTTPException(status_code=404, detail="Scenario not found")

    feedback = generate_feedback(
        scenario=scenario,
        initial_response=response.initial_response,
        revised_response=response.revised_response
    )

    return FeedbackResponse(**feedback)