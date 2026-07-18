"""
Vista que muestra los episodios recuperados
antes de construir el prompt.
"""

from memory_lab.models.episode import Episode
from memory_lab.utils.printer import print_text, print_title


def show_retrieved_episodes(
    episodes: list[Episode],
) -> None:

    print_title("RETRIEVED EPISODES")

    if not episodes:

        print_text("No episodes retrieved.")

        return

    for index, episode in enumerate(episodes, start=1):

        print(f"[{index}]")

        print(episode.summary)

        print()