"""
memory_ranker.py

Calcula el score de cada memoria y las
ordena por relevancia.
"""

from datetime import datetime


class MemoryRanker:

    def rank(
        self,
        memories: list,
    ) -> list:

        now = datetime.now()

        for memory in memories:

            memory.score = self.compute_score(
                memory,
                now,
            )

        return sorted(
            memories,
            key=lambda memory: memory.score,
            reverse=True,
        )

    def compute_score(
        self,
        memory,
        now: datetime,
    ) -> float:

        score = 1.0

        #
        # Frecuencia
        #

        score += (
            memory.access_count * 0.5
        )

        #
        # Recencia
        #

        if memory.last_access:

            last = datetime.fromisoformat(
                memory.last_access,
            )

            days = (
                now - last
            ).days

            score += max(
                0,
                30 - days,
            ) / 30

        return round(
            score,
            3,
        )