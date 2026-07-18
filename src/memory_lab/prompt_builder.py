"""
prompt_builder.py

Construye el prompt que será enviado al LLM.
"""

from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompts.chat_prompt import SYSTEM_PROMPT


class PromptBuilder:

    def build(
        self,
        context: PromptContext,
    ) -> list[dict]:

        return [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": self._build_user_prompt(
                    context,
                ),
            },
        ]

    def _build_user_prompt(
        self,
        context: PromptContext,
    ) -> str:

        sections: list[str] = []

        #
        # Context Blocks
        #

        for block in context.blocks:

            sections.append(
                "=============================="
            )

            sections.append(
                block.title
            )

            sections.append(
                "=============================="
            )

            sections.append("")

            for line in block.lines:

                sections.append(
                    f"- {line}"
                )

            sections.append("")
            sections.append("")

        #
        # Current Conversation
        #

        sections.append(
            "=============================="
        )

        sections.append(
            "CURRENT CONVERSATION"
        )

        sections.append(
            "=============================="
        )

        sections.append("")

        for message in context.conversation.messages:

            sections.append(
                f"{message.role.upper()}:"
            )

            sections.append(
                message.content
            )

            sections.append("")

        return "\n".join(
            sections,
        )