"""Update the database scheme

Revision ID: 07e21af5699c
Revises: 721b2863ae4b
Create Date: 2021-05-03 22:41:12.599687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07e21af5699c'
down_revision = '721b2863ae4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'content')
    op.drop_column('users', 'is_admin')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('posts', sa.Column('content', sa.TEXT(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
