# PeerNet AI with Supabase

This version replaces `users.json` with Supabase Auth and Postgres.

## Features

- Email/password registration
- Email verification
- Login and logout
- Resend verification email
- Password-reset email
- Change password while signed in
- Persistent profile
- Persistent conversations and messages
- Per-user favorites
- Row Level Security
- Optional admin dashboard
- OpenAI Responses API
- Streamlit Community Cloud support

## Setup

1. Create a free Supabase project.
2. Open Supabase SQL Editor.
3. Run `supabase/schema.sql`.
4. Copy Project URL and publishable/anon key.
5. Copy `.env.example` to `.env`.
6. Add your OpenAI and Supabase values.
7. Run:

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

## Supabase Auth configuration

Open:

```text
Authentication → Providers → Email
```

Keep email confirmation enabled for production.

Open:

```text
Authentication → URL Configuration
```

Use this locally:

```text
http://localhost:8501
```

Add your deployed Streamlit URL as an allowed redirect URL later.

## Streamlit Community Cloud Secrets

```toml
OPENAI_API_KEY = "your-openai-key"
OPENAI_MODEL = "gpt-5-mini"

SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_ANON_KEY = "your-publishable-or-anon-key"
SUPABASE_SERVICE_ROLE_KEY = "your-service-role-key"
SUPABASE_REDIRECT_URL = "https://your-app.streamlit.app"

PEERNET_ADMIN_EMAILS = "your-email@example.com"
```

`SUPABASE_SERVICE_ROLE_KEY` is optional and only needed for the admin
dashboard. Never commit it to GitHub.

## Make yourself an admin

After registering and verifying your account, run:

```sql
update public.profiles
set role = 'admin'
where email = 'your-email@example.com';
```

Add the same email to `PEERNET_ADMIN_EMAILS`.

## Security

- Supabase Auth stores password hashes, not plaintext passwords.
- RLS limits users to their own data.
- Never commit `.env` or `.streamlit/secrets.toml`.
- The service-role key bypasses RLS and must remain secret.


## Enterprise v2 UI
- Brighter tablet-style authentication cards
- Centered logo after login
- Responsive branding panel


## Colorful responsive final UI

This version adds:

- Colorful gradient login/register buttons
- Bright tablet-style authentication cards
- Responsive PC, laptop, tablet, and mobile layouts
- Centered PeerNet branding before and after login
- Desktop sidebar and compact responsive content
- Color-coded quick prompt cards
- Dark gradient chat composer
- Attach file, image, and code-mode controls
- Supabase authentication and persistent user data

### Attachment behavior

Text/config/log/JSON/YAML attachments are included in the AI prompt.
PDF files and images display as attached, but full binary/multimodal analysis
requires an additional document and vision-processing integration.


## AI login-image alignment update

- Replaced the empty right-side login panel with `images/Ai_think.png`.
- Removed the duplicate PeerNet logo that appeared below the panel.
- Matched the top alignment of the login card and AI-image card.
- Added responsive image sizing and rounded-corner treatment.
- Aligned the supporting text and feature pills directly beneath the AI image.


## Matched signed-in dashboard

This release rebuilds the post-login interface around the approved PeerNet AI
reference:

- Compact centered branding sidebar
- Functional Home, New Chat, History, Favorites, Settings, About, and Logout
- Welcome top bar with model and profile controls
- Branded hero with network decoration
- Six feature chips
- Five equal pastel quick-action cards
- Dark integrated composer with Attach, Image, and Code controls
- Connection/security status bar
- Functional tablet and mobile layouts
- Fixed mobile bottom navigation

The design is implemented with native Streamlit controls so navigation,
authentication, chat, attachments, history, favorites, settings, and logout
remain functional.


## Clean composer correction

This release fixes the dashboard issues shown in the screenshot:

- Custom HTML is dedented before rendering, preventing literal `<div>` code.
- The duplicate Streamlit chat input has been removed.
- There is exactly one functional message input.
- Attachment uses the `📎` symbol.
- Image upload uses the `🖼️` symbol.
- Code mode uses the `</>` symbol.
- The send action uses a glowing `↑` button.
- Desktop, tablet, and mobile composer layouts are responsive.


## Labeled composer controls

The single composer now follows the approved design:

- Prompt appears on the top row.
- `📎 Attach` is a labeled pill.
- `🖼️ Image` is a labeled pill.
- `</> Code` is a labeled pill.
- Character counter is aligned to the right.
- One glowing send button is used.
- No duplicate search field is rendered.


## Final rendering and composer fix

- All dashboard HTML now uses `st.html()` instead of Markdown rendering.
- Literal `<div>` and `<span>` code can no longer appear in the dashboard.
- Composer text is forced to visible white on a dark input background.
- The prompt is queued before the field is cleared.
- Only one search/composer field is rendered.


## Plus composer update

- Circular `+` button opens file and image upload controls.
- One bright white input field is used.
- Typed text is forced to dark navy for visibility.
- One circular glowing send button is used.
- Image and Code controls are compact below the input.
- No duplicate Streamlit chat bar is rendered.


## Modern white composer

- Circular colored `+` menu for files, images, and code mode
- One white rounded prompt field
- Dark visible typing text
- Compact model selector
- Microphone mode icon
- Colored circular send button
- Responsive desktop, tablet, and mobile styling
- No duplicate composer


## Single user avatar

- Removed the duplicate avatar from the top welcome bar.
- Kept one profile avatar in the sidebar.
- The avatar now displays the first letter of the user's full name.
- It falls back to username, email, and finally `P`.


## Final alignment update

- Removed the top-bar `Online` line under the username.
- Kept the sidebar `Online` indicator.
- Centered `Ai_think.png` horizontally inside the login-page bordered card.
- Added equal left and right spacing around the login image.
- Preserved responsive desktop, laptop, tablet, and mobile behavior.


## Exact login-image centering

- The AI image is horizontally centered relative to the visual-card borders.
- Equal left and right padding is enforced on desktop, laptop, tablet, and mobile.
- The image wrapper and all Streamlit-generated inner wrappers use centered flex layout.
- The heading, description, and feature pills are centered beneath the image.
- Previous conflicting visual-card alignment rules were removed.


## Borderless login AI visual

- Removed the outer border from the login-page AI visual section.
- Removed the container outline and container shadow.
- Kept the AI image centered with equal left and right spacing.
- Kept the image's subtle shadow for depth.
- Preserved centered heading, description, and feature pills.


# PeerNet AI v3

New in v3:

- PDF, text, log, configuration, JSON, YAML, Python, CSV, and XML extraction
- Searchable chat history
- Rename conversations
- Networking Tools page
- Daily per-user request limits
- Helpful / Not Helpful feedback
- Improved admin analytics
- File-size protection
- Existing Supabase authentication, favorites, profiles, responsive UI, and OpenAI integration retained

After upgrading, run the latest `supabase/schema.sql` in Supabase SQL Editor
to create `usage_events` and `message_feedback`.


## Voice input

This build adds:

- `🎙 Dictate` for one-time speech-to-text
- `▶ Start Voice` for continuous speech capture
- Stop controls while recording
- Voice transcript copied into the search field
- Typed text remains visible
- Existing uploads, model selector, and send button retained

Allow microphone access in the browser when prompted.


## Icon voice buttons

The voice controls now use compact play-style icons:

- `🎙` — Dictate once
- `▶` — Start continuous voice
- `■` — Stop recording
- Small labels appear below the icons
- Circular visual frames are responsive on desktop, tablet, and mobile


## Final composer alignment

- Upload, search, Dictate, Start Voice, model selector, and Send share one row.
- The Send button is no longer rendered below the search field.
- Every control uses matching 48–50 px height.
- The voice labels were removed to prevent vertical misalignment.
- On mobile, the search field uses the first row and all five controls use a
  single aligned second row.


## Stretched search and model selector correction

- The search field now expands across all available space.
- The empty gap before the voice controls has been removed.
- The `gpt-5-mini` model selector is visible again.
- Upload, search, Dictate, Start Voice, model selector, and Send remain in one row.
- Mobile keeps the search field on the first row and all action controls on the second.


## Final model and search correction

- Removed the unstable one-option Streamlit selectbox.
- Added a permanently visible `gpt-5-mini ▾` model pill.
- Search field uses the largest native Streamlit column.
- Removed conflicting accumulated composer CSS.
- Upload, search, Dictate, Start Voice, model, and Send stay aligned.


## Premium composer styling

- Dictate uses a blue-to-cyan gradient
- Start Voice uses a purple-to-cyan gradient
- Recording state uses a pulsing red style
- GPT-5 mini uses a polished gradient pill
- Send uses a premium blue-to-purple gradient
- Upload button gains matching hover styling
- Search input gets a clearer focus glow


## Voice icon underline fix

- Removed the thin line shown beneath Dictate and Start Voice icons.
- Added a small white mask over the recorder component artifact.
- Preserved the circular gradients, shadows, hover effects, and responsive layout.


## Voice component box removal

- Voice recorder components are clipped into true circles.
- All overflow outside the icon area is hidden.
- The old rectangular component background and underline are masked.
- Premium circular rings and shadows are preserved.
- Dictate and Start Voice functionality remains unchanged.


# PeerNet AI v4 — Working Model Dropdown

The model control is now a real Streamlit dropdown rather than a disabled
display button.

## Features

- Working model dropdown in the composer
- Selected model persists in the Streamlit session
- Selected model appears in the top bar and Settings page
- Selected model is passed to the OpenAI Responses API
- Usage records store the actual selected model
- Available models are configurable with `OPENAI_MODELS`

Example:

```env
OPENAI_MODEL=gpt-5-mini
OPENAI_MODELS=gpt-5-mini,gpt-5,gpt-4.1,gpt-4o-mini
```

Only models enabled for the configured OpenAI API account will successfully
answer requests. If a selected model is unavailable, PeerNet AI displays the
API error without exposing the API key.


## Enter to send

- Pressing Enter inside the search field now submits the prompt.
- Clicking the visible circular Send button still works.
- The hidden form submit control is used only to enable keyboard submission.
- Voice, upload, model selection, usage limits, and history remain unchanged.


# Final borderless composer

- Visible Send button removed
- Press Enter to submit
- Composer outer border removed
- Search-field border removed
- Upload, voice, and model-selector borders removed
- Soft gradients and shadows retained
- Working model dropdown retained
- Desktop, tablet, and mobile layouts preserved


## Final send-button placement

- Removed the old form Send button below the search field.
- Added one circular Send button at the far right of the composer.
- Pressing Enter still submits through the text-input callback.
- Upload, Dictate, Start Voice, model selector, and Send remain aligned.


# PeerNet AI v5 — Approved Dashboard

This version applies the approved commercial dashboard design with:

- Modern left sidebar and gradient New Chat button
- Good-morning hero with networking illustration
- Six premium networking feature cards
- Popular topic chips
- Borderless single-line composer
- Upload, Dictate, Start Voice, working model dropdown, and Send at the end
- Enter-to-send support
- Responsive desktop, tablet, and mobile styling
- Existing Supabase authentication, history, favorites, tools, usage limits,
  feedback, document analysis, and OpenAI integration retained


# PeerNet AI v6 — Premium Sidebar

New sidebar features:

- Compact profile card with user initial and online indicator
- Full-width gradient New Chat button
- Rounded active navigation
- Real recent conversations loaded from Supabase
- Quick AI tools
- Daily usage progress card
- Theme selector
- Professional product footer
- Responsive tablet and mobile sidebar sizing
- Existing authentication, chat, history, favorites, tools, usage limits,
  feedback, voice controls, model selection, and OpenAI integration retained


## Compact collapsible sidebar

- `Recent Chats` is collapsed by default.
- `Quick AI Tools` is collapsed by default.
- Expanding either section preserves all existing functionality.
- Reduced sidebar height and visual clutter.
- Compact hover and active styles added.


## Working theme selector

The sidebar theme selector now changes the full application:

- Light
- Dark
- Blue

The selected theme updates the page, sidebar, hero, feature cards, composer,
chat messages, recent-chat expanders, and model selector. The choice persists
for the active Streamlit session.


## Dark-theme chat visibility fix

- AI responses now use high-contrast light text in Dark theme.
- User messages remain visible.
- Code blocks, inline code, links, tables, and blockquotes are styled for Dark mode.
- Save, feedback, and other response buttons remain visible.
- Chat avatars are visible against the dark surface.


## Final Dark chat visibility repair

The text rules are now embedded directly in the Dark-theme stylesheet.

Fixed visibility for:

- User messages
- AI messages
- OpenAI/API errors
- Headings, paragraphs, lists, bold and italic text
- Links
- Inline code and code blocks
- Tables
- Blockquotes
- Save and feedback controls
- User and assistant avatars


## Profile-only top bar

- Removed the unused top theme button.
- Removed the model pill from the top bar.
- Kept only the profile avatar and dropdown indicator.
- Sidebar Light / Dark / Blue theme selector remains available.
- All chat, voice, upload, model selection, and Supabase features are unchanged.


## Glass profile avatar

- Removed the dropdown chevron completely.
- Added a glassmorphism profile container.
- Added blue-purple gradient avatar.
- Added green online indicator.
- Added soft glow and hover animation.
- Designed to remain visible in Light, Dark, and Blue themes.
- Responsive on desktop, tablet, and mobile.


## Glass profile theme correction

The profile avatar now has dedicated styling inside each actual theme:

- Light: bright frosted-glass card
- Dark: deep navy-purple glass card with high contrast
- Blue: cool blue frosted-glass card
- Green online indicator remains visible in every theme

The unreliable browser and operating-system theme selectors were removed.


## Profile clipping fix

- Increased top-bar height so the profile card is never cut off.
- Forced fixed avatar and glass-container dimensions.
- Removed overflow clipping from all profile wrappers.
- Applied identical geometry in Light, Dark, and Blue themes.
- Preserved hover, glow, gradient, and online status indicator.


## Simple bubble profile

- Removed the glassmorphism container.
- Removed the online status dot.
- Added one simple circular `Ⓟ` profile bubble.
- Kept subtle gradient and hover animation.
- Supports Light, Dark, and Blue themes.
- Responsive on desktop, tablet, and mobile.


## Final user profile bubble

- Uses the first letter of the logged-in user's full name.
- Falls back to username, then email, then `P`.
- Purple-blue circular bubble.
- Small green online indicator.
- No glass container.
- No dropdown chevron.
- Same geometry in Light, Dark, and Blue themes.
- Responsive on desktop, tablet, and mobile.


# PeerNet AI v7 — Profile Bubble Across All Themes

The profile bubble is now defined once in shared CSS rather than inside
individual theme styles.

Features:

- Shows the first letter of the logged-in user's full name
- Falls back to username, email, and then `P`
- Purple-blue circular bubble
- Green online indicator
- No glass container
- No dropdown chevron
- Same size and appearance in Light, Dark, and Blue themes
- Responsive desktop, tablet, and mobile layout
- Profile wrapper overflow protection prevents clipping


# Final Theme Profile Colors

- Light theme: dark-blue bubble with white user initial
- Dark theme: white bubble with black user initial
- Blue theme: blue-gradient bubble with white user initial
- Green online indicator remains visible
- User first-letter logic is preserved


# PeerNet AI v8 — Final Circle Profile

- Complete circle in Light, Dark, and Blue themes
- No borders or outlines
- Light: dark-blue bubble with white letter
- Dark: white bubble with black letter
- Blue: blue-gradient bubble with white letter
- Green online indicator
- Signed-in user's first initial
- Responsive desktop, tablet, and mobile layout
