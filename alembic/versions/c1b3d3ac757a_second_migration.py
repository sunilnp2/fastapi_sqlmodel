"""second migration

Revision ID: c1b3d3ac757a
Revises: e06af9d07cec
Create Date: 2024-02-14 15:54:43.106191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c1b3d3ac757a'
down_revision: Union[str, None] = 'e06af9d07cec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
