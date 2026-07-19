"""
session_stats_view.py

Vista para mostrar estadísticas
de ejecución del agente.
"""

from memory_lab.utils.console import (
    Console,
)

from memory_lab.utils.session_stats import (
    SessionStats,
)



def show_session_stats(
    stats: SessionStats,
) -> None:


    lines: list[str] = []


    #
    # Session
    #

    lines.append(
        f"Messages        : {stats.messages}"
    )


    lines.append(
        ""
    )


    #
    # Retrieved Memory
    #

    lines.append(
        "Retrieved Memory:"
    )


    lines.append(
        f"  🧠 Semantic    : {stats.semantic_retrieved}"
    )


    lines.append(
        f"  📖 Episodic    : {stats.episodic_retrieved}"
    )


    lines.append(
        f"  ⚙ Procedural  : {stats.procedural_retrieved}"
    )


    lines.append(
        ""
    )


    #
    # Memory Updates
    #

    lines.append(
        "Memory Updates:"
    )


    lines.append(
        f"  CREATE        : {stats.memory_created}"
    )


    lines.append(
        f"  UPDATE        : {stats.memory_updated}"
    )


    lines.append(
        ""
    )


    #
    # Timing
    #

    lines.append(
        "Execution:"
    )


    lines.append(
        f"  Retrieval     : {stats.retrieval_time:.3f}s"
    )


    lines.append(
        f"  Prompt Build  : {stats.prompt_time:.3f}s"
    )


    lines.append(
        f"  LLM Call      : {stats.llm_time:.3f}s"
    )


    lines.append(
        f"  Extraction    : {stats.extraction_time:.3f}s"
    )


    lines.append(
        ""
    )


    lines.append(
        f"Total Time      : {stats.total_time():.3f}s"
    )


    Console.panel(
        "📊 SESSION STATS",
        "\n".join(lines),
    )