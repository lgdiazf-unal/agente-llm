from dataclasses import dataclass

from memory_lab.models.conversation import Conversation
from memory_lab.models.message import Message


@dataclass(slots=True, frozen=True)
class PromptContext:
    """
    Estado del agente utilizado para construir el prompt.
    """

    conversation: Conversation

    @property
    def messages(self) -> list[Message]:
        """
        Devuelve los mensajes de la conversación.

        El PromptBuilder no necesita conocer cómo están
        almacenados internamente.
        """
        return self.conversation.messages