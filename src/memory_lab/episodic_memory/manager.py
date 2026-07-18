from memory_lab.models.episode import Episode
from memory_lab.repositories.base_episode_repository import (
    BaseEpisodeRepository,
)


class EpisodeManager:
    """
    Coordina la administración de la memoria episódica.

    En v0.7 simplemente persiste episodios.
    En versiones posteriores decidirá si crear,
    actualizar o fusionar.
    """

    def __init__(
        self,
        repository: BaseEpisodeRepository,
    ) -> None:

        self._repository = repository

    def process(
        self,
        episode: Episode | None,
    ) -> None:

        if episode is None:
            return

        self._repository.save(episode)