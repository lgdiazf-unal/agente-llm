from enum import Enum


class EpisodeDecision(str, Enum):
    """
    Decisión tomada por el EpisodeMatcher.
    """

    CREATE = "create"
    UPDATE = "update"