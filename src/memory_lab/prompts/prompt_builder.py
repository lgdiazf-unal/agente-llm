"""
Construye el prompt que será enviado al LLM.

Su responsabilidad es únicamente orquestar las distintas
secciones del prompt.
"""

from memory_lab.models.prompt import Prompt
from memory_lab.models.prompt_context import PromptContext

from memory_lab.prompts.sections.base import PromptSection
from memory_lab.prompts.sections.system import SystemSection
from memory_lab.prompts.sections.episodic_memory import (
    EpisodicMemorySection,
)
from memory_lab.prompts.sections.conversation import (
    ConversationSection,
)


class PromptBuilder:
    """
    Construye el prompt final utilizando un pipeline
    de secciones independientes.
    """

    def __init__(self) -> None:

        self._pipeline = self._build_pipeline()

    def build(
        self,
        context: PromptContext,
    ) -> Prompt:

        system_prompt = ""
        user_parts: list[str] = []

        for section in self._pipeline:

            if not section.is_enabled(context):
                continue

            content = section.build(context)

            if not content.strip():
                continue

            if isinstance(section, SystemSection):
                system_prompt = content
            else:
                user_parts.append(content)

        user_prompt = "\n\n".join(user_parts)

        return Prompt(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ]
        )

    def _build_pipeline(
        self,
    ) -> list[PromptSection]:

        return [

            SystemSection(),

            EpisodicMemorySection(),

            ConversationSection(),

        ]