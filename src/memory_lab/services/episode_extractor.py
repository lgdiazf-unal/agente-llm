"""
Servicio encargado de convertir una conversación
en un episodio utilizando el LLM.
"""

from memory_lab.llm import call_llm
from memory_lab.models.conversation import Conversation
from memory_lab.models.episode import Episode
from memory_lab.prompts.episode_prompt import SYSTEM_PROMPT
from memory_lab.utils.conversation_formatter import format_conversation


class EpisodeExtractor:

    def extract(
        self,
        conversation: Conversation,
    ) -> Episode:

        conversation_text = format_conversation(conversation)

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": conversation_text,
            },
        ]

        response = call_llm(messages)

        return Episode.create(
            summary=response,
        )