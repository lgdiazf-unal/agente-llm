"""
Servicio encargado de decidir si un episodio
debe crearse o actualizar uno existente.
"""

import json

from memory_lab.llm import call_llm
from memory_lab.models.episode import Episode
from memory_lab.prompts.episode_matcher_prompt import (
    SYSTEM_PROMPT,
)
from memory_lab.repositories.episode_repository import (
    EpisodeRepository,
)
from memory_lab.utils.json_parser import (
    parse_llm_json,
)


class EpisodeMatcher:

    def __init__(
        self,
        repository: EpisodeRepository,
    ) -> None:

        self.repository = repository

    def match(
        self,
        episode: Episode,
    ) -> Episode | None:

        episodes = self.repository.load_all()

        if not episodes:

            return None

        existing = json.dumps(
            [
                item.to_dict()
                for item in episodes
            ],
            indent=4,
            ensure_ascii=False,
        )

        candidate = json.dumps(
            episode.to_dict(),
            indent=4,
            ensure_ascii=False,
        )

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content":
                    f"Episodios existentes:\n\n"
                    f"{existing}\n\n"
                    f"Episodio candidato:\n\n"
                    f"{candidate}",
            },
        ]

        response = call_llm(
            messages,
        )

        decision = parse_llm_json(
            response,
        )

        if decision["action"] == "create":

            return None

        episode_id = decision["episode_id"]

        for existing_episode in episodes:

            if existing_episode.id == episode_id:

                return existing_episode

        return None