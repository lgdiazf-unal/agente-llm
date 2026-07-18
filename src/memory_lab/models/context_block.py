"""
context_block.py

Representa una sección del contexto enviada al PromptBuilder.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class ContextBlock:
    """
    Bloque genérico del contexto.
    """

    title: str

    lines: list[str]