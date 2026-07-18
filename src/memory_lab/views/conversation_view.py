from memory_lab.models.conversation import Conversation
from memory_lab.utils.printer import (
    print_separator,
    print_text,
    print_title,
)


def show(conversation: Conversation) -> None:

    print_title("WORKING MEMORY")

    if not conversation.messages:

        print_text("(vacía)")
        return

    for message in conversation.messages:

        print_text(f"[{message.role.upper()}]")
        print_text(message.content)

        print_separator()