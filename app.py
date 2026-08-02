import streamlit as st
from dotenv import load_dotenv

from ai_service import generate_answer, get_api_key
from auth import authenticate, ensure_admin_user, logout, register_user
from components import (
    export_conversation,
    initialize_state,
    queue_prompt,
    render_hero,
    render_main_header,
    render_profile,
    render_quick_cards,
    render_status,
)
from config import (
    APP_TITLE,
    DEFAULT_MODEL,
    FAVICON_PATH,
    LOGO_PATH,
    MODE_INSTRUCTIONS,
)
from styles import apply_styles


st.set_page_config(
    page_title=APP_TITLE,
    page_icon=FAVICON_PATH,
    layout="wide",
    initial_sidebar_state="expanded",
)

load_dotenv()
apply_styles()
initialize_state()
ensure_admin_user()

if "mobile_panel" not in st.session_state:
    st.session_state.mobile_panel = "home"


# Authentication
if not st.session_state.authenticated:
    st.markdown(
        '<div class="pn-auth-page-title">'
        '<h1>Welcome to <span>PeerNet AI</span></h1>'
        '<p>Sign in or create your account to continue.</p>'
        '</div>',
        unsafe_allow_html=True,
    )

    form_col, visual_col = st.columns([1, 1], gap="large")

    with form_col:
        with st.container(border=True):
            logo_left, logo_center, logo_right = st.columns([1, 1.2, 1])
            with logo_center:
                st.image(LOGO_PATH, width=125)

            login_tab, register_tab = st.tabs(["Login", "Register"])

            with login_tab:
                st.markdown(
                    '<div class="pn-tab-heading">Welcome back</div>'
                    '<div class="pn-tab-caption">'
                    'Sign in to continue to PeerNet AI.'
                    '</div>',
                    unsafe_allow_html=True,
                )

                with st.form("login_form"):
                    login_username = st.text_input(
                        "Username",
                        placeholder="Enter your username",
                    )
                    login_password = st.text_input(
                        "Password",
                        type="password",
                        placeholder="Enter your password",
                    )
                    st.checkbox("Remember me")
                    login_submitted = st.form_submit_button(
                        "Login →",
                        use_container_width=True,
                    )

                if login_submitted:
                    valid, display_name = authenticate(
                        login_username,
                        login_password,
                    )

                    if valid:
                        st.session_state.authenticated = True
                        st.session_state.username = login_username.strip()
                        st.session_state.display_name = display_name
                        st.rerun()
                    else:
                        st.error("Incorrect username or password.")

            with register_tab:
                st.markdown(
                    '<div class="pn-tab-heading">Create your account</div>'
                    '<div class="pn-tab-caption">'
                    'Join PeerNet AI and start learning today.'
                    '</div>',
                    unsafe_allow_html=True,
                )

                with st.form("register_form"):
                    full_name = st.text_input(
                        "Full name",
                        placeholder="Enter your full name",
                    )
                    register_username = st.text_input(
                        "Username",
                        placeholder="Choose a username",
                    )
                    email = st.text_input(
                        "Email",
                        placeholder="Enter your email",
                    )
                    register_password = st.text_input(
                        "Password",
                        type="password",
                        placeholder="Use at least 8 characters",
                    )
                    confirm_password = st.text_input(
                        "Confirm password",
                        type="password",
                        placeholder="Re-enter your password",
                    )
                    accept_terms = st.checkbox(
                        "I agree to the Terms & Conditions"
                    )
                    register_submitted = st.form_submit_button(
                        "Create Account",
                        use_container_width=True,
                    )

                if register_submitted:
                    if not accept_terms:
                        st.error("Please accept the Terms & Conditions.")
                    else:
                        success, message = register_user(
                            full_name,
                            register_username,
                            email,
                            register_password,
                            confirm_password,
                        )

                        if success:
                            st.success(message)
                        else:
                            st.error(message)

    with visual_col:
        with st.container(border=True):
            st.markdown(
                '<div class="pn-login-visual-top">'
                '<div class="pn-login-badge">PeerNet Solutions</div>'
                '</div>',
                unsafe_allow_html=True,
            )

            image_left, image_center, image_right = st.columns([1, 1.5, 1])

            with image_center:
                st.image(LOGO_PATH, width=230)

            st.markdown(
                '<div class="pn-login-visual-content">'
                '<h2>Learn. Troubleshoot.<br>Automate. Prepare.</h2>'
                '<p>'
                'A focused AI workspace for networking, SD-WAN, Meraki, '
                'Python automation, pyATS, testing, and interview preparation.'
                '</p>'
                '<div class="pn-login-feature-grid">'
                '<span>🌐 Networking</span>'
                '<span>☁️ SD-WAN</span>'
                '<span>🐍 Python</span>'
                '<span>🧪 pyATS</span>'
                '</div>'
                '</div>',
                unsafe_allow_html=True,
            )

    st.stop()


api_key = get_api_key()


# Sidebar
with st.sidebar:
    render_profile()

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    if st.button("💬 New Chat", use_container_width=True):
        st.session_state.messages = []
        st.session_state.pending_prompt = None
        st.rerun()

    with st.expander("🕘 Chat History"):
        if not st.session_state.messages:
            st.caption("No conversation yet")
        else:
            for message in st.session_state.messages[-6:]:
                role = "You" if message["role"] == "user" else "PeerNet AI"
                preview = message["content"].replace("\n", " ")[:80]
                st.markdown(f"**{role}:** {preview}...")

    st.button("⭐ Favorites", use_container_width=True, disabled=True)
    st.button("ℹ️ About", use_container_width=True, disabled=True)

    with st.expander("⚙️ Settings", expanded=True):
        selected_mode = st.selectbox(
            "Assistant mode",
            list(MODE_INSTRUCTIONS.keys()),
            key="sidebar_mode_selector",
        )
        st.write(f"Model: `{DEFAULT_MODEL}`")

    with st.expander("🔎 Search conversation"):
        search_text = st.text_input(
            "Search messages",
            placeholder="OSPF, SD-WAN, Python...",
            label_visibility="collapsed",
        )

        if search_text:
            matches = [
                message
                for message in st.session_state.messages
                if search_text.lower() in message["content"].lower()
            ]

            st.caption(f"{len(matches)} result(s)")

            for match in matches[:5]:
                preview = match["content"].replace("\n", " ")[:90]
                st.markdown(f"- {preview}...")

    if st.session_state.messages:
        st.download_button(
            "⬇️ Download Chat",
            data=export_conversation(st.session_state.messages),
            file_name="peernet_ai_conversation.txt",
            mime="text/plain",
            use_container_width=True,
        )

    if st.button("🚪 Logout", use_container_width=True):
        logout()


# Dashboard header
top_left, top_right = st.columns([5, 1])

with top_left:
    render_main_header()

with top_right:
    st.markdown(
        f"<div style='text-align:right;padding-top:.25rem;'>"
        f"<span class='pn-model-pill'>✦ {DEFAULT_MODEL}</span>"
        f"</div>",
        unsafe_allow_html=True,
    )


render_hero()

if not st.session_state.messages:
    render_quick_cards()


# Mobile navigation panels
if st.session_state.mobile_panel == "history":
    st.subheader("Chat History")

    if not st.session_state.messages:
        st.info("No conversation history yet.")
    else:
        for index, message in enumerate(st.session_state.messages[-12:], start=1):
            role = "You" if message["role"] == "user" else "PeerNet AI"
            with st.expander(f"{index}. {role}"):
                st.markdown(message["content"])

elif st.session_state.mobile_panel == "favorites":
    st.subheader("Favorites")
    st.info(
        "Favorites are ready for the next version. "
        "You will be able to save useful prompts and answers here."
    )

elif st.session_state.mobile_panel == "settings":
    st.subheader("Settings")

    mode_options = list(MODE_INSTRUCTIONS.keys())

    # Use one unique widget key and keep the selected value in session state.
    if "mobile_selected_mode" not in st.session_state:
        st.session_state.mobile_selected_mode = selected_mode

    mobile_mode = st.selectbox(
        "Assistant mode",
        mode_options,
        index=mode_options.index(st.session_state.mobile_selected_mode),
        key="mobile_settings_mode_selector",
    )

    st.session_state.mobile_selected_mode = mobile_mode
    selected_mode = mobile_mode

    st.write(f"Model: `{DEFAULT_MODEL}`")

    if api_key:
        st.success("OpenAI connection is configured.")
    else:
        st.warning("OPENAI_API_KEY is not configured.")


# Conversation display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# One normal functional chat input.
# It is intentionally not fixed or overlaid, so clicking and typing work
# reliably in Safari, Chrome, Edge, Android, iPhone, tablet, and laptop.
prompt = st.chat_input(
    "Ask PeerNet AI anything... e.g. Explain OSPF, troubleshoot SD-WAN, or create Python code",
    key="main_chat_input",
)

if prompt:
    queue_prompt(prompt)
    st.rerun()


# Prompt processing
if st.session_state.pending_prompt:
    pending = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

    st.session_state.messages.append(
        {"role": "user", "content": pending}
    )

    with st.chat_message("user"):
        st.markdown(pending)

    with st.chat_message("assistant"):
        with st.spinner("Generating answer..."):
            if not api_key:
                answer = (
                    "The OpenAI API key is not configured. Add "
                    "`OPENAI_API_KEY` to your `.env` file or Streamlit Secrets."
                )
            else:
                try:
                    answer = generate_answer(
                        api_key=api_key,
                        mode=selected_mode,
                        messages=st.session_state.messages,
                    )
                except Exception as error:
                    answer = f"Unable to generate an answer: {error}"

            st.markdown(answer)
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )


render_status(api_key, selected_mode, DEFAULT_MODEL)


# Native Streamlit mobile navigation.
# Native buttons are used instead of HTML links so every tap is functional.
with st.container(key="mobile_nav"):
    nav_columns = st.columns(5)

    with nav_columns[0]:
        if st.button("🏠\nHome", key="mobile_home", use_container_width=True):
            st.session_state.mobile_panel = "home"
            st.rerun()

    with nav_columns[1]:
        if st.button("💬\nNew Chat", key="mobile_new_chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.pending_prompt = None
            st.session_state.mobile_panel = "home"
            st.rerun()

    with nav_columns[2]:
        if st.button("🕘\nHistory", key="mobile_history", use_container_width=True):
            st.session_state.mobile_panel = "history"
            st.rerun()

    with nav_columns[3]:
        if st.button("⭐\nFavorites", key="mobile_favorites", use_container_width=True):
            st.session_state.mobile_panel = "favorites"
            st.rerun()

    with nav_columns[4]:
        if st.button("⚙️\nSettings", key="mobile_settings", use_container_width=True):
            st.session_state.mobile_panel = "settings"
            st.rerun()
