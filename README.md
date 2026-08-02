# PeerNet AI Final Design

A responsive Streamlit application matching the supplied PeerNet AI design.

## Included

- Login and Register screens
- Premium PeerNet member sidebar
- Desktop, tablet, and mobile responsive dashboard
- One dark functional chat input
- Popular question cards
- Assistant modes
- Chat history
- Conversation search
- Download chat
- Logout
- OpenAI integration
- PeerNet logo and favicon
- Design reference image

## Run locally

```powershell
cd C:\Users\Admin\Downloads\PeerNet_AI_Final_Design

& "C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe" `
-m pip install -r requirements.txt

& "C:\Users\Admin\AppData\Local\Programs\Python\Python314\python.exe" `
-m streamlit run app.py
```

## Default login

```text
Username: admin
Password: peernet123
```

Change this password before deployment.

## Local OpenAI key

Copy `.env.example` to `.env`, then add:

```text
OPENAI_API_KEY=your_key
```

## Streamlit Cloud Secrets

```toml
OPENAI_API_KEY = "your_key"
OPENAI_MODEL = "gpt-5-mini"
PEERNET_USERNAME = "your_username"
PEERNET_PASSWORD = "your_strong_password"
```

## Best laptop display

- Maximize Chrome or Edge
- Press `Ctrl + 0` for 100% browser zoom
- Refresh with `Ctrl + F5`
- Windows display scaling: 100% or 125%

## Streamlit limitation

This project closely matches the design while using standard Streamlit widgets.
The chat bar is the real Streamlit chat input, restyled with CSS. Some exact
pixel placement may vary slightly by Streamlit version, browser, resolution,
and operating-system scaling.


## Login-layout correction

This version rebuilds the login page using native Streamlit containers and
columns. The right-side logo and supporting text remain in the same bordered
panel and no longer separate vertically or create a blank upper panel.


## Mobile chat-bar fix

The mobile chat input now appears above the PeerNet bottom navigation.

The CSS uses:

```css
bottom: calc(78px + env(safe-area-inset-bottom));
```

This prevents the input from being hidden by:

- The PeerNet mobile navigation
- iPhone safe-area spacing
- Safari's bottom browser controls

After replacing an older version, refresh the mobile browser completely.
On iPhone Safari, close the tab and reopen the Network URL if cached CSS remains.


## Working mobile navigation

The mobile bottom navigation now uses real links instead of decorative spans.

Actions:

- **Home** returns to the main dashboard.
- **New Chat** clears the current conversation.
- **History** opens the chat-history panel.
- **Favorites** opens the favorites placeholder.
- **Settings** opens mobile assistant settings.

The app handles these actions through Streamlit query parameters and clears
the parameter after processing, preventing repeated actions during reruns.


## Final mobile interaction fix

This version removes all HTML navigation links and all fixed overlays.

- The chat input is the real native Streamlit `st.chat_input`.
- The mobile menu uses real native `st.button` controls.
- Home, New Chat, History, Favorites, and Settings now execute Python actions.
- The input is no longer hidden behind the mobile menu.
- Safari and Chrome taps are not blocked by overlapping fixed layers.


## Mobile bottom-bar correction

The mobile navigation now stays in one horizontal row at the bottom.

- Uses real Streamlit buttons
- Buttons remain clickable
- Chat input is fixed directly above the navigation
- iPhone safe-area spacing is included
- Streamlit's mobile column stacking is overridden only for this navigation
- Extra bottom page padding prevents content from being hidden


## Mobile Settings duplicate-key correction

The Settings page previously created more than one select box using the same
Streamlit key, which caused `StreamlitDuplicateElementKey`.

This version uses:

- `sidebar_mode_selector` for the sidebar
- `mobile_settings_mode_selector` for the mobile Settings page
- `mobile_selected_mode` in session state to preserve the mobile selection

Only one mobile Settings select box is rendered.


## Sidebar profile update

The PN avatar has been removed.

The sidebar now displays:

```text
PeerNet Solutions logo
PeerNet Member
Online
Premium Member
```

All items are centered on the same vertical axis.
