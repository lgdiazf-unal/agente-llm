"""
agent.py

Orquesta el ciclo principal del agente.
"""

from memory_lab.llm import call_llm
from memory_lab.models.conversation import Conversation
from memory_lab.models.prompt_context import PromptContext
from memory_lab.prompt_builder import PromptBuilder

from memory_lab.repositories.episode_repository import (
    EpisodeRepository,
)
from memory_lab.repositories.semantic_repository import (
    SemanticRepository,
)

from memory_lab.services.episode_extractor import (
    EpisodeExtractor,
)
from memory_lab.services.episode_manager import (
    EpisodeManager,
)
from memory_lab.services.episode_retriever import (
    EpisodeRetriever,
)

from memory_lab.services.semantic_extractor import (
    SemanticExtractor,
)
from memory_lab.services.semantic_manager import (
    SemanticManager,
)
from memory_lab.services.semantic_retriever import (
    SemanticRetriever,
)

from memory_lab.utils.printer import (
    print_text,
    print_title,
)

from memory_lab.views.conversation_view import (
    show_conversation,
)
from memory_lab.views.episodic_memory_view import (
    show_episodes,
)
from memory_lab.views.prompt_builder_view import (
    show_prompt,
)
from memory_lab.views.retrieved_episodes_view import (
    show_retrieved_episodes,
)


class Agent:

    def __init__(self) -> None:

        self.conversation = Conversation()

        self.prompt_builder = PromptBuilder()

        #
        # Episodic memory
        #

        self.episode_repository = EpisodeRepository()

        self.episode_extractor = EpisodeExtractor()

        self.episode_manager = EpisodeManager(
            repository=self.episode_repository,
        )

        self.episode_retriever = EpisodeRetriever(
            repository=self.episode_repository,
        )

        #
        # Semantic memory
        #

        self.semantic_repository = SemanticRepository()

        self.semantic_extractor = SemanticExtractor()

        self.semantic_manager = SemanticManager(
            repository=self.semantic_repository,
        )

        self.semantic_retriever = SemanticRetriever(
            repository=self.semantic_repository,
        )

        self.commands = {
            "/memorize": self.memorize,
            "/episodes": self.show_episodic_memory,
            "/help": self.show_help,
        }

    def run(self) -> None:

        print_title("LLM MEMORY LAB")
        print_text("Phase 0.8 - Semantic Memory")

        while True:

            print()

            user_input = input("Usuario: ").strip()

            if not user_input:

                continue

            if user_input.lower() == "exit":

                print()

                print_text("Hasta luego 👋")

                break

            command = self.commands.get(
                user_input.lower(),
            )

            if command:

                command()

                continue

            self.handle_chat(
                user_input,
            )

    def handle_chat(
        self,
        user_message: str,
    ) -> None:

        self.conversation.add_user_message(
            user_message,
        )

        show_conversation(
            self.conversation,
        )

        episodes = self.episode_retriever.retrieve(
            self.conversation,
        )

        facts = self.semantic_retriever.retrieve(
            self.conversation,
        )

        show_retrieved_episodes(
            episodes,
        )

        context = PromptContext(
            conversation=self.conversation,
            episodes=episodes,
            facts=facts,
        )

        messages = self.prompt_builder.build(
            context,
        )

        show_prompt(
            messages,
        )

        response = call_llm(
            messages,
        )

        self.conversation.add_assistant_message(
            response,
        )

        #
        # Episodic memory
        #

        episode = self.episode_extractor.extract(
            self.conversation,
        )

        self.episode_manager.process(
            episode,
        )

        #
        # Semantic memory
        #

        fact = self.semantic_extractor.extract(
            self.conversation,
        )

        self.semantic_manager.process(
            fact,
        )

        print_title(
            "ASSISTANT",
        )

        print_text(
            response,
        )

    def memorize(self) -> None:

        if not self.conversation.messages:

            print_title(
                "EPISODIC MEMORY",
            )

            print_text(
                "No hay conversación para memorizar.",
            )

            return

        episode = self.episode_extractor.extract(
            self.conversation,
        )

        self.episode_manager.process(
            episode,
        )

        fact = self.semantic_extractor.extract(
            self.conversation,
        )

        self.semantic_manager.process(
            fact,
        )

        print_title(
            "MEMORY",
        )

        print_text(
            "Memoria actualizada correctamente.",
        )

    def show_episodic_memory(self) -> None:

        episodes = self.episode_repository.load_all()

        show_episodes(
            episodes,
        )

    def show_help(self) -> None:

        print_title(
            "COMMANDS",
        )

        print("exit")
        print("/memorize")
        print("/episodes")
        print("/help")