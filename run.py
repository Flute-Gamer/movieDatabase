from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

#data = repo.insert(titulo="Zootopia 2", genero="Animação", ano=2025)

##filme_atualizar = "Batman"

##data = repo.update(titulo=filme_atualizar, tmdb_id="414906")


data = repo.select()

print(data)
