"""
Funciones auxiliares para construir secciones del prompt.
"""


def build_header(title: str) -> str:
    """
    Construye el encabezado estándar de una sección.
    """

    return (
        "==============================\n"
        f"{title}\n"
        "==============================\n\n"
    )