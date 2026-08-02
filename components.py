from datetime import datetime

import streamlit as st

from config import LOGO_PATH, QUICK_PROMPTS


def initialize_state() -> None:
    defaults = {
        "authenticated": False,
        "username": "",
        "display_name": "",
        "messages": [],
        "pending_prompt": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def queue_prompt(prompt: str) -> None:
    cleaned = prompt.strip()
    if cleaned:
        st.session_state.pending_prompt = cleaned


def export_conversation(messages: list[dict[str, str]]) -> str:
    lines = [
        "PeerNet AI Conversation Export",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
    ]

    for message in messages:
        lines.extend([f"{message['role'].upper()}:", message["content"], ""])

    return "\n".join(lines)


def render_profile() -> None:
    display_name = st.session_state.display_name or "PeerNet Member"

    st.image(LOGO_PATH, width=150)

    st.markdown(
        f'<div class="pn-profile pn-profile-no-avatar">'
        f'<div class="pn-member">{display_name}</div>'
        f'<div class="pn-online">'
        f'<span class="pn-online-dot"></span>'
        f'<span>Online</span>'
        f'</div>'
        f'<div class="pn-premium">'
        f'<span>♛</span>'
        f'<span>Premium Member</span>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def render_main_header() -> None:
    display_name = st.session_state.display_name or "PeerNet Member"

    st.markdown(
        f'<div class="pn-topline">'
        f'<div class="pn-bot">🤖</div>'
        f'<div>'
        f'<div class="pn-welcome-small">Welcome back, 👋</div>'
        f'<div class="pn-welcome-name">{display_name}</div>'
        f'</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        '<div class="pn-hero">'
        '<h1 class="pn-title">PeerNet <span>AI</span> ✦</h1>'
        '<div class="pn-subtitle">'
        '<span class="pn-subtitle-line">'
        'Your Smart Networking & Automation Assistant'
        '</span>'
        '<span class="pn-subtitle-line">'
        'Learn • Troubleshoot • Automate • Prepare'
        '</span>'
        '</div>'
        '<div class="pn-chip-row">'
        '<span class="pn-chip">🌐 Networking</span>'
        '<span class="pn-chip">☁️ SD-WAN</span>'
        '<span class="pn-chip">📶 Meraki</span>'
        '<span class="pn-chip">🐍 Python / pyATS</span>'
        '<span class="pn-chip">🎙️ Interview Prep</span>'
        '<span class="pn-chip">📋 Test Planning</span>'
        '</div>'
        '</div>',
        unsafe_allow_html=True,
    )


def render_quick_cards() -> None:
    st.markdown(
        '<div class="pn-question-title">✦ Try these popular questions</div>',
        unsafe_allow_html=True,
    )

    columns = st.columns(5)

    for index, (prompt, icon, color) in enumerate(QUICK_PROMPTS):
        with columns[index]:
            st.markdown(
                f'<div class="pn-card" style="background:{color};">'
                f'<div class="pn-card-icon">{icon}</div>'
                f'<div class="pn-card-title">{prompt}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )

            if st.button("Open →", key=f"quick_{index}", use_container_width=True):
                queue_prompt(prompt)
                st.rerun()


def render_status(api_key: str | None, selected_mode: str, model: str) -> None:
    status = "Connected to OpenAI" if api_key else "OpenAI key required"

    st.markdown(
        f'<div class="pn-status">'
        f'<span><span class="pn-status-live">● Live Workspace</span> · {status}</span>'
        f'<span>{selected_mode} · {model}</span>'
        f'<span>🛡 Your data is handled securely</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
