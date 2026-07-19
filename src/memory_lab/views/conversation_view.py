"""
Vista para mostrar la conversación actual.
"""

from memory_lab.models.conversation import (
    Conversation,
)

from memory_lab.utils.console import (
    Console,
)


def show_conversation(
    conversation: Conversation,
) -> None:

    Console.section(
        "💬 CONVERSATION",
    )

    for message in conversation.messages:

        Console.text(
            f"{message.role.upper()}:"
        )

        Console.text(
            message.content,
        )

        Console.blank()