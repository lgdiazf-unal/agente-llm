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

        user_prompt = self._build_user_prompt(
            context,
        )

        return [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

    def _build_user_prompt(
        self,
        context: PromptContext,
    ) -> str:

        sections: list[str] = []

        #
        # Semantic Memory
        #

        if context.facts:

            sections.append(
                "=============================="
            )

            sections.append(
                "SEMANTIC MEMORY"
            )

            sections.append(
                "=============================="
            )

            sections.append("")

            for fact in context.facts:

                sections.append(
                    f"- {fact.content}"
                )

            sections.append("")
            sections.append("")

        #
        # Episodic Memory
        #

        if context.episodes:

            sections.append(
                "=============================="
            )

            sections.append(
                "EPISODIC MEMORY"
            )

            sections.append(
                "=============================="
            )

            sections.append("")

            for episode in context.episodes:

                sections.append(
                    f"- {episode.summary}"
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