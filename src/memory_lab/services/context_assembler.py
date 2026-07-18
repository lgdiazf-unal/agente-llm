"""
context_assembler.py

Servicio encargado de construir el PromptContext
a partir de la conversación y las memorias.
"""

from memory_lab.models.context_block import ContextBlock
from memory_lab.models.conversation import Conversation
from memory_lab.models.prompt_context import PromptContext

from memory_lab.repositories.episode_repository import (
    EpisodeRepository,
)
from memory_lab.repositories.semantic_repository import (
    SemanticRepository,
)
from memory_lab.repositories.procedural_repository import (
    ProceduralRepository,
)

from memory_lab.services.episode_retriever import (
    EpisodeRetriever,
)
from memory_lab.services.semantic_retriever import (
    SemanticRetriever,
)
from memory_lab.services.procedural_retriever import (
    ProceduralRetriever,
)


class ContextAssembler:

    def __init__(
        self,
        episode_repository: EpisodeRepository,
        semantic_repository: SemanticRepository,
        procedural_repository: ProceduralRepository,
    ) -> None:

        self.episode_retriever = EpisodeRetriever(
            repository=episode_repository,
        )

        self.semantic_retriever = SemanticRetriever(
            repository=semantic_repository,
        )

        self.procedural_retriever = ProceduralRetriever(
            repository=procedural_repository,
        )

    def build(
        self,
        conversation: Conversation,
    ) -> PromptContext:

        blocks: list[ContextBlock] = []

        #
        # Semantic Memory
        #

        facts = self.semantic_retriever.retrieve(
            conversation,
        )

        if facts:

            blocks.append(
                ContextBlock(
                    title="SEMANTIC MEMORY",
                    lines=[
                        fact.content
                        for fact in facts
                    ],
                )
            )

        #
        # Episodic Memory
        #

        episodes = self.episode_retriever.retrieve(
            conversation,
        )

        if episodes:

            blocks.append(
                ContextBlock(
                    title="EPISODIC MEMORY",
                    lines=[
                        episode.summary
                        for episode in episodes
                    ],
                )
            )

        #
        # Procedural Memory
        #

        procedures = self.procedural_retriever.retrieve(
            conversation,
        )

        if procedures:

            blocks.append(
                ContextBlock(
                    title="PROCEDURAL MEMORY",
                    lines=[
                        procedure.content
                        for procedure in procedures
                    ],
                )
            )

        return PromptContext(
            conversation=conversation,
            blocks=blocks,
        )