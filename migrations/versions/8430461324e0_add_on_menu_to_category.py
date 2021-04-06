"""add on_menu to Category

Revision ID: 8430461324e0
Revises: 
Create Date: 2021-02-17 20:26:30.443999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8430461324e0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('on_menu', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'on_menu')
    # ### end Alembic commands ###