"""
episode_repository.py

Repositorio encargado de almacenar episodios.
"""

from __future__ import annotations

import json
from pathlib import Path

from memory_lab.models.episode import Episode


class EpisodeRepository:

    def __init__(
        self,
        file_path: str = "data/episodes.json",
    ) -> None:

        self._file = Path(file_path)

        self._file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self._file.exists():

            self._file.write_text(
                "[]",
                encoding="utf-8",
            )

    def load_all(
        self,
    ) -> list[Episode]:

        content = self._file.read_text(
            encoding="utf-8",
        )

        if not content.strip():

            return []

        data = json.loads(content)

        return [
            Episode.from_dict(item)
            for item in data
        ]

    def save(
        self,
        episode: Episode,
    ) -> None:

        episodes = self.load_all()

        episodes.append(
            episode,
        )

        self._write(
            episodes,
        )

    def update(
        self,
        episode: Episode,
    ) -> None:

        episodes = self.load_all()

        for index, current in enumerate(
            episodes,
        ):

            if current.id == episode.id:

                episodes[index] = episode

                break

        self._write(
            episodes,
        )

    def clear(
        self,
    ) -> None:

        self._file.write_text(
            "[]",
            encoding="utf-8",
        )

    def _write(
        self,
        episodes: list[Episode],
    ) -> None:

        serialized = [
            episode.to_dict()
            for episode in episodes
        ]

        self._file.write_text(
            json.dumps(
                serialized,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )