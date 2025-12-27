from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from dotenv import load_dotenv
load_dotenv()
import os
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class Filmes(DeclarativeBase):
    __tablename__ = "filmes"

    titulo: Mapped[str] = mapped_column(primary_key=True)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"Filme(titulo={self.titulo!r}, genero{self.genero!r}, ano={self.ano!r})"

#Insert
#data_insert = Filmes(titulo="Batman", genero="Drama", ano=2022)
#session.add(data_insert)
#session.commit()

#Delete
#session.query(Filmes).filter(Filmes.titulo=="alguma coisa").delete()
#session.commit()

#update
#session.query(Filmes).filter(Filmes.genero== "Drama").update({ "ano": 2000 })
#session.commit()

#Select
#data = session.query(Filmes).all()

session.close()