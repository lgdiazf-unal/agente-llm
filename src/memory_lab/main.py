"""
main.py

Punto de entrada de la aplicación.
"""

from memory_lab.llm import call_llm
from memory_lab.models.conversation import Conversation
from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompt_builder import PromptBuilder
from memory_lab.utils.printer import (
    print_text,
    print_title,
)
from memory_lab.views.conversation_view import show as show_conversation
from memory_lab.views.prompt_builder_view import show as  show_prompt


def main() -> None:

    print_title("LLM MEMORY LAB")
    print_text("Fase 2 - Working Memory")

    conversation = Conversation()

    builder = PromptBuilder()

    while True:

        print()

        user_message = input("Usuario: ")

        if user_message.lower() in {"exit", "quit"}:
            print("\nHasta luego 👋")
            break

        #
        # Actualizar memoria de trabajo
        #
        conversation.add_user_message(user_message)

        #
        # Mostrar memoria actual
        #
        show_conversation(conversation)

        #
        # Construir contexto
        #
        context = PromptContext(
            conversation=conversation,
        )

        #
        # Construir prompt
        #
        messages = builder.build(context)

        #
        # Mostrar prompt final
        #
        show_prompt(messages)

        #
        # Llamar al modelo
        #
        response = call_llm(messages)

        #
        # Actualizar memoria con la respuesta
        #
        conversation.add_assistant_message(response)

        #
        # Mostrar memoria actualizada
        #
        show_conversation(conversation)

        #
        # Mostrar respuesta
        #
        print_title("ASSISTANT")
        print_text(response)


if __name__ == "__main__":
    main()