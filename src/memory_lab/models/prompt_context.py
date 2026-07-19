"""
prompt_context.py

Contiene toda la información necesaria para construir
el prompt enviado al LLM.
"""

from dataclasses import dataclass, field

from memory_lab.models.conversation import (
    Conversation,
)

from memory_lab.models.context_block import (
    ContextBlock,
)


@dataclass(slots=True)
class PromptContext:
    """
    Contexto completo utilizado por PromptBuilder.

    Contiene:
    - conversación actual
    - bloques de memoria recuperada
    """


    conversation: Conversation


    blocks: list[ContextBlock] = field(
        default_factory=list,
    )