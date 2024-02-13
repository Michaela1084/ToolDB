"""empty message

Revision ID: 06f2884f061a
Revises: 
Create Date: 2024-02-12 01:20:57.174832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06f2884f061a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('tool',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('t_type', sa.String(length=200), nullable=False),
    sa.Column('dia', sa.String(length=200), nullable=True),
    sa.Column('flutes', sa.String(length=200), nullable=True),
    sa.Column('oal', sa.String(length=200), nullable=True),
    sa.Column('f_length', sa.String(length=200), nullable=True),
    sa.Column('link', sa.String(length=500), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tool')
    op.drop_table('user')
    # ### end Alembic commands ###
