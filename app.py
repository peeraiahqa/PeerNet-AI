import streamlit as st
import base64
import mimetypes
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from streamlit_mic_recorder import speech_to_text
from dotenv import load_dotenv

from ai_service import generate_answer
from connectivity_component import render_connectivity_monitor
from document_service import extract_uploaded_text
from config import (
    AI_LOGIN_IMAGE_PATH,
    APP_TITLE,
    DEFAULT_MODEL,
    MODEL_OPTIONS,
    FAVICON_PATH,
    LOGO_PATH,
    MODE_INSTRUCTIONS,
    DAILY_FREE_LIMIT,
    MAX_UPLOAD_MB,
    NETWORK_TOOLS,
)
from peernet_secrets import admin_emails
from styles import apply_styles
from supabase_service import (
    add_favorite,
    create_admin_client,
    create_conversation,
    delete_conversation,
    delete_favorite,
    list_conversations,
    list_favorites,
    load_messages,
    load_profile,
    resend_verification,
    save_message,
    send_password_reset,
    sign_in,
    sign_out,
    sign_up,
    update_password,
    update_profile,
    rename_conversation,
    search_conversations,
    get_today_usage,
    record_usage,
    save_feedback,
    admin_metrics,
)
from ui import (
    initialize_state,
    queue_prompt,
    render_connection_status,
    render_hero,
    render_quick_prompts,
    render_sidebar_profile,
    render_topbar,
)


st.set_page_config(
    page_title=APP_TITLE,
    page_icon=FAVICON_PATH,
    layout="wide",
    initial_sidebar_state="expanded",
)

load_dotenv()
initialize_state()
render_connectivity_monitor()

THEME_OPTIONS = ["Light", "Dark", "Blue"]

if "app_theme" not in st.session_state:
    st.session_state.app_theme = st.session_state.get(
        "sidebar_theme_selector",
        "Light",
    )

if "sidebar_theme_selector" not in st.session_state:
    st.session_state.sidebar_theme_selector = st.session_state.app_theme

if "settings_theme_selector" not in st.session_state:
    st.session_state.settings_theme_selector = st.session_state.app_theme


def _sync_theme_from_sidebar() -> None:
    selected = st.session_state.get("sidebar_theme_selector", "Light")
    st.session_state.app_theme = selected
    st.session_state.settings_theme_selector = selected


def _sync_theme_from_settings() -> None:
    selected = st.session_state.get("settings_theme_selector", "Light")
    st.session_state.app_theme = selected
    st.session_state.sidebar_theme_selector = selected


def _sync_mode_from_sidebar() -> None:
    selected = st.session_state.get(
        "assistant_mode_selector",
        list(MODE_INSTRUCTIONS.keys())[0],
    )
    st.session_state.mobile_assistant_mode_selector = selected


def _sync_mode_from_mobile() -> None:
    selected = st.session_state.get(
        "mobile_assistant_mode_selector",
        list(MODE_INSTRUCTIONS.keys())[0],
    )
    st.session_state.assistant_mode_selector = selected


active_theme = st.session_state.get("app_theme", "Light")
apply_styles(active_theme)

# Remove Streamlit toolbar/header/top white space.
st.html(
    """
    <style>
    header[data-testid="stHeader"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        min-height: 0 !important;
        max-height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stToolbar"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        min-height: 0 !important;
        max-height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .block-container,
    .stApp,
    section.main,
    section.main > div,
    div[data-testid="stAppViewBlockContainer"] {
        margin-top: 0 !important;
    }

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    .stApp,
    section.main,
    section.main > div,
    div[data-testid="stAppViewBlockContainer"] {
        padding-top: 0 !important;
    }

    [data-testid="stMainBlockContainer"],
    .block-container {
        padding-top: 0.25rem !important;
    }

    #MainMenu,
    footer {
        display: none !important;
        visibility: hidden !important;
    }

    @media (max-width: 900px) {
        [data-testid="stMainBlockContainer"],
        .block-container {
            padding-top: 0.15rem !important;
        }
    }
    </style>
    """
)




if "voice_transcript" not in st.session_state:
    st.session_state.voice_transcript = ""

if "selected_model" not in st.session_state:
    st.session_state.selected_model = DEFAULT_MODEL

if "generation_discard" not in st.session_state:
    st.session_state.generation_discard = False

if "assistant_mode_selector" not in st.session_state:
    st.session_state.assistant_mode_selector = list(MODE_INSTRUCTIONS.keys())[0]

if "mobile_assistant_mode_selector" not in st.session_state:
    st.session_state.mobile_assistant_mode_selector = (
        st.session_state.assistant_mode_selector
    )

if "show_recent_chats" not in st.session_state:
    st.session_state.show_recent_chats = False

selected_mode = st.session_state.assistant_mode_selector


@st.cache_resource
def _generation_executor() -> ThreadPoolExecutor:
    # One worker keeps one AI generation active per Streamlit process.
    return ThreadPoolExecutor(max_workers=4, thread_name_prefix="peernet_ai")


def _generation_active() -> bool:
    future = st.session_state.get("generation_future")
    return future is not None and not future.done()


def _stop_generation() -> None:
    """Request cancellation and discard a response if the HTTP call is already running."""
    future = st.session_state.get("generation_future")
    if future is not None and not future.done():
        future.cancel()

    # A running provider HTTP request may not be interruptible by Future.cancel().
    # Mark it discarded so its result is never saved or rendered.
    st.session_state.generation_discard = True
    st.session_state.generation_future = None
    st.session_state.generation_meta = None


def _finish_generation_if_ready() -> bool:
    """Persist a completed background answer. Returns True when state changed."""
    future = st.session_state.get("generation_future")
    meta = st.session_state.get("generation_meta")

    if future is None or meta is None or not future.done():
        return False

    discard = st.session_state.get("generation_discard", False)
    st.session_state.generation_future = None
    st.session_state.generation_meta = None
    st.session_state.generation_discard = False

    if discard:
        return True

    try:
        answer = future.result()
        record_usage(meta["mode"], meta["model"])
    except Exception as error:
        answer = f"Unable to generate an answer: {error}"

    save_message(meta["conversation_id"], "assistant", answer)
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
    return True


@st.fragment(run_every=0.5)
def _render_generation_status() -> None:
    """Poll the background request and keep its status above the composer."""
    if _finish_generation_if_ready():
        st.rerun()

    if _generation_active():
        with st.chat_message("assistant"):
            with st.spinner("Generating answer..."):
                st.markdown("Generating answer...")


def submit_composer_prompt() -> None:
    prompt_value = st.session_state.get("composer_prompt", "").strip()

    if prompt_value:
        st.session_state.voice_transcript = ""
        queue_prompt(prompt_value)
        st.session_state.composer_prompt = ""


def submit_mobile_composer_prompt() -> None:
    """Submit the dedicated mobile composer when Enter is pressed."""
    prompt_value = st.session_state.get("mobile_composer_prompt", "").strip()

    if prompt_value:
        st.session_state.voice_transcript = ""
        queue_prompt(prompt_value)
        st.session_state.mobile_composer_prompt = ""



def _image_data_uri(path: str) -> str:
    """Return a local image as a data URI for reliable mobile centering."""
    image_path = Path(path)
    mime_type = mimetypes.guess_type(image_path.name)[0] or "image/png"
    encoded = base64.b64encode(image_path.read_bytes()).decode("ascii")
    return f"data:{mime_type};base64,{encoded}"


def authentication_page() -> None:
    st.markdown(
        """<div class="pn-auth-title"><h1>Welcome to <span>PeerNet AI</span></h1><p>Secure networking, automation, troubleshooting, and interview preparation.</p></div>""",
        unsafe_allow_html=True,
    )
    form_col, visual_col = st.columns([1, 1.05], gap="large")
    with form_col:
        with st.container(border=True):
            # Use the original high-resolution logo data in both layouts.
            # This prevents Streamlit from downscaling the PNG before browser zoom.
            login_logo_uri = _image_data_uri(LOGO_PATH)
            st.markdown(
                f"""
                <div class="pn-desktop-login-logo">
                    <img src="{login_logo_uri}" alt="PeerNet Solutions logo">
                </div>
                <div class="pn-mobile-login-logo">
                    <img src="{login_logo_uri}" alt="PeerNet Solutions logo">
                </div>
                """,
                unsafe_allow_html=True,
            )

            login_tab, register_tab, reset_tab = st.tabs(["Login", "Register", "Forgot password"])
            with login_tab:
                with st.form("login_form"):
                    email = st.text_input("Email", placeholder="name@example.com")
                    password = st.text_input("Password", type="password", placeholder="Enter your password")
                    submitted = st.form_submit_button("Login →", width="stretch")
                if submitted:
                    try:
                        sign_in(email.strip(), password)
                        st.session_state.profile = load_profile()
                        st.success("Login successful.")
                        st.rerun()
                    except Exception as error:
                        st.error(f"Unable to sign in: {error}")
                with st.expander("Resend verification email"):
                    verification_email = st.text_input("Registered email", key="verification_email")
                    if st.button(
                        "Resend verification",
                        key="resend_verification",
                        width="stretch",
                    ):
                        try:
                            resend_verification(verification_email.strip())
                            st.success("Verification email sent.")
                        except Exception as error:
                            st.error(f"Unable to resend verification: {error}")
            with register_tab:
                with st.form("register_form"):
                    full_name = st.text_input("Full name")
                    username = st.text_input("Username")
                    email = st.text_input("Email address", key="register_email")
                    password = st.text_input("Password", type="password", key="register_password")
                    confirm_password = st.text_input("Confirm password", type="password")
                    accepted = st.checkbox("I agree to the Terms and Privacy Policy")
                    submitted = st.form_submit_button("Create account", width="stretch")
                if submitted:
                    if not accepted: st.error("Please accept the Terms and Privacy Policy.")
                    elif password != confirm_password: st.error("Passwords do not match.")
                    elif len(password) < 8: st.error("Password must contain at least 8 characters.")
                    else:
                        try:
                            response = sign_up(email.strip(), password, full_name.strip(), username.strip())
                            st.success("Registration complete. Check your email and verify the account before signing in." if not getattr(response, "session", None) else "Registration complete. You can continue.")
                        except Exception as error:
                            st.error(f"Unable to register: {error}")
            with reset_tab:
                reset_email = st.text_input("Email", key="reset_email")
                if st.button(
                    "Send reset link",
                    key="send_reset_link",
                    width="stretch",
                ):
                    try:
                        send_password_reset(reset_email.strip())
                        st.success("Password-reset email sent. Follow the link in the email.")
                    except Exception as error:
                        st.error(f"Unable to send reset email: {error}")
    with visual_col:
        with st.container(border=True, key="auth_visual_card"):
            st.image(
                AI_LOGIN_IMAGE_PATH,
                width="stretch",
            )
            st.markdown(
                """
                <div class="pn-auth-image-copy">
                    <h2>Learn. Troubleshoot. Automate. Prepare.</h2>
                    <p>
                        A focused AI workspace for networking, SD-WAN, Meraki,
                        Python automation, pyATS, testing, and interview preparation.
                    </p>
                    <div class="pn-auth-pills">
                        <span>🌐 Networking</span>
                        <span>☁️ SD-WAN</span>
                        <span>📶 Meraki</span>
                        <span>🐍 Python</span>
                        <span>🧪 pyATS</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )


if not st.session_state.get("authenticated"):
    authentication_page()
    st.stop()


profile = st.session_state.get("profile") or load_profile()
user_email = st.session_state.get("user_email", "").lower()
is_admin = user_email in admin_emails()

# Premium PeerNet AI sidebar.
with st.sidebar:
    render_sidebar_profile(profile)

    if st.button(
        "✨  New Chat",
        key="side_new_chat",
        width="stretch",
    ):
        st.session_state.messages = []
        st.session_state.current_conversation_id = None
        st.session_state.pending_prompt = None
        st.session_state.active_page = "Home"
        st.rerun()

    st.markdown(
        '<div class="pn-assistant-mode-label">Assistant mode</div>',
        unsafe_allow_html=True,
    )
    selected_mode = st.selectbox(
        "Assistant mode",
        list(MODE_INSTRUCTIONS.keys()),
        key="assistant_mode_selector",
        label_visibility="collapsed",
        help="Choose how PeerNet AI should structure its answers.",
        on_change=_sync_mode_from_sidebar,
    )

    st.markdown(
        '<div class="pn-side-section-label">WORKSPACE</div>',
        unsafe_allow_html=True,
    )

    if st.button("⌂  Dashboard", key="side_dashboard", width="stretch"):
        # The button interaction already reruns Streamlit once. Updating state
        # here is visible to the page router later in this same execution.
        st.session_state.active_page = "Home"

    if st.button("◴  Chat History", key="side_history", width="stretch"):
        # The button interaction already reruns Streamlit once. Updating state
        # here is visible to the page router later in this same execution.
        st.session_state.active_page = "History"

    if st.button("☆  Favorites", key="side_favorites", width="stretch"):
        # The button interaction already reruns Streamlit once. Updating state
        # here is visible to the page router later in this same execution.
        st.session_state.active_page = "Favorites"

    if st.button("🧰  AI Tools", key="side_tools", width="stretch"):
        # The button interaction already reruns Streamlit once. Updating state
        # here is visible to the page router later in this same execution.
        st.session_state.active_page = "Tools"

    if st.button("⚙  Settings", key="side_settings", width="stretch"):
        # The button interaction already reruns Streamlit once. Updating state
        # here is visible to the page router later in this same execution.
        st.session_state.active_page = "Settings"

    recent_label = (
        "⌄  Recent Chats"
        if st.session_state.show_recent_chats
        else "›  Recent Chats"
    )
    if st.button(recent_label, key="toggle_recent_chats", width="stretch"):
        st.session_state.show_recent_chats = (
            not st.session_state.show_recent_chats
        )

    # Avoid a Supabase conversation query on every sidebar interaction.
    # Fetch recent conversations only when the user opens this section.
    if st.session_state.show_recent_chats:
        recent_conversations = list_conversations()[:4]

        if recent_conversations:
            for conversation in recent_conversations:
                title = conversation.get("title") or "Untitled conversation"

                if st.button(
                    f"💬  {title[:28]}",
                    key=f"side_recent_{conversation['id']}",
                    width="stretch",
                ):
                    messages = load_messages(conversation["id"])
                    st.session_state.current_conversation_id = conversation["id"]
                    st.session_state.messages = [
                        {"role": item["role"], "content": item["content"]}
                        for item in messages
                    ]
                    st.session_state.active_page = "Home"
        else:
            st.caption("No recent conversations yet.")

    usage_today = get_today_usage()
    usage_percent = min(
        int((usage_today / max(DAILY_FREE_LIMIT, 1)) * 100),
        100,
    )

    st.html(
        f"""
        <div class="pn-side-usage-card">
            <div class="pn-side-usage-head">
                <strong>Today's Usage</strong>
                <span>{usage_percent}%</span>
            </div>
            <div class="pn-side-progress">
                <span style="width:{usage_percent}%"></span>
            </div>
            <small>{usage_today} / {DAILY_FREE_LIMIT} requests used</small>
        </div>
        """
    )

    # Custom sidebar Theme label with explicit contrast by active theme.
    sidebar_theme_name = st.session_state.get("app_theme", "Light")

    sidebar_theme_label_colors = {
        "Light": "#0b1e49",  # dark navy
        "Dark": "#ffffff",   # white
        "Blue": "#0b2f63",   # dark navy
    }

    sidebar_theme_label_color = sidebar_theme_label_colors.get(
        sidebar_theme_name,
        "#0b1e49",
    )

    st.markdown(
        f"""
        <div class="pn-sidebar-theme-label"
             style="color:{sidebar_theme_label_color} !important;">
            Theme
        </div>
        """,
        unsafe_allow_html=True,
    )

    theme_choice = st.selectbox(
        "Theme",
        THEME_OPTIONS,
        key="sidebar_theme_selector",
        on_change=_sync_theme_from_sidebar,
        label_visibility="collapsed",
    )

    if is_admin and st.button(
        "▦  Admin",
        key="side_admin",
        width="stretch",
    ):
        st.session_state.active_page = "Admin"
        st.rerun()

    st.markdown(
        """
        <div class="pn-side-footer">
            <strong>PeerNet AI</strong>
            <span>🚀 Powered by PeerNet Solutions</span>
            <small>© 2026 PeerNet Solutions</small>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("⇥  Logout", key="side_logout", width="stretch"):
        sign_out()
        st.rerun()

selected_page = st.session_state.get("active_page", "Home")

render_topbar(profile, st.session_state.selected_model)


# Make the active Stop button as prominent as Send in every PeerNet theme.
# We target only the two Stop-button keys, so no other buttons are affected.
st.html(
    """
    <style>
    [class*="st-key-composer_stop"] button,
    [class*="st-key-mobile_composer_stop"] button {
        background: linear-gradient(135deg, #246BFD 0%, #6C3BFF 55%, #D934C8 100%) !important;
        color: #FFFFFF !important;
        border: 0 !important;
        font-weight: 800 !important;
        box-shadow: 0 8px 22px rgba(91, 70, 255, 0.28) !important;
    }

    [class*="st-key-composer_stop"] button:hover,
    [class*="st-key-mobile_composer_stop"] button:hover {
        color: #FFFFFF !important;
        filter: brightness(1.06) !important;
    }

    [class*="st-key-composer_stop"] button:focus,
    [class*="st-key-mobile_composer_stop"] button:focus,
    [class*="st-key-composer_stop"] button:active,
    [class*="st-key-mobile_composer_stop"] button:active {
        color: #FFFFFF !important;
        border: 0 !important;
    }

    /* Keep the square stop symbol clearly visible in Light, Dark and Blue. */
    [class*="st-key-composer_stop"] button p,
    [class*="st-key-mobile_composer_stop"] button p {
        color: #FFFFFF !important;
        font-size: 1.05rem !important;
        font-weight: 900 !important;
    }
    </style>
    """
)

if selected_page == "Home":
    user_name = (
        profile.get("name")
        or profile.get("full_name")
        or profile.get("username")
        or "PeerNet User"
    )
    render_hero(user_name)
    render_quick_prompts()

    # Existing messages
    for index, message in enumerate(st.session_state.messages):
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

        if message["role"] == "assistant":
            with st.container(key=f"chat_actions_{index}"):
                action_cols = st.columns(
                    [1.5, 0.75, 0.75, 6],
                    gap="small",
                    vertical_alignment="center",
                )

                with action_cols[0]:
                    if st.button(
                        "⭐ Save",
                        key=f"favorite_{index}_{hash(message['content'])}",
                        width="stretch",
                    ):
                        add_favorite("Saved AI response", message["content"])
                        st.success("Saved to Favorites.")

                with action_cols[1]:
                    if st.button(
                        "👍",
                        key=f"helpful_{index}_{hash(message['content'])}",
                        width="stretch",
                    ):
                        save_feedback(
                            st.session_state.current_conversation_id,
                            message["content"],
                            "helpful",
                        )
                        st.success("Feedback saved.")

                with action_cols[2]:
                    if st.button(
                        "👎",
                        key=f"not_helpful_{index}_{hash(message['content'])}",
                        width="stretch",
                    ):
                        save_feedback(
                            st.session_state.current_conversation_id,
                            message["content"],
                            "not_helpful",
                        )
                        st.success("Feedback saved.")

    # Start queued generation before rendering the composer so the user
    # question and "Generating answer..." always appear ABOVE the search bar.
    if st.session_state.pending_prompt and not _generation_active():
        pending = st.session_state.pending_prompt
        st.session_state.pending_prompt = None
        attachment_note = ""

        # Attachments are read from the previous composer run when available.
        queued_file = st.session_state.pop("queued_uploaded_file", None)
        queued_image_name = st.session_state.pop("queued_uploaded_image_name", None)
        queued_code_mode = st.session_state.pop("queued_code_mode", False)

        if queued_file is not None:
            try:
                raw = queued_file["bytes"]
                file_size_mb = len(raw) / (1024 * 1024)
                if file_size_mb > MAX_UPLOAD_MB:
                    raise ValueError(
                        f"File exceeds the {MAX_UPLOAD_MB} MB limit."
                    )

                # Re-create a small UploadedFile-like object is unnecessary here;
                # preserve the extracted text captured at submit time.
                attachment_text = queued_file.get("text", "")
                attachment_note += (
                    f"\n\nAttached file: {queued_file['name']}\n"
                    f"```\n{attachment_text}\n```"
                )
            except Exception:
                attachment_note += "\n\nThe attached file could not be read."

        if queued_image_name:
            attachment_note += (
                f"\n\nAn image named {queued_image_name} was attached. "
                "Multimodal image analysis requires an additional vision call."
            )

        if queued_code_mode:
            attachment_note += (
                "\n\nUse code-focused mode. Provide executable examples, "
                "validation, and concise explanations."
            )

        pending += attachment_note

        if not st.session_state.current_conversation_id:
            conversation = create_conversation(pending[:80])
            st.session_state.current_conversation_id = conversation["id"]

        conversation_id = st.session_state.current_conversation_id
        save_message(conversation_id, "user", pending)
        st.session_state.messages.append(
            {"role": "user", "content": pending}
        )

        try:
            current_usage = get_today_usage()
            if current_usage >= DAILY_FREE_LIMIT and not is_admin:
                raise RuntimeError(
                    f"Daily limit reached ({DAILY_FREE_LIMIT}). "
                    "Please try again tomorrow."
                )

            mode_for_request = selected_mode
            model_for_request = st.session_state.selected_model
            messages_for_request = [
                dict(message) for message in st.session_state.messages
            ]

            st.session_state.generation_discard = False
            st.session_state.generation_meta = {
                "conversation_id": conversation_id,
                "mode": mode_for_request,
                "model": model_for_request,
            }
            st.session_state.generation_future = _generation_executor().submit(
                generate_answer,
                mode_for_request,
                messages_for_request,
                model_for_request,
            )
        except Exception as error:
            answer = f"Unable to generate an answer: {error}"
            save_message(conversation_id, "assistant", answer)
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        st.rerun()

    # Polling card is deliberately rendered here, immediately after chat history
    # and before both desktop and mobile composers.
    _render_generation_status()

    # Desktop/tablet composer. This remains unchanged above 700 px.
    with st.container(key="composer_tools"):
        (
            plus_col,
            input_col,
            dictate_col,
            voice_col,
            model_col,
            send_col,
        ) = st.columns(
            [0.48, 8.0, 0.62, 0.62, 1.45, 0.62],
            gap="small",
            vertical_alignment="center",
        )

        with plus_col:
            with st.popover("＋", width="stretch"):
                desktop_uploaded_file = st.file_uploader(
                    "📎 Upload file",
                    type=[
                        "txt", "log", "cfg", "conf", "json", "yaml", "yml",
                        "pdf", "py", "md", "csv", "xml",
                    ],
                    key="chat_attachment",
                )

                desktop_uploaded_image = st.file_uploader(
                    "🖼️ Upload image",
                    type=["png", "jpg", "jpeg", "webp"],
                    key="chat_image",
                )

                desktop_code_mode = st.checkbox(
                    "</> Code-focused response",
                    key="chat_code_mode",
                )

        with input_col:
            desktop_prompt = st.text_input(
                "Message",
                value=st.session_state.get("voice_transcript", ""),
                placeholder="Ask PeerNet AI anything...",
                label_visibility="collapsed",
                key="composer_prompt",
                max_chars=4000,
                on_change=submit_composer_prompt,
            )

        with dictate_col:
            desktop_dictated_text = speech_to_text(
                language="en",
                start_prompt="🎙",
                stop_prompt="■",
                just_once=True,
                use_container_width=True,
                key="dictate_once",
            )

            if desktop_dictated_text:
                st.session_state.voice_transcript = desktop_dictated_text
                st.rerun()

        with voice_col:
            desktop_continuous_voice = speech_to_text(
                language="en",
                start_prompt="▶",
                stop_prompt="■",
                just_once=False,
                use_container_width=True,
                key="continuous_voice",
            )

            if desktop_continuous_voice:
                st.session_state.voice_transcript = desktop_continuous_voice
                st.rerun()

        with model_col:
            desktop_selected_model = st.selectbox(
                "Model",
                MODEL_OPTIONS,
                index=MODEL_OPTIONS.index(
                    st.session_state.selected_model
                    if st.session_state.selected_model in MODEL_OPTIONS
                    else DEFAULT_MODEL
                ),
                label_visibility="collapsed",
                key="composer_model_selector",
            )

            if desktop_selected_model != st.session_state.selected_model:
                st.session_state.selected_model = desktop_selected_model

        with send_col:
            if _generation_active():
                desktop_submitted = False
                desktop_stop = st.button(
                    "■",
                    key="composer_stop",
                    width="stretch",
                    help="Stop generating",
                )
            else:
                desktop_stop = False
                desktop_submitted = st.button(
                    "➤",
                    key="composer_send",
                    width="stretch",
                )

        if desktop_uploaded_file:
            st.caption(f"📎 {desktop_uploaded_file.name}")

        if desktop_uploaded_image:
            st.caption(f"🖼️ {desktop_uploaded_image.name}")

    # Phone-only mode control, synchronized with the sidebar selector.
    # CSS hides the entire container on tablet, laptop, and desktop.
    with st.container(key="mobile_assistant_mode"):
        st.selectbox(
            "✨ Assistant mode",
            list(MODE_INSTRUCTIONS.keys()),
            key="mobile_assistant_mode_selector",
            label_visibility="visible",
            help="Choose how PeerNet AI should structure its answers.",
            on_change=_sync_mode_from_mobile,
        )

    # Dedicated phone composer. CSS hides it on desktop and tablet.
    with st.container(key="mobile_composer"):
        mobile_prompt = st.text_input(
            "Message",
            value=st.session_state.get("voice_transcript", ""),
            placeholder="Ask PeerNet AI anything...",
            label_visibility="collapsed",
            key="mobile_composer_prompt",
            max_chars=4000,
            on_change=submit_mobile_composer_prompt,
        )

        (
            mobile_plus_col,
            mobile_dictate_col,
            mobile_voice_col,
            mobile_model_col,
            mobile_send_col,
        ) = st.columns(
            [0.55, 0.55, 0.55, 1.75, 0.62],
            gap="small",
            vertical_alignment="center",
        )

        with mobile_plus_col:
            with st.popover("＋", width="stretch"):
                mobile_uploaded_file = st.file_uploader(
                    "📎 Upload file",
                    type=[
                        "txt", "log", "cfg", "conf", "json", "yaml", "yml",
                        "pdf", "py", "md", "csv", "xml",
                    ],
                    key="mobile_chat_attachment",
                )

                mobile_uploaded_image = st.file_uploader(
                    "🖼️ Upload image",
                    type=["png", "jpg", "jpeg", "webp"],
                    key="mobile_chat_image",
                )

                mobile_code_mode = st.checkbox(
                    "</> Code-focused response",
                    key="mobile_chat_code_mode",
                )

        with mobile_dictate_col:
            mobile_dictated_text = speech_to_text(
                language="en",
                start_prompt="🎙",
                stop_prompt="■",
                just_once=True,
                use_container_width=True,
                key="mobile_dictate_once",
            )

            if mobile_dictated_text:
                st.session_state.voice_transcript = mobile_dictated_text
                st.rerun()

        with mobile_voice_col:
            mobile_continuous_voice = speech_to_text(
                language="en",
                start_prompt="▶",
                stop_prompt="■",
                just_once=False,
                use_container_width=True,
                key="mobile_continuous_voice",
            )

            if mobile_continuous_voice:
                st.session_state.voice_transcript = mobile_continuous_voice
                st.rerun()

        with mobile_model_col:
            mobile_selected_model = st.selectbox(
                "Model",
                MODEL_OPTIONS,
                index=MODEL_OPTIONS.index(
                    st.session_state.selected_model
                    if st.session_state.selected_model in MODEL_OPTIONS
                    else DEFAULT_MODEL
                ),
                label_visibility="collapsed",
                key="mobile_composer_model_selector",
            )

            if mobile_selected_model != st.session_state.selected_model:
                st.session_state.selected_model = mobile_selected_model

        with mobile_send_col:
            if _generation_active():
                mobile_submitted = False
                mobile_stop = st.button(
                    "■",
                    key="mobile_composer_stop",
                    width="stretch",
                    help="Stop generating",
                )
            else:
                mobile_stop = False
                mobile_submitted = st.button(
                    "➤",
                    key="mobile_composer_send",
                    width="stretch",
                )

        if mobile_uploaded_file:
            st.caption(f"📎 {mobile_uploaded_file.name}")

        if mobile_uploaded_image:
            st.caption(f"🖼️ {mobile_uploaded_image.name}")

    # Use whichever composer supplied an attachment or option.
    uploaded_file = mobile_uploaded_file or desktop_uploaded_file
    uploaded_image = mobile_uploaded_image or desktop_uploaded_image
    code_mode = mobile_code_mode or desktop_code_mode

    if desktop_stop or mobile_stop:
        _stop_generation()
        st.rerun()

    if desktop_submitted or mobile_submitted:
        cleaned_prompt = (
            mobile_prompt.strip()
            if mobile_submitted
            else desktop_prompt.strip()
        )

        if cleaned_prompt:
            if _generation_active():
                st.warning("Stop the current response before sending another message.")
            else:
                selected_file = mobile_uploaded_file or desktop_uploaded_file
                selected_image = mobile_uploaded_image or desktop_uploaded_image
                selected_code_mode = mobile_code_mode or desktop_code_mode

                if selected_file is not None:
                    try:
                        st.session_state.queued_uploaded_file = {
                            "name": selected_file.name,
                            "bytes": selected_file.getvalue(),
                            "text": extract_uploaded_text(selected_file),
                        }
                    except Exception:
                        st.session_state.queued_uploaded_file = {
                            "name": selected_file.name,
                            "bytes": selected_file.getvalue(),
                            "text": "",
                        }

                st.session_state.queued_uploaded_image_name = (
                    selected_image.name if selected_image is not None else None
                )
                st.session_state.queued_code_mode = selected_code_mode

                st.session_state.voice_transcript = ""
                queue_prompt(cleaned_prompt)
                st.rerun()
        else:
            st.warning("Please type or dictate a message before sending.")


elif selected_page == "History":
    st.title("Chat History")

    search_query = st.text_input(
        "Search conversations",
        placeholder="Search by conversation title...",
        key="history_search",
    )

    conversations = search_conversations(search_query)

    if not conversations:
        st.info("No matching conversations found.")

    for conversation in conversations:
        with st.expander(conversation["title"]):
            messages = load_messages(conversation["id"])

            rename_col, action_col = st.columns([3, 1])

            with rename_col:
                new_title = st.text_input(
                    "Rename conversation",
                    value=conversation["title"],
                    key=f"rename_input_{conversation['id']}",
                )

            with action_col:
                if st.button(
                    "Rename",
                    key=f"rename_history_{conversation['id']}",
                    width="stretch",
                ):
                    rename_conversation(conversation["id"], new_title)
                    st.success("Conversation renamed.")
                    st.rerun()

            for message in messages:
                st.markdown(
                    f"**{message['role'].title()}:** "
                    f"{message['content']}"
                )

            open_col, delete_col = st.columns([3, 1])

            with open_col:
                if st.button(
                    "Open conversation",
                    key=f"open_history_{conversation['id']}",
                    width="stretch",
                ):
                    st.session_state.current_conversation_id = conversation["id"]
                    st.session_state.messages = [
                        {"role": item["role"], "content": item["content"]}
                        for item in messages
                    ]
                    st.session_state.active_page = "Home"
                    st.rerun()

            with delete_col:
                if st.button(
                    "Delete",
                    key=f"delete_history_{conversation['id']}",
                    width="stretch",
                ):
                    delete_conversation(conversation["id"])
                    st.rerun()


elif selected_page == "Favorites":
    st.title("Favorites")
    favorites = list_favorites()

    if not favorites:
        st.info("No favorites saved yet.")

    for favorite in favorites:
        with st.container(border=True):
            st.subheader(favorite["title"])
            st.markdown(favorite["content"])

            if st.button(
                "Remove",
                key=f"remove_favorite_{favorite['id']}",
            ):
                delete_favorite(favorite["id"])
                st.rerun()


elif selected_page == "Tools":
    st.title("Networking Tools")
    st.caption("Choose a specialized PeerNet AI workflow.")

    tool_cols = st.columns(2)

    for index, tool_name in enumerate(NETWORK_TOOLS):
        with tool_cols[index % 2]:
            with st.container(border=True):
                st.subheader(tool_name)

                descriptions = {
                    "CLI Output Analyzer": "Analyze show-command output and identify likely issues.",
                    "Configuration Validator": "Review router or switch configuration for errors and gaps.",
                    "Route Table Analyzer": "Inspect routing entries, next hops, and reachability.",
                    "SD-WAN Troubleshooter": "Troubleshoot control, data, NAT, policy, and underlay problems.",
                    "pyATS Test Generator": "Generate pyATS AEtest validation workflows.",
                    "REST API Generator": "Create safe GET, POST, PUT, PATCH, and DELETE examples.",
                    "PRD to Test Cases": "Convert product requirements into traceable test scenarios.",
                    "Interview Practice": "Practice networking and automation interview questions.",
                }

                st.write(descriptions[tool_name])

                if st.button(
                    "Open tool",
                    key=f"tool_{index}",
                    width="stretch",
                ):
                    st.session_state.pending_prompt = (
                        f"Use the {tool_name} workflow. "
                        "Ask me for the required input and guide me step by step."
                    )
                    st.session_state.active_page = "Home"
                    st.rerun()


elif selected_page == "Settings":
    st.title("Settings")
    st.write(f"Current mode: `{selected_mode}`")
    st.write(f"Model: `{st.session_state.selected_model}`")

    st.subheader("Appearance")

    # Use our own label instead of Streamlit's native selectbox label.
    # This guarantees readable contrast in Light, Dark, and Blue themes.
    current_theme = st.session_state.get("app_theme", "Light")

    theme_label_colors = {
        # Applied identically on mobile, tablet, laptop and desktop.
        "Light": "#0b1e49",  # dark navy
        "Dark": "#ffffff",   # white / maximum contrast
        "Blue": "#0b2f63",   # dark navy
    }

    theme_label_color = theme_label_colors.get(
        current_theme,
        "#0b1e49",
    )

    st.markdown(
        f"""
        <div class="pn-settings-theme-label"
             style="color:{theme_label_color} !important;">
            Theme
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.selectbox(
        "Theme",
        THEME_OPTIONS,
        key="settings_theme_selector",
        on_change=_sync_theme_from_settings,
        label_visibility="collapsed",
    )

    st.divider()
    st.subheader("Account")

    if st.button(
        "🚪 Logout",
        key="settings_logout",
    ):
        sign_out()
        st.rerun()

    with st.form("profile_form"):
        full_name = st.text_input(
            "Full name",
            value=profile.get("full_name", ""),
        )
        username = st.text_input(
            "Username",
            value=profile.get("username", ""),
        )
        bio = st.text_area(
            "Bio",
            value=profile.get("bio", ""),
        )
        submitted = st.form_submit_button("Save profile")

    if submitted:
        try:
            profile = update_profile(
                full_name.strip(),
                username.strip(),
                bio.strip(),
            )
            st.success("Profile updated.")
        except Exception as error:
            st.error(f"Unable to update profile: {error}")

    st.subheader("Change password")

    with st.form("change_password_form"):
        new_password = st.text_input(
            "New password",
            type="password",
        )
        confirm_password = st.text_input(
            "Confirm new password",
            type="password",
        )
        password_submitted = st.form_submit_button("Update password")

    if password_submitted:
        if len(new_password) < 8:
            st.error("Password must contain at least 8 characters.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            try:
                update_password(new_password)
                st.success("Password updated.")
            except Exception as error:
                st.error(f"Unable to update password: {error}")


elif selected_page == "About":
    st.title("About PeerNet AI")
    st.markdown(
        """
        PeerNet AI is a focused workspace for networking, SD-WAN,
        Meraki, Python automation, pyATS testing, troubleshooting,
        interview preparation, and test planning.

        **Core capabilities**

        - Networking and SD-WAN explanations
        - Automation and test-code generation
        - Persistent Supabase chat history
        - Favorites and profile management
        - Secure email authentication
        """
    )


elif selected_page == "Admin":
    st.title("Admin Dashboard")
    admin_client = create_admin_client()

    if not admin_client:
        st.error(
            "SUPABASE_SERVICE_ROLE_KEY is required for the admin dashboard."
        )
    else:
        profiles_response = (
            admin_client
            .table("profiles")
            .select("id,email,full_name,username,role,created_at")
            .order("created_at", desc=True)
            .execute()
        )

        conversations_response = (
            admin_client
            .table("conversations")
            .select("id")
            .execute()
        )

        users = profiles_response.data or []
        conversations = conversations_response.data or []
        metrics = admin_metrics()

        metric_one, metric_two, metric_three, metric_four = st.columns(4)
        metric_one.metric("Registered users", metrics["users"])
        metric_two.metric("Conversations", metrics["conversations"])
        metric_three.metric("AI requests", metrics["usage_events"])
        metric_four.metric("Feedback entries", metrics["feedback"])

        st.subheader("Recent users")
        st.dataframe(users, width="stretch")


# Functional mobile navigation.
with st.container(key="mobile_nav"):
    mobile_cols = st.columns(5)

    with mobile_cols[0]:
        if st.button(
            "⌂\nHome",
            key="mobile_home",
            width="stretch",
            type="primary" if selected_page == "Home" else "secondary",
        ):
            st.session_state.active_page = "Home"
            st.rerun()

    with mobile_cols[1]:
        if st.button(
            "✦\nNew Chat",
            key="mobile_new",
            width="stretch",
        ):
            st.session_state.messages = []
            st.session_state.current_conversation_id = None
            st.session_state.pending_prompt = None
            st.session_state.active_page = "Home"
            st.rerun()

    with mobile_cols[2]:
        if st.button(
            "◷\nHistory",
            key="mobile_history",
            width="stretch",
            type="primary" if selected_page == "History" else "secondary",
        ):
            st.session_state.active_page = "History"
            st.rerun()

    with mobile_cols[3]:
        if st.button(
            "☆\nFavorites",
            key="mobile_favorites",
            width="stretch",
            type="primary" if selected_page == "Favorites" else "secondary",
        ):
            st.session_state.active_page = "Favorites"
            st.rerun()

    with mobile_cols[4]:
        if st.button(
            "⚙\nSettings",
            key="mobile_settings",
            width="stretch",
            type="primary" if selected_page == "Settings" else "secondary",
        ):
            st.session_state.active_page = "Settings"
            st.rerun()
