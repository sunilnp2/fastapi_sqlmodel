"""second migration

Revision ID: c50b2f1106db
Revises: 61d7d27b8b6b
Create Date: 2024-02-14 16:12:26.392899

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c50b2f1106db'
down_revision: Union[str, None] = '61d7d27b8b6b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
