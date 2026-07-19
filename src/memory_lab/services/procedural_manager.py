"""
Servicio encargado de administrar
la memoria procedimental.
"""

from memory_lab.models.procedure import Procedure

from memory_lab.repositories.procedural_repository import (
    ProceduralRepository,
)

from memory_lab.services.procedural_matcher import (
    ProceduralMatcher,
)


class ProceduralManager:

    def __init__(
        self,
        repository: ProceduralRepository,
    ) -> None:

        self.repository = repository

        self.matcher = ProceduralMatcher()

    def process(
        self,
        procedure: Procedure | None,
    ) -> None:

        if procedure is None:

            return

        procedures = self.repository.load_all()

        decision = self.matcher.match(
            procedures,
            procedure,
        )

        action = decision["action"]

        if action == "create":

            self.repository.save(
                procedure,
            )

            return

        procedure_id = decision["procedure_id"]

        current = self.repository.get_by_id(
            procedure_id,
        )

        if current is None:

            self.repository.save(
                procedure,
            )

            return

        updated = Procedure(
            id=current.id,
            content=procedure.content,
        )

        self.repository.update(
            updated,
        )