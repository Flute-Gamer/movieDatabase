"""added tmdb url

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
        sa.Column("tmdb_id", sa.String(), nullable=True)
    )



def downgrade() -> None:
        op.drop_column("filmes", "tmdb_id")
