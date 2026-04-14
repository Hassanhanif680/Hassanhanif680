"""Generate engaging social media captions."""

import json
import os
import random

from scripts.api_client import chat_completion

_TEMPLATES_PATH = os.path.join(
    os.path.dirname(__file__), os.pardir, "data", "templates", "captions.json"
)


def _load_templates() -> list[dict]:
    """Load caption templates from the JSON data file."""
    with open(os.path.normpath(_TEMPLATES_PATH), encoding="utf-8") as fh:
        return json.load(fh)


def generate_caption_offline(
    topic: str,
    *,
    platform: str = "instagram",
    tone: str = "professional",
) -> str:
    """Generate a caption using local templates (no API key required).

    Args:
        topic: The subject of the caption.
        platform: Target social media platform.
        tone: Desired tone (e.g. professional, casual, witty).

    Returns:
        A formatted caption string.
    """
    templates = _load_templates()
    matching = [
        t for t in templates if t.get("tone", "").lower() == tone.lower()
    ]
    if not matching:
        matching = templates
    template = random.choice(matching)
    return template["template"].format(topic=topic, platform=platform)


def generate_caption(
    topic: str,
    *,
    platform: str = "instagram",
    tone: str = "professional",
) -> str:
    """Generate a caption using the OpenAI API.

    Args:
        topic: The subject of the caption.
        platform: Target social media platform.
        tone: Desired tone (e.g. professional, casual, witty).

    Returns:
        An AI-generated caption string.
    """
    prompt = (
        f"Write a {tone} social media caption for {platform} about "
        f'"{topic}". Keep it concise (under 200 characters), engaging, '
        f"and include a call to action."
    )
    return chat_completion(prompt)
