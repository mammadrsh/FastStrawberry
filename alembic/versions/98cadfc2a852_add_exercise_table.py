"""Add exercise table

Revision ID: 98cadfc2a852
Revises: 77a025e7f8a7
Create Date: 2024-05-19 16:17:21.081700

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '98cadfc2a852'
down_revision: Union[str, None] = '77a025e7f8a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
