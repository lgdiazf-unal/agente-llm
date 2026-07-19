"""
fact.py

Modelo que representa un conocimiento permanente del agente.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class Fact:
    """
    Representa un conocimiento semántico.
    """

    id: str
    content: str

    score: float
    access_count: int

    created_at: str
    updated_at: str
    last_access: str | None

    @classmethod
    def create(
        cls,
        content: str,
    ) -> "Fact":

        now = datetime.now().isoformat()

        return cls(
            id=str(uuid4()),
            content=content.strip(),
            score=1.0,
            access_count=0,
            created_at=now,
            updated_at=now,
            last_access=None,
        )

    def to_dict(
        self,
    ) -> dict:

        return {
            "id": self.id,
            "content": self.content,
            "score": self.score,
            "access_count": self.access_count,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "last_access": self.last_access,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "Fact":

        now = datetime.now().isoformat()

        return cls(
            id=data["id"],
            content=data["content"],
            score=data.get("score", 1.0),
            access_count=data.get("access_count", 0),
            created_at=data.get("created_at", now),
            updated_at=data.get("updated_at", now),
            last_access=data.get("last_access"),
        )