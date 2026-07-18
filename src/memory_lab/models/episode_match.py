from dataclasses import dataclass

from memory_lab.models.episode import Episode


@dataclass
class EpisodeMatch:

    matched: bool

    episode: Episode | None = None