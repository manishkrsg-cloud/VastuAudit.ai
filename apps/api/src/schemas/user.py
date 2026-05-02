"""Pydantic DTOs for User."""

from __future__ import annotations

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    first_name: str | None = None
    last_name: str | None = None


class UserRead(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    clerk_id: str
    subscription_tier: str
    created_at: datetime
    updated_at: datetime
