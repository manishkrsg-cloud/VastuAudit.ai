"""Application settings — single source of truth for environment variables."""

from functools import lru_cache
from typing import Literal

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", "../../.env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ----- app identity --------------------------------------------------
    app_name: str = "VastuAudit.ai"
    app_owner: str = "Qadr AI Agency Dubai"
    app_env: Literal["development", "staging", "production"] = "development"
    admin_email: str = "manish@qadr.ai"
    log_level: str = "INFO"

    # ----- data layer ----------------------------------------------------
    database_url: str = (
        "postgresql+asyncpg://vastuaudit:vastuaudit@localhost:5432/vastuaudit"
    )
    redis_url: str = "redis://localhost:6379/0"

    # ----- AI ------------------------------------------------------------
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-sonnet-4-6"
    anthropic_reasoning_model: str = "claude-opus-4-7"

    # ----- auth (Clerk) --------------------------------------------------
    clerk_secret_key: str = ""
    clerk_publishable_key: str = ""
    clerk_webhook_secret: str = ""

    # ----- storage (Cloudflare R2) ---------------------------------------
    r2_account_id: str = ""
    r2_access_key_id: str = ""
    r2_secret_access_key: str = ""
    r2_bucket_name: str = "vastuaudit-plans"
    r2_public_base_url: str = ""

    # ----- payments (Stripe) ---------------------------------------------
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_pro_id: str = ""
    stripe_price_consultant_id: str = ""

    # ----- email (Resend) ------------------------------------------------
    resend_api_key: str = ""
    resend_from_email: str = "hello@vastuaudit.ai"

    # ----- web / CORS ----------------------------------------------------
    cors_origins: str = (
        "http://localhost:3000,https://vastuaudit.ai,https://www.vastuaudit.ai"
    )

    # ----- observability -------------------------------------------------
    sentry_dsn: str = ""
    posthog_api_key: str = ""

    # ---------------------------------------------------------------------
    @computed_field  # type: ignore[prop-decorator]
    @property
    def cors_origins_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    @computed_field  # type: ignore[prop-decorator]
    @property
    def is_production(self) -> bool:
        return self.app_env == "production"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings: Settings = get_settings()
