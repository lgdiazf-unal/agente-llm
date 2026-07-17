"""
printer.py

Funciones auxiliares para mostrar información de forma consistente
durante la ejecución del proyecto.

Este módulo NO conoce nada sobre:
- OpenRouter
- Memorias
- Prompt Builder
- Agentes

Su única responsabilidad es imprimir información.
"""

from __future__ import annotations

import json
from pprint import pprint

LINE_WIDTH = 70


def print_title(title: str) -> None:
    """
    Imprime un título de sección.
    """

    print()
    print("=" * LINE_WIDTH)
    print(title)
    print("=" * LINE_WIDTH)


def print_step(step: str) -> None:
    """
    Imprime el paso actual del flujo.
    """

    print(f"\n➡ {step}")


def print_text(text: str) -> None:
    """
    Imprime texto plano.
    """

    print(text)


def print_json(data: object) -> None:
    """
    Imprime un objeto Python como JSON formateado.
    """

    print(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )
    )


def print_object(data: object) -> None:
    """
    Imprime cualquier objeto usando pprint.
    Útil para inspeccionar objetos del SDK.
    """

    pprint(data)


def print_separator(char: str = "-") -> None:
    """
    Imprime una línea separadora.
    """

    print(char * LINE_WIDTH)


def print_key_value(key: str, value: object) -> None:
    """
    Imprime pares clave/valor alineados.

    Ejemplo:
        Modelo               : deepseek-r1
        Prompt Tokens        : 145
    """

    print(f"{key:<25}: {value}")


def print_empty_line() -> None:
    """
    Imprime una línea en blanco.
    """

    print()