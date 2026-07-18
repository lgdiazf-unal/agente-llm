from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompts.chat_prompt import SYSTEM_PROMPT
from memory_lab.prompts.sections.base import PromptSection


class SystemSection(PromptSection):

    @property
    def name(self) -> str:
        return "System"

    def is_enabled(
        self,
        context: PromptContext,
    ) -> bool:

        return True

    def build(
        self,
        context: PromptContext,
    ) -> str:

        return SYSTEM_PROMPT