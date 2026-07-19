"""
memory_access_tracker.py

Actualiza las métricas de acceso de una memoria
y persiste los cambios.
"""

from datetime import datetime


class MemoryAccessTracker:

    def track(
        self,
        memory,
        repository,
    ) -> None:

        memory.access_count += 1

        now = datetime.now().isoformat()

        memory.last_access = now
        memory.updated_at = now

        repository.update(
            memory,
        )