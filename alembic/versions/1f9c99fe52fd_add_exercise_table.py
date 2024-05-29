"""Add exercise table

Revision ID: 1f9c99fe52fd
Revises: 98cadfc2a852
Create Date: 2024-05-19 16:21:53.258817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '1f9c99fe52fd'
down_revision: Union[str, None] = '98cadfc2a852'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
