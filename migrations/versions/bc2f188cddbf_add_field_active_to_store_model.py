"""add field active to Store model

Revision ID: bc2f188cddbf
Revises: 8430461324e0
Create Date: 2021-02-17 20:40:55.340977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc2f188cddbf'
down_revision = '8430461324e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'active')
    # ### end Alembic commands ###
