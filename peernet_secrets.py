import os
import streamlit as st


def get_secret(name: str, default: str | None = None) -> str | None:
    value = os.getenv(name)
    if value:
        return value

    try:
        secret = st.secrets.get(name)
        return str(secret) if secret is not None else default
    except Exception:
        return default


def require_secret(name: str) -> str:
    value = get_secret(name)
    if not value:
        raise RuntimeError(
            f"{name} is not configured. Add it to .env locally or "
            "Streamlit Community Cloud Secrets."
        )
    return value


def admin_emails() -> set[str]:
    raw = get_secret("PEERNET_ADMIN_EMAILS", "") or ""
    return {item.strip().lower() for item in raw.split(",") if item.strip()}
