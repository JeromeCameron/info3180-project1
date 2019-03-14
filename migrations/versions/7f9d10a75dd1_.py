"""empty message

Revision ID: 7f9d10a75dd1
Revises: c586a8f420d3
Create Date: 2019-03-13 22:59:01.355528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f9d10a75dd1'
down_revision = 'c586a8f420d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('joined_on', sa.String(length=50), nullable=True))
    op.drop_column('user_profiles', 'created_on')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('created_on', sa.VARCHAR(length=10), autoincrement=False, nullable=True))
    op.drop_column('user_profiles', 'joined_on')
    # ### end Alembic commands ###
