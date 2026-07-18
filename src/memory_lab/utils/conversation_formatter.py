"""
Convierte una conversación en texto plano para utilizarla
en prompts internos.
"""

from memory_lab.models.conversation import Conversation


def format_conversation(conversation: Conversation) -> str:

    lines: list[str] = []

    for message in conversation.messages:

        lines.append(f"{message.role.upper()}:")
        lines.append(message.content)
        lines.append("")

    return "\n".join(lines)