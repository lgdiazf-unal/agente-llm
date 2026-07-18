"""
episode_retriever.py

Recupera episodios relevantes para enriquecer
el contexto del agente.
"""

from memory_lab.models.conversation import Conversation
from memory_lab.models.episode import Episode
from memory_lab.repositories.episode_repository import EpisodeRepository


class EpisodeRetriever:
    """
    Primera implementación.

    Recupera simplemente los últimos N episodios.
    """

    def __init__(
        self,
        repository: EpisodeRepository,
        limit: int = 3,
    ) -> None:

        self._repository = repository
        self._limit = limit

    def retrieve(
        self,
        conversation: Conversation,
    ) -> list[Episode]:
        """
        Recupera los últimos N episodios.

        Por ahora no analiza la conversación.
        """

        episodes = self._repository.load_all()

        return episodes[-self._limit :]