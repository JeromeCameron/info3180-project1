"""empty message

Revision ID: dc134b529a96
Revises: 8c419c6f2cdf
Create Date: 2019-03-14 03:12:53.347073

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc134b529a96'
down_revision = '8c419c6f2cdf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('biography', sa.VARCHAR(), nullable=True))
    op.drop_column('user_profiles', 'biograph')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('biograph', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('user_profiles', 'biography')
    # ### end Alembic commands ###
