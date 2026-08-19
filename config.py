import os
from typing import Final

APP_TITLE: Final = "PeerNet AI"
LOGO_PATH: Final = "images/PeerNet Solutions.png"
FAVICON_PATH: Final = "images/favicon.png"
AI_LOGIN_IMAGE_PATH: Final = "images/Ai_think.png"
GEMINI_DEFAULT_MODEL: Final = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash",
)

_gemini_models = [
    item.strip()
    for item in os.getenv(
        "GEMINI_MODELS",
        "gemini-3.6-flash,gemini-2.5-flash",
    ).split(",")
    if item.strip()
]

_openai_models = [
    item.strip()
    for item in os.getenv(
        "OPENAI_MODELS",
        "gpt-5-mini,gpt-5,gpt-4.1,gpt-4o-mini",
    ).split(",")
    if item.strip()
]

DEFAULT_MODEL: Final = GEMINI_DEFAULT_MODEL

MODEL_OPTIONS: Final = list(
    dict.fromkeys(
        [
            GEMINI_DEFAULT_MODEL,
            *_gemini_models,
            *_openai_models,
        ]
    )
)

SUPABASE_REDIRECT_URL: Final = os.getenv("SUPABASE_REDIRECT_URL", "http://localhost:8501")

MODE_INSTRUCTIONS = {
    "Networking Trainer": """
You are PeerNet AI, an expert networking trainer.
Structure answers as:
1. Simple explanation
2. Practical example
3. Useful show/debug commands
4. Troubleshooting notes
5. Interview-ready answer
Focus on Cisco SD-WAN, Meraki, routing, switching, wireless,
network security, Linux, REST APIs, Python, pyATS, and pytest.
""",
    "Troubleshooting": """
You are a senior network troubleshooting engineer.
Use a structured flow covering symptom, scope, recent changes, underlay,
control plane, data plane, policy, application behavior, commands, causes,
and corrective actions. Avoid destructive commands unless requested.
""",
    "Python / pyATS": """
You are a senior Python network automation engineer.
Provide safe, readable, executable code with functions, type hints,
validation, comments, and error handling. Clearly mark sample data.
""",
    "Interview Prep": """
You are a technical interviewer for networking and Python automation roles.
Include a direct answer, project example, follow-up question, and mistake to avoid.
""",
    "Test Planning": """
You are a senior QA architect for networking products.
Create traceable positive, negative, resiliency, scale, rollback,
cleanup, and automation test coverage.
""",
}

QUICK_PROMPTS = [
    ("How does SD-WAN Auto VPN work?", "🌐", "card-blue"),
    ("Generate pyATS test cases for WAN failover", "🐍", "card-yellow"),
    ("Troubleshoot vEdge not joining vManage", "🛠️", "card-pink"),
    ("Explain Meraki Wireless overview", "📶", "card-green"),
    ("Create a detailed test plan from PRD", "📋", "card-purple"),
]


DAILY_FREE_LIMIT = int(os.getenv("DAILY_FREE_LIMIT", "25"))
MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", "8"))

NETWORK_TOOLS = [
    "CLI Output Analyzer",
    "Configuration Validator",
    "Route Table Analyzer",
    "SD-WAN Troubleshooter",
    "pyATS Test Generator",
    "REST API Generator",
    "PRD to Test Cases",
    "Interview Practice",
]
