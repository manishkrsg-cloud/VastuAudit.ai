"""Audit model — represents one Vastu audit run for a user."""

from __future__ import annotations

import enum
import uuid
from typing import TYPE_CHECKING, Any

from sqlalchemy import Enum as SAEnum
from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from src.models.user import User


class AuditStatus(str, enum.Enum):
    QUEUED = "queued"
    ANALYZING = "analyzing"
    READY = "ready"
    FAILED = "failed"


class Audit(Base, TimestampMixin):
    __tablename__ = "audits"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    title: Mapped[str] = mapped_column(
        String(255), nullable=False, default="Untitled audit"
    )
    status: Mapped[AuditStatus] = mapped_column(
        SAEnum(
            AuditStatus,
            name="audit_status",
            values_callable=lambda x: [e.value for e in x],
        ),
        nullable=False,
        default=AuditStatus.QUEUED,
        server_default=AuditStatus.QUEUED.value,
    )
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Inputs
    plan_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    main_door_direction: Mapped[str | None] = mapped_column(String(16), nullable=True)
    property_type: Mapped[str | None] = mapped_column(String(64), nullable=True)

    # Outputs
    score: Mapped[int | None] = mapped_column(Integer, nullable=True)
    doshas: Mapped[list[Any] | None] = mapped_column(JSONB, nullable=True)
    remedies: Mapped[list[Any] | None] = mapped_column(JSONB, nullable=True)
    report_url: Mapped[str | None] = mapped_column(String(2048), nullable=True)

    user: Mapped["User"] = relationship(back_populates="audits")

    def __repr__(self) -> str:
        return f"<Audit id={self.id} status={self.status.value} score={self.score}>"
