"""
semantic_repository.py

Repositorio encargado de almacenar memoria semántica.
"""

from __future__ import annotations

import json
from pathlib import Path

from memory_lab.models.fact import Fact


class SemanticRepository:

    def __init__(
        self,
        file_path: str = "data/facts.json",
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
    ) -> list[Fact]:

        content = self._file.read_text(
            encoding="utf-8",
        )

        if not content.strip():

            return []

        data = json.loads(
            content,
        )

        return [
            Fact.from_dict(item)
            for item in data
        ]

    def save(
        self,
        fact: Fact,
    ) -> None:

        facts = self.load_all()

        facts.append(
            fact,
        )

        self._write(
            facts,
        )

    def update(
        self,
        fact: Fact,
    ) -> None:

        facts = self.load_all()

        for index, current in enumerate(
            facts,
        ):

            if current.id == fact.id:

                facts[index] = fact

                break

        self._write(
            facts,
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
        facts: list[Fact],
    ) -> None:

        serialized = [
            fact.to_dict()
            for fact in facts
        ]

        self._file.write_text(
            json.dumps(
                serialized,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )