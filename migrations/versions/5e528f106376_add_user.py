"""add user

Revision ID: 5e528f106376
Revises: a3f142b4ce31
Create Date: 2022-09-18 12:40:20.949913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e528f106376'
down_revision = 'a3f142b4ce31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_model_username'), 'user_model', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_model_username'), table_name='user_model')
    op.drop_table('user_model')
    # ### end Alembic commands ###
