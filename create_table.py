from infra.configs.connection import DBConnctionHandler
from infra.configs.base import Base

from infra.entities.filmes import Filmes

def create_tables():
    with DBConnctionHandler() as db:
        Base.metadata.create_all(db.get_engine())
    print("Tabelas criadas com sucesso")

if __name__ == "__main__":
    create_tables()