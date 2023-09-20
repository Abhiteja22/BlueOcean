"""empty message

Revision ID: cff05313741d
Revises: f01bdda75e70
Create Date: 2021-10-19 16:24:55.339088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cff05313741d'
down_revision = 'f01bdda75e70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('town_input', sa.Column('budget', sa.Integer(), nullable=True))
    op.drop_column('town_input', 'OUTPUT')
    op.drop_column('town_input', 'town')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('town_input', sa.Column('town', sa.VARCHAR(length=64), nullable=True))
    op.add_column('town_input', sa.Column('OUTPUT', sa.INTEGER(), nullable=True))
    op.drop_column('town_input', 'budget')
    # ### end Alembic commands ###