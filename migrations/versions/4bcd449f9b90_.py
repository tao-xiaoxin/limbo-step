"""empty message

Revision ID: 4bcd449f9b90
Revises: 15fbe0c149d4
Create Date: 2022-09-27 23:08:36.557896

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bcd449f9b90'
down_revision = '15fbe0c149d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_user2account', sa.Column('is_activate', sa.Integer(), nullable=True, comment='小米登录密码'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('file_user2account', 'is_activate')
    # ### end Alembic commands ###
