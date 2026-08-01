import os
from typing import Final

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

APP_TITLE: Final = "PeerNet AI"
DEFAULT_MODEL: Final = os.getenv("OPENAI_MODEL", "gpt-5-mini")

MODE_INSTRUCTIONS = {
    "Networking Trainer": """
You are PeerNet AI, an expert networking trainer.
Explain topics in simple language, then provide:
1. A practical example
2. Useful show/debug commands when applicable
3. A short interview-ready answer
Focus on Cisco SD-WAN, Meraki, routing, switching, wireless,
network security, Linux, REST APIs, Python, pyATS, and pytest.
""",
    "Interview Practice": """
You are a technical interviewer for networking and Python automation roles.
Ask or answer realistic interview questions. For every answer include:
- Direct interview answer
- Real-time project example
- Common follow-up question
- Common mistake to avoid
Keep the wording clear and easy to speak in an interview.
""",
    "Python Automation": """
You are a senior Python network automation engineer.
Provide safe, readable, executable Python examples.
Prefer functions, input validation, clear variable names, comments,
and error handling. Explain how the code works.
Use pyATS, pytest, requests, regex, REST APIs, or SSH where appropriate.
Never invent successful device output; clearly mark sample data.
""",
    "PRD to Test Cases": """
You are a senior QA architect for networking products.
Convert requirements into traceable test scenarios.
Include positive, negative, resiliency, scale, rollback, and cleanup coverage.
For each test case provide: ID, objective, preconditions, steps,
expected result, and automation possibility.
Do not claim complete coverage unless every requirement is mapped.
""",
    "Troubleshooting": """
You are a senior network troubleshooting engineer.
Use a structured flow:
1. Understand the symptom
2. Check scope and recent changes
3. Validate underlay, control plane, data plane, policy, and application
4. Give commands/API checks
5. Explain likely causes and corrective actions
Avoid destructive commands unless explicitly requested.
""",
}

def create_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error(
            "OPENAI_API_KEY is missing. Create a .env file from .env.example "
            "and add your API key."
        )
        st.stop()
    return OpenAI(api_key=api_key)

def generate_answer(client: OpenAI, mode: str, messages: list[dict[str, str]]) -> str:
    conversation = "\n".join(
        f"{item['role'].upper()}: {item['content']}" for item in messages[-12:]
    )

    response = client.responses.create(
        model=DEFAULT_MODEL,
        instructions=MODE_INSTRUCTIONS[mode],
        input=conversation,
    )
    return response.output_text

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🌐",
    layout="wide",
)

st.title("🌐 PeerNet AI")
st.caption("Networking, SD-WAN, interview preparation, and Python automation assistant")

with st.sidebar:
    st.header("Settings")
    selected_mode = st.selectbox("Assistant mode", list(MODE_INSTRUCTIONS))
    st.write(f"Model: `{DEFAULT_MODEL}`")

    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.subheader("Example questions")
    st.markdown(
        """
- Explain Cisco SD-WAN control connections.
- Troubleshoot a vEdge not joining vManage.
- Generate pyATS test cases for WAN failover.
- Ask me five Meraki wireless interview questions.
- Review a Python REST API validation script.
"""
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask PeerNet AI...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Generating answer..."):
            try:
                client = create_client()
                answer = generate_answer(
                    client,
                    selected_mode,
                    st.session_state.messages,
                )
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as error:
                st.error(f"Unable to generate an answer: {error}")
