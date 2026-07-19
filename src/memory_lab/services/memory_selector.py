"""
memory_selector.py

Selecciona las memorias que serán incluidas
en el contexto enviado al LLM.
"""


class MemorySelector:

    def __init__(
        self,
        episodic_limit: int = 5,
        semantic_limit: int = 5,
        procedural_limit: int = 5,
    ) -> None:

        self.episodic_limit = episodic_limit
        self.semantic_limit = semantic_limit
        self.procedural_limit = procedural_limit

    def select_episodes(
        self,
        episodes: list,
    ) -> list:

        return episodes[
            : self.episodic_limit
        ]

    def select_facts(
        self,
        facts: list,
    ) -> list:

        return facts[
            : self.semantic_limit
        ]

    def select_procedures(
        self,
        procedures: list,
    ) -> list:

        return procedures[
            : self.procedural_limit
        ]