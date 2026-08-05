from datetime import datetime
import html
import textwrap

import streamlit as st

from config import LOGO_PATH, QUICK_PROMPTS


def initialize_state() -> None:
    defaults = {
        "authenticated": False,
        "messages": [],
        "current_conversation_id": None,
        "active_page": "Home",
        "pending_prompt": None,
        "composer_mode": "Text",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def queue_prompt(prompt: str) -> None:
    cleaned = prompt.strip()
    if cleaned:
        st.session_state.pending_prompt = cleaned


def _user_initial(profile: dict) -> str:
    """Return the first visible character of the user's name or email."""
    candidates = (
        profile.get("full_name"),
        profile.get("username"),
        profile.get("email"),
        "P",
    )

    for value in candidates:
        cleaned = str(value or "").strip()
        if cleaned:
            return html.escape(cleaned[0].upper())

    return "P"

def get_greeting_and_message():
    hour = datetime.now().hour

    if 5 <= hour < 12:
        return (
            "☀️ Good Morning",
            "Ready to build something amazing today?"
        )

    elif 12 <= hour < 17:
        return (
            "🌤 Good Afternoon",
            "Keep your momentum going!"
        )

    elif 17 <= hour < 21:
        return (
            "🌇 Good Evening",
            "Let's solve some networking challenges."
        )

    else:
        return (
            "🌙 Good Night",
            "Don't forget to save your work before you rest."
        )

def render_sidebar_profile(profile: dict) -> None:
    name = html.escape(
        profile.get("full_name")
        or profile.get("username")
        or "PeerNet User"
    )
    role = html.escape(profile.get("role", "member").title())
    initial = _user_initial(profile)

    st.image(LOGO_PATH, width=145)

    st.html(
        textwrap.dedent(
            f"""
            <div class="pn-sidebar-user-card">
                <div class="pn-sidebar-user-avatar">{initial}<span></span></div>
                <div class="pn-sidebar-user-copy">
                    <strong>{name}</strong>
                    <small>{role}</small>
                </div>
                <div class="pn-sidebar-user-status">●</div>
            </div>
            """
        )
    )


def render_topbar(profile: dict, model: str) -> None:
    initial = _user_initial(profile)

    st.html(
        textwrap.dedent(
            f"""
            <div class="pn-topbar pn-topbar-profile-only">
                <div class="pn-topbar-spacer"></div>
                <div
                    class="pn-v8-profile-bubble"
                    title="User profile"
                    aria-label="User profile"
                >
                    <span class="pn-v8-profile-letter">{initial}</span>
                    <span
                        class="pn-v8-profile-online"
                        title="Online"
                        aria-label="Online"
                    ></span>
                </div>
            </div>
            """
        )
    )

def render_hero(user_name: str) -> None:
    greeting, message = get_greeting_and_message()

    st.html(
        textwrap.dedent(
            f"""
            <section class="pn-dashboard-hero">
                <div class="pn-hero-copy">
                    <h1>{greeting}, {user_name}! 👋</h1>
                    <p>{message}</p>
                </div>

                <div class="pn-hero-art" aria-hidden="true">
                    <div class="pn-core-cube">⌘</div>

                    <span class="cube c1"></span>
                    <span class="cube c2"></span>
                    <span class="cube c3"></span>
                    <span class="cube c4"></span>

                    <i class="line l1"></i>
                    <i class="line l2"></i>
                    <i class="line l3"></i>
                    <i class="line l4"></i>
                </div>
            </section>
            """
        )
    )


def render_quick_prompts() -> None:
    cards = [
        ("Networking", "Design, configure and troubleshoot network architectures", "🌐", "card-blue", "Explain a networking concept with examples."),
        ("SD-WAN", "SD-WAN design, troubleshooting and best practices", "🛡️", "card-green", "Help me troubleshoot Cisco SD-WAN."),
        ("Meraki", "Meraki solutions, API, automation and monitoring", "M", "card-teal", "Help me with Cisco Meraki."),
        ("Python / pyATS", "Python automation, pyATS testing and network scripts", "🐍", "card-purple", "Generate a Python or pyATS automation."),
        ("Interview Prep", "Prepare for networking interviews with Q&A and scenarios", "◉", "card-orange", "Start a networking interview practice session."),
        ("Test Planning", "Test plans, test cases and automation strategies", "✓", "card-pink", "Create a test plan from my requirements."),
    ]

    columns = st.columns(6, gap="medium")
    for index, (title, description, icon, css_class, prompt) in enumerate(cards):
        with columns[index]:
            st.html(textwrap.dedent(f"""
                <article class="pn-feature-card {css_class}">
                    <div class="pn-feature-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </article>
            """))
            if st.button(
                title,
                key=f"feature_prompt_{index}",
                use_container_width=True,
            ):
                queue_prompt(prompt)
                st.rerun()

    st.html(textwrap.dedent("""
        <div class="pn-popular">
            <strong>🔥 Popular Topics</strong>
            <div>
                <span>SD-WAN</span><span>BGP</span><span>EVPN</span>
                <span>OSPF</span><span>Python</span><span>Security</span>
                <span>Meraki</span><span>Automation</span>
            </div>
        </div>
    """))

def render_connection_status(has_api_key: bool) -> None:
    connection = "Connected to OpenAI" if has_api_key else "OpenAI key required"
    st.html(textwrap.dedent(f"""
        <div class="pn-statusbar">
            <div class="pn-live-pill">✦ <b>Live Mode</b></div>
            <div class="pn-connected"><i></i>{connection}</div>
            <div class="pn-secure">♢ Your data is secure and encrypted</div>
        </div>
    """))
