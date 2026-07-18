"""
main.py
"""

from memory_lab.llm import call_llm
from memory_lab.models.conversation import Conversation
from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompt_builder import PromptBuilder
from memory_lab.services.episode_extractor import EpisodeExtractor
from memory_lab.utils.printer import print_text, print_title
from memory_lab.views.conversation_view import show_conversation
from memory_lab.views.prompt_builder_view import show_prompt


def main() -> None:

    print_title("LLM MEMORY LAB")
    print_text("Fase 3 - Episodic Memory")

    conversation = Conversation()

    builder = PromptBuilder()

    extractor = EpisodeExtractor()

    while True:

        print()

        user_message = input("Usuario: ")

        if user_message.lower() == "exit":
            break

        if user_message.lower() == "/memorize":

            if not conversation.messages:

                print_title("EPISODE")

                print_text("No hay conversación.")

                continue

            episode = extractor.extract(conversation)

            print_title("EPISODE")

            print_text(episode.summary)

            continue

        conversation.add_user_message(user_message)

        show_conversation(conversation)

        context = PromptContext(
            conversation=conversation,
        )

        messages = builder.build(context)

        show_prompt(messages)

        response = call_llm(messages)

        conversation.add_assistant_message(response)

        print_title("ASSISTANT")

        print_text(response)


if __name__ == "__main__":
    main()