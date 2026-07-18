"""
Construye la sección correspondiente
a la conversación actual.
"""

from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompts.sections.base import PromptSection


class ConversationSection(PromptSection):

    def build(
        self,
        context: PromptContext,
    ) -> str:

        lines: list[str] = []

        lines.append(
            "=============================="
        )

        lines.append(
            "CURRENT CONVERSATION"
        )

        lines.append(
            "=============================="
        )

        lines.append("")

        for message in context.conversation.messages:

            lines.append(
                f"{message.role.upper()}:"
            )

            lines.append(
                message.content
            )

            lines.append("")

        return "\n".join(lines)