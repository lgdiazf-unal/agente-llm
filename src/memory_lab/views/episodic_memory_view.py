from memory_lab.models.episode import Episode
from memory_lab.utils.printer import print_text, print_title


def show_episodes(
    episodes: list[Episode],
) -> None:

    print_title("EPISODIC MEMORY")

    if not episodes:

        print_text("No hay episodios almacenados.")
        return

    for index, episode in enumerate(episodes, start=1):

        print(f"[{index}]")
        print()

        print(f"ID: {episode.id}")
        print()

        print("Summary:")
        print(episode.summary)

        print()
        print("-" * 60)
        print()