"""API client for interacting with OpenAI's chat completions API."""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")


def get_client() -> OpenAI:
    """Return an authenticated OpenAI client.

    Raises:
        ValueError: If the OPENAI_API_KEY environment variable is not set.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is not set. "
            "Create a .env file with your key (see .env.example)."
        )
    return OpenAI(api_key=api_key)


def chat_completion(prompt: str, *, model: str | None = None) -> str:
    """Send a prompt to the OpenAI chat completions API and return the reply.

    Args:
        prompt: The user message to send.
        model: The model to use. Defaults to the OPENAI_MODEL env var or
               ``gpt-3.5-turbo``.

    Returns:
        The assistant's reply text.
    """
    client = get_client()
    response = client.chat.completions.create(
        model=model or DEFAULT_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    content = response.choices[0].message.content
    return content.strip() if content else ""
