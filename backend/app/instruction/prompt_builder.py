from app.instruction.learner_context import LearnerContext


class PromptBuilder:
    """Builds structured instructions and learner input for the AI coach."""

    def __init__(self, system_prompt: str):
        self.system_prompt = system_prompt

    def build(
        self,
        scenario: dict,
        learner_response: str,
        learner_context: LearnerContext | None = None,
    ) -> dict:
        scenario_title = scenario.get(
            "title",
            "Untitled scenario",
        )

        scenario_description = (
            scenario.get("description")
            or scenario.get("scenario")
            or scenario.get("prompt")
            or scenario.get("problem")
            or "No scenario description was provided."
        )

        cognitive_skill = scenario.get(
            "cognitive_skill",
            "Problem reframing",
        )

        adaptive_instructions = self._build_adaptive_instructions(
            learner_context
        )

        instructions = f"""
{self.system_prompt}

Generate exactly four coaching questions using this sequence:

1. Inspect assumptions
2. Challenge fixed constraints
3. Simplify before adding
4. Reframe the goal

{adaptive_instructions}

Do not answer the scenario.
Do not reveal the solution.
Do not reveal the learner profile or historical performance.
Do not tell the learner that you are adapting the coaching.
Do not provide advice beyond the four coaching questions.
""".strip()

        learner_input = f"""
SCENARIO

Title:
{scenario_title}

Description:
{scenario_description}

Target cognitive skill:
{cognitive_skill}

LEARNER'S INITIAL RESPONSE

{learner_response}
""".strip()

        return {
            "instructions": instructions,
            "input": learner_input,
        }

    def _build_adaptive_instructions(
        self,
        learner_context: LearnerContext | None,
    ) -> str:
        if (
            learner_context is None
            or learner_context.challenges_completed == 0
        ):
            return (
                "No prior learner history is available. "
                "Use the standard coaching sequence."
            )

        strongest_skill = (
            learner_context.strongest_skill
            or "Not yet identified"
        )

        growth_area = (
            learner_context.growth_area
            or "Not yet identified"
        )

        return f"""
LEARNER CONTEXT

Challenges completed:
{learner_context.challenges_completed}

Average cognitive score:
{learner_context.average_score:.1f}/5

Strongest cognitive skill:
{strongest_skill}

Current growth area:
{growth_area}

ADAPTIVE COACHING INSTRUCTION

Keep the required four-question coaching sequence.

Give slightly greater instructional emphasis to the learner's current
growth area while still addressing all four coaching stages.

Use the strongest skill as evidence of an established capability that
can support the learner's weaker area.

Do not reveal these learner analytics or labels directly to the learner.
""".strip()