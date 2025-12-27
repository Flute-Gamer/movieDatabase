from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

data = repo.insert(titulo="Batman", genero="Drama", ano=2022)

print(data)
