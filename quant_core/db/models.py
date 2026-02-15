from dataclasses import dataclass


@dataclass(slots=True)
class SkillNode:
    id: str
    name: str
    domain: str
    description: str
    prereqs_json: str
    mastery_score: float
    last_practiced: str | None
    target_mastery: float
