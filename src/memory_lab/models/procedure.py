"""
procedure.py

Modelo que representa una memoria procedimental.
"""

from dataclasses import dataclass
from uuid import uuid4


@dataclass(slots=True)
class Procedure:
    """
    Representa un procedimiento almacenado
    por el agente.
    """

    id: str

    content: str

    @classmethod
    def create(
        cls,
        content: str,
    ) -> "Procedure":

        return cls(
            id=str(uuid4()),
            content=content.strip(),
        )

    def to_dict(
        self,
    ) -> dict:

        return {
            "id": self.id,
            "content": self.content,
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "Procedure":

        return cls(
            id=data["id"],
            content=data["content"],
        )