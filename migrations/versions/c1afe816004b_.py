"""empty message

Revision ID: c1afe816004b
Revises: 5005cdc8d0a2
Create Date: 2024-06-09 16:46:08.824663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1afe816004b'
down_revision = '5005cdc8d0a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('home_world_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planets', ['home_world_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('home_world_id')

    # ### end Alembic commands ###