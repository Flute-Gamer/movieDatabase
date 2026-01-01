"""2

Revision ID: 31086498a9a9
Revises: 1dde45cf69f1
Create Date: 2026-01-01 17:12:48.290259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from infra.repository.filmes_repository import FilmesRepository



# revision identifiers, used by Alembic.
revision: str = '31086498a9a9'
down_revision: Union[str, Sequence[str], None] = '1dde45cf69f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    filmes_repository = FilmesRepository()
    filmes_repository.insert("De Volta Para o Futuro", "Ficção Científica", 1985)

def downgrade() -> None:
    """Downgrade schema."""
    pass
