"""adds moon model

Revision ID: 726605a7e242
Revises: 047ba3167dcc
Create Date: 2022-05-10 14:02:40.680401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '726605a7e242'
down_revision = '047ba3167dcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moon',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('size', sa.Float(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('gravity', sa.Float(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moon')
    # ### end Alembic commands ###
