"""
printer.py

Compatibilidad temporal.

Redirige las llamadas antiguas
hacia Console.
"""

from memory_lab.utils.console import (
    Console,
)


def print_title(
    text: str,
) -> None:

    Console.title(
        text,
    )


def print_text(
    text: str,
) -> None:

    Console.text(
        text,
    )


def print_step(
    text: str,
) -> None:

    Console.section(
        text,
    )


def print_json(
    data: dict | list,
) -> None:

    Console.json(
        data,
    )