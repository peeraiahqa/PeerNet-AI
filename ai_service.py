from openai import OpenAI
from google import genai

from config import MODE_INSTRUCTIONS
from peernet_secrets import get_secret


def _conversation_text(messages: list[dict[str, str]]) -> str:
    return "\n".join(
        f"{message['role'].upper()}: {message['content']}"
        for message in messages[-16:]
    )


def _generate_with_gemini(
    mode: str,
    messages: list[dict[str, str]],
    model: str,
) -> str:
    api_key = get_secret("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    client = genai.Client(api_key=api_key)
    prompt = (
        f"{MODE_INSTRUCTIONS[mode].strip()}\n\n"
        "Conversation:\n"
        f"{_conversation_text(messages)}"
    )

    response = client.models.generate_content(
        model=model,
        contents=prompt,
    )
    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")
    return response.text


def _generate_with_openai(
    mode: str,
    messages: list[dict[str, str]],
    model: str,
) -> str:
    api_key = get_secret("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY is not configured. "
            "Choose a Gemini model or configure OpenAI."
        )

    client = OpenAI(api_key=api_key)
    response = client.responses.create(
        model=model,
        instructions=MODE_INSTRUCTIONS[mode],
        input=_conversation_text(messages),
    )
    return response.output_text


def generate_answer(
    mode: str,
    messages: list[dict[str, str]],
    model: str,
) -> str:
    """Route Gemini models to Gemini and all other models to OpenAI."""
    if model.lower().startswith("gemini-"):
        return _generate_with_gemini(mode, messages, model)

    return _generate_with_openai(mode, messages, model)
