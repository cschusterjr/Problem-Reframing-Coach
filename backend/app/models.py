from datetime import datetime

from pydantic import BaseModel, Field


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


class RubricDimensionResponse(BaseModel):
    name: str
    score: int = Field(ge=1, le=5)
    feedback: str


class FeedbackResponse(BaseModel):
    scenario_id: str
    original_frame: str
    better_frame: str
    hidden_assumption: str
    simple_solution: str
    feedback: str

    # Legacy score retained temporarily for compatibility.
    score: int

    overall_rubric_score: float = Field(
        ge=1.0,
        le=5.0,
    )

    rubric_dimensions: list[RubricDimensionResponse]

    key_takeaway: str
    reflection_prompt: str
    real_world_applications: list[str]


class LearningAttemptResponse(BaseModel):
    timestamp: datetime
    scenario_id: str
    initial_response: str
    revised_response: str
    overall_score: float
    rubric: list[dict]
    key_takeaway: str


class LearningAnalyticsResponse(BaseModel):
    challenges_completed: int
    average_score: float
    strongest_skill: str | None
    growth_area: str | None