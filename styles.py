import streamlit as st


def apply_styles() -> None:
    st.markdown(
        """
<style>
:root {
    --pn-navy: #07182c;
    --pn-navy-2: #132f55;
    --pn-blue: #0b78e3;
    --pn-cyan: #16a9f5;
    --pn-teal: #18c7b3;
    --pn-text: #13213d;
    --pn-muted: #6a7890;
    --pn-line: rgba(11,120,227,.17);
    --pn-shadow: 0 18px 55px rgba(7,24,44,.10);
}

html, body, [class*="css"] {
    font-family: Inter, "Segoe UI", Arial, sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 88% 3%, rgba(22,169,245,.12), transparent 24%),
        linear-gradient(180deg,#f9fcff 0%,#eef6fc 100%);
}

.block-container {
    width: min(100%, 1450px);
    max-width: 1450px;
    margin: 0 auto;
    padding: .75rem 2rem 8rem;
}

/* Streamlit chrome */
header[data-testid="stHeader"] {
    background: rgba(255,255,255,.76);
    backdrop-filter: blur(14px);
    border-bottom: 1px solid rgba(11,120,227,.08);
}

[data-testid="stSidebar"] {
    width: 300px;
    min-width: 300px;
    max-width: 300px;
    background:
        radial-gradient(circle at 28% 0%,rgba(22,169,245,.18),transparent 35%),
        linear-gradient(180deg,#eef7ff 0%,#fbfdff 100%);
    border-right: 1px solid var(--pn-line);
}

[data-testid="stSidebar"] > div:first-child {
    width: 300px;
}

[data-testid="stSidebar"] [data-testid="stImage"] {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 auto !important;
    padding: 0;
}

[data-testid="stSidebar"] img {
    display: block;
    margin: 0 auto !important;
    object-fit: contain;
    filter: drop-shadow(0 10px 20px rgba(11,120,227,.20));
}

/* Authentication */

.pn-auth-page-title {
    max-width: 780px;
    margin: 0 auto 1.1rem;
    text-align: center;
}

.pn-auth-page-title h1 {
    margin: 0;
    color: var(--pn-text);
    font-size: clamp(2rem, 4vw, 3.1rem);
    font-weight: 900;
    letter-spacing: -.045em;
}

.pn-auth-page-title h1 span {
    background: linear-gradient(
        90deg,
        var(--pn-blue),
        var(--pn-cyan),
        var(--pn-teal)
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.pn-auth-page-title p {
    margin: .45rem 0 0;
    color: var(--pn-muted);
}

.pn-tab-heading {
    margin-top: .35rem;
    color: var(--pn-text);
    font-size: 1.22rem;
    font-weight: 850;
}

.pn-tab-caption {
    margin: .15rem 0 .85rem;
    color: var(--pn-muted);
    font-size: .92rem;
}

.pn-login-visual-top {
    display: flex;
    justify-content: center;
    margin-bottom: .6rem;
}

.pn-login-badge {
    display: inline-flex;
    padding: .45rem .8rem;
    border: 1px solid var(--pn-line);
    border-radius: 999px;
    background: rgba(255,255,255,.78);
    color: var(--pn-blue);
    font-size: .82rem;
    font-weight: 800;
}

.pn-login-visual-content {
    max-width: 520px;
    margin: .7rem auto 0;
    padding: 0 1.2rem 1.2rem;
    text-align: center;
}

.pn-login-visual-content h2 {
    margin: 0;
    color: var(--pn-text);
    font-size: clamp(1.7rem, 3vw, 2.5rem);
    line-height: 1.16;
    font-weight: 900;
    letter-spacing: -.035em;
}

.pn-login-visual-content p {
    max-width: 470px;
    margin: .85rem auto 0;
    color: var(--pn-muted);
    line-height: 1.65;
}

.pn-login-feature-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: .65rem;
    margin-top: 1.15rem;
}

.pn-login-feature-grid span {
    padding: .62rem .75rem;
    border: 1px solid var(--pn-line);
    border-radius: 16px;
    background: rgba(255,255,255,.80);
    color: var(--pn-text);
    font-size: .86rem;
    font-weight: 750;
    box-shadow: 0 8px 20px rgba(7,24,44,.05);
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--pn-line) !important;
    border-radius: 28px !important;
    background:
        radial-gradient(
            circle at 50% 18%,
            rgba(22,169,245,.11),
            transparent 36%
        ),
        rgba(255,255,255,.90) !important;
    box-shadow: var(--pn-shadow);
}

div[data-testid="stTabs"] button {
    min-height: 48px;
    border-radius: 15px 15px 0 0;
    font-weight: 800;
}

div[data-testid="stForm"] {
    padding: 1rem;
    border: 1px solid var(--pn-line);
    border-radius: 22px;
    background: rgba(248,251,255,.88);
}

/* Sidebar profile */
.pn-profile {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: .55rem;
    margin: .35rem auto 1.15rem;
    padding: 0;
    text-align: center;
}

.pn-profile-no-avatar {
    margin-top: .3rem;
}
.pn-member {
    width: 100%;
    margin: .1rem 0 0;
    text-align: center;
    font-weight: 850;
    color: var(--pn-text);
    font-size: 1.08rem;
    line-height: 1.2;
}

.pn-online,
.pn-premium {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: .35rem;
    margin: 0;
    border-radius: 999px;
    font-size: .80rem;
    font-weight: 750;
    line-height: 1;
}

.pn-online {
    padding: .42rem .78rem;
    background: #e7fbee;
    color: #138a4a;
}

.pn-premium {
    padding: .42rem .78rem;
    background: #e6f2ff;
    color: var(--pn-blue);
}

.pn-online-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #22bd66;
}

/* Header */
.pn-topline {
    display:flex;
    align-items:center;
    gap:.8rem;
    margin-bottom:.8rem;
}

.pn-bot {
    display:grid;
    place-items:center;
    width:48px;
    height:48px;
    border-radius:50%;
    background:linear-gradient(145deg,var(--pn-blue),var(--pn-cyan));
    color:white;
    font-size:1.3rem;
    box-shadow:0 10px 24px rgba(11,120,227,.22);
}

.pn-welcome-small {
    color:var(--pn-muted);
    font-size:.95rem;
    line-height:1.1;
}

.pn-welcome-name {
    color:var(--pn-text);
    font-weight:850;
    font-size:1.35rem;
    line-height:1.15;
}

.pn-model-pill {
    display:inline-block;
    padding:.56rem .9rem;
    border:1px solid var(--pn-line);
    border-radius:999px;
    background:rgba(255,255,255,.84);
    color:var(--pn-text);
    font-weight:760;
    box-shadow:0 8px 22px rgba(7,24,44,.06);
}

/* Hero */
.pn-hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem 1.8rem 1.55rem;
    border: 1px solid var(--pn-line);
    border-radius: 30px;
    background:
        radial-gradient(circle at 50% 10%, rgba(22,169,245,.13), transparent 34%),
        linear-gradient(135deg, rgba(255,255,255,.92), rgba(236,247,255,.86));
    box-shadow: var(--pn-shadow);
    text-align: center;
    overflow: hidden;
}

.pn-title {
    width: 100%;
    margin: 0;
    text-align: center;
    font-size: clamp(3rem, 6vw, 5.25rem);
    line-height: 1;
    letter-spacing: -.055em;
    font-weight: 900;
    color: var(--pn-text);
}

.pn-title span {
    background:linear-gradient(90deg,var(--pn-blue),var(--pn-cyan),var(--pn-teal));
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
}

.pn-subtitle {
    width: 100%;
    max-width: 760px;
    margin: .9rem auto 0;
    padding: 0;
    text-align: center;
    color: var(--pn-muted);
    font-size: 1.08rem;
    line-height: 1.7;
}

.pn-subtitle-line {
    display: block;
    width: 100%;
    text-align: center;
}

.pn-chip-row {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: .65rem;
    margin: 1.25rem auto 0;
    text-align: center;
}

.pn-chip {
    padding:.56rem .92rem;
    border:1px solid var(--pn-line);
    border-radius:999px;
    background:rgba(255,255,255,.92);
    color:var(--pn-text);
    font-size:.86rem;
    font-weight:760;
    box-shadow:0 8px 22px rgba(7,24,44,.06);
}

/* Cards */
.pn-question-title {
    text-align:center;
    color:var(--pn-text);
    font-weight:850;
    margin:1.25rem 0 1rem;
}

.pn-card {
    min-height:165px;
    padding:1rem;
    border:1px solid rgba(11,120,227,.12);
    border-radius:22px;
    box-shadow:0 12px 30px rgba(7,24,44,.06);
    transition:transform .2s ease,box-shadow .2s ease;
}

.pn-card:hover {
    transform:translateY(-4px);
    box-shadow:0 16px 34px rgba(7,24,44,.11);
}

.pn-card-icon {
    width:44px;
    height:44px;
    display:grid;
    place-items:center;
    margin-bottom:.75rem;
    border-radius:50%;
    background:rgba(255,255,255,.8);
    font-size:1.22rem;
}

.pn-card-title {
    color:var(--pn-text);
    font-weight:850;
    font-size:.95rem;
    line-height:1.42;
}

/* Status */
.pn-status {
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:1rem;
    flex-wrap:wrap;
    margin-top:1rem;
    padding:.9rem 1rem;
    border:1px solid var(--pn-line);
    border-radius:18px;
    background:rgba(255,255,255,.80);
    color:var(--pn-muted);
    font-size:.85rem;
}

.pn-status-live {
    color:var(--pn-blue);
    font-weight:850;
}

/* Streamlit widgets */
div[data-testid="stButton"] > button,
div[data-testid="stDownloadButton"] > button {
    min-height:45px;
    border-radius:16px;
    border:1px solid var(--pn-line);
    font-weight:760;
}

div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] > div > div {
    border-radius:16px;
}

div[data-testid="stChatMessage"] {
    border:1px solid rgba(11,120,227,.10);
    border-radius:20px;
    background:rgba(255,255,255,.78);
    box-shadow:0 8px 22px rgba(7,24,44,.05);
}

/* One normal functional dark prompt bar */

[data-testid="stChatInput"] {
    position: relative !important;
    left: auto !important;
    right: auto !important;
    bottom: auto !important;
    z-index: 10;
    width: 100%;
    margin: 1.2rem 0 1rem;
    padding: 4px;
    border-radius: 30px;
    background:
        linear-gradient(
            90deg,
            var(--pn-cyan),
            var(--pn-blue),
            var(--pn-cyan)
        );
    box-shadow: 0 16px 42px rgba(11,120,227,.28);
}

[data-testid="stChatInput"] > div {
    min-height: 64px !important;
    border: none !important;
    border-radius: 26px !important;
    background:
        linear-gradient(
            135deg,
            var(--pn-navy-2),
            var(--pn-navy)
        ) !important;
}

[data-testid="stChatInput"] textarea {
    color: white !important;
    caret-color: white !important;
    font-size: 1rem !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #c2cfdf !important;
}

[data-testid="stChatInput"] button {
    width: 52px !important;
    height: 52px !important;
    min-width: 52px !important;
    border-radius: 50% !important;
    border: 2px solid #2ba9ff !important;
    background:
        radial-gradient(
            circle at 35% 30%,
            #174c90,
            #07182c 72%
        ) !important;
    color: white !important;
    box-shadow:
        0 0 0 5px rgba(43,169,255,.10),
        0 0 25px rgba(43,169,255,.85) !important;
}

/* Native mobile navigation is hidden on desktop. */
.st-key-mobile_nav {
    display: none;
}

@media (max-width:1100px) {
    .block-container {
        width: 100%;
        max-width: 100%;
        padding-left: 1.25rem;
        padding-right: 1.25rem;
    }

    [data-testid="stSidebar"] {
        width: 280px;
        min-width: 280px;
        max-width: 280px;
    }

    [data-testid="stSidebar"] > div:first-child {
        width: 280px;
    }

    .pn-card {
        min-height: 150px;
        padding: .9rem;
    }
}

@media (max-width:900px) {
    .block-container {
        width: 100%;
        max-width: 100%;
        padding: .7rem 1rem 2rem;
    }

    [data-testid="stSidebar"],
    [data-testid="stSidebar"] > div:first-child {
        width: initial;
        min-width: initial;
        max-width: initial;
    }

    .pn-auth-page-title {
        margin-bottom: .8rem;
    }

    .pn-login-visual-content {
        padding-bottom: .8rem;
    }

    .pn-auth-visual {
        min-height: 300px;
    }

    .pn-hero {
        padding: 1.4rem 1rem;
        border-radius: 24px;
    }

    .pn-title {
        font-size: 3rem;
    }
}

@media (max-width:700px) {
    .block-container {
        padding:
            .6rem
            .7rem
            calc(12rem + env(safe-area-inset-bottom));
    }

    .pn-auth-shell {
        margin-top: 1vh;
        padding: .8rem;
        border-radius: 24px;
    }

    .pn-auth-heading {
        font-size: 1.95rem;
    }

    .pn-auth-visual {
        min-height: 220px;
    }

    .pn-title {
        font-size: 2.45rem;
    }

    .pn-subtitle {
        font-size: .94rem;
    }

    .pn-chip-row {
        gap: .4rem;
    }

    .pn-chip {
        font-size: .76rem;
        padding: .45rem .64rem;
    }

    /*
    Functional chat input fixed directly above the bottom menu.
    */
    [data-testid="stChatInput"] {
        position: fixed !important;
        left: 10px !important;
        right: 10px !important;
        bottom: calc(76px + env(safe-area-inset-bottom)) !important;
        z-index: 1200 !important;
        width: auto !important;
        margin: 0 !important;
        border-radius: 25px;
    }

    [data-testid="stChatInput"] > div {
        min-height: 58px !important;
        border-radius: 21px !important;
    }

    [data-testid="stChatInput"] textarea {
        font-size: .92rem !important;
        line-height: 1.35 !important;
    }

    [data-testid="stChatInput"] button {
        width: 46px !important;
        height: 46px !important;
        min-width: 46px !important;
    }

    /*
    Real Streamlit buttons forced into one horizontal bottom row.
    */
    .st-key-mobile_nav {
        display: block !important;
        position: fixed !important;
        left: 0 !important;
        right: 0 !important;
        bottom: 0 !important;
        z-index: 1100 !important;
        margin: 0 !important;
        padding:
            .42rem
            .3rem
            calc(.42rem + env(safe-area-inset-bottom)) !important;
        border-top: 1px solid var(--pn-line);
        border-radius: 0 !important;
        background: rgba(255,255,255,.98) !important;
        box-shadow: 0 -8px 28px rgba(7,24,44,.10);
        backdrop-filter: blur(14px);
    }

    .st-key-mobile_nav [data-testid="stHorizontalBlock"] {
        display: grid !important;
        grid-template-columns: repeat(5, minmax(0, 1fr)) !important;
        gap: .2rem !important;
        align-items: stretch !important;
    }

    .st-key-mobile_nav [data-testid="column"] {
        width: 100% !important;
        min-width: 0 !important;
        flex: none !important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] {
        width: 100% !important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button {
        width: 100% !important;
        min-height: 58px !important;
        padding: .25rem .05rem !important;
        border: 0 !important;
        border-radius: 12px !important;
        background: transparent !important;
        color: var(--pn-muted) !important;
        font-size: .64rem !important;
        line-height: 1.15 !important;
        white-space: pre-line !important;
        box-shadow: none !important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button:hover,
    .st-key-mobile_nav div[data-testid="stButton"] > button:active,
    .st-key-mobile_nav div[data-testid="stButton"] > button:focus {
        background: #eaf4ff !important;
        color: var(--pn-blue) !important;
        box-shadow: none !important;
    }

    .pn-status {
        margin-bottom: 1rem;
    }
}
</style>
        """,
        unsafe_allow_html=True,
    )
