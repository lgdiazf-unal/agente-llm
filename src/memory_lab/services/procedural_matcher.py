"""
Servicio encargado de decidir si un procedimiento
debe crearse o actualizarse.
"""

import json

from memory_lab.llm import call_llm

from memory_lab.models.procedure import Procedure

from memory_lab.prompts.procedural_matcher_prompt import (
    SYSTEM_PROMPT,
)

from memory_lab.utils.procedure_formatter import (
    format_procedures,
)


class ProceduralMatcher:

    def match(
        self,
        procedures: list[Procedure],
        candidate: Procedure,
    ) -> dict:

        procedures_text = format_procedures(
            procedures,
        )

        user_prompt = f"""
EXISTING PROCEDURES

{procedures_text}

----------------------------------------

CANDIDATE PROCEDURE

{candidate.content}
""".strip()

        response = call_llm(
            [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ]
        )

        return json.loads(
            response,
        )