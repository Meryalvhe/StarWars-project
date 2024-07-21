"""empty message

Revision ID: dc110574136f
Revises: ac56d38580be
Create Date: 2024-07-21 11:19:01.206402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc110574136f'
down_revision = 'ac56d38580be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('species', schema=None) as batch_op:
        batch_op.alter_column('average_height',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)
        batch_op.alter_column('average_lifespan',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('species', schema=None) as batch_op:
        batch_op.alter_column('average_lifespan',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('average_height',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=False)

    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.alter_column('body',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###