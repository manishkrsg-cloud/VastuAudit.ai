"""Clerk webhook handler.

Clerk signs webhook payloads with Svix. We verify the signature, then
upsert / soft-delete the corresponding user row.

Set the webhook signing secret as ``CLERK_WEBHOOK_SECRET`` (from the
Clerk dashboard → Webhooks → your endpoint → Signing Secret).
"""

from datetime import UTC, datetime
from typing import Any

from fastapi import APIRouter, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from svix.webhooks import Webhook, WebhookVerificationError

from src.api.deps import DbSession
from src.config import settings
from src.models.user import User
from src.utils.logging import get_logger

router = APIRouter()
log = get_logger(__name__)


@router.post("/clerk-webhook", status_code=status.HTTP_200_OK)
async def clerk_webhook(request: Request, db: DbSession) -> dict[str, str]:
    """Handle ``user.created`` / ``user.updated`` / ``user.deleted`` events from Clerk."""
    if not settings.clerk_webhook_secret:
        log.error("clerk.webhook.no_secret_configured")
        raise HTTPException(
            status.HTTP_503_SERVICE_UNAVAILABLE,
            "Clerk webhook secret not configured (CLERK_WEBHOOK_SECRET)",
        )

    headers = {
        "svix-id": request.headers.get("svix-id", ""),
        "svix-timestamp": request.headers.get("svix-timestamp", ""),
        "svix-signature": request.headers.get("svix-signature", ""),
    }
    body = await request.body()

    try:
        wh = Webhook(settings.clerk_webhook_secret)
        evt: dict[str, Any] = wh.verify(body, headers)
    except WebhookVerificationError as exc:
        log.warning("clerk.webhook.bad_signature", err=str(exc))
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "invalid webhook signature") from exc

    event_type: str = evt.get("type", "")
    data: dict[str, Any] = evt.get("data", {})
    log.info("clerk.webhook.received", event_type=event_type, clerk_id=data.get("id"))

    if event_type in ("user.created", "user.updated"):
        await _upsert_user(db, data)
    elif event_type == "user.deleted":
        await _soft_delete_user(db, data)
    else:
        log.info("clerk.webhook.ignored", event_type=event_type)

    return {"status": "processed", "event_type": event_type}


async def _upsert_user(db: AsyncSession, data: dict[str, Any]) -> None:
    clerk_id = data.get("id")
    if not clerk_id:
        return

    primary_email_id = data.get("primary_email_address_id")
    email = ""
    for ea in data.get("email_addresses", []) or []:
        addr = ea.get("email_address") or ""
        if ea.get("id") == primary_email_id:
            email = addr
            break
        email = email or addr

    user = (
        await db.execute(select(User).where(User.clerk_id == clerk_id))
    ).scalar_one_or_none()

    if user is None:
        user = User(
            clerk_id=clerk_id,
            email=email,
            first_name=data.get("first_name") or None,
            last_name=data.get("last_name") or None,
        )
        db.add(user)
        log.info("user.created", clerk_id=clerk_id, email=email)
    else:
        if email:
            user.email = email
        if data.get("first_name") is not None:
            user.first_name = data.get("first_name")
        if data.get("last_name") is not None:
            user.last_name = data.get("last_name")
        log.info("user.updated", clerk_id=clerk_id)


async def _soft_delete_user(db: AsyncSession, data: dict[str, Any]) -> None:
    clerk_id = data.get("id")
    if not clerk_id:
        return
    user = (
        await db.execute(select(User).where(User.clerk_id == clerk_id))
    ).scalar_one_or_none()
    if user is not None:
        user.deleted_at = datetime.now(UTC)
        log.info("user.deleted", clerk_id=clerk_id)
