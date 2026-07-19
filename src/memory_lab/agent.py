"""
agent.py

Orquesta el ciclo principal del agente.

v1.1.0
- Terminal Interface
- Pipeline visual
- Context Blocks
- Unified Memory View
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



#
# Utils
#

from memory_lab.utils.console import (
    Console,
)

from memory_lab.utils.pipeline import (
    Pipeline,
)



class Agent:


    def __init__(self) -> None:


        self.conversation = Conversation()


        self.prompt_builder = PromptBuilder()



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
        # Commands
        #

        self.commands = {

            "/memorize":
                self.memorize,

            "/episodes":
                self.show_episodic_memory,

            "/help":
                self.show_help,

        }



    def run(self) -> None:


        Console.title(
            "LLM MEMORY LAB v1.1.0",
        )


        while True:


            print()


            user_input = input(
                "Usuario: "
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



        show_retrieved_memory(
            episodes=episodes,
            facts=facts,
            procedures=procedures,
        )



        #
        # Build Context Blocks
        #

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



        #
        # Prompt
        #

        Pipeline.step(
            "Building prompt",
        )


        messages = self.prompt_builder.build(
            context,
        )


        show_prompt(
            messages,
        )



        #
        # LLM
        #

        Pipeline.step(
            "Calling LLM",
        )


        response = call_llm(
            messages,
        )


        self.conversation.add_assistant_message(
            response,
        )



        #
        # Memory Extraction
        #

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



        Pipeline.finish(
            "Processing completed",
        )



        Console.title(
            "🤖 ASSISTANT",
        )


        Console.text(
            response,
        )



    def memorize(self) -> None:



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



    def show_episodic_memory(self) -> None:


        episodes = self.episode_repository.load_all()


        show_episodes(
            episodes,
        )



    def show_help(self) -> None:


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
            "/help",
        )