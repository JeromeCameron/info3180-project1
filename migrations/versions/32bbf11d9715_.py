"""empty message

Revision ID: 32bbf11d9715
Revises: dc134b529a96
Create Date: 2019-03-14 22:24:05.386647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32bbf11d9715'
down_revision = 'dc134b529a96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('photo', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'photo')
    # ### end Alembic commands ###
