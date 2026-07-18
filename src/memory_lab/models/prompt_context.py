"""
prompt_context.py

Contiene toda la información necesaria para construir
el prompt que será enviado al LLM.
"""

from dataclasses import dataclass, field

from memory_lab.models.conversation import Conversation
from memory_lab.models.episode import Episode
from memory_lab.models.fact import Fact


@dataclass(slots=True)
class PromptContext:
    """
    Contexto completo utilizado por el PromptBuilder.
    """

    conversation: Conversation

    episodes: list[Episode] = field(
        default_factory=list,
    )

    facts: list[Fact] = field(
        default_factory=list,
    )