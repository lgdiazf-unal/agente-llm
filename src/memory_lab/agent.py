"""
agent.py

Orquesta el ciclo principal del agente.

v1.2.0
- Terminal Interface
- Pipeline visual
- Context Blocks
- Unified Memory View
- Session Dashboard
- Memory Quality Layer
"""

from memory_lab.llm import call_llm


from memory_lab.models.conversation import (
    Conversation,
)

from memory_lab.models.prompt_context import (
    PromptContext,
)

from memory_lab.models.context_block import (
    ContextBlock,
)


from memory_lab.prompt_builder import (
    PromptBuilder,
)


#
# Repositories
#

from memory_lab.repositories.episode_repository import (
    EpisodeRepository,
)

from memory_lab.repositories.semantic_repository import (
    SemanticRepository,
)

from memory_lab.repositories.procedural_repository import (
    ProceduralRepository,
)


#
# Services
#

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


from memory_lab.services.procedural_extractor import (
    ProceduralExtractor,
)

from memory_lab.services.procedural_manager import (
    ProceduralManager,
)

from memory_lab.services.procedural_retriever import (
    ProceduralRetriever,
)


#
# Memory Quality Layer
#

from memory_lab.services.memory_access_tracker import (
    MemoryAccessTracker,
)

from memory_lab.services.memory_decay_service import (
    MemoryDecayService,
)

from memory_lab.services.memory_ranker import (
    MemoryRanker,
)

from memory_lab.services.memory_selector import (
    MemorySelector,
)

#
# Views
#

from memory_lab.views.conversation_view import (
    show_conversation,
)

from memory_lab.views.episodic_memory_view import (
    show_episodes,
)

from memory_lab.views.prompt_builder_view import (
    show_prompt,
)

from memory_lab.views.retrieved_memory_view import (
    show_retrieved_memory,
)

from memory_lab.views.session_stats_view import (
    show_session_stats,
)


#
# Utils
#

from memory_lab.utils.console import (
    Console,
)

from memory_lab.utils.pipeline import (
    Pipeline,
)

from memory_lab.utils.session_stats import (
    SessionStats,
)


class Agent:


    def __init__(
        self,
    ) -> None:


        self.conversation = Conversation()

        self.prompt_builder = PromptBuilder()

        self.stats = SessionStats()


        #
        # Episodic Memory
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
        # Semantic Memory
        #

        self.semantic_repository = SemanticRepository()

        self.semantic_extractor = SemanticExtractor()

        self.semantic_manager = SemanticManager(
            repository=self.semantic_repository,
        )

        self.semantic_retriever = SemanticRetriever(
            repository=self.semantic_repository,
        )


        #
        # Procedural Memory
        #

        self.procedural_repository = ProceduralRepository()

        self.procedural_extractor = ProceduralExtractor()

        self.procedural_manager = ProceduralManager(
            repository=self.procedural_repository,
        )

        self.procedural_retriever = ProceduralRetriever(
            repository=self.procedural_repository,
        )


        #
        # Memory Quality Layer
        #

        self.memory_access_tracker = (
            MemoryAccessTracker()
        )

        self.memory_decay_service = (
            MemoryDecayService()
        )

        self.memory_ranker = (
            MemoryRanker()
        )

        self.memory_selector = (
            MemorySelector(
                episodic_limit=5,
                semantic_limit=5,
                procedural_limit=5,
            )
        )


        #
        # Commands
        #

        self.commands = {

            "/memorize":
                self.memorize,

            "/episodes":
                self.show_episodic_memory,

            "/stats":
                self.show_stats,

            "/help":
                self.show_help,

        }


    def run(
        self,
    ) -> None:


        Console.title(
            "LLM MEMORY LAB v1.2.0",
        )


        while True:


            print()


            user_input = input(
                "Usuario: ",
            ).strip()


            if not user_input:

                continue


            if user_input.lower() == "exit":

                Console.success(
                    "Hasta luego 👋",
                )

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


        self.stats.reset()


        self.stats.messages = (
            len(
                self.conversation.messages,
            )
            + 1
        )


        self.conversation.add_user_message(
            user_message,
        )


        Pipeline.start(
            "💬 USER INPUT",
        )


        Pipeline.step(
            user_message,
        )


        show_conversation(
            self.conversation,
        )


        #
        # Retrieve Memory
        #

        self.stats.start_timer(
            "retrieval",
        )


        Pipeline.step(
            "Retrieving episodic memory",
        )


        episodes = self.episode_retriever.retrieve(
            self.conversation,
        )


        Pipeline.step(
            "Retrieving semantic memory",
        )


        facts = self.semantic_retriever.retrieve(
            self.conversation,
        )


        Pipeline.step(
            "Retrieving procedural memory",
        )


        procedures = self.procedural_retriever.retrieve(
            self.conversation,
        )


        #
        # Memory Quality Layer
        #

        for episode in episodes:

            self.memory_access_tracker.track(
                episode,
                self.episode_repository,
            )

        for fact in facts:

            self.memory_access_tracker.track(
                fact,
                self.semantic_repository,
            )

        for procedure in procedures:

            self.memory_access_tracker.track(
                procedure,
                self.procedural_repository,
            )


        self.memory_decay_service.apply(
            episodes,
            self.episode_repository,
        )

        self.memory_decay_service.apply(
            facts,
            self.semantic_repository,
        )

        self.memory_decay_service.apply(
            procedures,
            self.procedural_repository,
        )


        episodes = self.memory_ranker.rank(
            episodes,
        )

        facts = self.memory_ranker.rank(
            facts,
        )

        procedures = self.memory_ranker.rank(
            procedures,
        )


        episodes = self.memory_selector.select_episodes(
            episodes,
        )

        facts = self.memory_selector.select_facts(
            facts,
        )

        procedures = self.memory_selector.select_procedures(
            procedures,
        )


        self.stats.episodic_retrieved = len(
            episodes,
        )

        self.stats.semantic_retrieved = len(
            facts,
        )

        self.stats.procedural_retrieved = len(
            procedures,
        )


        self.stats.retrieval_time = (
            self.stats.stop_timer(
                "retrieval",
            )
        )


        show_retrieved_memory(
            episodes=episodes,
            facts=facts,
            procedures=procedures,
        )


        #
        # Context Blocks
        #

        self.stats.start_timer(
            "prompt",
        )


        blocks: list[ContextBlock] = []


        if facts:

            blocks.append(

                ContextBlock(

                    title="🧠 SEMANTIC MEMORY",

                    lines=[
                        fact.content
                        for fact in facts
                    ],

                )

            )


        if episodes:

            blocks.append(

                ContextBlock(

                    title="📖 EPISODIC MEMORY",

                    lines=[
                        episode.summary
                        for episode in episodes
                    ],

                )

            )


        if procedures:

            blocks.append(

                ContextBlock(

                    title="⚙ PROCEDURAL MEMORY",

                    lines=[
                        procedure.content
                        for procedure in procedures
                    ],

                )

            )


        context = PromptContext(

            conversation=self.conversation,

            blocks=blocks,

        )


        Pipeline.step(
            "Building prompt",
        )


        messages = self.prompt_builder.build(
            context,
        )


        self.stats.prompt_time = (
            self.stats.stop_timer(
                "prompt",
            )
        )


        show_prompt(
            messages,
        )


        #
        # LLM
        #

        self.stats.start_timer(
            "llm",
        )


        Pipeline.step(
            "Calling LLM",
        )


        response = call_llm(
            messages,
        )


        self.stats.llm_time = (
            self.stats.stop_timer(
                "llm",
            )
        )


        self.conversation.add_assistant_message(
            response,
        )


        #
        # Memory Extraction
        #

        self.stats.start_timer(
            "extraction",
        )


        Pipeline.step(
            "Extracting episodic memory",
        )


        episode = self.episode_extractor.extract(
            self.conversation,
        )


        self.episode_manager.process(
            episode,
        )


        Pipeline.step(
            "Extracting semantic memory",
        )


        fact = self.semantic_extractor.extract(
            self.conversation,
        )


        self.semantic_manager.process(
            fact,
        )


        Pipeline.step(
            "Extracting procedural memory",
        )


        procedure = self.procedural_extractor.extract(
            self.conversation,
        )


        self.procedural_manager.process(
            procedure,
        )


        self.stats.extraction_time = (
            self.stats.stop_timer(
                "extraction",
            )
        )


        Pipeline.finish(
            "Processing completed",
        )


        Console.title(
            "🤖 ASSISTANT",
        )


        Console.text(
            response,
        )


        show_session_stats(
            self.stats,
        )


    def memorize(
        self,
    ) -> None:


        if not self.conversation.messages:

            Console.warning(
                "No hay conversación para memorizar.",
            )

            return


        Pipeline.start(
            "Manual Memory Update",
        )


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


        procedure = self.procedural_extractor.extract(
            self.conversation,
        )

        self.procedural_manager.process(
            procedure,
        )


        Console.success(
            "Memoria actualizada correctamente.",
        )


    def show_episodic_memory(
        self,
    ) -> None:


        episodes = self.episode_repository.load_all()


        show_episodes(
            episodes,
        )


    def show_stats(
        self,
    ) -> None:


        show_session_stats(
            self.stats,
        )


    def show_help(
        self,
    ) -> None:


        Console.title(
            "COMMANDS",
        )


        Console.text(
            "exit",
        )

        Console.text(
            "/memorize",
        )

        Console.text(
            "/episodes",
        )

        Console.text(
            "/stats",
        )

        Console.text(
            "/help",
        )