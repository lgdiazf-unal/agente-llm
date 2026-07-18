"""
Servicio encargado de recuperar memoria semántica.
"""

from memory_lab.models.conversation import Conversation
from memory_lab.models.fact import Fact
from memory_lab.repositories.semantic_repository import (
    SemanticRepository,
)


class SemanticRetriever:

    def __init__(
        self,
        repository: SemanticRepository,
    ) -> None:

        self.repository = repository

    def retrieve(
        self,
        conversation: Conversation,
    ) -> list[Fact]:
        """
        En esta primera implementación retorna toda
        la memoria semántica.

        En las siguientes etapas se incorporará un
        mecanismo de recuperación más selectivo.
        """

        return self.repository.load_all()