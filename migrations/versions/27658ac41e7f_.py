"""empty message

Revision ID: 27658ac41e7f
Revises: a0f74d3e2351
Create Date: 2020-05-16 06:37:10.667279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27658ac41e7f'
down_revision = 'a0f74d3e2351'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=120), nullable=False))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=120), nullable=False))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###