"""empty message

Revision ID: 303487b78a56
Revises: e5455c7ef416
Create Date: 2022-10-08 23:22:50.804980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '303487b78a56'
down_revision = 'e5455c7ef416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_task_log',
    sa.Column('id', sa.Integer(), nullable=False, comment='用户ID'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('user_id', sa.Integer(), nullable=True, comment='用户id'),
    sa.Column('task_type', sa.String(length=180), nullable=True, comment='任务类型'),
    sa.Column('content', sa.Text(), nullable=True, comment='日志内容'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_task_log')
    # ### end Alembic commands ###
