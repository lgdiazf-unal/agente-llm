"""
Servicio encargado de administrar la memoria semántica.
"""

from memory_lab.models.fact import Fact
from memory_lab.repositories.semantic_repository import (
    SemanticRepository,
)
from memory_lab.services.semantic_matcher import (
    SemanticMatcher,
)


class SemanticManager:

    def __init__(
        self,
        repository: SemanticRepository,
    ) -> None:

        self.repository = repository

        self.matcher = SemanticMatcher(
            repository=repository,
        )

    def process(
        self,
        fact: Fact | None,
    ) -> None:

        if fact is None:

            return

        existing = self.matcher.match(
            fact,
        )

        if existing is None:

            self.repository.save(
                fact,
            )

            return

        existing.content = fact.content

        self.repository.update(
            existing,
        )