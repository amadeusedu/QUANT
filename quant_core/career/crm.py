from dataclasses import dataclass

@dataclass(slots=True)
class Contact:
    name: str
    org: str
    notes: str
