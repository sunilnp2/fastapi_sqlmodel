"""second migration

Revision ID: 83fc4de2b9eb
Revises: c50b2f1106db
Create Date: 2024-02-14 16:29:30.185393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '83fc4de2b9eb'
down_revision: Union[str, None] = 'c50b2f1106db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
