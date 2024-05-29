"""create exercise table

Revision ID: 77a025e7f8a7
Revises: 7d4d21b4e16e
Create Date: 2024-05-17 19:19:40.821243

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '77a025e7f8a7'
down_revision: Union[str, None] = '7d4d21b4e16e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
