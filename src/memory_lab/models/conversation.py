from dataclasses import dataclass, field

from memory_lab.models.message import Message


@dataclass(slots=True)
class Conversation:
    """
    Representa la conversación actual entre el usuario
    y el asistente.
    """

    messages: list[Message] = field(default_factory=list)

    def add_user_message(self, content: str) -> None:
        self.messages.append(
            Message(
                role="user",
                content=content,
            )
        )

    def add_assistant_message(self, content: str) -> None:
        self.messages.append(
            Message(
                role="assistant",
                content=content,
            )
        )