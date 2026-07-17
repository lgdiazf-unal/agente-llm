"""
prompt_context.py

Contiene el estado necesario para construir el prompt que será enviado
al modelo.

En esta primera versión, únicamente contiene el mensaje del usuario.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PromptContext:
    """
    Contexto utilizado por PromptBuilder para construir el prompt.
    """

    user_message: str