"""
episode.py

Modelo que representa un recuerdo del agente.
"""

from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class Episode:
    """
    Representa un episodio almacenado por el agente.
    """

    id: str
    summary: str

    score: float
    access_count: int

    created_at: str
    updated_at: str
    last_access: str | None

    @classmethod
    def create(
        cls,
        summary: str,
    ) -> "Episode":

        now = datetime.now().isoformat()

        return cls(
            id=str(uuid4()),
            summary=summary.strip(),
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
            "summary": self.summary,
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
    ) -> "Episode":

        now = datetime.now().isoformat()

        return cls(
            id=data["id"],
            summary=data["summary"],
            score=data.get("score", 1.0),
            access_count=data.get("access_count", 0),
            created_at=data.get("created_at", now),
            updated_at=data.get("updated_at", now),
            last_access=data.get("last_access"),
        )