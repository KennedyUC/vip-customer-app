"""Contact us

Revision ID: ee7e57d31f15
Revises: 6eb181f6b086
Create Date: 2022-12-10 15:52:15.733542

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op


# revision identifiers, used by Alembic.
revision = 'ee7e57d31f15'
down_revision = '6eb181f6b086'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_us',
    sa.Column('id', sqlmodel.sql.sqltypes.GUID(), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('current_timestamp(0)'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('current_timestamp(0)'), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('message', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contact_us_id'), 'contact_us', ['id'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contact_us_id'), table_name='contact_us')
    op.drop_table('contact_us')
    # ### end Alembic commands ###
