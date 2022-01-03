"""add column to posts table

Revision ID: f5ba4dccf5f6
Revises: 5e1fef777b3a
Create Date: 2022-01-03 17:03:11.379341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f5ba4dccf5f6"
down_revision = "5e1fef777b3a"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
