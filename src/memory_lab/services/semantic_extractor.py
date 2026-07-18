"""
Servicio encargado de convertir una conversación
en memoria semántica utilizando el LLM.
"""

from memory_lab.llm import call_llm
from memory_lab.models.conversation import Conversation
from memory_lab.models.fact import Fact
from memory_lab.prompts.semantic_prompt import SYSTEM_PROMPT
from memory_lab.utils.conversation_formatter import format_conversation


class SemanticExtractor:

    def extract(
        self,
        conversation: Conversation,
    ) -> Fact | None:

        conversation_text = format_conversation(
            conversation,
        )

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

        response = call_llm(
            messages,
        ).strip()

        if response.upper() == "NONE":

            return None

        return Fact.create(
            content=response,
        )