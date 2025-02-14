"""added Goal model

Revision ID: 78680e3deeff
Revises: 95b2cb2aec17
Create Date: 2023-05-08 11:14:23.626678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78680e3deeff'
down_revision = '95b2cb2aec17'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('goal_title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('goal', 'goal_title')
    # ### end Alembic commands ###
