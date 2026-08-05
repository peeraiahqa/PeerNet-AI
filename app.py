import streamlit as st
from streamlit_mic_recorder import speech_to_text
from dotenv import load_dotenv

from ai_service import generate_answer
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

active_theme = st.session_state.get("sidebar_theme_selector", "Light")
apply_styles(active_theme)



if "voice_transcript" not in st.session_state:
    st.session_state.voice_transcript = ""

if "selected_model" not in st.session_state:
    st.session_state.selected_model = DEFAULT_MODEL


def submit_composer_prompt() -> None:
    prompt_value = st.session_state.get("composer_prompt", "").strip()

    if prompt_value:
        st.session_state.voice_transcript = ""
        queue_prompt(prompt_value)
        st.session_state.composer_prompt = ""


def authentication_page() -> None:
    st.markdown(
        """<div class="pn-auth-title"><h1>Welcome to <span>PeerNet AI</span></h1><p>Secure networking, automation, troubleshooting, and interview preparation.</p></div>""",
        unsafe_allow_html=True,
    )
    form_col, visual_col = st.columns([1, 1.05], gap="large")
    with form_col:
        with st.container(border=True):
            _, logo_center, _ = st.columns([1, 1.25, 1])
            with logo_center:
                st.image(LOGO_PATH, width=145)
            login_tab, register_tab, reset_tab = st.tabs(["Login", "Register", "Forgot password"])
            with login_tab:
                with st.form("login_form"):
                    email = st.text_input("Email", placeholder="name@example.com")
                    password = st.text_input("Password", type="password", placeholder="Enter your password")
                    submitted = st.form_submit_button("Login →", use_container_width=True)
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
                    if st.button("Resend verification", use_container_width=True):
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
                    submitted = st.form_submit_button("Create account", use_container_width=True)
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
                if st.button("Send reset link", use_container_width=True):
                    try:
                        send_password_reset(reset_email.strip())
                        st.success("Password-reset email sent. Follow the link in the email.")
                    except Exception as error:
                        st.error(f"Unable to send reset email: {error}")
    with visual_col:
        with st.container(border=True, key="auth_visual_card"):
            st.image(
                AI_LOGIN_IMAGE_PATH,
                use_container_width=True,
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
        use_container_width=True,
    ):
        st.session_state.messages = []
        st.session_state.current_conversation_id = None
        st.session_state.pending_prompt = None
        st.session_state.active_page = "Home"
        st.rerun()

    st.markdown(
        '<div class="pn-side-section-label">WORKSPACE</div>',
        unsafe_allow_html=True,
    )

    if st.button("⌂  Dashboard", key="side_dashboard", use_container_width=True):
        st.session_state.active_page = "Home"
        st.rerun()

    if st.button("◴  Chat History", key="side_history", use_container_width=True):
        st.session_state.active_page = "History"
        st.rerun()

    if st.button("☆  Favorites", key="side_favorites", use_container_width=True):
        st.session_state.active_page = "Favorites"
        st.rerun()

    if st.button("🧰  AI Tools", key="side_tools", use_container_width=True):
        st.session_state.active_page = "Tools"
        st.rerun()

    if st.button("⚙  Settings", key="side_settings", use_container_width=True):
        st.session_state.active_page = "Settings"
        st.rerun()

    if st.button("ⓘ  About", key="side_about", use_container_width=True):
        st.session_state.active_page = "About"
        st.rerun()

    with st.expander("◴  Recent Chats", expanded=False):
        recent_conversations = list_conversations()[:4]

        if recent_conversations:
            for conversation in recent_conversations:
                title = conversation.get("title") or "Untitled conversation"

                if st.button(
                    f"💬  {title[:28]}",
                    key=f"side_recent_{conversation['id']}",
                    use_container_width=True,
                ):
                    messages = load_messages(conversation["id"])
                    st.session_state.current_conversation_id = conversation["id"]
                    st.session_state.messages = [
                        {"role": item["role"], "content": item["content"]}
                        for item in messages
                    ]
                    st.session_state.active_page = "Home"
                    st.rerun()
        else:
            st.caption("No recent conversations yet.")

    with st.expander("⚡  Quick AI Tools", expanded=False):
        quick_tools = [
            ("📄 PRD → Test Plan", "Create test cases and a test plan from my PRD."),
            ("🐍 Generate Python", "Generate a Python network automation script."),
            ("🌐 Network Config", "Review and validate my network configuration."),
            ("🛡 Troubleshoot", "Help me troubleshoot a networking issue."),
        ]

        for index, (label, prompt_text) in enumerate(quick_tools):
            if st.button(
                label,
                key=f"side_quick_tool_{index}",
                use_container_width=True,
            ):
                st.session_state.pending_prompt = prompt_text
                st.session_state.active_page = "Home"
                st.rerun()

    selected_mode = st.selectbox(
        "Assistant mode",
        list(MODE_INSTRUCTIONS.keys()),
        label_visibility="collapsed",
        key="assistant_mode_selector",
    )

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

    theme_choice = st.selectbox(
        "Theme",
        ["Light", "Dark", "Blue"],
        index=0,
        key="sidebar_theme_selector",
    )

    if is_admin and st.button(
        "▦  Admin",
        key="side_admin",
        use_container_width=True,
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

    if st.button("⇥  Logout", key="side_logout", use_container_width=True):
        sign_out()
        st.rerun()

selected_page = st.session_state.get("active_page", "Home")

render_topbar(profile, st.session_state.selected_model)

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
                action_cols = st.columns([1, 1, 1, 5])

                with action_cols[0]:
                    if st.button(
                        "⭐ Save",
                        key=f"favorite_{index}_{hash(message['content'])}",
                    ):
                        add_favorite("Saved AI response", message["content"])
                        st.success("Saved to Favorites.")

                with action_cols[1]:
                    if st.button(
                        "👍",
                        key=f"helpful_{index}_{hash(message['content'])}",
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
                    ):
                        save_feedback(
                            st.session_state.current_conversation_id,
                            message["content"],
                            "not_helpful",
                        )
                        st.success("Feedback saved.")

    # Modern single-row PeerNet AI composer.
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
            with st.popover("＋", use_container_width=True):
                uploaded_file = st.file_uploader(
                    "📎 Upload file",
                    type=[
                        "txt", "log", "cfg", "conf", "json", "yaml", "yml",
                        "pdf", "py", "md", "csv", "xml",
                    ],
                    key="chat_attachment",
                )

                uploaded_image = st.file_uploader(
                    "🖼️ Upload image",
                    type=["png", "jpg", "jpeg", "webp"],
                    key="chat_image",
                )

                code_mode = st.checkbox(
                    "</> Code-focused response",
                    key="chat_code_mode",
                )

        with input_col:
            prompt = st.text_input(
                "Message",
                value=st.session_state.get("voice_transcript", ""),
                placeholder="Ask PeerNet AI anything...",
                label_visibility="collapsed",
                key="composer_prompt",
                max_chars=4000,
                on_change=submit_composer_prompt,
            )

        with dictate_col:
            dictated_text = speech_to_text(
                language="en",
                start_prompt="🎙",
                stop_prompt="■",
                just_once=True,
                use_container_width=True,
                key="dictate_once",
            )

            if dictated_text:
                st.session_state.voice_transcript = dictated_text
                st.rerun()

        with voice_col:
            continuous_voice = speech_to_text(
                language="en",
                start_prompt="▶",
                stop_prompt="■",
                just_once=False,
                use_container_width=True,
                key="continuous_voice",
            )

            if continuous_voice:
                st.session_state.voice_transcript = continuous_voice
                st.rerun()


        with model_col:
            selected_model = st.selectbox(
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

            if selected_model != st.session_state.selected_model:
                st.session_state.selected_model = selected_model

        with send_col:
            submitted = st.button(
                "➤",
                key="composer_send",
                use_container_width=True,
            )

        if uploaded_file:
            st.caption(f"📎 {uploaded_file.name}")

        if uploaded_image:
            st.caption(f"🖼️ {uploaded_image.name}")

    if submitted:
        cleaned_prompt = prompt.strip()

        if cleaned_prompt:
            st.session_state.voice_transcript = ""
            queue_prompt(cleaned_prompt)
            st.rerun()
        else:
            st.warning("Please type or dictate a message before sending.")

    if st.session_state.pending_prompt:
        pending = st.session_state.pending_prompt
        st.session_state.pending_prompt = None
        attachment_note = ""

        if uploaded_file is not None:
            try:
                raw = uploaded_file.getvalue()

                file_size_mb = len(raw) / (1024 * 1024)

                if file_size_mb > MAX_UPLOAD_MB:
                    raise ValueError(
                        f"File exceeds the {MAX_UPLOAD_MB} MB limit."
                    )

                attachment_text = extract_uploaded_text(uploaded_file)
                attachment_note += (
                    f"\n\nAttached file: {uploaded_file.name}\n"
                    f"```\n{attachment_text}\n```"
                )
            except Exception:
                attachment_note += "\n\nThe attached file could not be read."

        if uploaded_image is not None:
            attachment_note += (
                f"\n\nAn image named {uploaded_image.name} was attached. "
                "Multimodal image analysis requires an additional vision call."
            )

        if code_mode:
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

        with st.chat_message("user"):
            st.markdown(pending)

        with st.chat_message("assistant"):
            with st.spinner("Generating answer..."):
                try:
                    current_usage = get_today_usage()

                    if current_usage >= DAILY_FREE_LIMIT and not is_admin:
                        raise RuntimeError(
                            f"Daily limit reached ({DAILY_FREE_LIMIT}). "
                            "Please try again tomorrow."
                        )

                    answer = generate_answer(
                        selected_mode,
                        st.session_state.messages,
                        st.session_state.selected_model,
                    )
                    record_usage(
                        selected_mode,
                        st.session_state.selected_model,
                    )
                except Exception as error:
                    answer = f"Unable to generate an answer: {error}"

                st.markdown(answer)

        save_message(conversation_id, "assistant", answer)
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )
        st.rerun()


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
                    use_container_width=True,
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
                    use_container_width=True,
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
                    use_container_width=True,
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
                    use_container_width=True,
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
        st.dataframe(users, use_container_width=True)


# Functional mobile navigation.
with st.container(key="mobile_nav"):
    mobile_cols = st.columns(5)

    with mobile_cols[0]:
        if st.button("⌂\nHome", key="mobile_home", use_container_width=True):
            st.session_state.active_page = "Home"
            st.rerun()

    with mobile_cols[1]:
        if st.button("☵\nNew Chat", key="mobile_new", use_container_width=True):
            st.session_state.messages = []
            st.session_state.current_conversation_id = None
            st.session_state.pending_prompt = None
            st.session_state.active_page = "Home"
            st.rerun()

    with mobile_cols[2]:
        if st.button("◷\nHistory", key="mobile_history", use_container_width=True):
            st.session_state.active_page = "History"
            st.rerun()

    with mobile_cols[3]:
        if st.button("☆\nFavorites", key="mobile_favorites", use_container_width=True):
            st.session_state.active_page = "Favorites"
            st.rerun()

    with mobile_cols[4]:
        if st.button("⚙\nSettings", key="mobile_settings", use_container_width=True):
            st.session_state.active_page = "Settings"
            st.rerun()
