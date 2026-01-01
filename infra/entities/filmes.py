from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from infra.configs.base import Base

class Filmes(Base):
    __tablename__ = "filmes"

    titulo: Mapped[str] = mapped_column(primary_key=True)
    genero: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    imdb_url: Mapped[str] = mapped_column(nullable=True)
    imdb_image_url: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f"Filme(titulo={self.titulo!r}, genero{self.genero!r}, ano={self.ano!r}, imdb_url={self.imdb_url!r}, imdb_image_url={self.imdb_image_url!r})"