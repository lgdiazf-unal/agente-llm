"""
Vista para mostrar memoria episódica.
"""

from memory_lab.models.episode import (
    Episode,
)

from memory_lab.utils.console import (
    Console,
)


def show_episodes(
    episodes: list[Episode],
) -> None:

    Console.section(
        "📖 EPISODIC MEMORY",
    )

    if not episodes:

        Console.warning(
            "No existen episodios almacenados.",
        )

        return


    for episode in episodes:

        Console.text(
            f"- {episode.summary}"
        )