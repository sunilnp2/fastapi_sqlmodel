"""second migration

Revision ID: 61d7d27b8b6b
Revises: c1b3d3ac757a
Create Date: 2024-02-14 15:56:10.094154

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '61d7d27b8b6b'
down_revision: Union[str, None] = 'c1b3d3ac757a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
