"""empty message

Revision ID: 861d3b286cac
Revises: e9f66fd6ea10
Create Date: 2022-10-11 23:18:04.268212

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '861d3b286cac'
down_revision = 'e9f66fd6ea10'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_task_log', sa.Column('time_stamp', sa.String(length=180), nullable=True, comment='创建时间'))
    op.drop_column('file_task_log', 'create_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_task_log', sa.Column('create_time', mysql.DATETIME(), nullable=True, comment='创建时间'))
    op.drop_column('file_task_log', 'time_stamp')
    # ### end Alembic commands ###