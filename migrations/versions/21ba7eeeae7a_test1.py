"""test1

Revision ID: 21ba7eeeae7a
Revises: 15a385fd42a
Create Date: 2015-10-25 05:50:30.249233

"""

# revision identifiers, used by Alembic.
revision = '21ba7eeeae7a'
down_revision = '15a385fd42a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doubes', sa.Column('img', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('doubes', 'img')
    ### end Alembic commands ###