from app.analytics.service import LearningAnalyticsService
from app.instruction.learner_context import LearnerContext
from app.storage.attempt import LearningAttempt


class LearnerContextService:
    """
    Builds learner context from historical learning attempts.
    """

    def __init__(
        self,
        analytics_service: LearningAnalyticsService | None = None,
    ):
        self.analytics_service = (
            analytics_service
            or LearningAnalyticsService()
        )

    def build(
        self,
        attempts: list[LearningAttempt],
    ) -> LearnerContext:
        summary = self.analytics_service.summarize(
            attempts
        )

        return LearnerContext(
            strongest_skill=summary[
                "strongest_skill"
            ],
            growth_area=summary[
                "growth_area"
            ],
            challenges_completed=summary[
                "challenges_completed"
            ],
            average_score=summary[
                "average_score"
            ],
        )