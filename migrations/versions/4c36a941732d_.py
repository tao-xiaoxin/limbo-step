"""empty message

Revision ID: 4c36a941732d
Revises: 82c3a3142e42
Create Date: 2022-09-29 12:43:52.499547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c36a941732d'
down_revision = '82c3a3142e42'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_user2push',
    sa.Column('app_id', sa.String(length=180), nullable=False, comment='推送+token'),
    sa.Column('uid', sa.Integer(), nullable=True, comment='绑定用户id'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('is_activate', sa.Boolean(), nullable=True, comment='是否有效'),
    sa.PrimaryKeyConstraint('app_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_user2push')
    # ### end Alembic commands ###
