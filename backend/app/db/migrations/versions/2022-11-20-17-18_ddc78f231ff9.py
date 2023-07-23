"""Make people fields optional

Revision ID: ddc78f231ff9
Revises: 7244568ec5be
Create Date: 2022-11-20 17:18:09.131024

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op


# revision identifiers, used by Alembic.
revision = 'ddc78f231ff9'
down_revision = '7244568ec5be'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('people', 'age',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('people', 'gender',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('people', 'occupation',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('people', 'occupation',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('people', 'gender',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('people', 'age',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
