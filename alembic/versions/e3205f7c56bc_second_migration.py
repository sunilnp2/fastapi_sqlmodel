"""second migration

Revision ID: e3205f7c56bc
Revises: 83fc4de2b9eb
Create Date: 2024-02-14 16:37:40.429979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e3205f7c56bc'
down_revision: Union[str, None] = '83fc4de2b9eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
