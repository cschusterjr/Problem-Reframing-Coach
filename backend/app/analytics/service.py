from app.storage.attempt import LearningAttempt


class LearningAnalyticsService:
    """
    Calculates learner-level analytics from completed attempts.
    """

    def summarize(
        self,
        attempts: list[LearningAttempt],
    ) -> dict:
        if not attempts:
            return {
                "challenges_completed": 0,
                "average_score": 0.0,
                "strongest_skill": None,
                "growth_area": None,
            }

        average_score = round(
            sum(
                attempt.overall_score
                for attempt in attempts
            )
            / len(attempts),
            1,
        )

        dimension_scores: dict[str, list[int]] = {}

        for attempt in attempts:
            for dimension in attempt.rubric:
                name = dimension.get("name")
                score = dimension.get("score")

                if name is None or score is None:
                    continue

                dimension_scores.setdefault(
                    name,
                    [],
                ).append(score)

        dimension_averages = {
            name: round(
                sum(scores) / len(scores),
                1,
            )
            for name, scores
            in dimension_scores.items()
            if scores
        }

        strongest_skill = None
        growth_area = None

        if dimension_averages:
            strongest_skill = max(
                dimension_averages,
                key=dimension_averages.get,
            )

            growth_area = min(
                dimension_averages,
                key=dimension_averages.get,
            )

        return {
            "challenges_completed": len(attempts),
            "average_score": average_score,
            "strongest_skill": strongest_skill,
            "growth_area": growth_area,
        }