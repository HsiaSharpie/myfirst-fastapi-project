"""add user table

Revision ID: fa17ffab9afa
Revises: f5ba4dccf5f6
Create Date: 2022-01-03 21:26:28.757689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "fa17ffab9afa"
down_revision = "f5ba4dccf5f6"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    pass


def downgrade():
    op.drop_table("users")
    pass
