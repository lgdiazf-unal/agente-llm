"""
Servicio encargado de administrar la memoria episódica.
"""

from memory_lab.models.episode import Episode
from memory_lab.repositories.episode_repository import EpisodeRepository
from memory_lab.services.episode_matcher import EpisodeMatcher


class EpisodeManager:

    def __init__(
        self,
        repository: EpisodeRepository,
    ) -> None:

        self.repository = repository

        self.matcher = EpisodeMatcher(
            repository=repository,
        )

    def process(
        self,
        episode: Episode,
    ) -> None:

        existing = self.matcher.match(
            episode,
        )

        if existing is None:

            self.repository.save(
                episode,
            )

            return

        existing.summary = episode.summary

        self.repository.update(
            existing,
        )