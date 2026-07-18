from memory_lab.utils.printer import (
    print_json,
    print_title,
)


def show(messages: list[dict]) -> None:

    print_title("PROMPT")

    print_json(messages)