"""
episode.py

Modelo que representa un recuerdo del agente.
"""

from dataclasses import dataclass
from uuid import uuid4


@dataclass(slots=True)
class Episode:
    """
    Representa un episodio almacenado por el agente.
    """

    id: str
    summary: str

    @classmethod
    def create(cls, summary: str) -> "Episode":
        """
        Crea un episodio con un identificador único.
        """

        return cls(
            id=str(uuid4()),
            summary=summary.strip(),
        )

    def to_dict(self) -> dict:

        return {
            "id": self.id,
            "summary": self.summary,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Episode":

        return cls(
            id=data["id"],
            summary=data["summary"],
        )