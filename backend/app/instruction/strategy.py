from dataclasses import dataclass


@dataclass
class InstructionalStrategy:
    """
    Describes HOW the AI should coach a learner.
    """

    name: str
    coaching_goal: str
    coaching_principles: list[str]