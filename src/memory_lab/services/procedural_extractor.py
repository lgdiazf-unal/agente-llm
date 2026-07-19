"""
Servicio encargado de convertir una conversación
en memoria procedimental utilizando el LLM.
"""

from memory_lab.llm import call_llm

from memory_lab.models.conversation import (
    Conversation,
)
from memory_lab.models.procedure import (
    Procedure,
)

from memory_lab.prompts.procedural_prompt import (
    SYSTEM_PROMPT,
)

from memory_lab.utils.conversation_formatter import (
    format_conversation,
)
from memory_lab.utils.json_parser import (
    parse_llm_json,
)


class ProceduralExtractor:

    def extract(
        self,
        conversation: Conversation,
    ) -> Procedure | None:

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
        )

        data = parse_llm_json(
            response,
        )

        if data.get("action") == "none":

            return None

        return Procedure.create(
            content=data["procedure"],
        )