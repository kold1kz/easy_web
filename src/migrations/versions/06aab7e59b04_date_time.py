"""date + time

Revision ID: 06aab7e59b04
Revises: 93d5a6600671
Create Date: 2023-11-01 10:08:54.798394

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '06aab7e59b04'
down_revision: Union[str, None] = '93d5a6600671'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('Victorina',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=True),
    sa.Column('answer', sa.String(), nullable=True),
    sa.Column('date', sa.Datetime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # 


def downgrade() -> None:
    op.drop_table('Victorina')
