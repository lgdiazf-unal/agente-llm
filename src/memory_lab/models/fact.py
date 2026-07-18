"""
fact.py

Modelo que representa un conocimiento permanente del agente.
"""

from dataclasses import dataclass
from uuid import uuid4


@dataclass(slots=True)
class Fact:
    """
    Representa un conocimiento semántico.
    """

    id: str
    content: str

    @classmethod
    def create(
        cls,
        content: str,
    ) -> "Fact":

        return cls(
            id=str(uuid4()),
            content=content.strip(),
        )

    def to_dict(self) -> dict:

        return {
            "id": self.id,
            "content": self.content,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "Fact":

        return cls(
            id=data["id"],
            content=data["content"],
        )