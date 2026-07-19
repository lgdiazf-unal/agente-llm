"""
console.py

Sistema centralizado de salida por terminal.

Responsable de:
- títulos
- secciones
- paneles
- colores
- estados
- JSON
"""

from __future__ import annotations

import json


class Console:

    WIDTH = 70


    class Color:

        RESET = "\033[0m"

        CYAN = "\033[96m"

        GREEN = "\033[92m"

        YELLOW = "\033[93m"

        RED = "\033[91m"

        BLUE = "\033[94m"

        MAGENTA = "\033[95m"



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
            Console.Color.CYAN
            +
            text.center(
                Console.WIDTH,
            )
            +
            Console.Color.RESET
        )

        Console.separator()



    @staticmethod
    def section(
        text: str,
    ) -> None:

        print()

        print(
            Console.Color.BLUE
            +
            f"▶ {text}"
            +
            Console.Color.RESET
        )

        Console.separator()



    @staticmethod
    def panel(
        title: str,
        content: str,
    ) -> None:

        Console.separator()

        print(
            Console.Color.MAGENTA
            +
            title
            +
            Console.Color.RESET
        )

        Console.separator()

        print(
            content
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
            Console.Color.GREEN
            +
            f"✓ {text}"
            +
            Console.Color.RESET
        )



    @staticmethod
    def warning(
        text: str,
    ) -> None:

        print(
            Console.Color.YELLOW
            +
            f"⚠ {text}"
            +
            Console.Color.RESET
        )



    @staticmethod
    def error(
        text: str,
    ) -> None:

        print(
            Console.Color.RED
            +
            f"✗ {text}"
            +
            Console.Color.RESET
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