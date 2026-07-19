"""
procedural_repository.py

Repositorio encargado de almacenar
memoria procedimental.
"""

from __future__ import annotations

import json
from pathlib import Path

from memory_lab.models.procedure import Procedure


class ProceduralRepository:

    def __init__(
        self,
        file_path: str = "data/procedures.json",
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
    ) -> list[Procedure]:

        content = self._file.read_text(
            encoding="utf-8",
        )

        if not content.strip():

            return []

        data = json.loads(content)

        return [
            Procedure.from_dict(item)
            for item in data
        ]

    def save(
        self,
        procedure: Procedure,
    ) -> None:

        procedures = self.load_all()

        procedures.append(
            procedure,
        )

        self._write(
            procedures,
        )

    def update(
        self,
        procedure: Procedure,
    ) -> None:

        procedures = self.load_all()

        for index, current in enumerate(
            procedures,
        ):

            if current.id == procedure.id:

                procedures[index] = procedure

                break

        self._write(
            procedures,
        )

    def get_by_id(
        self,
        procedure_id: str,
    ) -> Procedure | None:

        procedures = self.load_all()

        for procedure in procedures:

            if procedure.id == procedure_id:

                return procedure

        return None

    def clear(
        self,
    ) -> None:

        self._file.write_text(
            "[]",
            encoding="utf-8",
        )

    def _write(
        self,
        procedures: list[Procedure],
    ) -> None:

        serialized = [
            procedure.to_dict()
            for procedure in procedures
        ]

        self._file.write_text(
            json.dumps(
                serialized,
                indent=4,
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )