from memory_lab.models.episode import Episode
from memory_lab.repositories.episode_repository import EpisodeRepository

repo = EpisodeRepository()

episode = Episode.create(
    "El usuario se llama Luis."
)

repo.save(episode)

for item in repo.load_all():
    print(item)