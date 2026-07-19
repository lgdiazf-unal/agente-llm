"""
session_stats.py

Recolector de métricas de ejecución del agente.

Responsable de almacenar:
- tiempos de ejecución
- cantidad de memorias recuperadas
- operaciones realizadas
- estadísticas de sesión
"""

from __future__ import annotations

import time

from dataclasses import dataclass, field


@dataclass
class SessionStats:


    start_time: float = field(
        default_factory=time.time,
    )


    retrieval_time: float = 0.0


    prompt_time: float = 0.0


    llm_time: float = 0.0


    extraction_time: float = 0.0



    messages: int = 0



    semantic_retrieved: int = 0


    episodic_retrieved: int = 0


    procedural_retrieved: int = 0



    memory_created: int = 0


    memory_updated: int = 0



    _timers: dict[str, float] = field(
        default_factory=dict,
        repr=False,
    )



    def start_timer(
        self,
        name: str,
    ) -> None:

        self._timers[name] = time.time()



    def stop_timer(
        self,
        name: str,
    ) -> float:

        if name not in self._timers:

            return 0.0


        elapsed = (
            time.time()
            -
            self._timers[name]
        )


        return elapsed



    def total_time(
        self,
    ) -> float:

        return (
            time.time()
            -
            self.start_time
        )



    def reset(
        self,
    ) -> None:

        self.start_time = time.time()

        self.retrieval_time = 0.0

        self.prompt_time = 0.0

        self.llm_time = 0.0

        self.extraction_time = 0.0

        self.messages = 0

        self.semantic_retrieved = 0

        self.episodic_retrieved = 0

        self.procedural_retrieved = 0

        self.memory_created = 0

        self.memory_updated = 0

        self._timers.clear()