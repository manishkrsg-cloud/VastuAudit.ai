"""initial: users + audits

Revision ID: 0001_initial
Revises:
Create Date: 2026-05-02 09:00:00

"""

from __future__ import annotations

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "0001_initial"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ----- users ---------------------------------------------------------
    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("clerk_id", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=320), nullable=False),
        sa.Column("first_name", sa.String(length=120), nullable=True),
        sa.Column("last_name", sa.String(length=120), nullable=True),
        sa.Column(
            "subscription_tier",
            sa.String(length=32),
            nullable=False,
            server_default="free",
        ),
        sa.Column("stripe_customer_id", sa.String(length=255), nullable=True),
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
        sa.UniqueConstraint("clerk_id", name=op.f("uq_users_clerk_id")),
        sa.UniqueConstraint(
            "stripe_customer_id", name=op.f("uq_users_stripe_customer_id")
        ),
    )
    op.create_index(op.f("ix_users_clerk_id"), "users", ["clerk_id"], unique=False)
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=False)
    op.create_index(
        "ix_users_subscription_tier",
        "users",
        ["subscription_tier"],
        unique=False,
    )

    # ----- audits --------------------------------------------------------
    audit_status = postgresql.ENUM(
        "queued",
        "analyzing",
        "ready",
        "failed",
        name="audit_status",
        create_type=False,
    )
    audit_status.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "audits",
        sa.Column("id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "title",
            sa.String(length=255),
            nullable=False,
            server_default="Untitled audit",
        ),
        sa.Column(
            "status",
            audit_status,
            nullable=False,
            server_default="queued",
        ),
        sa.Column("error_message", sa.Text(), nullable=True),
        sa.Column("plan_url", sa.String(length=2048), nullable=True),
        sa.Column("main_door_direction", sa.String(length=16), nullable=True),
        sa.Column("property_type", sa.String(length=64), nullable=True),
        sa.Column("score", sa.Integer(), nullable=True),
        sa.Column("doshas", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("remedies", postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column("report_url", sa.String(length=2048), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.func.now(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            ondelete="CASCADE",
            name=op.f("fk_audits_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_audits")),
    )
    op.create_index(op.f("ix_audits_user_id"), "audits", ["user_id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_audits_user_id"), table_name="audits")
    op.drop_table("audits")
    sa.Enum(name="audit_status").drop(op.get_bind(), checkfirst=True)
    op.drop_index("ix_users_subscription_tier", table_name="users")
    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_index(op.f("ix_users_clerk_id"), table_name="users")
    op.drop_table("users")
