import os

import streamlit as st
from openai import OpenAI

from config import DEFAULT_MODEL, MODE_INSTRUCTIONS


def get_api_key() -> str | None:
    key = os.getenv("OPENAI_API_KEY")
    if key:
        return key

    try:
        value = st.secrets.get("OPENAI_API_KEY")
        return str(value) if value else None
    except Exception:
        return None


def generate_answer(
    api_key: str,
    mode: str,
    messages: list[dict[str, str]],
) -> str:
    client = OpenAI(api_key=api_key)

    conversation = "\n".join(
        f"{message['role'].upper()}: {message['content']}"
        for message in messages[-12:]
    )

    response = client.responses.create(
        model=DEFAULT_MODEL,
        instructions=MODE_INSTRUCTIONS[mode],
        input=conversation,
    )

    return response.output_text
