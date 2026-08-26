import streamlit as st


def _apply_base_styles() -> None:
    st.html(
        """
<style>
:root {
    --navy:#06172f;
    --navy2:#0c2a52;
    --blue:#0a75f5;
    --cyan:#13b9ff;
    --purple:#6844f5;
    --pink:#db43d0;
    --green:#19bd66;
    --text:#0b1e49;
    --muted:#647495;
    --line:rgba(19,116,241,.18);
    --shadow:0 18px 50px rgba(31,83,157,.12);
}

html, body, [class*="css"] {
    font-family:Inter,"Segoe UI",Arial,sans-serif;
}

.stApp {
    color:var(--text);
    background:
        radial-gradient(circle at 96% 0%,rgba(19,185,255,.11),transparent 24%),
        linear-gradient(180deg,#fbfdff 0%,#eef7ff 100%);
}

.block-container {
    width:min(100%,1450px);
    max-width:1450px;
    padding:.45rem 1.15rem 1.5rem;
}

/* STREAMLIT CHROME */
header[data-testid="stHeader"] {
    height:2.6rem;
    background:rgba(255,255,255,.76);
    backdrop-filter:blur(14px);
}

/* SIDEBAR */
[data-testid="stSidebar"] {
    width:240px!important;
    min-width:240px!important;
    max-width:240px!important;
    border-right:1px solid var(--line);
    background:
        radial-gradient(circle at 25% 0%,rgba(19,185,255,.13),transparent 25%),
        linear-gradient(180deg,#f8fbff,#fff);
}

[data-testid="stSidebar"] > div:first-child {
    width:240px!important;
}

[data-testid="stSidebar"] [data-testid="stImage"] {
    display:flex;
    justify-content:center;
    margin:.15rem auto 0;
}

[data-testid="stSidebar"] img {
    display:block;
    margin:0 auto!important;
    filter:drop-shadow(0 8px 20px rgba(12,99,231,.20));
}

.pn-sidebar-profile {
    display:flex;
    flex-direction:column;
    align-items:center;
    margin:.15rem 0 .9rem;
    text-align:center;
}

.pn-side-avatar {
    position:relative;
    width:46px;
    height:46px;
    display:grid;
    place-items:center;
    margin:.15rem auto .35rem;
    border-radius:50%;
    color:#fff;
    font-size:1.05rem;
    font-weight:900;
    text-transform:uppercase;
    background:linear-gradient(145deg,#0d77ef,#1ec4bd);
    box-shadow:0 9px 22px rgba(13,119,239,.22);
}

.pn-side-avatar span {
    position:absolute;
    right:-1px;
    bottom:1px;
    width:11px;
    height:11px;
    border:2px solid #fff;
    border-radius:50%;
    background:#20c36b;
}

.pn-side-name {
    color:var(--text);
    font-size:.94rem;
    font-weight:900;
}

.pn-side-online {
    display:flex;
    align-items:center;
    gap:.28rem;
    margin-top:.08rem;
    color:#238859;
    font-size:.65rem;
    font-weight:750;
}

.pn-side-online i,
.pn-welcome-copy span i,
.pn-connected i {
    width:7px;
    height:7px;
    display:inline-block;
    border-radius:50%;
    background:#1bc46c;
}

.pn-side-premium {
    margin-top:.52rem;
    padding:.32rem .65rem;
    border-radius:999px;
    color:#7342df;
    font-size:.68rem;
    font-weight:850;
    background:#f0eaff;
}

[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    min-height:40px;
    justify-content:flex-start;
    padding:.35rem .7rem;
    border:0;
    border-radius:11px;
    color:#26395c;
    background:transparent;
    box-shadow:none;
    font-size:.78rem;
    font-weight:750;
}

[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover,
[data-testid="stSidebar"] div[data-testid="stButton"] > button:focus {
    color:#0874ed;
    background:#e7f2ff;
}

[data-testid="stSidebar"] .st-key-side_home button {
    color:#0874ed!important;
    background:#e3efff!important;
}

.pn-mode-label {
    margin:.8rem .1rem .35rem;
    color:#65738f;
    font-size:.6rem;
    font-weight:850;
    letter-spacing:.04em;
}

[data-testid="stSidebar"] div[data-testid="stSelectbox"] > div > div {
    min-height:39px;
    border:1px solid var(--line);
    border-radius:11px;
    background:#fff;
    font-size:.74rem;
}

.pn-sidebar-spacer {
    height:1.4rem;
}

[data-testid="stSidebar"] .st-key-side_logout button {
    justify-content:center!important;
    color:#f04450!important;
    border:1px solid #ff9da5!important;
    background:#fff8f8!important;
}

/* TOP BAR */
.pn-topbar {
    display:flex;
    align-items:center;
    justify-content:space-between;
    min-height:56px;
    margin-bottom:.45rem;
    padding:0 .35rem;
}

.pn-welcome {
    display:flex;
    align-items:center;
    gap:.62rem;
}

.pn-welcome-no-avatar {
    gap:0;
    padding-left:.1rem;
}

.pn-avatar {
    width:40px;
    height:40px;
    display:grid;
    place-items:center;
    border-radius:50%;
    color:#fff;
    font-size:.75rem;
    font-weight:900;
    background:linear-gradient(145deg,#146eea,#0fb8d1);
    box-shadow:0 8px 20px rgba(20,110,234,.22);
}

.pn-welcome-copy small {
    display:block;
    color:#405273;
    font-size:.69rem;
    line-height:1;
}

.pn-welcome-copy strong {
    display:block;
    margin-top:.12rem;
    color:var(--text);
    font-size:1.05rem;
    line-height:1.05;
}

.pn-top-actions {
    display:flex;
    align-items:center;
    gap:.55rem;
}

.pn-model,
.pn-round {
    display:grid;
    place-items:center;
    border:1px solid var(--line);
    color:var(--text);
    background:#fff;
    box-shadow:0 6px 18px rgba(34,86,160,.07);
}

.pn-model {
    min-height:38px;
    padding:0 .9rem;
    border-radius:999px;
    font-size:.72rem;
    font-weight:850;
}

.pn-round {
    width:38px;
    height:38px;
    border-radius:50%;
}

/* AUTHENTICATION - preserve the approved login */
[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card) {
    align-items:stretch!important;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card) > [data-testid="column"] {
    display:flex;
    flex-direction:column;
}

.pn-auth-title {
    max-width:900px;
    margin:0 auto .8rem;
    text-align:center;
}

.pn-auth-title h1 {
    margin:0;
    color:var(--text);
    font-size:clamp(2.2rem,4vw,3.3rem);
    font-weight:950;
    letter-spacing:-.045em;
}

.pn-auth-title h1 span {
    background:linear-gradient(90deg,var(--blue),var(--purple),var(--cyan));
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.pn-auth-title p {
    color:var(--muted);
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border:1px solid rgba(10,117,245,.22)!important;
    border-radius:24px!important;
    background:rgba(255,255,255,.98)!important;
    box-shadow:0 15px 42px rgba(31,98,190,.12)!important;
}

div[data-testid="stTabs"] button {
    min-height:47px;
    border-radius:13px 13px 0 0;
    font-weight:850;
}

div[data-testid="stForm"] {
    padding:1rem;
    border:1px solid rgba(10,117,245,.12);
    border-radius:18px;
    background:#fff;
}

div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-testid="stSelectbox"] > div > div {
    border-radius:13px!important;
    background:#fff!important;
}

div[data-testid="stFormSubmitButton"] > button {
    min-height:48px;
    border:0!important;
    color:#fff!important;
    background:linear-gradient(90deg,#0876f9,#6f40f4,#e43cbd)!important;
    box-shadow:0 10px 25px rgba(111,64,244,.24)!important;
}

/* HERO */
.pn-hero {
    position:relative;
    overflow:hidden;
    display:flex;
    flex-direction:column;
    align-items:center;
    min-height:272px;
    padding:1.35rem 1.3rem 1.05rem;
    border:1px solid var(--line);
    border-radius:24px;
    background:
        radial-gradient(circle at 17% 20%,rgba(123,74,245,.05),transparent 20%),
        linear-gradient(135deg,#fff,#f0f8ff);
    box-shadow:var(--shadow);
    text-align:center;
}

.pn-network-decoration {
    position:absolute;
    right:2.5%;
    top:8%;
    width:190px;
    height:175px;
    opacity:.34;
    pointer-events:none;
}

.pn-network-decoration i {
    position:absolute;
    width:8px;
    height:8px;
    border-radius:50%;
    background:#8bc5ff;
}

.pn-network-decoration .n1{left:20px;top:30px}
.pn-network-decoration .n2{left:78px;top:12px}
.pn-network-decoration .n3{left:144px;top:30px}
.pn-network-decoration .n4{left:55px;top:92px}
.pn-network-decoration .n5{left:122px;top:84px}
.pn-network-decoration .n6{left:160px;top:142px}

.pn-network-decoration b {
    position:absolute;
    height:1px;
    transform-origin:left center;
    background:#8bc5ff;
}

.pn-network-decoration .e1{left:25px;top:34px;width:57px;transform:rotate(-18deg)}
.pn-network-decoration .e2{left:82px;top:16px;width:67px;transform:rotate(16deg)}
.pn-network-decoration .e3{left:25px;top:34px;width:80px;transform:rotate(50deg)}
.pn-network-decoration .e4{left:58px;top:95px;width:70px;transform:rotate(-8deg)}
.pn-network-decoration .e5{left:125px;top:87px;width:65px;transform:rotate(55deg)}

.pn-welcome-pill {
    z-index:1;
    padding:.32rem .72rem;
    border:1px solid var(--line);
    border-radius:999px;
    color:var(--text);
    background:#edf5ff;
    font-size:.72rem;
    font-weight:850;
}

.pn-title {
    z-index:1;
    margin:.35rem 0 0;
    color:var(--text);
    font-size:clamp(3.1rem,5.4vw,4.65rem);
    line-height:1;
    letter-spacing:-.055em;
    font-weight:950;
}

.pn-title span {
    background:linear-gradient(90deg,#0b76f2,#7242ef,#17b9f3);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.pn-subtitle {
    z-index:1;
    display:flex;
    flex-direction:column;
    gap:.2rem;
    margin:.58rem auto 0;
    color:var(--muted);
    font-size:.86rem;
}

.pn-subtitle strong {
    color:var(--text);
    font-size:1.05rem;
}

.pn-chip-row {
    z-index:1;
    width:100%;
    display:flex;
    justify-content:center;
    flex-wrap:wrap;
    gap:.75rem;
    margin-top:1.05rem;
}

.pn-chip {
    min-width:132px;
    padding:.54rem .8rem;
    border:1px solid var(--line);
    border-radius:999px;
    color:var(--text);
    background:#fff;
    box-shadow:0 7px 18px rgba(30,83,150,.07);
    font-size:.74rem;
}

/* QUICK CARDS */
.pn-card {
    position:relative;
    min-height:174px;
    padding:1rem;
    border:1px solid rgba(10,117,245,.14);
    border-radius:18px;
    box-shadow:0 9px 24px rgba(34,86,160,.06);
    transition:transform .18s ease,box-shadow .18s ease;
}

.pn-card:hover {
    transform:translateY(-3px);
    box-shadow:0 14px 30px rgba(34,86,160,.12);
}

.card-blue {background:linear-gradient(145deg,#f1f7ff,#e8f3ff)}
.card-yellow {background:linear-gradient(145deg,#fffaf0,#fff2d8)}
.card-pink {background:linear-gradient(145deg,#fff4fd,#fde8f8)}
.card-green {background:linear-gradient(145deg,#effff7,#e3f9ef)}
.card-purple {background:linear-gradient(145deg,#faf6ff,#eee7ff)}

.pn-card-icon {
    width:42px;
    height:42px;
    display:grid;
    place-items:center;
    border-radius:50%;
    background:rgba(255,255,255,.9);
    font-size:1.15rem;
}

.pn-card-title {
    max-width:150px;
    margin-top:.72rem;
    color:var(--text);
    font-size:.9rem;
    font-weight:900;
    line-height:1.35;
}

.pn-card-arrow {
    position:absolute;
    right:.75rem;
    bottom:.68rem;
    width:29px;
    height:29px;
    display:grid;
    place-items:center;
    border-radius:50%;
    color:#0c4080;
    background:rgba(255,255,255,.78);
    font-weight:900;
}

/* Hide visual Open buttons; whole card remains followed by functional transparent button area */
div[data-testid="stHorizontalBlock"]:has(.pn-card) div[data-testid="stButton"] > button {
    min-height:1px;
    height:1px;
    padding:0;
    border:0;
    opacity:0;
}

/* FINAL VOICE COMPOSER */
.st-key-composer_tools {
    width:100%;
    margin-top:.9rem;
    padding:.62rem .72rem;
    border:1px solid rgba(25,116,235,.22);
    border-radius:24px;
    background:linear-gradient(90deg,#ffffff,#f6fbff);
    box-shadow:0 12px 34px rgba(31,83,157,.13);
    box-sizing:border-box;
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"] {
    width:100%;
    align-items:center!important;
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"] {
    min-width:0!important;
    display:flex!important;
    align-items:center!important;
    justify-content:center!important;
    padding:0!important;
}

/* Upload */
.st-key-composer_tools div[data-testid="stPopover"] {
    width:48px;
}

.st-key-composer_tools div[data-testid="stPopover"] > button {
    width:48px!important;
    height:48px!important;
    min-height:48px!important;
    margin:0!important;
    padding:0!important;
    border:1px solid rgba(20,126,245,.28)!important;
    border-radius:50%!important;
    color:#0b2c5c!important;
    background:#ffffff!important;
    box-shadow:0 7px 18px rgba(20,105,210,.12)!important;
    font-size:1.35rem!important;
}

/* Stretched input */
.st-key-composer_tools div[data-testid="stTextInput"] {
    width:100%!important;
    margin:0!important;
}

.st-key-composer_tools div[data-testid="stTextInput"] > div,
.st-key-composer_tools [data-baseweb="input"] {
    width:100%!important;
}

.st-key-composer_tools div[data-testid="stTextInput"] input,
.st-key-composer_tools [data-baseweb="input"] input {
    width:100%!important;
    height:48px!important;
    min-height:48px!important;
    margin:0!important;
    padding:0 1rem!important;
    border:1px solid rgba(20,116,235,.16)!important;
    border-radius:999px!important;
    color:#10244a!important;
    -webkit-text-fill-color:#10244a!important;
    caret-color:#0a75f5!important;
    background:#ffffff!important;
    box-shadow:inset 0 1px 2px rgba(21,64,125,.04)!important;
    font-size:.92rem!important;
    opacity:1!important;
}

.st-key-composer_tools div[data-testid="stTextInput"] input::placeholder {
    color:#7b879d!important;
    -webkit-text-fill-color:#7b879d!important;
    opacity:1!important;
}

/* Voice buttons */
.st-key-composer_tools iframe {
    display:block!important;
    width:50px!important;
    min-width:50px!important;
    max-width:50px!important;
    height:50px!important;
    min-height:50px!important;
    max-height:50px!important;
    margin:0 auto!important;
    border:1px solid rgba(20,126,245,.28)!important;
    border-radius:50%!important;
    background:#ffffff!important;
    box-shadow:0 7px 18px rgba(20,105,210,.12)!important;
    overflow:hidden!important;
}

/* Fixed visible model pill */
.st-key-composer_tools .st-key-composer_model_display {
    width:100%!important;
}

.st-key-composer_tools .st-key-composer_model_display button {
    width:100%!important;
    height:48px!important;
    min-height:48px!important;
    margin:0!important;
    padding:0 .7rem!important;
    border:1px solid rgba(20,126,245,.18)!important;
    border-radius:999px!important;
    color:#10244a!important;
    background:#ffffff!important;
    box-shadow:none!important;
    opacity:1!important;
    font-size:.75rem!important;
    font-weight:700!important;
    white-space:nowrap!important;
}

/* Send */
.st-key-composer_tools .st-key-composer_send {
    width:50px!important;
}

.st-key-composer_tools .st-key-composer_send button {
    width:50px!important;
    min-width:50px!important;
    height:50px!important;
    min-height:50px!important;
    margin:0!important;
    padding:0!important;
    border:0!important;
    border-radius:50%!important;
    color:#ffffff!important;
    background:linear-gradient(145deg,#0a77ef,#6c45f1)!important;
    box-shadow:
        0 8px 22px rgba(76,74,230,.30),
        0 0 0 4px rgba(49,157,255,.08)!important;
    font-size:1.05rem!important;
    font-weight:900!important;
}

.st-key-composer_tools [data-testid="stCaptionContainer"] {
    margin:.3rem .5rem 0!important;
    color:#62718c!important;
}

[data-testid="stChatInput"] {
    display:none!important;
}

@media(max-width:700px) {
    .st-key-composer_tools {
        padding:.5rem;
        border-radius:20px;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"] {
        display:grid!important;
        grid-template-columns:repeat(5,minmax(0,1fr))!important;
        grid-template-rows:48px 48px!important;
        gap:8px 7px!important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"] {
        width:100%!important;
        min-width:0!important;
        flex:none!important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(2) {
        grid-column:1 / -1!important;
        grid-row:1!important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(1) {
        grid-column:1!important;
        grid-row:2!important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(3) {
        grid-column:2!important;
        grid-row:2!important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(4) {
        grid-column:3!important;
        grid-row:2!important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(5) {
        grid-column:4!important;
        grid-row:2!important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(6) {
        grid-column:5!important;
        grid-row:2!important;
    }

    .st-key-composer_tools .st-key-composer_model_display button {
        padding:0 .15rem!important;
        font-size:.55rem!important;
    }

    .st-key-composer_tools div[data-testid="stTextInput"] input {
        font-size:.78rem!important;
    }
}

/* STATUS */
.pn-statusbar {
    display:grid;
    grid-template-columns:auto auto 1fr;
    align-items:center;
    gap:.65rem;
    margin-top:.68rem;
    padding:.45rem .6rem;
    border:1px solid var(--line);
    border-radius:15px;
    color:var(--muted);
    background:rgba(255,255,255,.88);
    font-size:.67rem;
}

.pn-live-pill {
    padding:.34rem .62rem;
    border-radius:999px;
    color:#2d36a7;
    background:#eef0ff;
}

.pn-connected {
    display:flex;
    align-items:center;
    gap:.3rem;
    color:#5a6b88;
}

.pn-secure {
    justify-self:end;
}

/* OTHER CONTROLS */
div[data-testid="stButton"] > button,
div[data-testid="stDownloadButton"] > button {
    min-height:42px;
    border:1px solid var(--line);
    border-radius:13px;
    font-weight:780;
}

div[data-testid="stChatMessage"] {
    border:1px solid rgba(11,117,241,.10);
    border-radius:18px;
    background:rgba(255,255,255,.82);
    box-shadow:0 7px 20px rgba(34,86,160,.05);
}

/* MOBILE NAV */
.st-key-mobile_nav {
    display:none;
}

/* TABLET */
@media(max-width:1050px) {
    [data-testid="stSidebar"] {
        width:190px!important;
        min-width:190px!important;
        max-width:190px!important;
    }

    [data-testid="stSidebar"] > div:first-child {
        width:190px!important;
    }

    .block-container {
        padding-left:.8rem;
        padding-right:.8rem;
    }

    .pn-chip {
        min-width:112px;
        padding:.43rem .55rem;
        font-size:.65rem;
    }

    .pn-card {
        min-height:150px;
        padding:.75rem;
    }

    .pn-card-title {
        font-size:.72rem;
    }
}

/* MOBILE */
@media(max-width:700px) {
    .block-container {
        padding:.35rem .48rem calc(5.3rem + env(safe-area-inset-bottom));
    }

    [data-testid="stSidebar"] {
        width:280px!important;
        min-width:280px!important;
        max-width:280px!important;
    }

    [data-testid="stSidebar"] > div:first-child {
        width:280px!important;
    }

    .pn-topbar {
        min-height:48px;
        padding:0;
    }

    .pn-avatar {
        width:34px;
        height:34px;
        font-size:.65rem;
    }

    .pn-welcome-copy small {
        font-size:.56rem;
    }

    .pn-welcome-copy strong {
        font-size:.78rem;
    }

    .pn-model {
        min-height:32px;
        padding:0 .55rem;
        font-size:.58rem;
    }

    .pn-round {
        width:32px;
        height:32px;
    }

    .pn-hero {
        min-height:305px;
        padding:1rem .45rem .85rem;
    }

    .pn-network-decoration {
        display:none;
    }

    .pn-title {
        font-size:2.5rem;
    }

    .pn-subtitle {
        max-width:270px;
        font-size:.72rem;
    }

    .pn-subtitle strong {
        font-size:.83rem;
    }

    .pn-chip-row {
        display:grid;
        grid-template-columns:repeat(3,minmax(0,1fr));
        gap:.35rem;
    }

    .pn-chip {
        min-width:0;
        display:flex;
        flex-direction:column;
        align-items:center;
        gap:.18rem;
        padding:.45rem .16rem;
        border-radius:12px;
        font-size:.58rem;
    }

    .pn-card {
        min-height:122px;
        padding:.55rem;
    }

    .pn-card-icon {
        width:32px;
        height:32px;
        font-size:.88rem;
    }

    .pn-card-title {
        margin-top:.4rem;
        font-size:.63rem;
    }

    .pn-card-arrow {
        width:22px;
        height:22px;
        right:.4rem;
        bottom:.4rem;
        font-size:.65rem;
    }

    .st-key-composer_tools {
        padding:.5rem .55rem;
    }

    .st-key-composer_tools div[data-testid="stTextInput"] input {
        min-height:43px;
        font-size:.74rem;
    }

    .st-key-composer_tools div[data-testid="stFormSubmitButton"] > button {
        width:43px;
        height:43px;
        min-height:43px;
    }

    .st-key-composer_tools > div > [data-testid="stHorizontalBlock"]:last-of-type {
        display:grid!important;
        grid-template-columns:1fr 1fr 1fr!important;
        gap:.28rem!important;
    }

    .st-key-composer_tools > div > [data-testid="stHorizontalBlock"]:last-of-type > [data-testid="column"] {
        width:100%!important;
        min-width:0!important;
        flex:none!important;
    }

    .st-key-composer_tools > div > [data-testid="stHorizontalBlock"]:last-of-type > [data-testid="column"]:last-child {
        display:none!important;
    }

    .st-key-composer_tools div[data-testid="stPopover"] > button,
    .st-key-composer_tools [data-testid="stToggle"] label {
        width:100%;
        min-height:38px;
        padding:.2rem .25rem;
        font-size:.62rem;
    }

    .st-key-composer_tools {
        padding:.38rem .42rem;
        border-radius:24px;
    }

    .st-key-composer_tools div[data-testid="stPopover"] > button {
        width:40px;
        height:40px;
        min-height:40px;
        font-size:1.25rem;
    }

    .st-key-composer_tools div[data-testid="stTextInput"] input,
    .st-key-composer_tools [data-baseweb="input"] input {
        min-height:43px!important;
        padding:0 .3rem!important;
        font-size:.78rem!important;
    }

    .st-key-composer_tools div[data-testid="stSelectbox"] > div > div {
        min-height:37px;
        padding-left:.15rem!important;
        padding-right:.15rem!important;
        font-size:.56rem!important;
    }

    .st-key-composer_tools [data-testid="stToggle"] label {
        min-height:37px;
        font-size:.82rem;
    }

    .st-key-composer_tools div[data-testid="stFormSubmitButton"] > button {
        width:41px;
        height:41px;
        min-height:41px;
        font-size:.95rem;
    }

    .pn-statusbar {
        grid-template-columns:auto 1fr;
    }

    .pn-secure {
        display:none;
    }

    .st-key-mobile_nav {
        display:block;
        position:fixed;
        left:0;
        right:0;
        bottom:0;
        z-index:1000;
        margin:0;
        padding:.32rem .25rem calc(.32rem + env(safe-area-inset-bottom));
        border-top:1px solid var(--line);
        background:rgba(255,255,255,.98);
        box-shadow:0 -8px 24px rgba(31,83,157,.10);
        backdrop-filter:blur(14px);
    }

    .st-key-mobile_nav [data-testid="stHorizontalBlock"] {
        display:grid!important;
        grid-template-columns:repeat(5,minmax(0,1fr))!important;
        gap:.12rem!important;
    }

    .st-key-mobile_nav [data-testid="column"] {
        width:100%!important;
        min-width:0!important;
        flex:none!important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button {
        width:100%;
        min-height:50px;
        padding:.15rem .03rem;
        border:0;
        color:#5c6c89;
        background:transparent;
        box-shadow:none;
        white-space:pre-line;
        font-size:.58rem;
        line-height:1.15;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button:hover {
        color:#0874ed;
        background:#e7f2ff;
    }

    }
    
@media screen and (max-width: 700px) {

    .st-key-settings_logout {
        width: auto !important;
        display: inline-block !important;
    }

    .st-key-settings_logout button {
        width: auto !important;
        min-width: 90px !important;
        height: 36px !important;
        min-height: 36px !important;

        padding: 0 14px !important;

        background: #dc2626 !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;

        font-size: 0.75rem !important;
        font-weight: 700 !important;
    }

    .st-key-settings_logout button:hover {
        background: #b91c1c !important;
        color: white !important;
    }
}

/* FINAL RENDERING SAFETY */
.pn-topbar pre,
.pn-hero pre,
.pn-sidebar-profile pre,
.pn-statusbar pre,
.pn-card pre {
    display:none!important;
}

/* Explicit keyed composer input styling: visible typed text */
.st-key-composer_prompt input,
.st-key-composer_tools input[type="text"],
.st-key-composer_tools [data-baseweb="input"] input {
    color:#ffffff!important;
    -webkit-text-fill-color:#ffffff!important;
    caret-color:#ffffff!important;
    background:#0a2345!important;
    border:1px solid rgba(105,181,255,.38)!important;
    border-radius:999px!important;
    opacity:1!important;
}

.st-key-composer_prompt input::placeholder,
.st-key-composer_tools input[type="text"]::placeholder {
    color:#aebdd3!important;
    -webkit-text-fill-color:#aebdd3!important;
    opacity:1!important;
}

.st-key-composer_tools form {
    background:transparent!important;
}

/* Prevent any second native chat bar */
[data-testid="stChatInput"],
.stChatFloatingInputContainer {
    display:none!important;
}


/* FINAL INPUT VISIBILITY OVERRIDE */
.st-key-composer_tools input[type="text"] {
    color:#10244a!important;
    -webkit-text-fill-color:#10244a!important;
    background-color:#fff!important;
    opacity:1!important;
}

.st-key-composer_tools input[type="text"]::selection {
    color:#fff;
    background:#0a75f5;
}


/* EXACTLY CENTERED LOGIN VISUAL CARD */
.st-key-auth_visual_card {
    width:100%;
    height:100%;
}

.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    width:100%;
    height:100%;
    display:flex !important;
    flex-direction:column !important;
    align-items:center !important;
    justify-content:flex-start !important;
    box-sizing:border-box !important;
    padding:16px 24px 24px !important;
    margin:0 !important;
    overflow:hidden !important;
    text-align:center !important;
}

.st-key-auth_visual_card
[data-testid="stVerticalBlockBorderWrapper"]
> div {
    width:100% !important;
    display:flex !important;
    flex-direction:column !important;
    align-items:center !important;
    box-sizing:border-box !important;
}

.st-key-auth_visual_card [data-testid="stImage"] {
    width:100% !important;
    display:flex !important;
    justify-content:center !important;
    align-items:center !important;
    box-sizing:border-box !important;
    margin:0 auto 28px !important;
    padding:0 !important;
}

.st-key-auth_visual_card [data-testid="stImage"] > div {
    width:100% !important;
    display:flex !important;
    justify-content:center !important;
    align-items:center !important;
    margin:0 auto !important;
    padding:0 !important;
}

.st-key-auth_visual_card [data-testid="stImage"] img {
    display:block !important;
    width:min(100%, 570px) !important;
    max-width:570px !important;
    height:auto !important;
    max-height:none !important;
    margin-left:auto !important;
    margin-right:auto !important;
    border-radius:22px !important;
    object-fit:contain !important;
    object-position:center center !important;
    box-shadow:0 14px 34px rgba(5,28,71,.18) !important;
}

.pn-auth-image-copy {
    width:100%;
    max-width:620px;
    margin:0 auto !important;
    padding:0 12px;
    box-sizing:border-box;
    text-align:center !important;
}

.pn-auth-image-copy h2 {
    width:100%;
    margin:0 auto;
    color:var(--text);
    font-size:1.65rem;
    font-weight:950;
    text-align:center;
}

.pn-auth-image-copy p {
    width:100%;
    max-width:540px;
    margin:.55rem auto 0;
    color:var(--muted);
    font-size:.89rem;
    line-height:1.6;
    text-align:center;
}

.pn-auth-pills {
    width:100%;
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    align-items:center;
    gap:.45rem;
    margin:.8rem auto 0;
    padding:0;
}

.pn-auth-pills span {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:.43rem .66rem;
    border:1px solid var(--line);
    border-radius:999px;
    background:#fff;
    color:var(--text);
    font-size:.72rem;
    font-weight:750;
}

/* Keep the image centered on tablets and phones too. */
@media(max-width:900px) {
    .st-key-auth_visual_card
    > div[data-testid="stVerticalBlockBorderWrapper"] {
        padding:14px 18px 22px !important;
    }

    .st-key-auth_visual_card [data-testid="stImage"] img {
        width:min(100%, 520px) !important;
        max-width:520px !important;
    }
}

@media(max-width:700px) {
    .st-key-auth_visual_card
    > div[data-testid="stVerticalBlockBorderWrapper"] {
        padding:12px 12px 20px !important;
    }

    .st-key-auth_visual_card [data-testid="stImage"] {
        margin-bottom:20px !important;
    }

    .st-key-auth_visual_card [data-testid="stImage"] img {
        width:100% !important;
        max-width:430px !important;
        border-radius:18px !important;
    }

    .pn-auth-image-copy h2 {
        font-size:1.28rem;
    }

    .pn-auth-image-copy p {
        font-size:.78rem;
    }
}


/* LOGIN AI VISUAL — BORDER REMOVED */
.st-key-auth_visual_card,
.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    border:none !important;
    outline:none !important;
    box-shadow:none !important;
    background:transparent !important;
}

.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    padding:16px 24px 24px !important;
}

.st-key-auth_visual_card [data-testid="stImage"],
.st-key-auth_visual_card [data-testid="stImage"] > div {
    border:none !important;
    outline:none !important;
    background:transparent !important;
    box-shadow:none !important;
}

.st-key-auth_visual_card [data-testid="stImage"] img {
    border:none !important;
    outline:none !important;
    margin-left:auto !important;
    margin-right:auto !important;
    box-shadow:0 14px 34px rgba(5,28,71,.18) !important;
}

/* Keep text and pills centered below the borderless visual. */
.st-key-auth_visual_card .pn-auth-image-copy,
.st-key-auth_visual_card .pn-auth-pills {
    margin-left:auto !important;
    margin-right:auto !important;
    text-align:center !important;
}


/* EXACTLY CENTERED LOGIN VISUAL CARD */
.st-key-auth_visual_card {
    width:100%;
    height:100%;
}

.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    width:100%;
    height:100%;
    display:flex !important;
    flex-direction:column !important;
    align-items:center !important;
    justify-content:flex-start !important;
    box-sizing:border-box !important;
    padding:16px 24px 24px !important;
    margin:0 !important;
    overflow:hidden !important;
    text-align:center !important;
}

.st-key-auth_visual_card
[data-testid="stVerticalBlockBorderWrapper"]
> div {
    width:100% !important;
    display:flex !important;
    flex-direction:column !important;
    align-items:center !important;
    box-sizing:border-box !important;
}

.st-key-auth_visual_card [data-testid="stImage"] {
    width:100% !important;
    display:flex !important;
    justify-content:center !important;
    align-items:center !important;
    box-sizing:border-box !important;
    margin:0 auto 28px !important;
    padding:0 !important;
}

.st-key-auth_visual_card [data-testid="stImage"] > div {
    width:100% !important;
    display:flex !important;
    justify-content:center !important;
    align-items:center !important;
    margin:0 auto !important;
    padding:0 !important;
}

.st-key-auth_visual_card [data-testid="stImage"] img {
    display:block !important;
    width:min(100%, 570px) !important;
    max-width:570px !important;
    height:auto !important;
    max-height:none !important;
    margin-left:auto !important;
    margin-right:auto !important;
    border-radius:22px !important;
    object-fit:contain !important;
    object-position:center center !important;
    box-shadow:0 14px 34px rgba(5,28,71,.18) !important;
}

.pn-auth-image-copy {
    width:100%;
    max-width:620px;
    margin:0 auto !important;
    padding:0 12px;
    box-sizing:border-box;
    text-align:center !important;
}

.pn-auth-image-copy h2 {
    width:100%;
    margin:0 auto;
    color:var(--text);
    font-size:1.65rem;
    font-weight:950;
    text-align:center;
}

.pn-auth-image-copy p {
    width:100%;
    max-width:540px;
    margin:.55rem auto 0;
    color:var(--muted);
    font-size:.89rem;
    line-height:1.6;
    text-align:center;
}

.pn-auth-pills {
    width:100%;
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    align-items:center;
    gap:.45rem;
    margin:.8rem auto 0;
    padding:0;
}

.pn-auth-pills span {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    padding:.43rem .66rem;
    border:1px solid var(--line);
    border-radius:999px;
    background:#fff;
    color:var(--text);
    font-size:.72rem;
    font-weight:750;
}

/* Keep the image centered on tablets and phones too. */
@media(max-width:900px) {
    .st-key-auth_visual_card
    > div[data-testid="stVerticalBlockBorderWrapper"] {
        padding:14px 18px 22px !important;
    }

    .st-key-auth_visual_card [data-testid="stImage"] img {
        width:min(100%, 520px) !important;
        max-width:520px !important;
    }
}

@media(max-width:700px) {
    .st-key-auth_visual_card
    > div[data-testid="stVerticalBlockBorderWrapper"] {
        padding:12px 12px 20px !important;
    }

    .st-key-auth_visual_card [data-testid="stImage"] {
        margin-bottom:20px !important;
    }

    .st-key-auth_visual_card [data-testid="stImage"] img {
        width:100% !important;
        max-width:430px !important;
        border-radius:18px !important;
    }

    .pn-auth-image-copy h2 {
        font-size:1.28rem;
    }

    .pn-auth-image-copy p {
        font-size:.78rem;
    }
}


/* LOGIN AI VISUAL — BORDER REMOVED */
.st-key-auth_visual_card,
.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    border:none !important;
    outline:none !important;
    box-shadow:none !important;
    background:transparent !important;
}

.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    padding:16px 24px 24px !important;
}

.st-key-auth_visual_card [data-testid="stImage"],
.st-key-auth_visual_card [data-testid="stImage"] > div {
    border:none !important;
    outline:none !important;
    background:transparent !important;
    box-shadow:none !important;
}

.st-key-auth_visual_card [data-testid="stImage"] img {
    border:none !important;
    outline:none !important;
    margin-left:auto !important;
    margin-right:auto !important;
    box-shadow:0 14px 34px rgba(5,28,71,.18) !important;
}

/* Keep text and pills centered below the borderless visual. */
.st-key-auth_visual_card .pn-auth-image-copy,
.st-key-auth_visual_card .pn-auth-pills {
    margin-left:auto !important;
    margin-right:auto !important;
    text-align:center !important;
}

/* LOGIN AI VISUAL — BORDER REMOVED */
.st-key-auth_visual_card,
.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    border:none !important;
    outline:none !important;
    box-shadow:none !important;
    background:transparent !important;
}

.st-key-auth_visual_card > div[data-testid="stVerticalBlockBorderWrapper"] {
    padding:16px 24px 24px !important;
}

.st-key-auth_visual_card [data-testid="stImage"],
.st-key-auth_visual_card [data-testid="stImage"] > div {
    border:none !important;
    outline:none !important;
    background:transparent !important;
    box-shadow:none !important;
}

.st-key-auth_visual_card [data-testid="stImage"] img {
    border:none !important;
    outline:none !important;
    margin-left:auto !important;
    margin-right:auto !important;
    box-shadow:0 14px 34px rgba(5,28,71,.18) !important;
}

/* Keep text and pills centered below the borderless visual. */
.st-key-auth_visual_card .pn-auth-image-copy,
.st-key-auth_visual_card .pn-auth-pills {
    margin-left:auto !important;
    margin-right:auto !important;
    text-align:center !important;
}


/* PREMIUM COMPOSER BUTTONS */
.st-key-composer_tools iframe {
    border:0!important;
    background:linear-gradient(145deg,#00c6ff,#0072ff)!important;
    box-shadow:
        0 10px 24px rgba(0,114,255,.28),
        0 0 0 4px rgba(0,198,255,.10)!important;
}

.st-key-composer_tools
[data-testid="column"]:nth-child(4) iframe {
    background:linear-gradient(145deg,#6a5cff,#00c2ff)!important;
    box-shadow:
        0 10px 24px rgba(106,92,255,.28),
        0 0 0 4px rgba(0,194,255,.10)!important;
}

.st-key-composer_tools iframe:hover {
    transform:translateY(-2px) scale(1.03);
    box-shadow:
        0 14px 28px rgba(44,116,255,.34),
        0 0 0 5px rgba(0,194,255,.12)!important;
}

.st-key-composer_tools .st-key-composer_model_display button {
    color:#17335f!important;
    background:
        linear-gradient(135deg,#ffffff 0%,#eef6ff 55%,#f2edff 100%)!important;
    border:1px solid rgba(60,121,240,.24)!important;
    box-shadow:
        0 8px 22px rgba(54,94,170,.14),
        inset 0 1px 0 rgba(255,255,255,.8)!important;
    font-weight:850!important;
    letter-spacing:.01em!important;
}

.st-key-composer_tools .st-key-composer_model_display button:hover {
    transform:translateY(-1px);
    border-color:rgba(91,82,236,.38)!important;
    box-shadow:
        0 12px 26px rgba(78,90,210,.20),
        0 0 0 4px rgba(111,76,239,.08)!important;
}

.st-key-composer_tools .st-key-composer_send button {
    background:linear-gradient(145deg,#2563eb,#7c3aed)!important;
    box-shadow:
        0 10px 24px rgba(76,74,230,.34),
        0 0 0 5px rgba(99,102,241,.10)!important;
}

.st-key-composer_tools .st-key-composer_send button:hover {
    transform:translateY(-2px) scale(1.03);
    box-shadow:
        0 14px 30px rgba(76,74,230,.42),
        0 0 0 6px rgba(99,102,241,.14)!important;
}

.st-key-composer_tools div[data-testid="stPopover"] > button {
    color:#0b3f86!important;
    background:linear-gradient(145deg,#eaf6ff,#dcecff)!important;
    border:1px solid rgba(37,99,235,.22)!important;
    box-shadow:
        0 8px 20px rgba(37,99,235,.14),
        inset 0 1px 0 rgba(255,255,255,.8)!important;
}

.st-key-composer_tools div[data-testid="stPopover"] > button:hover {
    color:#fff!important;
    background:linear-gradient(145deg,#0ea5e9,#4f46e5)!important;
    transform:translateY(-1px);
}

/* Stronger input focus */
.st-key-composer_tools div[data-testid="stTextInput"] input:focus {
    border-color:#4f8cff!important;
    box-shadow:
        0 0 0 4px rgba(79,140,255,.10),
        inset 0 1px 2px rgba(21,64,125,.04)!important;
}

/* Recording emphasis */
.st-key-composer_tools iframe[title*="Stop"],
.st-key-composer_tools iframe[aria-label*="Stop"] {
    background:linear-gradient(145deg,#ff4d5f,#e11d48)!important;
    box-shadow:
        0 0 0 6px rgba(225,29,72,.10),
        0 10px 24px rgba(225,29,72,.28)!important;
    animation:pnPulse 1.15s ease-in-out infinite;
}

@keyframes pnPulse {
    0%,100% { transform:scale(1); }
    50% { transform:scale(1.06); }
}


/* REMOVE RECORDER UNDERLINE ARTIFACT */
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(3),
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(4) {
    position:relative !important;
    overflow:visible !important;
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(3)::after,
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(4)::after {
    content:"";
    position:absolute;
    left:50%;
    bottom:5px;
    width:38px;
    height:7px;
    transform:translateX(-50%);
    border-radius:999px;
    background:#ffffff;
    pointer-events:none;
    z-index:5;
}

.st-key-composer_tools iframe {
    border-bottom:0 !important;
    outline:0 !important;
}

/* Mobile mask adjustment */
@media(max-width:700px) {
    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(3)::after,
    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(4)::after {
        bottom:3px;
        width:32px;
        height:6px;
    }
}


/* FINAL VOICE COMPONENT BOX REMOVAL */
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(3),
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(4) {
    width:54px !important;
    min-width:54px !important;
    max-width:54px !important;
    height:54px !important;
    min-height:54px !important;
    max-height:54px !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    overflow:hidden !important;
    border:0 !important;
    outline:0 !important;
    background:transparent !important;
    box-shadow:none !important;
    border-radius:50% !important;
    clip-path:circle(50% at 50% 50%) !important;
    isolation:isolate !important;
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(3) > div,
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(4) > div {
    width:54px !important;
    min-width:54px !important;
    max-width:54px !important;
    height:54px !important;
    min-height:54px !important;
    max-height:54px !important;
    margin:0 !important;
    padding:0 !important;
    overflow:hidden !important;
    border:0 !important;
    outline:0 !important;
    background:transparent !important;
    box-shadow:none !important;
    border-radius:50% !important;
    clip-path:circle(50% at 50% 50%) !important;
}

.st-key-composer_tools iframe {
    display:block !important;
    width:54px !important;
    min-width:54px !important;
    max-width:54px !important;
    height:54px !important;
    min-height:54px !important;
    max-height:54px !important;
    margin:0 !important;
    padding:0 !important;
    border:0 !important;
    outline:0 !important;
    overflow:hidden !important;
    border-radius:50% !important;
    clip-path:circle(49% at 50% 50%) !important;
    background:transparent !important;
    box-shadow:none !important;
}

/* Add the premium circular ring outside the clipped component. */
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(3)::before,
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(4)::before {
    content:"";
    position:absolute;
    inset:1px;
    border-radius:50%;
    pointer-events:none;
    z-index:10;
    border:2px solid rgba(30,144,255,.30);
    box-shadow:
        0 8px 20px rgba(0,114,255,.20),
        0 0 0 4px rgba(0,198,255,.08);
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(3)::before {
    background:linear-gradient(
        145deg,
        rgba(0,198,255,.08),
        rgba(0,114,255,.05)
    );
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(4)::before {
    background:linear-gradient(
        145deg,
        rgba(106,92,255,.08),
        rgba(0,194,255,.05)
    );
}

/* Remove old underline masks and any stale pseudo-elements. */
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(3)::after,
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"]:nth-child(4)::after {
    display:none !important;
    content:none !important;
}

@media(max-width:700px) {
    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(3),
    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(4),
    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(3) > div,
    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(4) > div,
    .st-key-composer_tools iframe {
        width:46px !important;
        min-width:46px !important;
        max-width:46px !important;
        height:46px !important;
        min-height:46px !important;
        max-height:46px !important;
    }
}


/* WORKING PREMIUM MODEL DROPDOWN */
.st-key-composer_tools .st-key-composer_model_selector {
    width:100% !important;
    min-width:0 !important;
    margin:0 !important;
}

.st-key-composer_tools
.st-key-composer_model_selector
div[data-testid="stSelectbox"] {
    display:block !important;
    width:100% !important;
    min-width:0 !important;
    margin:0 !important;
    visibility:visible !important;
    opacity:1 !important;
}

.st-key-composer_tools
.st-key-composer_model_selector
div[data-testid="stSelectbox"] > div {
    width:100% !important;
}

.st-key-composer_tools
.st-key-composer_model_selector
div[data-testid="stSelectbox"] > div > div {
    width:100% !important;
    height:48px !important;
    min-height:48px !important;
    padding-left:.75rem !important;
    padding-right:.4rem !important;
    border:1px solid rgba(80,91,230,.26) !important;
    border-radius:999px !important;
    color:#17335f !important;
    background:
        linear-gradient(135deg,#ffffff 0%,#eef6ff 55%,#f2edff 100%) !important;
    box-shadow:
        0 8px 22px rgba(54,94,170,.14),
        inset 0 1px 0 rgba(255,255,255,.85) !important;
    font-size:.73rem !important;
    font-weight:800 !important;
    cursor:pointer !important;
}

.st-key-composer_tools
.st-key-composer_model_selector
div[data-testid="stSelectbox"] > div > div:hover {
    border-color:rgba(91,82,236,.45) !important;
    box-shadow:
        0 12px 26px rgba(78,90,210,.20),
        0 0 0 4px rgba(111,76,239,.08) !important;
}

.st-key-composer_tools
.st-key-composer_model_selector
svg {
    color:#5d4bdd !important;
}

/* Remove any old disabled model-display button if stale markup exists. */
.st-key-composer_tools .st-key-composer_model_display {
    display:none !important;
}

@media(max-width:700px) {
    .st-key-composer_tools
    .st-key-composer_model_selector
    div[data-testid="stSelectbox"] > div > div {
        min-height:46px !important;
        height:46px !important;
        padding-left:.2rem !important;
        padding-right:.12rem !important;
        font-size:.55rem !important;
    }
}


/* ENTER-TO-SEND SUPPORT */
.st-key-composer_tools .st-key-composer_form {
    width:100% !important;
}

.st-key-composer_tools .st-key-composer_form div[data-testid="stForm"] {
    width:100% !important;
    margin:0 !important;
    padding:0 !important;
    border:0 !important;
    background:transparent !important;
    box-shadow:none !important;
}

.st-key-composer_tools
.st-key-composer_form
div[data-testid="stFormSubmitButton"] {
    position:absolute !important;
    width:1px !important;
    height:1px !important;
    overflow:hidden !important;
    opacity:0 !important;
    pointer-events:none !important;
}

.st-key-composer_tools
.st-key-composer_form
div[data-testid="stFormSubmitButton"] > button {
    width:1px !important;
    min-width:1px !important;
    height:1px !important;
    min-height:1px !important;
    padding:0 !important;
    margin:0 !important;
    border:0 !important;
    opacity:0 !important;
}

/* Keep the visible circular send button unchanged. */
.st-key-composer_tools .st-key-composer_send button {
    pointer-events:auto !important;
}


/* FINAL BORDERLESS ENTER-TO-SEND COMPOSER */
.st-key-composer_tools {
    width:100% !important;
    margin-top:.9rem !important;
    padding:.55rem .65rem !important;
    border:none !important;
    outline:none !important;
    border-radius:24px !important;
    background:linear-gradient(90deg,#ffffff,#f7fbff) !important;
    box-shadow:0 12px 32px rgba(31,83,157,.12) !important;
    box-sizing:border-box !important;
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"] {
    width:100% !important;
    align-items:center !important;
}

.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"] {
    min-width:0 !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    padding:0 !important;
}

/* Hidden submit button: Enter still submits the form. */
.st-key-composer_tools .st-key-composer_form {
    width:100% !important;
}

.st-key-composer_tools .st-key-composer_form div[data-testid="stForm"] {
    width:100% !important;
    margin:0 !important;
    padding:0 !important;
    border:none !important;
    outline:none !important;
    background:transparent !important;
    box-shadow:none !important;
}

.st-key-composer_tools
.st-key-composer_form
div[data-testid="stFormSubmitButton"] {
    position:absolute !important;
    width:1px !important;
    height:1px !important;
    overflow:hidden !important;
    opacity:0 !important;
    pointer-events:none !important;
}

.st-key-composer_tools
.st-key-composer_form
div[data-testid="stFormSubmitButton"] > button {
    width:1px !important;
    min-width:1px !important;
    height:1px !important;
    min-height:1px !important;
    padding:0 !important;
    margin:0 !important;
    border:none !important;
    opacity:0 !important;
}

/* Borderless search field */
.st-key-composer_tools div[data-testid="stTextInput"] {
    width:100% !important;
    margin:0 !important;
}

.st-key-composer_tools div[data-testid="stTextInput"] > div,
.st-key-composer_tools [data-baseweb="input"] {
    width:100% !important;
    border:none !important;
    outline:none !important;
    box-shadow:none !important;
}

.st-key-composer_tools div[data-testid="stTextInput"] input,
.st-key-composer_tools [data-baseweb="input"] input {
    width:100% !important;
    height:48px !important;
    min-height:48px !important;
    margin:0 !important;
    padding:0 1rem !important;
    border:none !important;
    outline:none !important;
    border-radius:999px !important;
    color:#10244a !important;
    -webkit-text-fill-color:#10244a !important;
    caret-color:#0a75f5 !important;
    background:#f8fbff !important;
    box-shadow:inset 0 1px 2px rgba(21,64,125,.04) !important;
    font-size:.92rem !important;
    opacity:1 !important;
}

.st-key-composer_tools div[data-testid="stTextInput"] input:focus {
    border:none !important;
    outline:none !important;
    box-shadow:
        0 0 0 4px rgba(79,140,255,.08),
        inset 0 1px 2px rgba(21,64,125,.04) !important;
}

.st-key-composer_tools div[data-testid="stTextInput"] input::placeholder {
    color:#7b879d !important;
    -webkit-text-fill-color:#7b879d !important;
    opacity:1 !important;
}

/* Borderless upload button */
.st-key-composer_tools div[data-testid="stPopover"] > button {
    width:48px !important;
    height:48px !important;
    min-height:48px !important;
    margin:0 !important;
    padding:0 !important;
    border:none !important;
    outline:none !important;
    border-radius:50% !important;
    color:#0b3f86 !important;
    background:linear-gradient(145deg,#eaf6ff,#dcecff) !important;
    box-shadow:0 8px 20px rgba(37,99,235,.14) !important;
    font-size:1.35rem !important;
}

/* Borderless circular voice controls */
.st-key-composer_tools iframe {
    display:block !important;
    width:50px !important;
    min-width:50px !important;
    max-width:50px !important;
    height:50px !important;
    min-height:50px !important;
    max-height:50px !important;
    margin:0 auto !important;
    padding:0 !important;
    border:none !important;
    outline:none !important;
    border-radius:50% !important;
    background:transparent !important;
    box-shadow:0 8px 20px rgba(37,99,235,.14) !important;
    overflow:hidden !important;
    clip-path:circle(49% at 50% 50%) !important;
}

/* Borderless working model dropdown */
.st-key-composer_tools .st-key-composer_model_selector,
.st-key-composer_tools .st-key-composer_model_selector div[data-testid="stSelectbox"] {
    width:100% !important;
    margin:0 !important;
}

.st-key-composer_tools
.st-key-composer_model_selector
div[data-testid="stSelectbox"] > div > div {
    width:100% !important;
    height:48px !important;
    min-height:48px !important;
    padding-left:.75rem !important;
    padding-right:.35rem !important;
    border:none !important;
    outline:none !important;
    border-radius:999px !important;
    color:#17335f !important;
    background:linear-gradient(135deg,#ffffff,#eef6ff,#f2edff) !important;
    box-shadow:0 8px 20px rgba(54,94,170,.12) !important;
    font-size:.73rem !important;
    font-weight:800 !important;
}

/* Remove any stale visible send control. */
.st-key-composer_tools .st-key-composer_send,
.st-key-composer_tools .st-key-composer_model_display {
    display:none !important;
}

[data-testid="stChatInput"] {
    display:none !important;
}

@media(max-width:700px) {
    .st-key-composer_tools {
        padding:.5rem !important;
        border-radius:20px !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"] {
        display:grid !important;
        grid-template-columns:44px 1fr 1fr 1.4fr !important;
        grid-template-rows:48px 48px !important;
        gap:8px 7px !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"] {
        width:100% !important;
        min-width:0 !important;
        flex:none !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(2) {
        grid-column:1 / -1 !important;
        grid-row:1 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(1) {
        grid-column:1 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(3) {
        grid-column:2 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(4) {
        grid-column:3 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(5) {
        grid-column:4 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    .st-key-composer_model_selector
    div[data-testid="stSelectbox"] > div > div {
        font-size:.56rem !important;
        padding-left:.2rem !important;
        padding-right:.12rem !important;
    }

    .st-key-composer_tools div[data-testid="stTextInput"] input {
        font-size:.78rem !important;
    }
}


/* FINAL SEND BUTTON POSITIONING */
.st-key-composer_tools .st-key-composer_form,
.st-key-composer_tools div[data-testid="stForm"],
.st-key-composer_tools div[data-testid="stFormSubmitButton"] {
    display:none !important;
}

/* Ensure only the far-right circular send button is visible. */
.st-key-composer_tools .st-key-composer_send {
    display:flex !important;
    width:50px !important;
    height:50px !important;
    align-items:center !important;
    justify-content:center !important;
}

.st-key-composer_tools .st-key-composer_send button {
    display:flex !important;
    width:50px !important;
    min-width:50px !important;
    height:50px !important;
    min-height:50px !important;
    margin:0 !important;
    padding:0 !important;
    align-items:center !important;
    justify-content:center !important;
    border:none !important;
    border-radius:50% !important;
    color:#ffffff !important;
    background:linear-gradient(145deg,#2563eb,#7c3aed) !important;
    box-shadow:
        0 10px 24px rgba(76,74,230,.34),
        0 0 0 5px rgba(99,102,241,.10) !important;
    font-size:1.05rem !important;
    font-weight:900 !important;
}

/* Remove any generic form button styling that could recreate the old Send button. */
.st-key-composer_tools div[data-testid="stFormSubmitButton"] > button,
.st-key-composer_tools button[kind="secondaryFormSubmit"] {
    display:none !important;
}

@media(max-width:700px) {
    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"] {
        display:grid !important;
        grid-template-columns:44px 1fr 1fr 1.4fr 48px !important;
        grid-template-rows:48px 48px !important;
        gap:8px 7px !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(2) {
        grid-column:1 / -1 !important;
        grid-row:1 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(1) {
        grid-column:1 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(3) {
        grid-column:2 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(4) {
        grid-column:3 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(5) {
        grid-column:4 !important;
        grid-row:2 !important;
    }

    .st-key-composer_tools
    > div
    > [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(6) {
        grid-column:5 !important;
        grid-row:2 !important;
    }
}


/* =========================================================
   PEERNET AI V5 — APPROVED DASHBOARD
   ========================================================= */
:root {
    --pn-bg:#f6f9ff;
    --pn-ink:#0b1e49;
    --pn-muted:#667495;
    --pn-blue:#2563eb;
    --pn-purple:#7c3aed;
}

.stApp {
    background:
        radial-gradient(circle at 82% 8%,rgba(123,92,255,.10),transparent 26%),
        linear-gradient(180deg,#fbfdff 0%,#f3f7ff 100%) !important;
}

.block-container {
    max-width:1550px !important;
    padding:.45rem 1.7rem 1.3rem !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
    width:300px !important;
    min-width:300px !important;
    max-width:300px !important;
    border-right:1px solid rgba(53,95,166,.12) !important;
    background:rgba(255,255,255,.94) !important;
    box-shadow:8px 0 30px rgba(37,77,137,.04) !important;
}
[data-testid="stSidebar"] > div:first-child { width:300px !important; }

[data-testid="stSidebar"] [data-testid="stImage"] {
    justify-content:flex-start !important;
    margin:.35rem 0 .2rem .1rem !important;
}
[data-testid="stSidebar"] img {
    width:150px !important;
    margin:0 !important;
}
.pn-sidebar-profile {
    align-items:flex-start !important;
    text-align:left !important;
    padding:.1rem .1rem .8rem !important;
}
.pn-side-avatar,
.pn-side-premium { display:none !important; }
.pn-side-name {
    font-size:.88rem !important;
    margin-top:.15rem !important;
}
.pn-side-online {
    font-size:.65rem !important;
}

[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    min-height:44px !important;
    justify-content:flex-start !important;
    border:none !important;
    border-radius:12px !important;
    color:#253756 !important;
    background:transparent !important;
    box-shadow:none !important;
    font-size:.82rem !important;
}
[data-testid="stSidebar"] .st-key-side_new_chat button {
    min-height:50px !important;
    justify-content:center !important;
    color:#fff !important;
    background:linear-gradient(90deg,#2367f2,#9a35e8) !important;
    box-shadow:0 10px 22px rgba(74,79,224,.22) !important;
    font-weight:900 !important;
    margin:.45rem 0 .8rem !important;
}
[data-testid="stSidebar"] .st-key-side_dashboard button,
[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    color:#175eea !important;
    background:#edf4ff !important;
}
.pn-mode-label {
    margin-top:1rem !important;
}

/* Top bar */
.pn-topbar {
    min-height:64px !important;
    margin:0 0 .55rem !important;
}
.pn-top-actions { gap:.6rem !important; }
.pn-round,
.pn-top-avatar {
    width:42px;
    height:42px;
    display:grid;
    place-items:center;
    border:none;
    border-radius:50%;
    background:#fff;
    color:#10244a;
    box-shadow:0 6px 18px rgba(33,76,141,.10);
}
.pn-top-avatar {
    color:#fff;
    font-weight:900;
    background:linear-gradient(145deg,#7443ef,#9f35e6);
}
.pn-chevron { color:#243a62; }

/* Hero */
.pn-dashboard-hero {
    position:relative;
    min-height:240px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    overflow:hidden;
    padding:2.1rem 2.4rem;
    border-radius:26px;
    background:
        radial-gradient(circle at 80% 40%,rgba(107,72,245,.18),transparent 28%),
        linear-gradient(115deg,#f7fbff 0%,#eaf3ff 46%,#ede7ff 100%);
    box-shadow:0 16px 45px rgba(50,89,155,.11);
}
.pn-hero-copy { z-index:2; }
.pn-hero-copy h1 {
    margin:0;
    color:#0a1d47;
    font-size:clamp(2.2rem,4vw,3.4rem);
    line-height:1.05;
    letter-spacing:-.045em;
    font-weight:950;
}
.pn-hero-copy h1 span {
    background:linear-gradient(90deg,#5f36e8,#2f6ce8);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.pn-hero-copy p {
    margin:.8rem 0 0;
    color:#5f6f90;
    font-size:1.12rem;
}
.pn-hero-art {
    position:relative;
    width:400px;
    height:180px;
}
.pn-core-cube,
.pn-hero-art .cube {
    position:absolute;
    display:grid;
    place-items:center;
    border-radius:16px;
    background:linear-gradient(145deg,#20a8ff,#7742f5);
    box-shadow:0 16px 28px rgba(75,66,232,.24);
}
.pn-core-cube {
    left:145px;
    top:48px;
    width:110px;
    height:96px;
    color:#fff;
    font-size:2.2rem;
}
.pn-hero-art .cube { width:42px; height:42px; border-radius:11px; }
.pn-hero-art .c1{left:42px;top:30px}
.pn-hero-art .c2{right:28px;top:25px}
.pn-hero-art .c3{left:70px;bottom:10px}
.pn-hero-art .c4{right:52px;bottom:22px}
.pn-hero-art .line {
    position:absolute;
    height:2px;
    background:rgba(255,255,255,.9);
    transform-origin:left center;
}
.pn-hero-art .l1{left:82px;top:52px;width:92px;transform:rotate(18deg)}
.pn-hero-art .l2{left:245px;top:74px;width:110px;transform:rotate(-18deg)}
.pn-hero-art .l3{left:105px;top:144px;width:78px;transform:rotate(-28deg)}
.pn-hero-art .l4{left:247px;top:126px;width:92px;transform:rotate(18deg)}

/* Feature cards */
div[data-testid="stHorizontalBlock"]:has(.pn-feature-card) {
    margin-top:1.2rem !important;
}
.pn-feature-card {
    min-height:260px;
    padding:1.45rem 1.2rem;
    border:none;
    border-radius:22px;
    background:#fff;
    box-shadow:0 14px 35px rgba(39,81,145,.09);
    transition:.2s ease;
}
.pn-feature-card:hover {
    transform:translateY(-5px);
    box-shadow:0 20px 40px rgba(39,81,145,.14);
}
.pn-feature-icon {
    width:56px;
    height:56px;
    display:grid;
    place-items:center;
    border-radius:50%;
    color:#fff;
    font-size:1.25rem;
    font-weight:900;
    background:linear-gradient(145deg,#2672f2,#6d44ed);
}
.card-green .pn-feature-icon{background:linear-gradient(145deg,#29cf71,#1cab66)}
.card-teal .pn-feature-icon{background:linear-gradient(145deg,#24d2c4,#29a98e)}
.card-purple .pn-feature-icon{background:linear-gradient(145deg,#7248f5,#9342ef)}
.card-orange .pn-feature-icon{background:linear-gradient(145deg,#ff9f2c,#ff6b20)}
.card-pink .pn-feature-icon{background:linear-gradient(145deg,#ff5c85,#ef356c)}
.pn-feature-card h3 {
    margin:1.2rem 0 .65rem;
    color:#0c1f4b;
    font-size:1.02rem;
    font-weight:900;
}
.pn-feature-card p {
    margin:0;
    color:#667493;
    font-size:.82rem;
    line-height:1.7;
}
div[data-testid="stHorizontalBlock"]:has(.pn-feature-card)
div[data-testid="stButton"] > button {
    height:1px !important;
    min-height:1px !important;
    padding:0 !important;
    border:0 !important;
    opacity:0 !important;
}

/* Topics */
.pn-popular {
    margin:1.35rem 0 1rem;
    text-align:center;
}
.pn-popular strong {
    display:block;
    margin-bottom:.8rem;
    color:#14254d;
}
.pn-popular div {
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:.7rem;
}
.pn-popular span {
    padding:.5rem 1.15rem;
    border-radius:999px;
    color:#243a60;
    background:#edf3fc;
    box-shadow:inset 0 0 0 1px rgba(41,93,175,.05);
    font-size:.74rem;
}

/* Composer */
.st-key-composer_tools {
    width:100% !important;
    margin-top:1rem !important;
    padding:.75rem .85rem !important;
    border:none !important;
    border-radius:26px !important;
    background:#fff !important;
    box-shadow:0 18px 45px rgba(48,82,145,.14) !important;
}
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"] {
    align-items:center !important;
}
.st-key-composer_tools
> div
> [data-testid="stHorizontalBlock"]
> [data-testid="column"] {
    min-width:0 !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
}
.st-key-composer_tools div[data-testid="stTextInput"] {
    width:100% !important;
    margin:0 !important;
}
.st-key-composer_tools div[data-testid="stTextInput"] input,
.st-key-composer_tools [data-baseweb="input"] input {
    width:100% !important;
    min-height:54px !important;
    border:none !important;
    border-radius:999px !important;
    color:#10244a !important;
    -webkit-text-fill-color:#10244a !important;
    background:#f8fbff !important;
    box-shadow:none !important;
    padding:0 1.1rem !important;
}
.st-key-composer_tools div[data-testid="stPopover"] > button,
.st-key-composer_tools iframe {
    width:52px !important;
    min-width:52px !important;
    max-width:52px !important;
    height:52px !important;
    min-height:52px !important;
    max-height:52px !important;
    border:none !important;
    border-radius:50% !important;
    background:#f8fbff !important;
    box-shadow:0 7px 18px rgba(45,83,143,.09) !important;
}
.st-key-composer_tools .st-key-composer_model_selector div[data-testid="stSelectbox"] > div > div {
    min-height:52px !important;
    border:none !important;
    border-radius:999px !important;
    background:#f6f8fd !important;
    box-shadow:0 7px 18px rgba(45,83,143,.08) !important;
}
.st-key-composer_tools .st-key-composer_send button {
    width:54px !important;
    min-width:54px !important;
    height:54px !important;
    min-height:54px !important;
    border:none !important;
    border-radius:50% !important;
    color:#fff !important;
    background:linear-gradient(145deg,#2563eb,#8b35e8) !important;
    box-shadow:0 12px 25px rgba(85,67,225,.31) !important;
}
.st-key-composer_tools .st-key-composer_form,
.st-key-composer_tools div[data-testid="stForm"],
.st-key-composer_tools div[data-testid="stFormSubmitButton"] {
    display:none !important;
}

/* Chat */
div[data-testid="stChatMessage"] {
    border:none !important;
    border-radius:20px !important;
    background:rgba(255,255,255,.88) !important;
    box-shadow:0 8px 24px rgba(36,75,138,.08) !important;
}

/* Mobile */
@media(max-width:900px) {
    [data-testid="stSidebar"] {
        width:260px !important;
        min-width:260px !important;
        max-width:260px !important;
    }
    [data-testid="stSidebar"] > div:first-child { width:260px !important; }
    .pn-dashboard-hero { min-height:220px; padding:1.5rem; }
    .pn-hero-art { width:300px; transform:scale(.82); transform-origin:right center; }
    .pn-feature-card { min-height:220px; padding:1rem; }
}
@media(max-width:700px) {
    .block-container { padding:.35rem .5rem 6rem !important; }
    .pn-dashboard-hero {
        min-height:220px;
        padding:1.25rem;
    }
    .pn-hero-copy h1 { font-size:2rem; }
    .pn-hero-art { display:none; }
    div[data-testid="stHorizontalBlock"]:has(.pn-feature-card) {
        display:grid !important;
        grid-template-columns:repeat(2,minmax(0,1fr)) !important;
        gap:.65rem !important;
    }
    div[data-testid="stHorizontalBlock"]:has(.pn-feature-card)
    > [data-testid="column"] {
        width:100% !important;
        min-width:0 !important;
        flex:none !important;
    }
    .pn-feature-card { min-height:205px; }
}


/* =========================================================
   PEERNET AI V6 — PREMIUM SIDEBAR
   ========================================================= */
[data-testid="stSidebar"] {
    width:315px !important;
    min-width:315px !important;
    max-width:315px !important;
    background:
        radial-gradient(circle at 20% 0%,rgba(63,132,255,.11),transparent 24%),
        linear-gradient(180deg,#fbfdff 0%,#f6f9ff 100%) !important;
    border-right:1px solid rgba(45,90,160,.10) !important;
    box-shadow:10px 0 30px rgba(35,76,142,.05) !important;
}

[data-testid="stSidebar"] > div:first-child {
    width:315px !important;
    padding:1rem .85rem 1.1rem !important;
}

[data-testid="stSidebar"] [data-testid="stImage"] {
    display:flex !important;
    justify-content:flex-start !important;
    margin:0 0 .55rem .15rem !important;
}

[data-testid="stSidebar"] img {
    width:155px !important;
    margin:0 !important;
    filter:drop-shadow(0 8px 18px rgba(33,94,191,.16)) !important;
}

.pn-sidebar-user-card {
    display:grid;
    grid-template-columns:50px 1fr auto;
    align-items:center;
    gap:.7rem;
    padding:.75rem;
    margin:.15rem 0 .8rem;
    border-radius:18px;
    background:rgba(255,255,255,.86);
    box-shadow:0 10px 26px rgba(38,80,145,.08);
    backdrop-filter:blur(12px);
}

.pn-sidebar-user-avatar {
    position:relative;
    width:50px;
    height:50px;
    display:grid;
    place-items:center;
    border-radius:50%;
    color:#fff;
    font-weight:950;
    background:linear-gradient(145deg,#2468f2,#8a3bea);
    box-shadow:0 10px 22px rgba(74,68,222,.25);
}

.pn-sidebar-user-avatar span {
    position:absolute;
    right:1px;
    bottom:1px;
    width:11px;
    height:11px;
    border:2px solid #fff;
    border-radius:50%;
    background:#20c36b;
}

.pn-sidebar-user-copy {
    display:flex;
    flex-direction:column;
    min-width:0;
}

.pn-sidebar-user-copy strong {
    overflow:hidden;
    color:#10234d;
    font-size:.88rem;
    font-weight:900;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.pn-sidebar-user-copy small {
    margin-top:.12rem;
    color:#7885a0;
    font-size:.66rem;
}

.pn-sidebar-user-status {
    color:#20c36b;
    font-size:.72rem;
}

.pn-side-section-label {
    margin:1rem .35rem .38rem;
    color:#8b96aa;
    font-size:.58rem;
    font-weight:900;
    letter-spacing:.08em;
}

[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    min-height:42px !important;
    justify-content:flex-start !important;
    padding:.34rem .65rem !important;
    border:none !important;
    border-radius:12px !important;
    color:#31425f !important;
    background:transparent !important;
    box-shadow:none !important;
    font-size:.76rem !important;
    font-weight:750 !important;
    transition:.18s ease !important;
}

[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    color:#1763e8 !important;
    background:#eaf2ff !important;
    transform:translateX(2px);
}

[data-testid="stSidebar"] .st-key-side_new_chat button {
    min-height:50px !important;
    justify-content:center !important;
    margin:.2rem 0 .8rem !important;
    color:#fff !important;
    background:linear-gradient(90deg,#2267f2,#a337e5) !important;
    box-shadow:0 12px 25px rgba(79,66,221,.24) !important;
    font-size:.84rem !important;
    font-weight:900 !important;
}

[data-testid="stSidebar"] .st-key-side_new_chat button:hover {
    color:#fff !important;
    background:linear-gradient(90deg,#1559e8,#922bd9) !important;
    transform:translateY(-1px);
}

[data-testid="stSidebar"] .st-key-side_dashboard button {
    color:#1763e8 !important;
    background:#eaf2ff !important;
    box-shadow:inset 3px 0 0 #2f75ef !important;
}

[data-testid="stSidebar"] .st-key-side_recent_* button {
    min-height:36px !important;
    font-size:.7rem !important;
}

[data-testid="stSidebar"] div[data-testid="stSelectbox"] {
    margin:.35rem 0 .5rem !important;
}

[data-testid="stSidebar"] div[data-testid="stSelectbox"] > div > div {
    min-height:40px !important;
    border:none !important;
    border-radius:12px !important;
    background:#fff !important;
    box-shadow:0 7px 18px rgba(40,79,140,.07) !important;
    font-size:.7rem !important;
}

.pn-side-usage-card {
    margin:.75rem 0 .65rem;
    padding:.8rem;
    border-radius:16px;
    background:linear-gradient(145deg,#ffffff,#eef5ff);
    box-shadow:0 10px 24px rgba(40,79,140,.08);
}

.pn-side-usage-head {
    display:flex;
    align-items:center;
    justify-content:space-between;
    color:#1d3157;
    font-size:.72rem;
}

.pn-side-usage-head span {
    color:#2563eb;
    font-weight:900;
}

.pn-side-progress {
    width:100%;
    height:7px;
    margin:.55rem 0 .42rem;
    overflow:hidden;
    border-radius:999px;
    background:#dfe8f4;
}

.pn-side-progress span {
    display:block;
    height:100%;
    border-radius:999px;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
}

.pn-side-usage-card small {
    color:#7a879e;
    font-size:.63rem;
}

.pn-side-footer {
    display:flex;
    flex-direction:column;
    gap:.12rem;
    margin:1rem .2rem .55rem;
    padding-top:.8rem;
    border-top:1px solid rgba(50,90,150,.10);
    color:#72809a;
    text-align:center;
}

.pn-side-footer strong {
    color:#31425f;
    font-size:.7rem;
}

.pn-side-footer span,
.pn-side-footer small {
    font-size:.58rem;
}

[data-testid="stSidebar"] .st-key-side_logout button {
    justify-content:center !important;
    color:#e14b5b !important;
    background:#fff4f5 !important;
    border:1px solid rgba(225,75,91,.16) !important;
}

@media(max-width:1000px) {
    [data-testid="stSidebar"] {
        width:280px !important;
        min-width:280px !important;
        max-width:280px !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        width:280px !important;
    }
}

@media(max-width:700px) {
    [data-testid="stSidebar"] {
        width:290px !important;
        min-width:290px !important;
        max-width:290px !important;
    }

    [data-testid="stSidebar"] > div:first-child {
        width:290px !important;
    }

    .pn-sidebar-user-card {
        grid-template-columns:46px 1fr auto;
        padding:.65rem;
    }

    .pn-sidebar-user-avatar {
        width:46px;
        height:46px;
    }
}


/* COMPACT COLLAPSIBLE SIDEBAR SECTIONS */
[data-testid="stSidebar"] div[data-testid="stExpander"] {
    margin:.35rem 0 !important;
    border:none !important;
    border-radius:12px !important;
    background:transparent !important;
    box-shadow:none !important;
}

[data-testid="stSidebar"]
div[data-testid="stExpander"]
details {
    border:none !important;
    border-radius:12px !important;
    background:transparent !important;
}

[data-testid="stSidebar"]
div[data-testid="stExpander"]
summary {
    min-height:40px !important;
    padding:.35rem .6rem !important;
    border:none !important;
    border-radius:12px !important;
    color:#31425f !important;
    background:transparent !important;
    font-size:.75rem !important;
    font-weight:800 !important;
}

[data-testid="stSidebar"]
div[data-testid="stExpander"]
summary:hover {
    color:#1763e8 !important;
    background:#eaf2ff !important;
}

[data-testid="stSidebar"]
div[data-testid="stExpander"]
details[open] > summary {
    color:#1763e8 !important;
    background:#eaf2ff !important;
}

[data-testid="stSidebar"]
div[data-testid="stExpander"]
[data-testid="stExpanderDetails"] {
    padding:.3rem .15rem .25rem !important;
}

[data-testid="stSidebar"]
div[data-testid="stExpander"]
div[data-testid="stButton"] > button {
    min-height:34px !important;
    padding:.22rem .5rem !important;
    border-radius:10px !important;
    font-size:.68rem !important;
}

[data-testid="stSidebar"]
div[data-testid="stExpander"]
[data-testid="stCaptionContainer"] {
    padding:.2rem .5rem !important;
    color:#8a96ab !important;
    font-size:.64rem !important;
}


/* PEERNET AI V8 — FINAL COMPLETE CIRCLE PROFILE */
.pn-glass-profile,
.pn-glass-avatar,
.pn-profile-online,
.pn-profile-menu,
.pn-profile-bubble,
.pn-profile-symbol,
.pn-profile-initial,
.pn-user-bubble-profile,
.pn-user-bubble-letter,
.pn-user-bubble-online,
.pn-user-profile-bubble,
.pn-user-profile-letter,
.pn-user-profile-online,
.pn-chevron {
    display:none !important;
}

.pn-topbar-profile-only {
    width:100% !important;
    height:64px !important;
    min-height:64px !important;
    display:grid !important;
    grid-template-columns:minmax(0,1fr) 52px !important;
    align-items:center !important;
    margin:0 0 .55rem !important;
    padding:6px 4px 6px 0 !important;
    overflow:visible !important;
    box-sizing:border-box !important;
}

.pn-v8-profile-bubble {
    position:relative !important;
    width:48px !important;
    height:48px !important;
    min-width:48px !important;
    min-height:48px !important;
    max-width:48px !important;
    max-height:48px !important;
    aspect-ratio:1 / 1 !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    justify-self:end !important;
    align-self:center !important;
    margin:0 !important;
    padding:0 !important;
    box-sizing:border-box !important;
    border:none !important;
    outline:none !important;
    border-radius:50% !important;
    overflow:visible !important;
    opacity:1 !important;
    visibility:visible !important;
    z-index:20 !important;
    color:#ffffff !important;
    background:#0b2f63 !important;
    box-shadow:0 9px 22px rgba(11,47,99,.24) !important;
}

.pn-v8-profile-letter {
    width:100% !important;
    height:100% !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    margin:0 !important;
    padding:0 !important;
    color:inherit !important;
    -webkit-text-fill-color:currentColor !important;
    font-family:Inter,"Segoe UI",Arial,sans-serif !important;
    font-size:1rem !important;
    font-weight:900 !important;
    line-height:1 !important;
    text-align:center !important;
    text-transform:uppercase !important;
}

.pn-v8-profile-online {
    position:absolute !important;
    right:-1px !important;
    bottom:-1px !important;
    width:11px !important;
    height:11px !important;
    min-width:11px !important;
    min-height:11px !important;
    display:block !important;
    margin:0 !important;
    padding:0 !important;
    border:none !important;
    outline:none !important;
    border-radius:50% !important;
    background:#22c55e !important;
    box-shadow:0 2px 7px rgba(34,197,94,.35) !important;
    z-index:22 !important;
}

div:has(> .pn-topbar-profile-only),
div:has(> .pn-topbar-profile-only) > div,
div:has(.pn-v8-profile-bubble) {
    overflow:visible !important;
}

@media(max-width:700px) {
    .pn-topbar-profile-only {
        height:58px !important;
        min-height:58px !important;
        grid-template-columns:minmax(0,1fr) 46px !important;
    }

    .pn-v8-profile-bubble {
        width:44px !important;
        height:44px !important;
        min-width:44px !important;
        min-height:44px !important;
        max-width:44px !important;
        max-height:44px !important;
    }

    .pn-v8-profile-letter {
        font-size:.92rem !important;
    }

    .pn-v8-profile-online {
        width:10px !important;
        height:10px !important;
        min-width:10px !important;
        min-height:10px !important;
    }
}


/* =========================================================
   DEDICATED PHONE COMPOSER
   Desktop and tablet remain on the existing composer.
   ========================================================= */
.st-key-composer_tools {
    display:block !important;
}

.st-key-mobile_composer {
    display:none !important;
}

@media screen and (max-width:700px) {
    /* Hide only the desktop composer on phones. */
    .st-key-composer_tools {
        display:none !important;
    }

    .st-key-mobile_composer {
        display:block !important;
        width:100% !important;
        max-width:100% !important;
        margin:.75rem auto 1rem !important;
        padding:.7rem !important;
        border:none !important;
        outline:none !important;
        border-radius:22px !important;
        background:rgba(255,255,255,.96) !important;
        box-shadow:0 14px 34px rgba(39,81,145,.13) !important;
        box-sizing:border-box !important;
        overflow:visible !important;
    }

    /* First row: full-width prompt. */
    .st-key-mobile_composer div[data-testid="stTextInput"],
    .st-key-mobile_composer div[data-testid="stTextInput"] > div,
    .st-key-mobile_composer [data-baseweb="input"] {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        margin:0 !important;
    }

    .st-key-mobile_composer div[data-testid="stTextInput"] input,
    .st-key-mobile_composer [data-baseweb="input"] input {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        height:50px !important;
        min-height:50px !important;
        margin:0 !important;
        padding:0 .95rem !important;
        border:none !important;
        outline:none !important;
        border-radius:15px !important;
        color:#10244a !important;
        -webkit-text-fill-color:#10244a !important;
        caret-color:#2563eb !important;
        background:#f4f8ff !important;
        box-shadow:inset 0 1px 2px rgba(21,64,125,.05) !important;
        font-size:.86rem !important;
        opacity:1 !important;
        box-sizing:border-box !important;
    }

    .st-key-mobile_composer div[data-testid="stTextInput"] input::placeholder {
        color:#7786a0 !important;
        -webkit-text-fill-color:#7786a0 !important;
        opacity:1 !important;
    }

    /* Second row: +, dictate, voice, model and send. */
    .st-key-mobile_composer [data-testid="stHorizontalBlock"] {
        width:100% !important;
        max-width:100% !important;
        display:grid !important;
        grid-template-columns:44px 44px 44px minmax(104px,1fr) 48px !important;
        gap:8px !important;
        align-items:center !important;
        margin-top:.6rem !important;
        box-sizing:border-box !important;
    }

    .st-key-mobile_composer
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"] {
        width:100% !important;
        min-width:0 !important;
        max-width:none !important;
        display:flex !important;
        align-items:center !important;
        justify-content:center !important;
        flex:none !important;
        margin:0 !important;
        padding:0 !important;
        overflow:visible !important;
    }

    /* Attachment button. */
    .st-key-mobile_composer div[data-testid="stPopover"],
    .st-key-mobile_composer div[data-testid="stPopover"] > button {
        width:44px !important;
        min-width:44px !important;
        max-width:44px !important;
        height:44px !important;
        min-height:44px !important;
        max-height:44px !important;
        margin:0 !important;
        padding:0 !important;
    }

    .st-key-mobile_composer div[data-testid="stPopover"] > button {
        border:none !important;
        outline:none !important;
        border-radius:50% !important;
        color:#17406f !important;
        background:#edf5ff !important;
        box-shadow:0 7px 18px rgba(37,99,235,.12) !important;
        font-size:1.15rem !important;
    }

    /* Voice components. */
    .st-key-mobile_composer iframe {
        display:block !important;
        width:44px !important;
        min-width:44px !important;
        max-width:44px !important;
        height:44px !important;
        min-height:44px !important;
        max-height:44px !important;
        margin:0 !important;
        padding:0 !important;
        border:none !important;
        outline:none !important;
        border-radius:50% !important;
        clip-path:circle(49% at 50% 50%) !important;
        background:transparent !important;
        box-shadow:0 7px 18px rgba(37,99,235,.12) !important;
        overflow:hidden !important;
    }

    /* Model selector. */
    .st-key-mobile_composer div[data-testid="stSelectbox"],
    .st-key-mobile_composer div[data-testid="stSelectbox"] > div {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        margin:0 !important;
    }

    .st-key-mobile_composer
    div[data-testid="stSelectbox"] > div > div {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        height:44px !important;
        min-height:44px !important;
        padding-left:.55rem !important;
        padding-right:.25rem !important;
        border:none !important;
        outline:none !important;
        border-radius:14px !important;
        color:#17335f !important;
        background:#eef4ff !important;
        box-shadow:0 7px 18px rgba(54,94,170,.10) !important;
        font-size:.66rem !important;
        font-weight:800 !important;
    }

    .st-key-mobile_composer div[data-testid="stSelectbox"] svg {
        color:#654ee7 !important;
    }

    /* Send button. */
    .st-key-mobile_composer .st-key-mobile_composer_send,
    .st-key-mobile_composer .st-key-mobile_composer_send button {
        width:48px !important;
        min-width:48px !important;
        max-width:48px !important;
        height:48px !important;
        min-height:48px !important;
        max-height:48px !important;
        margin:0 !important;
        padding:0 !important;
    }

    .st-key-mobile_composer .st-key-mobile_composer_send button {
        display:flex !important;
        align-items:center !important;
        justify-content:center !important;
        border:none !important;
        outline:none !important;
        border-radius:50% !important;
        color:#fff !important;
        background:linear-gradient(145deg,#2563eb,#7c3aed) !important;
        box-shadow:0 10px 24px rgba(76,74,230,.30) !important;
        font-size:1rem !important;
        font-weight:900 !important;
    }

    .st-key-mobile_composer [data-testid="stCaptionContainer"] {
        margin:.35rem .25rem 0 !important;
        color:#667495 !important;
        font-size:.66rem !important;
    }
}

</style>
        """
    )


def apply_styles(theme: str = "Light") -> None:
    """Apply the existing PeerNet styles, then the selected color theme."""
    _apply_base_styles()

    theme_name = str(theme or "Light").strip().lower()

    themes = {
        "light": """
<style>
.pn-v8-profile-bubble {
    color:#ffffff !important;
    background:#0b2f63 !important;
    border:none !important;
    border-radius:50% !important;
}
.pn-v8-profile-letter {
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
}

/* Light theme profile */
.pn-user-profile-bubble { color:#ffffff !important; background:#0b2f63 !important; box-shadow:0 10px 24px rgba(11,47,99,.28),0 0 0 4px rgba(37,99,235,.07) !important; }
.pn-user-profile-letter { color:#ffffff !important; -webkit-text-fill-color:#ffffff !important; }
.pn-user-profile-online { background:#22c55e !important; border-color:#ffffff !important; }


/* Light theme profile */
.pn-glass-profile {
    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.92),
            rgba(226,239,255,.72)
        ) !important;
    border:1px solid rgba(255,255,255,.90) !important;
    box-shadow:
        0 12px 28px rgba(58,74,180,.16),
        inset 0 1px 0 rgba(255,255,255,.95) !important;
}

.pn-glass-avatar {
    background:
        linear-gradient(145deg,#2468f2 0%,#7b3fe8 58%,#a033df 100%) !important;
}

.pn-profile-online {
    border-color:#ffffff !important;
}
.stApp {
    color:#0b1e49 !important;
    background:
        radial-gradient(circle at 96% 0%,rgba(19,185,255,.11),transparent 24%),
        linear-gradient(180deg,#fbfdff 0%,#eef7ff 100%) !important;
}

@media screen and (max-width:700px) {
    .st-key-mobile_composer {
        color:#0b1e49 !important;
        background:rgba(255,255,255,.97) !important;
    }
}

</style>
""",
        "dark": """
<style>
.pn-v8-profile-bubble {
    color:#111827 !important;
    background:#ffffff !important;
    border:none !important;
    border-radius:50% !important;
}
.pn-v8-profile-letter {
    color:#111827 !important;
    -webkit-text-fill-color:#111827 !important;
}

/* Dark theme profile */
.pn-user-profile-bubble { color:#111827 !important; background:#ffffff !important; box-shadow:0 10px 24px rgba(0,0,0,.34),0 0 0 4px rgba(255,255,255,.08) !important; }
.pn-user-profile-letter { color:#111827 !important; -webkit-text-fill-color:#111827 !important; }
.pn-user-profile-online { background:#22c55e !important; border-color:#101c2f !important; }


/* Dark theme profile */
.pn-glass-profile {
    background:
        linear-gradient(
            145deg,
            rgba(27,42,68,.92),
            rgba(49,36,88,.78)
        ) !important;
    border:1px solid rgba(148,163,184,.20) !important;
    box-shadow:
        0 14px 30px rgba(0,0,0,.34),
        0 0 0 4px rgba(110,85,240,.08),
        inset 0 1px 0 rgba(255,255,255,.08) !important;
}

.pn-glass-avatar {
    color:#ffffff !important;
    background:
        linear-gradient(145deg,#3b82f6 0%,#7c3aed 58%,#c026d3 100%) !important;
    box-shadow:
        0 10px 22px rgba(91,64,220,.38),
        inset 0 1px 0 rgba(255,255,255,.18) !important;
}

.pn-profile-online {
    border-color:#101c2f !important;
    background:#22c55e !important;
}
.stApp {
    color:#f3f7ff !important;
    background:
        radial-gradient(circle at 82% 8%,rgba(91,72,214,.20),transparent 28%),
        linear-gradient(180deg,#091322 0%,#06101d 100%) !important;
}

header[data-testid="stHeader"] {
    background:rgba(8,18,32,.82) !important;
}

[data-testid="stSidebar"] {
    color:#f3f7ff !important;
    background:
        radial-gradient(circle at 20% 0%,rgba(60,110,220,.16),transparent 26%),
        linear-gradient(180deg,#0d192b 0%,#091423 100%) !important;
    border-right-color:rgba(148,163,184,.16) !important;
}

.pn-sidebar-user-card,
.pn-side-usage-card,
.pn-feature-card,
.st-key-composer_tools,
div[data-testid="stChatMessage"] {
    color:#f3f7ff !important;
    background:#101c2f !important;
    box-shadow:0 16px 38px rgba(0,0,0,.30) !important;
}

.pn-dashboard-hero {
    background:
        radial-gradient(circle at 80% 40%,rgba(107,72,245,.24),transparent 30%),
        linear-gradient(115deg,#101d31 0%,#13243e 48%,#241d45 100%) !important;
}

.pn-hero-copy h1,
.pn-feature-card h3,
.pn-popular strong,
.pn-sidebar-user-copy strong,
.pn-side-usage-head,
.pn-side-footer strong,
[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    color:#f3f7ff !important;
}

.pn-hero-copy p,
.pn-feature-card p,
.pn-sidebar-user-copy small,
.pn-side-usage-card small,
.pn-side-footer,
.pn-side-section-label {
    color:#a9b6cc !important;
}

.pn-popular span,
.st-key-composer_tools div[data-testid="stTextInput"] input,
.st-key-composer_tools [data-baseweb="input"] input,
.st-key-composer_tools div[data-testid="stPopover"] > button,
.st-key-composer_tools .st-key-composer_model_selector div[data-testid="stSelectbox"] > div > div,
[data-testid="stSidebar"] div[data-testid="stSelectbox"] > div > div,
[data-testid="stSidebar"] div[data-testid="stExpander"] details,
[data-testid="stSidebar"] div[data-testid="stExpander"] summary {
    color:#f3f7ff !important;
    -webkit-text-fill-color:#f3f7ff !important;
    background:#13233b !important;
}

.st-key-composer_tools div[data-testid="stTextInput"] input::placeholder {
    color:#91a0ba !important;
    -webkit-text-fill-color:#91a0ba !important;
}

[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover,
[data-testid="stSidebar"] div[data-testid="stExpander"] summary:hover,
[data-testid="stSidebar"] div[data-testid="stExpander"] details[open] > summary {
    color:#8fc2ff !important;
    background:#172b48 !important;
}

.pn-side-progress {
    background:#263b58 !important;
}


/* Direct Dark-theme chat visibility */
div[data-testid="stChatMessage"] {
    color:#f8fafc !important;
    background:#101c2f !important;
    border:1px solid rgba(148,163,184,.10) !important;
}

div[data-testid="stChatMessage"]
[data-testid="stMarkdownContainer"],
div[data-testid="stChatMessage"]
[data-testid="stMarkdownContainer"] *,
div[data-testid="stChatMessage"]
[data-testid="stChatMessageContent"],
div[data-testid="stChatMessage"] p,
div[data-testid="stChatMessage"] span,
div[data-testid="stChatMessage"] li,
div[data-testid="stChatMessage"] strong,
div[data-testid="stChatMessage"] em,
div[data-testid="stChatMessage"] h1,
div[data-testid="stChatMessage"] h2,
div[data-testid="stChatMessage"] h3,
div[data-testid="stChatMessage"] h4,
div[data-testid="stChatMessage"] h5,
div[data-testid="stChatMessage"] h6 {
    color:#f8fafc !important;
    -webkit-text-fill-color:#f8fafc !important;
    opacity:1 !important;
}

div[data-testid="stChatMessage"] a,
div[data-testid="stChatMessage"] a * {
    color:#7dd3fc !important;
    -webkit-text-fill-color:#7dd3fc !important;
}

div[data-testid="stChatMessage"] code {
    color:#bae6fd !important;
    -webkit-text-fill-color:#bae6fd !important;
    background:#1b304d !important;
}

div[data-testid="stChatMessage"] pre,
div[data-testid="stChatMessage"] pre *,
div[data-testid="stChatMessage"] [data-testid="stCodeBlock"] {
    color:#e5eefc !important;
    -webkit-text-fill-color:#e5eefc !important;
    background:#081321 !important;
}

div[data-testid="stChatMessage"] blockquote,
div[data-testid="stChatMessage"] blockquote * {
    color:#cbd5e1 !important;
    -webkit-text-fill-color:#cbd5e1 !important;
    border-left-color:#60a5fa !important;
}

div[data-testid="stChatMessage"] table,
div[data-testid="stChatMessage"] th,
div[data-testid="stChatMessage"] td {
    color:#f8fafc !important;
    -webkit-text-fill-color:#f8fafc !important;
    border-color:rgba(148,163,184,.18) !important;
}

div[data-testid="stChatMessage"] th {
    background:#162943 !important;
}

div[data-testid="stChatMessage"] td {
    background:#101c2f !important;
}

div[data-testid="stChatMessage"] div[data-testid="stButton"] > button {
    color:#dbeafe !important;
    -webkit-text-fill-color:#dbeafe !important;
    background:#162943 !important;
    border:1px solid rgba(148,163,184,.14) !important;
}

div[data-testid="stChatMessage"] div[data-testid="stButton"] > button:hover {
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    background:#1d3556 !important;
}

div[data-testid="stChatMessage"]
[data-testid="stChatMessageAvatarUser"],
div[data-testid="stChatMessage"]
[data-testid="stChatMessageAvatarAssistant"] {
    background:#1c3150 !important;
}


@media screen and (max-width:700px) {
    .st-key-mobile_composer {
        color:#f3f7ff !important;
        background:#101c2f !important;
        box-shadow:0 16px 36px rgba(0,0,0,.30) !important;
    }

    .st-key-mobile_composer div[data-testid="stTextInput"] input,
    .st-key-mobile_composer [data-baseweb="input"] input,
    .st-key-mobile_composer div[data-testid="stSelectbox"] > div > div,
    .st-key-mobile_composer div[data-testid="stPopover"] > button {
        color:#f3f7ff !important;
        -webkit-text-fill-color:#f3f7ff !important;
        background:#13233b !important;
    }

    .st-key-mobile_composer div[data-testid="stTextInput"] input::placeholder {
        color:#91a0ba !important;
        -webkit-text-fill-color:#91a0ba !important;
    }
}

</style>
""",
        "blue": """
<style>
.pn-v8-profile-bubble {
    color:#ffffff !important;
    background:linear-gradient(145deg,#0284c7 0%,#2563eb 55%,#4f46e5 100%) !important;
    border:none !important;
    border-radius:50% !important;
}
.pn-v8-profile-letter {
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
}

/* Blue theme profile */
.pn-user-profile-bubble { color:#ffffff !important; background:linear-gradient(145deg,#0284c7 0%,#2563eb 55%,#4f46e5 100%) !important; box-shadow:0 10px 24px rgba(2,84,170,.30),0 0 0 4px rgba(56,189,248,.08) !important; }
.pn-user-profile-letter { color:#ffffff !important; -webkit-text-fill-color:#ffffff !important; }
.pn-user-profile-online { background:#22c55e !important; border-color:#eaf4ff !important; }


/* Blue theme profile */
.pn-glass-profile {
    background:
        linear-gradient(
            145deg,
            rgba(244,250,255,.94),
            rgba(202,231,255,.78)
        ) !important;
    border:1px solid rgba(118,190,255,.42) !important;
    box-shadow:
        0 12px 28px rgba(0,116,217,.22),
        0 0 0 4px rgba(0,153,255,.07),
        inset 0 1px 0 rgba(255,255,255,.88) !important;
}

.pn-glass-avatar {
    background:
        linear-gradient(145deg,#0284c7 0%,#2563eb 52%,#6d28d9 100%) !important;
}

.pn-profile-online {
    border-color:#f4faff !important;
}
.stApp {
    color:#0b2f63 !important;
    background:
        radial-gradient(circle at 82% 8%,rgba(0,170,255,.16),transparent 28%),
        linear-gradient(180deg,#f4faff 0%,#e7f3ff 100%) !important;
}

[data-testid="stSidebar"] {
    background:
        radial-gradient(circle at 20% 0%,rgba(0,140,255,.16),transparent 26%),
        linear-gradient(180deg,#f3f9ff 0%,#eaf4ff 100%) !important;
    border-right-color:rgba(18,102,194,.14) !important;
}

.pn-dashboard-hero {
    background:
        radial-gradient(circle at 80% 40%,rgba(0,132,255,.18),transparent 30%),
        linear-gradient(115deg,#f5fbff 0%,#dff0ff 48%,#dce9ff 100%) !important;
}

.pn-sidebar-user-card,
.pn-side-usage-card,
.pn-feature-card,
.st-key-composer_tools,
div[data-testid="stChatMessage"] {
    box-shadow:0 14px 35px rgba(25,94,170,.12) !important;
}

[data-testid="stSidebar"] .st-key-side_new_chat button,
.st-key-composer_tools .st-key-composer_send button {
    background:linear-gradient(145deg,#0a84ff,#2563eb) !important;
}

.pn-popular span,
.st-key-composer_tools div[data-testid="stTextInput"] input,
.st-key-composer_tools [data-baseweb="input"] input,
.st-key-composer_tools div[data-testid="stPopover"] > button,
.st-key-composer_tools .st-key-composer_model_selector div[data-testid="stSelectbox"] > div > div {
    color:#0b2f63 !important;
    -webkit-text-fill-color:#0b2f63 !important;
    background:#eef7ff !important;
}


/* Prevent Streamlit/parent wrappers from clipping the profile */
div:has(> .pn-topbar-profile-only),
div:has(> .pn-topbar-profile-only) > div,
div:has(.pn-glass-profile) {
    overflow:visible !important;
}

/* Light-theme sizing */
.pn-glass-profile {
    transform:none !important;
}

/* Dark and Blue themes use exactly the same geometry */
@media (prefers-color-scheme: dark) {
    .pn-glass-profile,
    .pn-glass-avatar {
        transform:none !important;
    }
}

@media(max-width:700px) {
    .pn-topbar-profile-only {
        min-height:64px !important;
    }

    .pn-glass-profile {
        width:52px !important;
        height:52px !important;
        min-width:52px !important;
        min-height:52px !important;
        max-width:52px !important;
        max-height:52px !important;
        border-radius:18px !important;
    }

    .pn-glass-avatar {
        width:41px !important;
        height:41px !important;
        min-width:41px !important;
        min-height:41px !important;
        max-width:41px !important;
        max-height:41px !important;
        line-height:41px !important;
        font-size:.9rem !important;
    }
}


/* Light theme */
.pn-profile-bubble {
    background:linear-gradient(145deg,#2563eb,#8b3be8) !important;
    color:#ffffff !important;
}

/* Dark theme */
@media (prefers-color-scheme: dark) {
    .pn-profile-bubble {
        background:linear-gradient(145deg,#3b82f6,#8b5cf6) !important;
        box-shadow:
            0 12px 26px rgba(0,0,0,.34),
            0 0 0 4px rgba(99,102,241,.08) !important;
    }
}

/* Blue theme */
body.blue-theme .pn-profile-bubble,
.pn-profile-bubble.theme-blue {
    background:linear-gradient(145deg,#0284c7,#2563eb) !important;
}

@media(max-width:700px) {
    .pn-topbar-profile-only {
        min-height:58px !important;
    }

    .pn-profile-bubble {
        width:44px;
        height:44px;
        min-width:44px;
        min-height:44px;
    }

    .pn-profile-symbol {
        font-size:1.15rem;
    }
}


/* Light theme */
.pn-user-bubble-profile {
    background:
        linear-gradient(145deg,#3b82f6 0%,#6366f1 48%,#8b5cf6 100%) !important;
}

.pn-user-bubble-online {
    border-color:#ffffff !important;
}

/* Dark theme overrides embedded by active theme */
[data-testid="stChatMessage"] ~ .pn-topbar-profile-only
.pn-user-bubble-profile {
    color:#ffffff !important;
}

/* Blue theme */
body.blue-theme .pn-user-bubble-profile,
.pn-user-bubble-profile.theme-blue {
    background:
        linear-gradient(145deg,#0284c7 0%,#2563eb 52%,#6d28d9 100%) !important;
}

/* Prevent clipping from parent wrappers */
div:has(> .pn-topbar-profile-only),
div:has(> .pn-topbar-profile-only) > div,
div:has(.pn-user-bubble-profile) {
    overflow:visible !important;
}

@media(max-width:700px) {
    .pn-topbar-profile-only {
        min-height:58px !important;
    }

    .pn-user-bubble-profile {
        width:44px;
        height:44px;
        min-width:44px;
        min-height:44px;
    }

    .pn-user-bubble-letter {
        font-size:.92rem;
    }

    .pn-user-bubble-online {
        width:10px;
        height:10px;
    }
}


/* =========================================================
   V7 PROFILE BUBBLE — SHARED BY LIGHT, DARK AND BLUE THEMES
   ========================================================= */
.pn-glass-profile,
.pn-glass-avatar,
.pn-profile-online,
.pn-profile-menu,
.pn-profile-bubble,
.pn-profile-symbol,
.pn-profile-initial,
.pn-user-bubble-profile,
.pn-user-bubble-letter,
.pn-user-bubble-online,
.pn-chevron {
    display:none !important;
}

.pn-topbar-profile-only {
    width:100% !important;
    min-height:66px !important;
    height:66px !important;
    display:grid !important;
    grid-template-columns:minmax(0,1fr) 52px !important;
    align-items:center !important;
    column-gap:12px !important;
    margin:0 0 .55rem !important;
    padding:7px 5px 7px 0 !important;
    overflow:visible !important;
    box-sizing:border-box !important;
}

.pn-topbar-profile-only,
.pn-topbar-profile-only *,
.pn-user-profile-bubble,
.pn-user-profile-bubble * {
    box-sizing:border-box !important;
}

.pn-topbar-spacer {
    min-width:0 !important;
}

.pn-user-profile-bubble {
    position:relative !important;
    width:48px !important;
    height:48px !important;
    min-width:48px !important;
    min-height:48px !important;
    max-width:48px !important;
    max-height:48px !important;
    display:grid !important;
    place-items:center !important;
    justify-self:end !important;
    align-self:center !important;
    margin:0 !important;
    padding:0 !important;
    border:0 !important;
    outline:0 !important;
    border-radius:50% !important;
    color:#ffffff !important;
    background:linear-gradient(
        145deg,
        #3b82f6 0%,
        #6366f1 48%,
        #8b5cf6 100%
    ) !important;
    box-shadow:
        0 10px 24px rgba(76,74,230,.30),
        0 0 0 4px rgba(99,102,241,.08) !important;
    overflow:visible !important;
    opacity:1 !important;
    visibility:visible !important;
    transform:none !important;
    isolation:isolate !important;
    z-index:20 !important;
    transition:
        transform .18s ease,
        box-shadow .18s ease !important;
}

.pn-user-profile-bubble:hover {
    transform:translateY(-2px) scale(1.04) !important;
    box-shadow:
        0 14px 30px rgba(76,74,230,.38),
        0 0 0 5px rgba(99,102,241,.12) !important;
}

.pn-user-profile-letter {
    width:100% !important;
    height:100% !important;
    display:grid !important;
    place-items:center !important;
    margin:0 !important;
    padding:0 !important;
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    font-family:Inter,"Segoe UI",Arial,sans-serif !important;
    font-size:1rem !important;
    font-weight:950 !important;
    line-height:1 !important;
    text-align:center !important;
    text-transform:uppercase !important;
    opacity:1 !important;
    visibility:visible !important;
}

.pn-user-profile-online {
    position:absolute !important;
    right:-1px !important;
    bottom:-1px !important;
    width:11px !important;
    height:11px !important;
    min-width:11px !important;
    min-height:11px !important;
    display:block !important;
    border:2px solid #ffffff !important;
    border-radius:50% !important;
    background:#22c55e !important;
    box-shadow:
        0 0 0 3px rgba(34,197,94,.11),
        0 4px 10px rgba(34,197,94,.30) !important;
    opacity:1 !important;
    visibility:visible !important;
    z-index:22 !important;
}

/* Dark theme only changes the online-dot ring for contrast.
   The bubble itself remains identical in every theme. */
.stApp[style*="091322"] .pn-user-profile-online,
.stApp[style*="06101d"] .pn-user-profile-online {
    border-color:#101c2f !important;
}

/* Ensure Streamlit wrappers never clip the profile. */
div:has(> .pn-topbar-profile-only),
div:has(> .pn-topbar-profile-only) > div,
div:has(.pn-user-profile-bubble) {
    overflow:visible !important;
}

@media(max-width:700px) {
    .pn-topbar-profile-only {
        min-height:60px !important;
        height:60px !important;
        grid-template-columns:minmax(0,1fr) 46px !important;
        padding-top:7px !important;
        padding-bottom:7px !important;
    }

    .pn-user-profile-bubble {
        width:44px !important;
        height:44px !important;
        min-width:44px !important;
        min-height:44px !important;
        max-width:44px !important;
        max-height:44px !important;
    }

    .pn-user-profile-letter {
        font-size:.92rem !important;
    }

    .pn-user-profile-online {
        width:10px !important;
        height:10px !important;
        min-width:10px !important;
        min-height:10px !important;
    }
}
/* =========================================================
   MOBILE COMPOSER — CLEAN TWO-ROW LAYOUT
   ========================================================= */
@media screen and (max-width: 700px) {

    html,
    body,
    .stApp {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
    }

    .block-container {
        width: 100% !important;
        max-width: 100% !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
        padding-bottom: 6.5rem !important;
        overflow-x: hidden !important;
    }

    /* Composer outer card */
    .st-key-composer_tools {
        width: calc(100% - 0.2rem) !important;
        max-width: calc(100% - 0.2rem) !important;
        margin: 0.55rem auto !important;
        padding: 0.55rem !important;
        border-radius: 18px !important;
        box-sizing: border-box !important;
        overflow: visible !important;
    }

    /* Convert Streamlit columns into a mobile grid */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"] {
        width: 100% !important;
        max-width: 100% !important;

        display: grid !important;
        grid-template-columns:
            44px
            44px
            minmax(95px, 1fr)
            48px !important;

        grid-template-rows:
            50px
            46px !important;

        column-gap: 8px !important;
        row-gap: 9px !important;

        align-items: center !important;
        box-sizing: border-box !important;
    }

    /* Reset desktop column sizing */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"] {
        width: 100% !important;
        min-width: 0 !important;
        max-width: none !important;
        flex: none !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    /* Search field: complete first row */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(2) {
        grid-column: 1 / -1 !important;
        grid-row: 1 !important;
    }

    /* Plus / attachment */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(1) {
        grid-column: 1 !important;
        grid-row: 2 !important;
    }

    /* Dictate */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(3) {
        grid-column: 2 !important;
        grid-row: 2 !important;
    }

    /* Start voice */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(4) {
        display: none !important;
    }

    /* Model dropdown */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(5) {
        grid-column: 3 !important;
        grid-row: 2 !important;
    }

    /* Send button */
    .st-key-composer_tools
    [data-testid="stHorizontalBlock"]
    > [data-testid="column"]:nth-child(6) {
        grid-column: 4 !important;
        grid-row: 2 !important;
    }

    /* Search input width */
    .st-key-composer_tools div[data-testid="stTextInput"],
    .st-key-composer_tools div[data-testid="stTextInput"] > div,
    .st-key-composer_tools [data-baseweb="input"] {
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;
    }

    .st-key-composer_tools
    div[data-testid="stTextInput"] input {
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;
        height: 48px !important;

        padding: 0 0.9rem !important;
        font-size: 0.82rem !important;

        border-radius: 14px !important;
        box-sizing: border-box !important;
    }

    /* Plus button */
    .st-key-composer_tools
    div[data-testid="stPopover"] > button {
        width: 44px !important;
        height: 44px !important;
        min-width: 44px !important;
        min-height: 44px !important;
        padding: 0 !important;
        border-radius: 50% !important;
    }

    /* Dictate / microphone */
    .st-key-composer_tools iframe {
        width: 44px !important;
        height: 44px !important;
        min-width: 44px !important;
        min-height: 44px !important;
        max-width: 44px !important;
        max-height: 44px !important;
        border: none !important;
    }

    /* Model dropdown */
    .st-key-composer_tools
    div[data-testid="stSelectbox"],
    .st-key-composer_tools
    div[data-testid="stSelectbox"] > div {
        width: 100% !important;
        min-width: 0 !important;
        max-width: 100% !important;
    }

    .st-key-composer_tools
    div[data-testid="stSelectbox"] > div > div {
        width: 100% !important;
        min-width: 0 !important;
        height: 44px !important;

        padding-left: 0.45rem !important;
        padding-right: 0.3rem !important;

        border-radius: 14px !important;
        font-size: 0.66rem !important;
    }

    /* Send */
    .st-key-composer_tools
    .st-key-composer_send button {
        width: 46px !important;
        height: 46px !important;
        min-width: 46px !important;
        min-height: 46px !important;

        padding: 0 !important;
        border-radius: 50% !important;
    }

    /* Prevent mobile bottom navigation overlap */
    .pn-mobile-nav {
        z-index: 1000 !important;
    }
}

@media screen and (max-width:700px) {
    .st-key-mobile_composer {
        color:#0b2f63 !important;
        background:rgba(247,252,255,.98) !important;
        box-shadow:0 15px 34px rgba(25,94,170,.14) !important;
    }

    .st-key-mobile_composer div[data-testid="stTextInput"] input,
    .st-key-mobile_composer [data-baseweb="input"] input,
    .st-key-mobile_composer div[data-testid="stSelectbox"] > div > div,
    .st-key-mobile_composer div[data-testid="stPopover"] > button {
        color:#0b2f63 !important;
        -webkit-text-fill-color:#0b2f63 !important;
        background:#eef7ff !important;
    }
}

/* =========================================================
   MOBILE CHAT RESPONSE ACTIONS
   ========================================================= */
@media screen and (max-width:700px) {

    [class*="st-key-chat_actions_"] {
        width:100% !important;
        margin:.35rem 0 .2rem !important;
        padding:0 !important;
    }

    [class*="st-key-chat_actions_"]
    [data-testid="stHorizontalBlock"] {
        width:100% !important;
        display:grid !important;
        grid-template-columns:
            minmax(82px,auto)
            46px
            46px
            1fr !important;
        gap:7px !important;
        align-items:center !important;
    }

    [class*="st-key-chat_actions_"]
    [data-testid="column"] {
        width:100% !important;
        min-width:0 !important;
        max-width:none !important;
        flex:none !important;
        padding:0 !important;
        margin:0 !important;
    }

    /* Hide unused spacer column */
    [class*="st-key-chat_actions_"]
    [data-testid="column"]:nth-child(4) {
        display:none !important;
    }

    [class*="st-key-chat_actions_"]
    div[data-testid="stButton"] {
        width:100% !important;
        margin:0 !important;
    }

    [class*="st-key-chat_actions_"]
    div[data-testid="stButton"] > button {
        width:100% !important;
        height:40px !important;
        min-height:40px !important;
        margin:0 !important;
        padding:0 .55rem !important;
        border:1px solid rgba(37,99,235,.16) !important;
        border-radius:12px !important;
        background:#ffffff !important;
        box-shadow:0 5px 14px rgba(35,75,140,.07) !important;
        font-size:.72rem !important;
        white-space:nowrap !important;
    }

    /* Like and dislike buttons */
    [class*="st-key-chat_actions_"]
    [data-testid="column"]:nth-child(2)
    button,
    [class*="st-key-chat_actions_"]
    [data-testid="column"]:nth-child(3)
    button {
        width:42px !important;
        min-width:42px !important;
        padding:0 !important;
        border-radius:50% !important;
        font-size:.9rem !important;
    }
}

</style>
""",
    }

    st.html(
        themes.get(theme_name, themes["light"])
    )

    st.html(
        """
<style>
@media screen and (max-width:700px) {
    html, body, .stApp,
    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    .block-container {
        width:100% !important;
        min-width:0 !important;
        max-width:100vw !important;
        box-sizing:border-box !important;
        overflow-x:hidden !important;
    }

    [data-testid="stMainBlockContainer"],
    .block-container {
        padding-left:.45rem !important;
        padding-right:.45rem !important;
        padding-bottom:6.6rem !important;
    }

    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {
        display:none !important;
    }

    div[data-testid="stChatMessage"],
    div[data-testid="stChatMessage"] *,
    div[data-testid="stAlert"],
    div[data-testid="stAlert"] *,
    [data-testid="stException"],
    [data-testid="stException"] * {
        min-width:0 !important;
        max-width:100% !important;
        box-sizing:border-box !important;
        overflow-wrap:anywhere !important;
        word-break:break-word !important;
    }

    div[data-testid="stChatMessage"] pre,
    div[data-testid="stChatMessage"] code,
    div[data-testid="stAlert"] pre,
    div[data-testid="stAlert"] code,
    [data-testid="stException"] pre,
    [data-testid="stException"] code {
        white-space:pre-wrap !important;
        overflow-wrap:anywhere !important;
        word-break:break-word !important;
        max-width:100% !important;
        overflow-x:auto !important;
    }

    [class*="st-key-chat_actions_"] {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        overflow:hidden !important;
    }

    [class*="st-key-chat_actions_"] [data-testid="stHorizontalBlock"] {
        width:100% !important;
        display:grid !important;
        grid-template-columns:minmax(78px,94px) 42px 42px !important;
        gap:7px !important;
        justify-content:start !important;
        overflow:hidden !important;
    }

    [class*="st-key-chat_actions_"] [data-testid="column"] {
        width:100% !important;
        min-width:0 !important;
        flex:none !important;
        padding:0 !important;
        margin:0 !important;
    }

    [class*="st-key-chat_actions_"] [data-testid="column"]:nth-child(4) {
        display:none !important;
    }

    [class*="st-key-chat_actions_"] div[data-testid="stButton"] > button {
        height:40px !important;
        min-height:40px !important;
        border-radius:12px !important;
        font-size:.69rem !important;
        white-space:nowrap !important;
    }

    [class*="st-key-chat_actions_"] [data-testid="column"]:nth-child(2) button,
    [class*="st-key-chat_actions_"] [data-testid="column"]:nth-child(3) button {
        width:40px !important;
        min-width:40px !important;
        max-width:40px !important;
        padding:0 !important;
        border-radius:50% !important;
    }

    .st-key-composer_tools {
        display:none !important;
    }

    .st-key-mobile_composer {
        display:block !important;
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        margin:.65rem 0 .8rem !important;
        padding:.58rem !important;
        border-radius:20px !important;
        box-sizing:border-box !important;
        overflow:hidden !important;
    }

    .st-key-mobile_composer div[data-testid="stTextInput"],
    .st-key-mobile_composer div[data-testid="stTextInput"] > div,
    .st-key-mobile_composer [data-baseweb="input"] {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        box-sizing:border-box !important;
    }

    .st-key-mobile_composer div[data-testid="stTextInput"] input,
    .st-key-mobile_composer [data-baseweb="input"] input {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        height:48px !important;
        padding:0 .85rem !important;
        box-sizing:border-box !important;
        font-size:.82rem !important;
    }

    .st-key-mobile_composer [data-testid="stHorizontalBlock"] {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        display:grid !important;
        grid-template-columns:40px 40px 40px minmax(72px,1fr) 46px !important;
        gap:6px !important;
        align-items:center !important;
        margin-top:.55rem !important;
        box-sizing:border-box !important;
        overflow:hidden !important;
    }

    .st-key-mobile_composer [data-testid="stHorizontalBlock"] > [data-testid="column"] {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        flex:none !important;
        margin:0 !important;
        padding:0 !important;
        overflow:hidden !important;
    }

    .st-key-mobile_composer div[data-testid="stPopover"],
    .st-key-mobile_composer div[data-testid="stPopover"] > button,
    .st-key-mobile_composer iframe {
        width:40px !important;
        min-width:40px !important;
        max-width:40px !important;
        height:40px !important;
        min-height:40px !important;
        max-height:40px !important;
        margin:0 !important;
        padding:0 !important;
        box-sizing:border-box !important;
    }

    .st-key-mobile_composer div[data-testid="stSelectbox"],
    .st-key-mobile_composer div[data-testid="stSelectbox"] > div {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
    }

    .st-key-mobile_composer div[data-testid="stSelectbox"] > div > div {
        width:100% !important;
        min-width:0 !important;
        max-width:100% !important;
        height:42px !important;
        min-height:42px !important;
        font-size:.57rem !important;
        white-space:nowrap !important;
        overflow:hidden !important;
        box-sizing:border-box !important;
    }

    .st-key-mobile_composer .st-key-mobile_composer_send,
    .st-key-mobile_composer .st-key-mobile_composer_send button {
        width:46px !important;
        min-width:46px !important;
        max-width:46px !important;
        height:46px !important;
        min-height:46px !important;
        max-height:46px !important;
        margin:0 !important;
        padding:0 !important;
        box-sizing:border-box !important;
        transform:none !important;
    }

    .st-key-mobile_nav {
        left:0 !important;
        right:0 !important;
        width:100vw !important;
        max-width:100vw !important;
        box-sizing:border-box !important;
        overflow:hidden !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   LOGIN LOGO — RELIABLE PHONE CENTERING
   Desktop/laptop/tablet remain unchanged.
   ========================================================= */

.pn-mobile-login-logo {
    display:none;
}

/* Phone only */
@media screen and (max-width:600px) {
    .st-key-login_logo_desktop {
        display:none !important;
    }

    .pn-mobile-login-logo {
        width:100% !important;
        display:flex !important;
        justify-content:center !important;
        align-items:center !important;
        margin:0 auto .7rem !important;
        padding:.25rem 0 0 !important;
        text-align:center !important;
        box-sizing:border-box !important;
    }

    .pn-mobile-login-logo img {
        display:block !important;
        width:145px !important;
        max-width:145px !important;
        height:auto !important;
        margin:0 auto !important;
        padding:0 !important;
        object-fit:contain !important;
    }
}

/* Tablet/laptop/desktop */
@media screen and (min-width:601px) {
    .st-key-login_logo_desktop {
        display:block !important;
    }

    .pn-mobile-login-logo {
        display:none !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* PHONE-ONLY SETTINGS THEME CONTROL */
@media screen and (max-width:600px) {
    .st-key-settings_theme_selector {
        width:100% !important;
        max-width:260px !important;
        margin:.2rem 0 .8rem !important;
    }

    .st-key-settings_theme_selector div[data-testid="stSelectbox"],
    .st-key-settings_theme_selector div[data-testid="stSelectbox"] > div {
        width:100% !important;
        max-width:260px !important;
    }

    .st-key-settings_theme_selector
    div[data-testid="stSelectbox"] > div > div {
        min-height:40px !important;
        height:40px !important;
        border:none !important;
        border-radius:12px !important;
        background:#eef4ff !important;
        box-shadow:0 7px 18px rgba(54,94,170,.10) !important;
        font-size:.75rem !important;
        font-weight:750 !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   SETTINGS THEME SELECTOR — DARK MODE READABILITY FIX
   Scope is limited to the Settings theme selector only.
   ========================================================= */

.st-key-settings_theme_selector [data-baseweb="select"] > div,
.st-key-settings_theme_selector [data-baseweb="select"] span,
.st-key-settings_theme_selector [data-baseweb="select"] input,
.st-key-settings_theme_selector [data-baseweb="select"] svg {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
}

/* Keep the closed selector light so "Light / Dark / Blue" remains visible
   even when the rest of the app uses the Dark theme. */
.st-key-settings_theme_selector
div[data-testid="stSelectbox"] > div > div {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    background:#f7fbff !important;
    border:1px solid rgba(80,91,230,.18) !important;
    box-shadow:0 7px 18px rgba(54,94,170,.10) !important;
}

/* Selected value text */
.st-key-settings_theme_selector
[data-baseweb="select"] div {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
}

/* Dropdown arrow */
.st-key-settings_theme_selector svg {
    color:#5d4bdd !important;
    fill:#5d4bdd !important;
}

/* Phone sizing stays compact. */
@media screen and (max-width:600px) {
    .st-key-settings_theme_selector
    div[data-testid="stSelectbox"] > div > div {
        min-height:40px !important;
        height:40px !important;
        border-radius:12px !important;
        font-size:.75rem !important;
        font-weight:750 !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* Settings > Appearance > Theme: field-label contrast fix */
.st-key-settings_theme_selector label,
.st-key-settings_theme_selector label p,
.st-key-settings_theme_selector [data-testid="stWidgetLabel"],
.st-key-settings_theme_selector [data-testid="stWidgetLabel"] p {
    color:#dce9ff !important;
    -webkit-text-fill-color:#dce9ff !important;
    opacity:1 !important;
    font-weight:700 !important;
}

/* Do not disturb the already-readable selected value. */
.st-key-settings_theme_selector [data-baseweb="select"] > div,
.st-key-settings_theme_selector [data-baseweb="select"] span,
.st-key-settings_theme_selector [data-baseweb="select"] div {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    opacity:1 !important;
}

@media screen and (max-width:600px) {
    .st-key-settings_theme_selector label,
    .st-key-settings_theme_selector label p,
    .st-key-settings_theme_selector [data-testid="stWidgetLabel"],
    .st-key-settings_theme_selector [data-testid="stWidgetLabel"] p {
        color:#eef5ff !important;
        -webkit-text-fill-color:#eef5ff !important;
        opacity:1 !important;
        font-size:.82rem !important;
        font-weight:800 !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   FINAL SETTINGS THEME LABEL CONTRAST
   Custom label replaces Streamlit native widget label.
   ========================================================= */

.pn-settings-theme-label {
    margin:.15rem 0 .35rem !important;
    padding:0 !important;
    opacity:1 !important;
    font-size:.86rem !important;
    font-weight:800 !important;
    line-height:1.25 !important;
}

/* Hide any residual native selectbox label area for this widget. */
.st-key-settings_theme_selector
[data-testid="stWidgetLabel"] {
    display:none !important;
}

/* Keep the selected value readable on the light selector surface
   in Light, Dark and Blue themes. */
.st-key-settings_theme_selector
div[data-testid="stSelectbox"] > div > div,
.st-key-settings_theme_selector
[data-baseweb="select"] > div {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    background:#f7fbff !important;
    opacity:1 !important;
}

/* Selected value text */
.st-key-settings_theme_selector
[data-baseweb="select"] span,
.st-key-settings_theme_selector
[data-baseweb="select"] div {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    opacity:1 !important;
}

/* Dropdown arrow */
.st-key-settings_theme_selector svg {
    color:#5d4bdd !important;
    fill:#5d4bdd !important;
}

/* Phone-only compact sizing */
@media screen and (max-width:600px) {
    .pn-settings-theme-label {
        margin:.1rem 0 .3rem !important;
        font-size:.82rem !important;
        font-weight:850 !important;
    }

    .st-key-settings_theme_selector {
        width:100% !important;
        max-width:260px !important;
        margin:0 0 .85rem !important;
    }

    .st-key-settings_theme_selector
    div[data-testid="stSelectbox"] > div > div {
        min-height:40px !important;
        height:40px !important;
        border-radius:12px !important;
        font-size:.75rem !important;
        font-weight:750 !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   SETTINGS THEME LABEL — ALL SCREEN SIZES
   Applies to mobile, tablet, laptop and desktop.
   ========================================================= */

.pn-settings-theme-label {
    display:block !important;
    margin:.15rem 0 .38rem !important;
    padding:0 !important;
    opacity:1 !important;
    font-size:.9rem !important;
    font-weight:800 !important;
    line-height:1.25 !important;
}

/* Completely suppress Streamlit's native selectbox label so it cannot
   overlap or inherit the wrong theme color on any screen size. */
.st-key-settings_theme_selector [data-testid="stWidgetLabel"],
.st-key-settings_theme_selector label {
    display:none !important;
}

/* Selector stays intentionally light in all themes for reliable contrast. */
.st-key-settings_theme_selector {
    width:100% !important;
    max-width:340px !important;
    margin:0 0 .9rem !important;
}

.st-key-settings_theme_selector div[data-testid="stSelectbox"],
.st-key-settings_theme_selector div[data-testid="stSelectbox"] > div {
    width:100% !important;
    max-width:340px !important;
}

.st-key-settings_theme_selector
div[data-testid="stSelectbox"] > div > div,
.st-key-settings_theme_selector
[data-baseweb="select"] > div {
    min-height:44px !important;
    height:44px !important;
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    background:#f7fbff !important;
    border:1px solid rgba(80,91,230,.18) !important;
    border-radius:12px !important;
    box-shadow:0 7px 18px rgba(54,94,170,.10) !important;
    opacity:1 !important;
    font-size:.82rem !important;
    font-weight:750 !important;
}

/* Selected value */
.st-key-settings_theme_selector [data-baseweb="select"] span,
.st-key-settings_theme_selector [data-baseweb="select"] div {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    opacity:1 !important;
}

/* Dropdown arrow */
.st-key-settings_theme_selector svg {
    color:#5d4bdd !important;
    fill:#5d4bdd !important;
}

/* Tablet */
@media screen and (min-width:601px) and (max-width:1100px) {
    .pn-settings-theme-label {
        font-size:.88rem !important;
    }

    .st-key-settings_theme_selector {
        max-width:320px !important;
    }

    .st-key-settings_theme_selector
    div[data-testid="stSelectbox"] > div > div {
        min-height:42px !important;
        height:42px !important;
    }
}

/* Phone */
@media screen and (max-width:600px) {
    .pn-settings-theme-label {
        margin:.1rem 0 .3rem !important;
        font-size:.82rem !important;
        font-weight:850 !important;
    }

    .st-key-settings_theme_selector {
        max-width:260px !important;
    }

    .st-key-settings_theme_selector
    div[data-testid="stSelectbox"] > div > div {
        min-height:40px !important;
        height:40px !important;
        font-size:.75rem !important;
    }
}

/* Laptop / desktop */
@media screen and (min-width:1101px) {
    .pn-settings-theme-label {
        font-size:.9rem !important;
    }

    .st-key-settings_theme_selector {
        max-width:340px !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   FINAL THEME LABEL CONTRAST — ALL DEVICES
   Mobile / Tablet / Laptop / Desktop
   ========================================================= */

.pn-settings-theme-label {
    display:block !important;
    margin:.15rem 0 .38rem !important;
    padding:0 !important;
    opacity:1 !important;
    font-weight:800 !important;
    line-height:1.25 !important;
    /* Do NOT set color here.
       app.py provides the active-theme color inline:
       Light -> navy, Dark -> white, Blue -> navy. */
}

/* Never show Streamlit's native label; it can inherit the wrong theme color. */
.st-key-settings_theme_selector [data-testid="stWidgetLabel"],
.st-key-settings_theme_selector label {
    display:none !important;
}

/* Selected theme value remains readable in every app theme. */
.st-key-settings_theme_selector
div[data-testid="stSelectbox"] > div > div,
.st-key-settings_theme_selector
[data-baseweb="select"] > div,
.st-key-settings_theme_selector
[data-baseweb="select"] span {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    background:#f7fbff !important;
    opacity:1 !important;
}

/* Mobile */
@media screen and (max-width:600px) {
    .pn-settings-theme-label {
        font-size:.82rem !important;
    }
}

/* Tablet */
@media screen and (min-width:601px) and (max-width:1100px) {
    .pn-settings-theme-label {
        font-size:.88rem !important;
    }
}

/* Laptop + Desktop */
@media screen and (min-width:1101px) {
    .pn-settings-theme-label {
        font-size:.90rem !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   FINAL THEME LABEL CONTRAST
   Applies to:
   - Settings Theme selector
   - Sidebar Theme selector
   Across mobile / tablet / laptop / desktop
   ========================================================= */

/* SETTINGS custom label */
.pn-settings-theme-label {
    display:block !important;
    margin:.15rem 0 .38rem !important;
    padding:0 !important;
    opacity:1 !important;
    font-weight:800 !important;
    line-height:1.25 !important;
}

/* SIDEBAR custom label */
.pn-sidebar-theme-label {
    display:block !important;
    margin:.55rem .15rem .28rem !important;
    padding:0 !important;
    opacity:1 !important;
    font-size:.72rem !important;
    font-weight:850 !important;
    line-height:1.2 !important;
}

/* Hide Streamlit native labels in both locations so inherited theme
   colors can never cause overlap or low contrast. */
.st-key-settings_theme_selector [data-testid="stWidgetLabel"],
.st-key-settings_theme_selector label,
.st-key-sidebar_theme_selector [data-testid="stWidgetLabel"],
.st-key-sidebar_theme_selector label {
    display:none !important;
}

/* SETTINGS selector value */
.st-key-settings_theme_selector
div[data-testid="stSelectbox"] > div > div,
.st-key-settings_theme_selector
[data-baseweb="select"] > div,
.st-key-settings_theme_selector
[data-baseweb="select"] span {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    background:#f7fbff !important;
    opacity:1 !important;
}

/* SIDEBAR selector value */
.st-key-sidebar_theme_selector
div[data-testid="stSelectbox"] > div > div,
.st-key-sidebar_theme_selector
[data-baseweb="select"] > div,
.st-key-sidebar_theme_selector
[data-baseweb="select"] span {
    color:#17335f !important;
    -webkit-text-fill-color:#17335f !important;
    background:#f7fbff !important;
    opacity:1 !important;
}

/* Dropdown arrows */
.st-key-settings_theme_selector svg,
.st-key-sidebar_theme_selector svg {
    color:#5d4bdd !important;
    fill:#5d4bdd !important;
}

/* Phone */
@media screen and (max-width:600px) {
    .pn-settings-theme-label {
        font-size:.82rem !important;
    }

    /* Sidebar is hidden on phone, but keep this safe if shown later. */
    .pn-sidebar-theme-label {
        font-size:.72rem !important;
    }
}

/* Tablet */
@media screen and (min-width:601px) and (max-width:1100px) {
    .pn-settings-theme-label {
        font-size:.88rem !important;
    }

    .pn-sidebar-theme-label {
        font-size:.72rem !important;
    }
}

/* Laptop + Desktop */
@media screen and (min-width:1101px) {
    .pn-settings-theme-label {
        font-size:.90rem !important;
    }

    .pn-sidebar-theme-label {
        font-size:.74rem !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   GLOBAL TOP-SPACE FIX
   Login + Dashboard | Phone + Tablet + Laptop + Desktop
   ========================================================= */

/* Style-only containers must never consume vertical layout space. */
div[data-testid="stElementContainer"]:has(
    div[data-testid="stMarkdownContainer"] > style
) {
    display:none !important;
    height:0 !important;
    min-height:0 !important;
    margin:0 !important;
    padding:0 !important;
}

/* Keep the main content close to the top edge. */
[data-testid="stMainBlockContainer"],
.block-container {
    margin-top:0 !important;
}

/* Desktop / laptop */
@media screen and (min-width:1101px) {
    [data-testid="stMainBlockContainer"],
    .block-container {
        padding-top:.35rem !important;
    }
}

/* Tablet */
@media screen and (min-width:601px) and (max-width:1100px) {
    [data-testid="stMainBlockContainer"],
    .block-container {
        padding-top:.25rem !important;
    }
}

/* Phone */
@media screen and (max-width:600px) {
    [data-testid="stMainBlockContainer"],
    .block-container {
        padding-top:.18rem !important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* =========================================================
   PEERNET AI — STOP BUTTON + COMPOSER INPUT HINT FIX
   Only these two requested changes are applied.
   ========================================================= */

/* Hide "Press Enter to apply" and 0/4000 in composer inputs only. */
.st-key-composer_tools [data-testid="InputInstructions"],
.st-key-mobile_composer [data-testid="InputInstructions"],
.st-key-composer_prompt [data-testid="InputInstructions"],
.st-key-mobile_composer_prompt [data-testid="InputInstructions"] {
    display:none !important;
    visibility:hidden !important;
    height:0 !important;
    min-height:0 !important;
    max-height:0 !important;
    margin:0 !important;
    padding:0 !important;
    overflow:hidden !important;
}

.st-key-composer_tools div[data-testid="stTextInput"],
.st-key-mobile_composer div[data-testid="stTextInput"] {
    margin-bottom:0 !important;
    padding-bottom:0 !important;
}

/* Desktop / laptop / tablet Stop button */
[class*="st-key-composer_stop"] {
    width:54px !important;
    min-width:54px !important;
    max-width:54px !important;
    height:54px !important;
    min-height:54px !important;
    max-height:54px !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    margin:0 !important;
    padding:0 !important;
    border-radius:50% !important;
}

[class*="st-key-composer_stop"] button {
    width:54px !important;
    min-width:54px !important;
    max-width:54px !important;
    height:54px !important;
    min-height:54px !important;
    max-height:54px !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
    margin:0 !important;
    padding:0 !important;
    border:0 !important;
    outline:0 !important;
    border-radius:50% !important;
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    background:linear-gradient(145deg,#ef4444 0%,#e11d48 52%,#a21caf 100%) !important;
    box-shadow:
        0 10px 24px rgba(225,29,72,.30),
        0 0 0 5px rgba(239,68,68,.09) !important;
    font-size:1rem !important;
    font-weight:900 !important;
    line-height:1 !important;
}

[class*="st-key-composer_stop"] button p {
    margin:0 !important;
    padding:0 !important;
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    font-size:1rem !important;
    font-weight:900 !important;
    line-height:1 !important;
}

[class*="st-key-composer_stop"] button:hover {
    color:#ffffff !important;
    -webkit-text-fill-color:#ffffff !important;
    filter:brightness(1.07) !important;
}

/* Mobile Stop button */
@media screen and (max-width:700px) {
    [class*="st-key-mobile_composer_stop"] {
        width:48px !important;
        min-width:48px !important;
        max-width:48px !important;
        height:48px !important;
        min-height:48px !important;
        max-height:48px !important;
        display:flex !important;
        align-items:center !important;
        justify-content:center !important;
        margin:0 !important;
        padding:0 !important;
        border-radius:50% !important;
    }

    [class*="st-key-mobile_composer_stop"] button {
        width:48px !important;
        min-width:48px !important;
        max-width:48px !important;
        height:48px !important;
        min-height:48px !important;
        max-height:48px !important;
        display:flex !important;
        align-items:center !important;
        justify-content:center !important;
        margin:0 !important;
        padding:0 !important;
        border:0 !important;
        outline:0 !important;
        border-radius:50% !important;
        color:#ffffff !important;
        -webkit-text-fill-color:#ffffff !important;
        background:linear-gradient(145deg,#ef4444 0%,#e11d48 52%,#a21caf 100%) !important;
        box-shadow:
            0 9px 21px rgba(225,29,72,.28),
            0 0 0 4px rgba(239,68,68,.08) !important;
        font-size:.95rem !important;
        font-weight:900 !important;
        line-height:1 !important;
    }

    [class*="st-key-mobile_composer_stop"] button p {
        margin:0 !important;
        padding:0 !important;
        color:#ffffff !important;
        -webkit-text-fill-color:#ffffff !important;
        font-size:.95rem !important;
        font-weight:900 !important;
        line-height:1 !important;
    }
}
</style>
        """
    )


    # Modern liquid-glass login treatment.
    # Every layout rule is scoped to the authentication row so dashboard,
    # simulator, connectivity monitor, and authenticated pages are untouched.
    st.html(
        """
<style>
/* PEERNET AUTH — MODERN LIQUID GLASS (SCOPED) */
.pn-auth-title {
    position:relative;
    z-index:1;
    max-width:920px;
    margin:.35rem auto 1.15rem;
    padding:.7rem 1rem;
    isolation:isolate;
}

.pn-auth-title::before,
.pn-auth-title::after {
    content:"";
    position:fixed;
    z-index:-1;
    border-radius:999px;
    pointer-events:none;
    filter:blur(10px);
    opacity:.62;
    animation:pn-liquid-float 13s ease-in-out infinite alternate;
}

.pn-auth-title::before {
    width:clamp(220px,31vw,470px);
    height:clamp(220px,31vw,470px);
    top:4vh;
    left:-9vw;
    background:radial-gradient(circle at 35% 35%,
        rgba(0,198,255,.34),rgba(37,99,235,.16) 45%,transparent 72%);
}

.pn-auth-title::after {
    width:clamp(250px,34vw,520px);
    height:clamp(250px,34vw,520px);
    right:-10vw;
    bottom:-11vh;
    background:radial-gradient(circle at 45% 42%,
        rgba(236,72,153,.24),rgba(124,58,237,.18) 48%,transparent 73%);
    animation-delay:-5s;
}

.pn-auth-title h1 {
    text-shadow:0 8px 28px rgba(37,99,235,.10);
}

.pn-auth-title p {
    margin:.45rem auto 0;
    max-width:720px;
    font-weight:600;
    letter-spacing:.005em;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card) {
    position:relative;
    z-index:1;
    gap:clamp(1rem,2.2vw,2rem)!important;
    padding:clamp(.35rem,1vw,.8rem);
    border:1px solid rgba(255,255,255,.72);
    border-radius:32px;
    background:
        linear-gradient(135deg,rgba(255,255,255,.44),rgba(237,246,255,.20));
    box-shadow:
        0 26px 70px rgba(30,76,145,.14),
        inset 0 1px 0 rgba(255,255,255,.92);
    backdrop-filter:blur(22px) saturate(145%);
    -webkit-backdrop-filter:blur(22px) saturate(145%);
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stVerticalBlockBorderWrapper"],
.st-key-auth_visual_card
> div[data-testid="stVerticalBlockBorderWrapper"] {
    border:1px solid rgba(255,255,255,.74)!important;
    border-radius:27px!important;
    background:
        linear-gradient(145deg,rgba(255,255,255,.78),rgba(238,247,255,.48))!important;
    box-shadow:
        0 20px 48px rgba(20,75,150,.13),
        inset 0 1px 0 rgba(255,255,255,.96)!important;
    backdrop-filter:blur(24px) saturate(150%)!important;
    -webkit-backdrop-filter:blur(24px) saturate(150%)!important;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stTabs"] {
    padding:.28rem;
    border:1px solid rgba(113,151,221,.19);
    border-radius:17px;
    background:rgba(225,239,255,.48);
    box-shadow:inset 0 1px 0 rgba(255,255,255,.9);
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stTabs"] button {
    border-radius:13px!important;
    transition:transform .2s ease,background .2s ease,box-shadow .2s ease;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stTabs"] button[aria-selected="true"] {
    color:#075fc7!important;
    background:rgba(255,255,255,.86)!important;
    box-shadow:0 8px 22px rgba(35,91,177,.13),inset 0 1px 0 #fff;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stForm"] {
    border:1px solid rgba(255,255,255,.78)!important;
    border-radius:20px!important;
    background:rgba(255,255,255,.48)!important;
    box-shadow:inset 0 1px 0 rgba(255,255,255,.92)!important;
    backdrop-filter:blur(16px)!important;
    -webkit-backdrop-filter:blur(16px)!important;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stTextInput"] input {
    min-height:48px;
    border:1px solid rgba(84,132,215,.22)!important;
    border-radius:14px!important;
    background:rgba(255,255,255,.66)!important;
    box-shadow:inset 0 1px 0 rgba(255,255,255,.96);
    transition:border-color .2s ease,box-shadow .2s ease,transform .2s ease;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stTextInput"] input:focus {
    border-color:rgba(37,99,235,.56)!important;
    box-shadow:0 0 0 4px rgba(37,99,235,.11),inset 0 1px 0 #fff!important;
    transform:translateY(-1px);
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stFormSubmitButton"] > button,
[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stButton"] > button {
    min-height:48px;
    border:1px solid rgba(255,255,255,.52)!important;
    border-radius:15px!important;
    color:#fff!important;
    background:linear-gradient(110deg,#0876f9 0%,#6554f2 50%,#d83ebd 100%)!important;
    box-shadow:
        0 13px 28px rgba(78,75,224,.25),
        inset 0 1px 0 rgba(255,255,255,.38)!important;
    transition:transform .2s ease,box-shadow .2s ease,filter .2s ease;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stFormSubmitButton"] > button:hover,
[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
> [data-testid="column"]:first-child
div[data-testid="stButton"] > button:hover {
    transform:translateY(-2px);
    filter:saturate(1.08);
    box-shadow:
        0 17px 34px rgba(78,75,224,.31),
        0 0 0 4px rgba(101,84,242,.08)!important;
}

.st-key-auth_visual_card .pn-auth-image-copy {
    padding:0 1rem 1rem;
}

.st-key-auth_visual_card .pn-auth-pills span {
    border:1px solid rgba(255,255,255,.78)!important;
    background:rgba(255,255,255,.62)!important;
    box-shadow:0 7px 18px rgba(43,89,158,.09),inset 0 1px 0 #fff;
    backdrop-filter:blur(12px);
    -webkit-backdrop-filter:blur(12px);
    transition:transform .2s ease,box-shadow .2s ease;
}

.st-key-auth_visual_card .pn-auth-pills span:hover {
    transform:translateY(-2px);
    box-shadow:0 11px 23px rgba(43,89,158,.14),inset 0 1px 0 #fff;
}

@keyframes pn-liquid-float {
    0% { transform:translate3d(0,0,0) scale(1); }
    55% { transform:translate3d(3vw,2vh,0) scale(1.07); }
    100% { transform:translate3d(-1vw,5vh,0) scale(.96); }
}

@media(max-width:900px) {
    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card) {
        padding:.45rem;
        border-radius:25px;
    }
}

@media(max-width:600px) {
    .pn-auth-title {
        margin:.1rem auto .65rem;
        padding:.35rem .45rem;
    }

    .pn-auth-title h1 {
        font-size:clamp(1.85rem,9vw,2.4rem);
    }

    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card) {
        gap:.8rem!important;
        padding:.2rem;
        border-radius:22px;
    }

    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
    > [data-testid="column"]:first-child
    div[data-testid="stVerticalBlockBorderWrapper"],
    .st-key-auth_visual_card
    > div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius:21px!important;
    }
}

@media(prefers-reduced-motion:reduce) {
    .pn-auth-title::before,
    .pn-auth-title::after {
        animation:none!important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* PEERNET AUTH ENHANCEMENTS — SCOPED */

/* Light network-node pattern behind the two login cards. */
[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)::before {
    content:"";
    position:absolute;
    inset:0;
    z-index:-1;
    border-radius:32px;
    pointer-events:none;
    opacity:.38;
    background-image:
        radial-gradient(circle at 8% 18%,rgba(29,120,236,.56) 0 3px,transparent 4px),
        radial-gradient(circle at 22% 76%,rgba(124,58,237,.42) 0 3px,transparent 4px),
        radial-gradient(circle at 44% 27%,rgba(0,184,219,.44) 0 3px,transparent 4px),
        radial-gradient(circle at 63% 82%,rgba(37,99,235,.40) 0 3px,transparent 4px),
        radial-gradient(circle at 82% 20%,rgba(216,62,189,.36) 0 3px,transparent 4px),
        radial-gradient(circle at 94% 68%,rgba(0,184,219,.40) 0 3px,transparent 4px),
        linear-gradient(26deg,transparent 18%,rgba(77,135,224,.13) 18.15%,rgba(77,135,224,.13) 18.35%,transparent 18.5%),
        linear-gradient(151deg,transparent 31%,rgba(114,92,225,.11) 31.15%,rgba(114,92,225,.11) 31.35%,transparent 31.5%),
        linear-gradient(62deg,transparent 67%,rgba(0,174,220,.10) 67.15%,rgba(0,174,220,.10) 67.35%,transparent 67.5%);
}

/* Keep the form and visual columns exactly the same height on wider screens. */
@media(min-width:901px) {
    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
    > [data-testid="column"] {
        align-self:stretch!important;
    }

    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
    > [data-testid="column"]
    > div[data-testid="stVerticalBlock"] {
        height:100%!important;
    }

    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
    > [data-testid="column"]:first-child
    > div[data-testid="stVerticalBlock"]
    > div[data-testid="stVerticalBlockBorderWrapper"],
    .st-key-auth_visual_card
    > div[data-testid="stVerticalBlockBorderWrapper"] {
        min-height:100%!important;
        height:100%!important;
        box-sizing:border-box!important;
    }
}

/* Full-resolution source logo: same artwork and visual size, sharper on zoom. */
.pn-desktop-login-logo {
    width:100%;
    display:flex;
    justify-content:center;
    align-items:center;
    margin:0 auto .55rem;
    padding:.15rem 0 0;
    text-align:center;
}

.pn-desktop-login-logo img {
    display:block;
    width:145px;
    max-width:145px;
    height:auto;
    margin:0 auto;
    object-fit:contain;
    image-rendering:auto;
}

.st-key-send_reset_link button {
    border:1px solid rgba(255,255,255,.56)!important;
    color:#fff!important;
    -webkit-text-fill-color:#fff!important;
    background:linear-gradient(110deg,#0891b2 0%,#0b78e3 52%,#6d4bea 100%)!important;
    box-shadow:
        0 13px 27px rgba(11,120,227,.25),
        inset 0 1px 0 rgba(255,255,255,.38)!important;
}

.st-key-send_reset_link button:hover {
    background:linear-gradient(110deg,#0787a7 0%,#086ed2 52%,#6240dc 100%)!important;
    box-shadow:
        0 17px 33px rgba(11,120,227,.31),
        0 0 0 4px rgba(11,120,227,.09)!important;
}

@media(max-width:600px) {
    .pn-desktop-login-logo {
        display:none!important;
    }

    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)::before {
        border-radius:22px;
        opacity:.27;
    }
}

@media(min-width:601px) {
    .pn-desktop-login-logo {
        display:flex!important;
    }

    .pn-mobile-login-logo {
        display:none!important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* AUTH BUTTON CLIPPING FIX — SCOPED */

/* Let tab content determine the required card height. The columns still
   stretch together, but neither form nor its action button can be clipped. */
@media(min-width:901px) {
    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
    > [data-testid="column"]:first-child
    > div[data-testid="stVerticalBlock"]
    > div[data-testid="stVerticalBlockBorderWrapper"],
    .st-key-auth_visual_card
    > div[data-testid="stVerticalBlockBorderWrapper"] {
        height:auto!important;
        min-height:100%!important;
        overflow:visible!important;
    }

    [data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
    > [data-testid="column"]:first-child {
        overflow:visible!important;
    }
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
div[data-testid="stForm"],
[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
div[data-testid="stForm"] > div {
    overflow:visible!important;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
div[data-testid="stFormSubmitButton"] {
    width:100%!important;
    min-height:52px!important;
    padding:2px 0 3px!important;
    overflow:visible!important;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
div[data-testid="stFormSubmitButton"] > button {
    width:100%!important;
    min-height:48px!important;
    height:auto!important;
    margin:0!important;
    padding:.72rem 1rem!important;
    line-height:1.2!important;
    overflow:visible!important;
}

[data-testid="stHorizontalBlock"]:has(.st-key-auth_visual_card)
div[data-testid="stFormSubmitButton"] > button p {
    margin:0!important;
    line-height:1.2!important;
}

/* Dedicated verification action color. */
.st-key-resend_verification button {
    min-height:46px!important;
    border:1px solid rgba(255,255,255,.58)!important;
    border-radius:14px!important;
    color:#fff!important;
    -webkit-text-fill-color:#fff!important;
    background:linear-gradient(110deg,#059669 0%,#0ea5a8 48%,#0b78e3 100%)!important;
    box-shadow:
        0 12px 25px rgba(5,150,105,.22),
        inset 0 1px 0 rgba(255,255,255,.38)!important;
}

.st-key-resend_verification button:hover {
    transform:translateY(-2px);
    background:linear-gradient(110deg,#047f5a 0%,#0c9296 48%,#086bc9 100%)!important;
    box-shadow:
        0 16px 31px rgba(5,150,105,.28),
        0 0 0 4px rgba(14,165,168,.09)!important;
}
</style>
        """
    )


    st.html(
        """
<style>
/* SIDEBAR COLOR ENHANCEMENTS — SCOPED */

.pn-assistant-mode-label {
    margin:.8rem .3rem .35rem!important;
    color:#34517d!important;
    font-size:.76rem!important;
    font-weight:850!important;
    letter-spacing:.055em!important;
    text-transform:uppercase!important;
}

.pn-side-section-label {
    display:flex!important;
    align-items:center!important;
    width:fit-content!important;
    margin:1.05rem .2rem .55rem!important;
    padding:.45rem .82rem!important;
    border:1px solid rgba(93,75,225,.18)!important;
    border-radius:999px!important;
    color:#294873!important;
    background:linear-gradient(105deg,rgba(8,145,178,.13),rgba(37,99,235,.12),rgba(217,70,239,.11))!important;
    box-shadow:0 8px 19px rgba(61,86,166,.10),inset 0 1px 0 rgba(255,255,255,.82)!important;
    font-size:.84rem!important;
    font-weight:900!important;
    letter-spacing:.085em!important;
}

/* Assistant-mode and Theme selectors use the same colorful glass control. */
.st-key-assistant_mode_selector div[data-baseweb="select"] > div,
.st-key-sidebar_theme_selector div[data-baseweb="select"] > div {
    min-height:45px!important;
    border:1px solid rgba(74,98,219,.25)!important;
    border-radius:14px!important;
    color:#17345f!important;
    background:
        linear-gradient(110deg,rgba(224,249,255,.96),rgba(233,239,255,.96) 52%,rgba(250,232,255,.94))!important;
    box-shadow:
        0 10px 22px rgba(58,79,165,.13),
        inset 0 1px 0 rgba(255,255,255,.95)!important;
    font-size:.92rem!important;
    font-weight:800!important;
}

.st-key-assistant_mode_selector div[data-baseweb="select"] > div:hover,
.st-key-sidebar_theme_selector div[data-baseweb="select"] > div:hover {
    border-color:rgba(91,73,221,.42)!important;
    box-shadow:
        0 13px 26px rgba(58,79,165,.17),
        0 0 0 4px rgba(92,75,220,.07)!important;
}

/* Make Today's Usage a noticeable liquid-glass status card. */
.pn-side-usage-card {
    position:relative!important;
    overflow:hidden!important;
    margin-top:.9rem!important;
    padding:1rem!important;
    border:1px solid rgba(74,116,225,.24)!important;
    border-radius:18px!important;
    color:#17345f!important;
    background:
        radial-gradient(circle at 90% 5%,rgba(217,70,239,.18),transparent 36%),
        linear-gradient(135deg,rgba(224,249,255,.94),rgba(233,239,255,.94) 54%,rgba(250,232,255,.91))!important;
    box-shadow:
        0 14px 31px rgba(45,78,160,.16),
        inset 0 1px 0 rgba(255,255,255,.96)!important;
}

.pn-side-usage-card::after {
    content:"";
    position:absolute;
    width:76px;
    height:76px;
    right:-26px;
    bottom:-34px;
    border-radius:50%;
    background:rgba(14,165,233,.14);
    pointer-events:none;
}

.pn-side-usage-head strong {
    font-size:.91rem!important;
    font-weight:900!important;
}

.pn-side-usage-head span {
    display:inline-flex!important;
    align-items:center!important;
    justify-content:center!important;
    min-width:42px!important;
    padding:.25rem .48rem!important;
    border-radius:999px!important;
    color:#fff!important;
    background:linear-gradient(110deg,#0891b2,#2563eb,#9333ea)!important;
    box-shadow:0 6px 14px rgba(37,99,235,.22)!important;
    font-weight:900!important;
}

.pn-side-progress {
    height:9px!important;
    border-radius:999px!important;
    background:rgba(255,255,255,.72)!important;
    box-shadow:inset 0 1px 3px rgba(36,63,119,.12)!important;
}

.pn-side-progress span {
    border-radius:999px!important;
    background:linear-gradient(90deg,#06b6d4,#2563eb,#8b5cf6,#ec4899)!important;
    box-shadow:0 0 12px rgba(91,92,230,.32)!important;
}

.pn-side-usage-card small {
    color:#526887!important;
    font-weight:700!important;
}

/* Dedicated high-contrast logout action. */
.st-key-side_logout button {
    min-height:46px!important;
    border:1px solid rgba(255,255,255,.55)!important;
    border-radius:14px!important;
    color:#fff!important;
    -webkit-text-fill-color:#fff!important;
    background:linear-gradient(110deg,#f97316 0%,#ef4444 48%,#c026d3 100%)!important;
    box-shadow:
        0 12px 26px rgba(225,57,81,.24),
        inset 0 1px 0 rgba(255,255,255,.38)!important;
    font-weight:900!important;
}

.st-key-side_logout button:hover {
    transform:translateY(-2px)!important;
    filter:saturate(1.08)!important;
    box-shadow:
        0 16px 32px rgba(225,57,81,.30),
        0 0 0 4px rgba(239,68,68,.08)!important;
}

@media(max-width:600px) {
    .pn-side-section-label {
        font-size:.79rem!important;
    }

    .pn-side-usage-card {
        padding:.85rem!important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* LOGOUT VISIBILITY FIX — ALL THEMES */
section[data-testid="stSidebar"] [class*="st-key-side_logout"] {
    position:relative!important;
    z-index:10!important;
    width:100%!important;
    margin:.8rem 0 .35rem!important;
    padding:0!important;
    background:transparent!important;
    isolation:isolate!important;
}

section[data-testid="stSidebar"] [class*="st-key-side_logout"]
div[data-testid="stButton"] {
    width:100%!important;
    margin:0!important;
    padding:0!important;
    background:transparent!important;
}

section[data-testid="stSidebar"] [class*="st-key-side_logout"] button {
    position:relative!important;
    z-index:11!important;
    width:100%!important;
    min-height:46px!important;
    margin:0!important;
    padding:.68rem 1rem!important;
    border:1px solid rgba(255,255,255,.58)!important;
    border-radius:14px!important;
    opacity:1!important;
    color:#ffffff!important;
    -webkit-text-fill-color:#ffffff!important;
    background:linear-gradient(110deg,#f97316 0%,#ef4444 48%,#c026d3 100%)!important;
    box-shadow:
        0 12px 26px rgba(225,57,81,.28),
        inset 0 1px 0 rgba(255,255,255,.42)!important;
    font-weight:900!important;
    line-height:1.2!important;
    overflow:hidden!important;
}

section[data-testid="stSidebar"] [class*="st-key-side_logout"] button p,
section[data-testid="stSidebar"] [class*="st-key-side_logout"] button span,
section[data-testid="stSidebar"] [class*="st-key-side_logout"] button div {
    position:relative!important;
    z-index:12!important;
    margin:0!important;
    color:#ffffff!important;
    -webkit-text-fill-color:#ffffff!important;
    background:transparent!important;
    font-weight:900!important;
    line-height:1.2!important;
    opacity:1!important;
}

section[data-testid="stSidebar"] [class*="st-key-side_logout"] button:hover,
section[data-testid="stSidebar"] [class*="st-key-side_logout"] button:focus,
section[data-testid="stSidebar"] [class*="st-key-side_logout"] button:active {
    border-color:rgba(255,255,255,.72)!important;
    color:#ffffff!important;
    -webkit-text-fill-color:#ffffff!important;
    background:linear-gradient(110deg,#ea6810 0%,#dd3841 48%,#ae20c0 100%)!important;
    box-shadow:
        0 16px 32px rgba(225,57,81,.34),
        0 0 0 4px rgba(239,68,68,.10)!important;
}

/* Prevent the footer card from visually covering the action. */
section[data-testid="stSidebar"] .pn-side-footer {
    position:relative!important;
    z-index:1!important;
    margin-bottom:.35rem!important;
}
</style>
        """
    )


    st.html(
        """
<style>
/* MOBILE ASSISTANT MODE — PHONE ONLY */
.st-key-mobile_assistant_mode {
    display:none!important;
}

@media screen and (max-width:700px) {
    .st-key-mobile_assistant_mode {
        position:relative!important;
        display:block!important;
        width:100%!important;
        margin:.35rem 0 .65rem!important;
        padding:.62rem .72rem .72rem!important;
        border:1px solid rgba(92,75,220,.22)!important;
        border-radius:18px!important;
        background:
            radial-gradient(circle at 92% 8%,rgba(236,72,153,.17),transparent 34%),
            linear-gradient(120deg,rgba(224,249,255,.94),rgba(233,239,255,.94) 52%,rgba(250,232,255,.92))!important;
        box-shadow:
            0 12px 27px rgba(53,79,163,.15),
            inset 0 1px 0 rgba(255,255,255,.95)!important;
        box-sizing:border-box!important;
        overflow:visible!important;
    }

    .pn-mobile-mode-label {
        margin:0 0 .42rem!important;
        color:#254a7b!important;
        font-size:.82rem!important;
        font-weight:900!important;
        letter-spacing:.025em!important;
    }

    .st-key-mobile_assistant_mode_selector {
        width:100%!important;
        margin:0!important;
    }

    .st-key-mobile_assistant_mode_selector
    div[data-baseweb="select"] > div {
        min-height:44px!important;
        border:1px solid rgba(69,96,214,.30)!important;
        border-radius:14px!important;
        color:#17345f!important;
        background:linear-gradient(110deg,#f0fdff 0%,#eef2ff 52%,#fdf0ff 100%)!important;
        box-shadow:
            0 9px 20px rgba(56,79,162,.13),
            inset 0 1px 0 #fff!important;
        font-size:.88rem!important;
        font-weight:850!important;
    }

    .st-key-mobile_assistant_mode_selector
    div[data-baseweb="select"] > div:focus-within {
        border-color:rgba(91,75,220,.52)!important;
        box-shadow:
            0 11px 23px rgba(56,79,162,.17),
            0 0 0 4px rgba(91,75,220,.08)!important;
    }
}

@media screen and (min-width:701px) {
    .st-key-mobile_assistant_mode {
        display:none!important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* MOBILE MODE LABEL LAYOUT FIX */
@media screen and (max-width:700px) {
    .st-key-mobile_assistant_mode {
        padding:.78rem .75rem .75rem!important;
        overflow:visible!important;
    }

    .st-key-mobile_assistant_mode
    div[data-testid="stSelectbox"] {
        display:flex!important;
        flex-direction:column!important;
        gap:.42rem!important;
        width:100%!important;
        margin:0!important;
        padding:0!important;
        overflow:visible!important;
    }

    .st-key-mobile_assistant_mode
    div[data-testid="stSelectbox"] > label,
    .st-key-mobile_assistant_mode
    label[data-testid="stWidgetLabel"] {
        position:static!important;
        display:flex!important;
        width:100%!important;
        height:auto!important;
        min-height:18px!important;
        margin:0!important;
        padding:0 .15rem!important;
        color:#254a7b!important;
        font-size:.82rem!important;
        font-weight:900!important;
        line-height:1.25!important;
        opacity:1!important;
        transform:none!important;
        overflow:visible!important;
    }

    .st-key-mobile_assistant_mode
    div[data-testid="stSelectbox"] > label p,
    .st-key-mobile_assistant_mode
    label[data-testid="stWidgetLabel"] p {
        margin:0!important;
        color:#254a7b!important;
        font-size:.82rem!important;
        font-weight:900!important;
        line-height:1.25!important;
    }

    .st-key-mobile_assistant_mode_selector {
        margin:0!important;
        padding:0!important;
    }
}
</style>
        """
    )
















    st.html(
        """
<style>
/* CLEAN MOBILE GLASS NAV — STABLE */
@media screen and (max-width:700px) {
    .block-container {
        padding-bottom:calc(6rem + env(safe-area-inset-bottom))!important;
    }

    .st-key-mobile_nav {
        position:fixed!important;
        left:10px!important;
        right:10px!important;
        bottom:10px!important;
        z-index:1100!important;
        width:auto!important;
        max-width:none!important;
        margin:0!important;
        padding:.42rem .38rem calc(.40rem + env(safe-area-inset-bottom))!important;
        border:1px solid rgba(188,208,237,.72)!important;
        border-radius:22px!important;
        background:rgba(248,251,255,.94)!important;
        box-shadow:0 14px 34px rgba(30,64,125,.20)!important;
        backdrop-filter:blur(22px) saturate(145%)!important;
        -webkit-backdrop-filter:blur(22px) saturate(145%)!important;
        box-sizing:border-box!important;
        overflow:visible!important;
    }

    .st-key-mobile_nav [data-testid="stHorizontalBlock"] {
        display:grid!important;
        grid-template-columns:repeat(5,minmax(0,1fr))!important;
        align-items:center!important;
        gap:.14rem!important;
        width:100%!important;
        overflow:visible!important;
    }

    .st-key-mobile_nav [data-testid="column"],
    .st-key-mobile_nav div[data-testid="stButton"] {
        width:100%!important;
        min-width:0!important;
        overflow:visible!important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button {
        width:100%!important;
        min-width:0!important;
        height:50px!important;
        min-height:50px!important;
        margin:0!important;
        padding:.22rem .03rem!important;
        border:0!important;
        border-radius:14px!important;
        color:#344968!important;
        -webkit-text-fill-color:#344968!important;
        background:transparent!important;
        box-shadow:none!important;
        transform:none!important;
        white-space:pre-line!important;
        overflow:hidden!important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button,
    .st-key-mobile_nav div[data-testid="stButton"] > button * {
        color:#344968!important;
        -webkit-text-fill-color:#344968!important;
        font-size:.64rem!important;
        font-weight:800!important;
        line-height:1.22!important;
        text-shadow:none!important;
        opacity:1!important;
    }

    /* Selected destination: compact dark-indigo pill, never theme-generated white. */
    .st-key-mobile_nav div[data-testid="stButton"]
    > button[data-testid="stBaseButton-primary"] {
        border:1px solid rgba(255,255,255,.64)!important;
        color:#ffffff!important;
        -webkit-text-fill-color:#ffffff!important;
        background:linear-gradient(145deg,#075985,#1d4ed8 52%,#5b21b6)!important;
        box-shadow:0 9px 20px rgba(29,78,216,.29)!important;
    }

    .st-key-mobile_nav div[data-testid="stButton"]
    > button[data-testid="stBaseButton-primary"],
    .st-key-mobile_nav div[data-testid="stButton"]
    > button[data-testid="stBaseButton-primary"] * {
        color:#ffffff!important;
        -webkit-text-fill-color:#ffffff!important;
        text-shadow:0 1px 2px rgba(10,25,65,.25)!important;
        font-weight:900!important;
    }

    /* New Chat: the only elevated action. */
    .st-key-mobile_nav [data-testid="column"]:nth-child(2)
    div[data-testid="stButton"] > button {
        height:56px!important;
        min-height:56px!important;
        margin-top:-10px!important;
        border:1px solid rgba(255,255,255,.66)!important;
        border-radius:17px!important;
        color:#ffffff!important;
        -webkit-text-fill-color:#ffffff!important;
        background:linear-gradient(145deg,#4338ca,#7e22ce 55%,#be185d)!important;
        box-shadow:0 12px 25px rgba(109,40,217,.34)!important;
        transform:translateY(-2px)!important;
    }

    .st-key-mobile_nav [data-testid="column"]:nth-child(2)
    div[data-testid="stButton"] > button,
    .st-key-mobile_nav [data-testid="column"]:nth-child(2)
    div[data-testid="stButton"] > button * {
        color:#ffffff!important;
        -webkit-text-fill-color:#ffffff!important;
        font-weight:900!important;
        text-shadow:0 1px 2px rgba(30,20,80,.28)!important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button:hover {
        filter:brightness(.96)!important;
    }
}

@media screen and (max-width:390px) {
    .st-key-mobile_nav {
        left:6px!important;
        right:6px!important;
        padding-left:.25rem!important;
        padding-right:.25rem!important;
    }

    .st-key-mobile_nav [data-testid="stHorizontalBlock"] {
        gap:.05rem!important;
    }

    .st-key-mobile_nav div[data-testid="stButton"] > button,
    .st-key-mobile_nav div[data-testid="stButton"] > button * {
        font-size:.58rem!important;
    }
}
</style>
        """
    )


    st.html(
        """
<style>
/* NEW CHAT INDIGO PALETTE ONLY */
@media screen and (max-width:700px) {
    .st-key-mobile_nav [data-testid="column"]:nth-child(2)
    div[data-testid="stButton"] > button {
        border-color:rgba(255,255,255,.66)!important;
        color:#ffffff!important;
        -webkit-text-fill-color:#ffffff!important;
        background:linear-gradient(145deg,#075985 0%,#1d4ed8 52%,#5b21b6 100%)!important;
        box-shadow:
            0 13px 27px rgba(29,78,216,.35),
            0 0 0 4px rgba(37,99,235,.09),
            inset 0 1px 0 rgba(255,255,255,.40)!important;
    }

    .st-key-mobile_nav [data-testid="column"]:nth-child(2)
    div[data-testid="stButton"] > button:hover,
    .st-key-mobile_nav [data-testid="column"]:nth-child(2)
    div[data-testid="stButton"] > button:focus {
        color:#ffffff!important;
        -webkit-text-fill-color:#ffffff!important;
        background:linear-gradient(145deg,#064d73 0%,#193fb4 52%,#4c1d95 100%)!important;
    }

    .st-key-mobile_nav [data-testid="column"]:nth-child(2)
    div[data-testid="stButton"] > button * {
        color:#ffffff!important;
        -webkit-text-fill-color:#ffffff!important;
    }
}
</style>
        """
    )
