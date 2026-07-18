from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompts.sections.base import PromptSection
from memory_lab.prompts.sections.helpers import build_header


class EpisodicMemorySection(PromptSection):

    @property
    def name(self) -> str:
        return "Episodic Memory"

    def is_enabled(
        self,
        context: PromptContext,
    ) -> bool:

        return bool(
            context.episodes,
        )

    def build(
        self,
        context: PromptContext,
    ) -> str:

        text = build_header(
            "EPISODIC MEMORY",
        )

        for episode in context.episodes:

            text += f"- {episode.summary}\n"

        text += "\n"

        return text