"""
Utilidades para representar procedimientos como texto.
"""

from memory_lab.models.procedure import Procedure


def format_procedures(
    procedures: list[Procedure],
) -> str:

    if not procedures:

        return "No procedures."

    lines: list[str] = []

    for procedure in procedures:

        lines.append(
            f"ID: {procedure.id}"
        )

        lines.append(
            f"CONTENT: {procedure.content}"
        )

        lines.append("")

    return "\n".join(lines)