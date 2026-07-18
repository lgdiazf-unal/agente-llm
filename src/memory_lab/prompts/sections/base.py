"""
Clase base para todas las secciones del prompt.
"""

from abc import ABC
from abc import abstractmethod

from memory_lab.models.prompt_context import PromptContext


class PromptSection(ABC):
    """
    Contrato para cualquier sección del prompt.
    """

    @abstractmethod
    def build(
        self,
        context: PromptContext,
    ) -> str:
        """
        Construye una sección del prompt.

        Retorna una cadena vacía si la sección
        no tiene contenido.
        """
        raise NotImplementedError