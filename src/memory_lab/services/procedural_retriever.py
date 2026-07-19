"""
Servicio encargado de recuperar memoria procedimental.
"""

from memory_lab.models.conversation import Conversation
from memory_lab.models.procedure import Procedure

from memory_lab.repositories.procedural_repository import (
    ProceduralRepository,
)


class ProceduralRetriever:

    def __init__(
        self,
        repository: ProceduralRepository,
    ) -> None:

        self.repository = repository

    def retrieve(
        self,
        conversation: Conversation,
    ) -> list[Procedure]:
        """
        Primera implementación.

        Recupera todos los procedimientos.

        En versiones posteriores se reemplazará
        por recuperación basada en relevancia.
        """

        return self.repository.load_all()