"""
main.py

Punto de entrada de la aplicación.
"""

from memory_lab.llm import call_llm
from memory_lab.models.conversation import Conversation
from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompt_builder import PromptBuilder
from memory_lab.repositories.episode_repository import EpisodeRepository
from memory_lab.services.episode_extractor import EpisodeExtractor
from memory_lab.utils.printer import print_text, print_title
from memory_lab.views.conversation_view import show_conversation
from memory_lab.views.episodic_memory_view import show_episodes
from memory_lab.views.prompt_builder_view import show_prompt


def main() -> None:

    print_title("LLM MEMORY LAB")
    print_text("Phase 0.5 - Episodic Memory")

    conversation = Conversation()

    prompt_builder = PromptBuilder()

    extractor = EpisodeExtractor()

    repository = EpisodeRepository()

    while True:

        print()

        user_message = input("Usuario: ").strip()

        if not user_message:
            continue

        #
        # Salir
        #
        if user_message.lower() == "exit":
            break

        #
        # Extraer y almacenar un episodio
        #
        if user_message.lower() == "/memorize":

            if not conversation.messages:

                print_title("EPISODIC MEMORY")
                print_text("No hay conversación para memorizar.")
                continue

            episode = extractor.extract(conversation)

            repository.save(episode)

            print_title("EPISODIC MEMORY")
            print_text("Episodio almacenado correctamente.")

            continue

        #
        # Mostrar episodios almacenados
        #
        if user_message.lower() == "/episodes":

            episodes = repository.load_all()

            show_episodes(episodes)

            continue

        #
        # Conversación normal
        #
        conversation.add_user_message(user_message)

        print()

        show_conversation(conversation)

        context = PromptContext(
            conversation=conversation,
        )

        messages = prompt_builder.build(context)

        show_prompt(messages)

        response = call_llm(messages)

        conversation.add_assistant_message(response)

        print_title("ASSISTANT")

        print_text(response)


if __name__ == "__main__":
    main()