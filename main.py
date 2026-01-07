from fastapi import FastAPI
from infra.repository.filmes_repository import FilmesRepository
from get_movies import get_poster

app = FastAPI()
repo = FilmesRepository()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/movies")
def movies():
    filmes = repo.select()
    #print("filmes: ", filmes)
    resultado = []
    for filme in filmes:
        resultado.append({
            "titulo": filme.titulo,
            "poster_link": get_poster(filme.tmdb_id)
        })
    print(resultado)

    return("Filmes :", filmes)