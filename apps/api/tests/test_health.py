"""Smoke test for the liveness probe — does not need DB or Redis running."""

from fastapi.testclient import TestClient

from src.main import app


def test_root() -> None:
    with TestClient(app) as client:
        response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "VastuAudit.ai"
    assert body["owner"] == "Qadr AI Agency Dubai"


def test_health_liveness() -> None:
    with TestClient(app) as client:
        response = client.get("/api/v1/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["app"] == "VastuAudit.ai"
    assert body["owner"] == "Qadr AI Agency Dubai"
