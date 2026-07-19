"""
console.py

Sistema centralizado de salida por terminal.

Responsable de:
- títulos
- secciones
- texto
- JSON
- estados
- separadores
"""


from __future__ import annotations

import json


class Console:

    WIDTH = 60


    @staticmethod
    def separator() -> None:

        print(
            "─" * Console.WIDTH
        )


    @staticmethod
    def title(
        text: str,
    ) -> None:

        Console.separator()

        print(
            text.center(
                Console.WIDTH,
            )
        )

        Console.separator()


    @staticmethod
    def section(
        text: str,
    ) -> None:

        print()

        print(
            f"▶ {text}"
        )

        Console.separator()


    @staticmethod
    def text(
        text: str,
    ) -> None:

        print(
            text
        )


    @staticmethod
    def success(
        text: str,
    ) -> None:

        print(
            f"✓ {text}"
        )


    @staticmethod
    def warning(
        text: str,
    ) -> None:

        print(
            f"⚠ {text}"
        )


    @staticmethod
    def error(
        text: str,
    ) -> None:

        print(
            f"✗ {text}"
        )


    @staticmethod
    def json(
        data: dict | list,
    ) -> None:

        print(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
            )
        )


    @staticmethod
    def blank() -> None:

        print()