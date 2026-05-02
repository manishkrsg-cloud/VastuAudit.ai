"""User model. Source of truth is Clerk; we mirror the minimum we need."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Index, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from src.models.audit import Audit


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    # Clerk identity
    clerk_id: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True
    )
    email: Mapped[str] = mapped_column(String(320), nullable=False, index=True)
    first_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(120), nullable=True)

    # Subscription state — keep in sync via Stripe webhook (Sprint 4)
    subscription_tier: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
        default="free",
        server_default="free",
    )  # free | pro | consultant | enterprise
    stripe_customer_id: Mapped[str | None] = mapped_column(
        String(255), nullable=True, unique=True
    )

    # Soft-delete (Clerk user.deleted)
    deleted_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    audits: Mapped[list["Audit"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )

    __table_args__ = (
        Index("ix_users_subscription_tier", "subscription_tier"),
    )

    def __repr__(self) -> str:
        return f"<User {self.email!r} ({self.subscription_tier})>"
