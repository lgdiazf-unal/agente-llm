"""
pipeline.py

Visualización del flujo interno del agente.
"""

from memory_lab.utils.console import (
    Console,
)


class Pipeline:


    @staticmethod
    def step(
        message: str,
    ) -> None:

        Console.success(
            message,
        )


    @staticmethod
    def start(
        message: str,
    ) -> None:

        Console.section(
            message,
        )


    @staticmethod
    def finish(
        message: str,
    ) -> None:

        Console.success(
            message,
        )