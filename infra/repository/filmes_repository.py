from infra.configs.connection import DBConnctionHandler
from infra.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnctionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        
    def insert(self, titulo, genero, ano):
        with DBConnctionHandler() as db:
            data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, titulo):
        with DBConnctionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()
        
    def update(self, titulo, ano):
        with DBConnctionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"ano": ano})
            db.session.commit()