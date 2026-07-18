"""
Servicio encargado de decidir si un conocimiento
debe crearse o actualizar uno existente.
"""

import json

from memory_lab.llm import call_llm
from memory_lab.models.fact import Fact
from memory_lab.prompts.semantic_matcher_prompt import (
    SYSTEM_PROMPT,
)
from memory_lab.repositories.semantic_repository import (
    SemanticRepository,
)
from memory_lab.utils.json_parser import (
    parse_llm_json,
)


class SemanticMatcher:

    def __init__(
        self,
        repository: SemanticRepository,
    ) -> None:

        self.repository = repository

    def match(
        self,
        fact: Fact,
    ) -> Fact | None:

        facts = self.repository.load_all()

        if not facts:

            return None

        existing = json.dumps(
            [
                item.to_dict()
                for item in facts
            ],
            indent=4,
            ensure_ascii=False,
        )

        candidate = json.dumps(
            fact.to_dict(),
            indent=4,
            ensure_ascii=False,
        )

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content":
                    f"Existing facts:\n\n"
                    f"{existing}\n\n"
                    f"Candidate fact:\n\n"
                    f"{candidate}",
            },
        ]

        response = call_llm(
            messages,
        )

        decision = parse_llm_json(
            response,
        )

        if decision["action"] == "create":

            return None

        fact_id = decision["fact_id"]

        for existing_fact in facts:

            if existing_fact.id == fact_id:

                return existing_fact

        return None