"""
episode.py

Representa un recuerdo generado a partir de una conversación.
"""

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Episode:
    """
    Representa un episodio extraído desde una conversación.
    """

    summary: str