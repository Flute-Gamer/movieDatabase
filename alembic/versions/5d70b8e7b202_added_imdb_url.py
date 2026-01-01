"""added imdb url

Revision ID: 5d70b8e7b202
Revises: 31086498a9a9
Create Date: 2026-01-01 17:39:40.117357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d70b8e7b202'
down_revision: Union[str, Sequence[str], None] = '31086498a9a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "filmes",
        sa.Column("imdb_url", sa.String(), nullable=True)
    )

    op.add_column(
        "filmes",
        sa.Column("imdb_image_url", sa.String(), nullable=True)
    )


def downgrade() -> None:
        op.drop_column("filmes", "imdb_url")
        op.drop_column("filmes", "imdb_image_url")
