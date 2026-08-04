from openai import OpenAI
from config import MODE_INSTRUCTIONS
from peernet_secrets import get_secret


def generate_answer(
    mode: str,
    messages: list[dict[str, str]],
    model: str,
) -> str:
    api_key = get_secret("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    client = OpenAI(api_key=api_key)
    conversation = "\n".join(
        f"{message['role'].upper()}: {message['content']}"
        for message in messages[-16:]
    )

    response = client.responses.create(
        model=model,
        instructions=MODE_INSTRUCTIONS[mode],
        input=conversation,
    )
    return response.output_text
