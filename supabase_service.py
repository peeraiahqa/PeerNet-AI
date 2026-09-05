from typing import Any

import streamlit as st
from supabase import Client, create_client

from config import SUPABASE_REDIRECT_URL
from peernet_secrets import get_secret, require_secret


def create_user_client() -> Client:
    return create_client(
        require_secret("SUPABASE_URL"),
        require_secret("SUPABASE_ANON_KEY"),
    )


def get_client() -> Client:
    if "supabase_client" not in st.session_state:
        st.session_state.supabase_client = create_user_client()

    client: Client = st.session_state.supabase_client
    access_token = st.session_state.get("access_token")
    refresh_token = st.session_state.get("refresh_token")

    if access_token and refresh_token:
        try:
            client.auth.set_session(access_token, refresh_token)
        except Exception:
            clear_auth_state()

    return client


def create_admin_client() -> Client | None:
    service_key = get_secret("SUPABASE_SERVICE_ROLE_KEY")
    if not service_key:
        return None

    return create_client(require_secret("SUPABASE_URL"), service_key)


def save_session(auth_response: Any) -> None:
    session = getattr(auth_response, "session", None)
    user = getattr(auth_response, "user", None)

    if not session or not user:
        return

    st.session_state.access_token = session.access_token
    st.session_state.refresh_token = session.refresh_token
    st.session_state.user_id = user.id
    st.session_state.user_email = user.email or ""
    st.session_state.authenticated = True


def clear_auth_state() -> None:
    for key in (
        "access_token",
        "refresh_token",
        "user_id",
        "user_email",
        "profile",
        "messages",
        "current_conversation_id",
    ):
        st.session_state.pop(key, None)

    st.session_state.authenticated = False


def sign_up(email: str, password: str, full_name: str, username: str) -> Any:
    return get_client().auth.sign_up(
        {
            "email": email,
            "password": password,
            "options": {
                "data": {"full_name": full_name, "username": username},
                "email_redirect_to": SUPABASE_REDIRECT_URL,
            },
        }
    )


def sign_in(email: str, password: str) -> Any:
    response = get_client().auth.sign_in_with_password(
        {"email": email, "password": password}
    )
    save_session(response)
    return response


def sign_out() -> None:
    try:
        get_client().auth.sign_out()
    finally:
        clear_auth_state()


def delete_current_account() -> None:
    """Permanently delete the signed-in user and all cascading account data."""
    user_id = st.session_state.get("user_id")
    if not user_id:
        raise RuntimeError("No signed-in account was found.")

    admin_client = create_admin_client()
    if not admin_client:
        raise RuntimeError(
            "Account deletion is temporarily unavailable. "
            "Please contact PeerNet Solutions support."
        )

    # All PeerNet AI user tables reference auth.users with ON DELETE CASCADE.
    # Deleting the authenticated user removes their associated application data.
    admin_client.auth.admin.delete_user(user_id)
    clear_auth_state()


def send_password_reset(email: str) -> None:
    get_client().auth.reset_password_for_email(
        email,
        {"redirect_to": SUPABASE_REDIRECT_URL},
    )


def update_password(new_password: str) -> None:
    get_client().auth.update_user({"password": new_password})


def resend_verification(email: str) -> None:
    get_client().auth.resend(
        {
            "type": "signup",
            "email": email,
            "options": {"email_redirect_to": SUPABASE_REDIRECT_URL},
        }
    )


def load_profile() -> dict[str, Any]:
    user_id = st.session_state.get("user_id")
    if not user_id:
        return {}

    response = (
        get_client()
        .table("profiles")
        .select("*")
        .eq("id", user_id)
        .limit(1)
        .execute()
    )

    profile = response.data[0] if response.data else {}
    st.session_state.profile = profile
    return profile


def update_profile(full_name: str, username: str, bio: str) -> dict[str, Any]:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("profiles")
        .update({"full_name": full_name, "username": username, "bio": bio})
        .eq("id", user_id)
        .select("*")
        .execute()
    )

    profile = response.data[0] if response.data else {}
    st.session_state.profile = profile
    return profile


def list_conversations() -> list[dict[str, Any]]:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("conversations")
        .select("*")
        .eq("user_id", user_id)
        .order("updated_at", desc=True)
        .execute()
    )
    return response.data or []


def create_conversation(title: str) -> dict[str, Any]:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("conversations")
        .insert({"user_id": user_id, "title": title[:120]})
        .select("*")
        .execute()
    )
    return response.data[0]


def delete_conversation(conversation_id: str) -> None:
    user_id = st.session_state["user_id"]

    (
        get_client()
        .table("conversations")
        .delete()
        .eq("id", conversation_id)
        .eq("user_id", user_id)
        .execute()
    )


def load_messages(conversation_id: str) -> list[dict[str, Any]]:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("messages")
        .select("*")
        .eq("conversation_id", conversation_id)
        .eq("user_id", user_id)
        .order("created_at")
        .execute()
    )
    return response.data or []


def save_message(
    conversation_id: str,
    role: str,
    content: str,
) -> dict[str, Any]:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("messages")
        .insert(
            {
                "conversation_id": conversation_id,
                "user_id": user_id,
                "role": role,
                "content": content,
            }
        )
        .select("*")
        .execute()
    )

    return response.data[0]


def list_favorites() -> list[dict[str, Any]]:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("favorites")
        .select("*")
        .eq("user_id", user_id)
        .order("created_at", desc=True)
        .execute()
    )
    return response.data or []


def add_favorite(title: str, content: str) -> dict[str, Any]:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("favorites")
        .insert(
            {
                "user_id": user_id,
                "title": title[:120],
                "content": content,
            }
        )
        .select("*")
        .execute()
    )
    return response.data[0]


def delete_favorite(favorite_id: str) -> None:
    user_id = st.session_state["user_id"]

    (
        get_client()
        .table("favorites")
        .delete()
        .eq("id", favorite_id)
        .eq("user_id", user_id)
        .execute()
    )


def rename_conversation(conversation_id: str, title: str) -> None:
    user_id = st.session_state["user_id"]
    cleaned = title.strip()[:120]

    if not cleaned:
        raise ValueError("Conversation title cannot be empty.")

    (
        get_client()
        .table("conversations")
        .update({"title": cleaned, "updated_at": "now()"})
        .eq("id", conversation_id)
        .eq("user_id", user_id)
        .execute()
    )


def search_conversations(query: str) -> list[dict[str, Any]]:
    cleaned = query.strip()

    if not cleaned:
        return list_conversations()

    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("conversations")
        .select("*")
        .eq("user_id", user_id)
        .ilike("title", f"%{cleaned}%")
        .order("updated_at", desc=True)
        .execute()
    )

    return response.data or []


def get_today_usage() -> int:
    user_id = st.session_state["user_id"]

    response = (
        get_client()
        .table("usage_events")
        .select("id", count="exact")
        .eq("user_id", user_id)
        .gte("created_at", "today")
        .execute()
    )

    return int(response.count or 0)


def record_usage(mode: str, model: str) -> None:
    user_id = st.session_state["user_id"]

    (
        get_client()
        .table("usage_events")
        .insert(
            {
                "user_id": user_id,
                "mode": mode,
                "model": model,
            }
        )
        .execute()
    )


def save_feedback(
    conversation_id: str | None,
    message_content: str,
    rating: str,
) -> None:
    user_id = st.session_state["user_id"]

    (
        get_client()
        .table("message_feedback")
        .insert(
            {
                "user_id": user_id,
                "conversation_id": conversation_id,
                "message_content": message_content[:8000],
                "rating": rating,
            }
        )
        .execute()
    )


def admin_metrics() -> dict[str, int]:
    admin_client = create_admin_client()

    if not admin_client:
        raise RuntimeError("SUPABASE_SERVICE_ROLE_KEY is not configured.")

    profiles = (
        admin_client.table("profiles").select("id", count="exact").execute()
    )
    conversations = (
        admin_client.table("conversations").select("id", count="exact").execute()
    )
    usage = (
        admin_client.table("usage_events").select("id", count="exact").execute()
    )
    feedback = (
        admin_client.table("message_feedback").select("id", count="exact").execute()
    )

    return {
        "users": int(profiles.count or 0),
        "conversations": int(conversations.count or 0),
        "usage_events": int(usage.count or 0),
        "feedback": int(feedback.count or 0),
    }
