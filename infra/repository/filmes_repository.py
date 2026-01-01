from infra.configs.connection import DBConnctionHandler
from infra.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnctionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        
    def insert(self, titulo, genero, ano, tmdb_id):
        with DBConnctionHandler() as db:
            data_insert = Filmes(titulo=titulo, genero=genero, ano=ano, tmdb_id=tmdb_id)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, titulo):
        with DBConnctionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()
        
    def update(self, titulo, tmdb_id):
        with DBConnctionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"tmdb_id": tmdb_id})
            db.session.commit()