"""Added posted_on column on posts

Revision ID: 4d38fd3d369e
Revises:
Create Date: 2017-07-22 19:25:32.558399

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '4d38fd3d369e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('posted_on', sa.DateTime(), nullable=True))
    op.execute('UPDATE post SET posted_on ="{}"'.format('2017-07-15 16:00:00'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'posted_on')
    # ### end Alembic commands ###