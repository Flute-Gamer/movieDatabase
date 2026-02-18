from fastapi import FastAPI
from infra.repository.filmes_repository import FilmesRepository
from get_movies import get_poster
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
repo = FilmesRepository()

origins = [
    "https://movie-front-sand.vercel.app/",
    "https://movie-front-5p4wrrmfv-igors-projects-01c1ee87.vercel.app",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
            **filme.__dict__,
            "poster_link": f"https://image.tmdb.org/t/p/w500{get_poster(filme.tmdb_id)}"
        })
    print(resultado)

    return("Filmes :", resultado)