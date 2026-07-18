"""
prompt_context.py

Contiene toda la información necesaria para construir
el prompt que será enviado al LLM.
"""

from dataclasses import dataclass, field

from memory_lab.models.context_block import ContextBlock
from memory_lab.models.conversation import Conversation


@dataclass(slots=True)
class PromptContext:
    """
    Contexto completo utilizado por el PromptBuilder.
    """

    conversation: Conversation

    blocks: list[ContextBlock] = field(
        default_factory=list,
    )