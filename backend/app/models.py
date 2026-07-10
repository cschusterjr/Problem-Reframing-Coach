from pydantic import BaseModel


class InitialResponse(BaseModel):
    scenario_id: str
    user_response: str


class CoachingResponse(BaseModel):
    scenario_id: str
    initial_response: str
    coaching_questions: list[str]


class RevisedResponse(BaseModel):
    scenario_id: str
    initial_response: str
    revised_response: str


class FeedbackResponse(BaseModel):
    scenario_id: str
    original_frame: str
    better_frame: str
    hidden_assumption: str
    simple_solution: str
    feedback: str
    score: int
    key_takeaway: str
    reflection_prompt: str
    real_world_applications: list[str]