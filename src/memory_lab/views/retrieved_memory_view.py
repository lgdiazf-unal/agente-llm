"""
Vista para mostrar todas las memorias recuperadas.
"""

from memory_lab.models.episode import (
    Episode,
)

from memory_lab.models.fact import (
    Fact,
)

from memory_lab.models.procedure import (
    Procedure,
)

from memory_lab.utils.console import (
    Console,
)


def show_retrieved_memory(
    episodes: list[Episode],
    facts: list[Fact],
    procedures: list[Procedure],
) -> None:


    #
    # Episodic Memory
    #

    if episodes:

        content = "\n".join(
            [
                f"- {episode.summary}"
                for episode in episodes
            ]
        )

        Console.panel(
            "📖 EPISODIC MEMORY",
            content,
        )


    #
    # Semantic Memory
    #

    if facts:

        content = "\n".join(
            [
                f"- {fact.content}"
                for fact in facts
            ]
        )

        Console.panel(
            "🧠 SEMANTIC MEMORY",
            content,
        )


    #
    # Procedural Memory
    #

    if procedures:

        content = "\n".join(
            [
                f"- {procedure.content}"
                for procedure in procedures
            ]
        )

        Console.panel(
            "⚙ PROCEDURAL MEMORY",
            content,
        )


    if not episodes and not facts and not procedures:

        Console.warning(
            "No memory retrieved."
        )