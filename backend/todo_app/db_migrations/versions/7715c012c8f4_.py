"""empty message

Revision ID: 7715c012c8f4
Revises: 8b559799339b
Create Date: 2022-10-13 23:47:41.962246

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7715c012c8f4"
down_revision = "8b559799339b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("todos", sa.Column("duration", sa.SmallInteger(), nullable=True))
    op.drop_column("todos", "order_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("todos", sa.Column("order_id", sa.INTEGER(), nullable=False))
    op.drop_column("todos", "duration")
    # ### end Alembic commands ###
