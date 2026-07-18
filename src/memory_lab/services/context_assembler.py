"""
context_assembler.py

Servicio encargado de construir el PromptContext
a partir de la conversación y las memorias.
"""

from memory_lab.models.conversation import Conversation
from memory_lab.models.prompt_context import PromptContext

from memory_lab.repositories.episode_repository import (
    EpisodeRepository,
)
from memory_lab.repositories.semantic_repository import (
    SemanticRepository,
)

from memory_lab.services.episode_retriever import (
    EpisodeRetriever,
)
from memory_lab.services.semantic_retriever import (
    SemanticRetriever,
)


class ContextAssembler:

    def __init__(
        self,
        episode_repository: EpisodeRepository,
        semantic_repository: SemanticRepository,
    ) -> None:

        self.episode_retriever = EpisodeRetriever(
            repository=episode_repository,
        )

        self.semantic_retriever = SemanticRetriever(
            repository=semantic_repository,
        )

    def build(
        self,
        conversation: Conversation,
    ) -> PromptContext:

        episodes = self.episode_retriever.retrieve(
            conversation,
        )

        facts = self.semantic_retriever.retrieve(
            conversation,
        )

        return PromptContext(
            conversation=conversation,
            episodes=episodes,
            facts=facts,
        )