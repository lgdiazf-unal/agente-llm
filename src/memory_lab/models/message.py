from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Message:
    """
    Representa un mensaje dentro de una conversación.
    """

    role: str
    content: str