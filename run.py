from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

data = repo.insert(titulo="Zootopia 2", genero="Animação", ano=2025)

print(data)
