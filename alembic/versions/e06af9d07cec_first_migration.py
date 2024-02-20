"""first migration

Revision ID: e06af9d07cec
Revises: 0b4017e34eb4
Create Date: 2024-02-13 10:28:19.012618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e06af9d07cec'
down_revision: Union[str, None] = '0b4017e34eb4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
