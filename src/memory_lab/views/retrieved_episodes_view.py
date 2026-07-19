"""
Vista para mostrar episodios recuperados.
"""

from memory_lab.models.episode import (
    Episode,
)

from memory_lab.utils.console import (
    Console,
)


def show_retrieved_episodes(
    episodes: list[Episode],
) -> None:

    Console.section(
        "🔎 RETRIEVED EPISODES",
    )

    if not episodes:

        Console.text(
            "Sin episodios relevantes.",
        )

        return


    for episode in episodes:

        Console.text(
            f"- {episode.summary}"
        )