"""Pydantic DTOs for Audit."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from src.models.audit import AuditStatus


class AuditCreate(BaseModel):
    title: str = Field(default="Untitled audit", max_length=255)
    main_door_direction: str | None = Field(
        default=None,
        description="One of N, NE, E, SE, S, SW, W, NW (or full name).",
    )
    property_type: str | None = Field(
        default=None,
        description="e.g. 'apartment', 'villa', 'office', 'retail'.",
    )


class AuditRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    status: AuditStatus
    plan_url: str | None
    main_door_direction: str | None
    property_type: str | None
    score: int | None
    doshas: list[Any] | None
    remedies: list[Any] | None
    report_url: str | None
    error_message: str | None
    created_at: datetime
    updated_at: datetime
