# PeerNet AI

PeerNet AI is a Streamlit-based assistant for:

- Networking concepts
- Cisco SD-WAN and Meraki
- Interview preparation
- Python network automation
- PRD-to-test-case generation
- Troubleshooting guidance

## 1. Prerequisites

Install Python 3.10 or newer.

Check Python:

```bash
python --version
```

## 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install packages

```bash
pip install -r requirements.txt
```

## 4. Configure the API key

Copy `.env.example` to `.env`.

Windows Command Prompt:

```bash
copy .env.example .env
```

PowerShell:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace:

```env
OPENAI_API_KEY=replace_with_your_api_key
```

Never upload or commit the `.env` file.

## 5. Run the application

```bash
streamlit run app.py
```

Streamlit normally opens:

```text
http://localhost:8501
```

## 6. Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `.gitignore`.
3. Do not upload `.env`.
4. In Streamlit Community Cloud, create an app from the repository.
5. Add secrets in the app settings:

```toml
OPENAI_API_KEY = "your-key"
OPENAI_MODEL = "gpt-5-mini"
```

For Streamlit Cloud secrets, you may replace the environment lookup with
`st.secrets`, or configure the secret as an environment variable through your
deployment setup.

## Important

OpenAI API usage is billed separately from a ChatGPT subscription. Add spending
limits and monitor usage in your API account.
