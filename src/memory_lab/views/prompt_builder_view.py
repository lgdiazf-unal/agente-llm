"""
Vista para mostrar el prompt generado.
"""

from memory_lab.utils.console import (
    Console,
)


def show_prompt(
    messages: list[dict],
) -> None:

    Console.section(
        "📝 PROMPT",
    )


    for message in messages:

        Console.text(
            message["role"].upper()
        )

        Console.text(
            message["content"]
        )

        Console.blank()