import hashlib
import json
import os
import secrets
from pathlib import Path

import streamlit as st

USERS_FILE = Path("users.json")


def _hash_password(password: str, salt_hex: str | None = None) -> tuple[str, str]:
    salt = bytes.fromhex(salt_hex) if salt_hex else secrets.token_bytes(16)
    digest = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        200_000,
    )
    return salt.hex(), digest.hex()


def _load_users() -> dict[str, dict[str, str]]:
    if not USERS_FILE.exists():
        return {}

    try:
        data = json.loads(USERS_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        return {}


def _save_users(users: dict[str, dict[str, str]]) -> None:
    USERS_FILE.write_text(json.dumps(users, indent=2), encoding="utf-8")


def ensure_admin_user() -> None:
    users = _load_users()
    username = os.getenv("PEERNET_USERNAME", "admin").strip()
    password = os.getenv("PEERNET_PASSWORD", "peernet123")

    if username and username not in users:
        salt, password_hash = _hash_password(password)
        users[username] = {
            "salt": salt,
            "password_hash": password_hash,
            "display_name": "PeerNet Member",
        }
        _save_users(users)


def register_user(
    full_name: str,
    username: str,
    email: str,
    password: str,
    confirm_password: str,
) -> tuple[bool, str]:
    full_name = full_name.strip()
    username = username.strip()
    email = email.strip()

    if len(full_name) < 2:
        return False, "Please enter your full name."

    if len(username) < 3:
        return False, "Username must contain at least 3 characters."

    if "@" not in email:
        return False, "Please enter a valid email address."

    if len(password) < 8:
        return False, "Password must contain at least 8 characters."

    if password != confirm_password:
        return False, "Passwords do not match."

    users = _load_users()

    if username in users:
        return False, "That username is already registered."

    if any(record.get("email", "").lower() == email.lower() for record in users.values()):
        return False, "That email address is already registered."

    salt, password_hash = _hash_password(password)
    users[username] = {
        "salt": salt,
        "password_hash": password_hash,
        "display_name": full_name,
        "email": email,
    }

    try:
        _save_users(users)
    except OSError as error:
        return False, f"Unable to save the account: {error}"

    return True, "Registration completed. You can now sign in."


def authenticate(username: str, password: str) -> tuple[bool, str]:
    users = _load_users()
    record = users.get(username.strip())

    if not record:
        return False, ""

    _, candidate_hash = _hash_password(password, salt_hex=record["salt"])

    valid = secrets.compare_digest(candidate_hash, record["password_hash"])
    return valid, record.get("display_name", "PeerNet Member") if valid else ""


def logout() -> None:
    st.session_state.authenticated = False
    st.session_state.username = ""
    st.session_state.display_name = ""
    st.session_state.messages = []
    st.session_state.pending_prompt = None
    st.rerun()
