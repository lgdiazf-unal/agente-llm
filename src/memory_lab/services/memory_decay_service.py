"""
memory_decay_service.py

Reduce progresivamente el score de memorias
que llevan tiempo sin utilizarse.
"""

from datetime import datetime


class MemoryDecayService:

    def apply(
        self,
        memories: list,
        repository,
    ) -> None:

        now = datetime.now()

        for memory in memories:

            if memory.last_access is None:

                continue

            last_access = datetime.fromisoformat(
                memory.last_access,
            )

            days = (
                now - last_access
            ).days

            if days <= 30:

                continue

            decay = (
                days - 30
            ) * 0.02

            new_score = max(
                1.0,
                memory.score - decay,
            )

            if new_score == memory.score:

                continue

            memory.score = round(
                new_score,
                3,
            )

            memory.updated_at = (
                now.isoformat()
            )

            repository.update(
                memory,
            )