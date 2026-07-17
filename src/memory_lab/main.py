"""
main.py

Punto de entrada de la aplicación.
"""

from memory_lab.llm import call_llm
from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompt_builder import PromptBuilder
from memory_lab.utils.printer import print_text, print_title


def main() -> None:

    print_title("LLM MEMORY LAB")
    print_text("Fase 1 - Prompt Builder")

    user_message = input("\nUsuario: ")

    context = PromptContext(
        user_message=user_message,
    )

    builder = PromptBuilder()

    messages = builder.build(context)

    response = call_llm(messages)

    print_title("RESPUESTA FINAL")

    print_text(response)


if __name__ == "__main__":
    main()