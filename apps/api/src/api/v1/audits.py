"""Audits API.

Sprint 1.1: skeleton only. Full implementation lands in Sprint 1.2 once
the R2 upload helper and Vastu engine v1 exist.
"""

from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.post("", status_code=status.HTTP_501_NOT_IMPLEMENTED, summary="Create a Vastu audit")
async def create_audit() -> dict[str, str]:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Audit creation lands in Sprint 1.2 (R2 upload + Vastu engine v1).",
    )


@router.get("/{audit_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED, summary="Get a Vastu audit")
async def get_audit(audit_id: str) -> dict[str, str]:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Audit retrieval lands in Sprint 1.2.",
    )
