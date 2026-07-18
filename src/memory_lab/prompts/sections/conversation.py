from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompts.sections.base import PromptSection
from memory_lab.prompts.sections.helpers import build_header


class ConversationSection(PromptSection):

    @property
    def name(self) -> str:
        return "Conversation"

    def is_enabled(
        self,
        context: PromptContext,
    ) -> bool:

        return True

    def build(
        self,
        context: PromptContext,
    ) -> str:

        text = build_header(
            "CURRENT CONVERSATION",
        )

        for message in context.conversation.messages:

            text += f"{message.role.upper()}:\n"

            text += f"{message.content}\n\n"

        return text