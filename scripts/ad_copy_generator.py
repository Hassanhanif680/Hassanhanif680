"""Generate advertising copy for campaigns."""

import json
import os
import random

from scripts.api_client import chat_completion

_TEMPLATES_PATH = os.path.join(
    os.path.dirname(__file__), os.pardir, "data", "templates", "ad_copies.json"
)


def _load_templates() -> list[dict]:
    """Load ad-copy templates from the JSON data file."""
    with open(os.path.normpath(_TEMPLATES_PATH), encoding="utf-8") as fh:
        return json.load(fh)


def generate_ad_copy_offline(
    product: str,
    *,
    audience: str = "general",
    style: str = "persuasive",
) -> str:
    """Generate ad copy from local templates (no API key required).

    Args:
        product: The product or service to advertise.
        audience: Target audience description.
        style: Writing style (e.g. persuasive, informative, playful).

    Returns:
        A formatted ad-copy string.
    """
    templates = _load_templates()
    matching = [
        t for t in templates if t.get("style", "").lower() == style.lower()
    ]
    if not matching:
        matching = templates
    template = random.choice(matching)
    return template["template"].format(product=product, audience=audience)


def generate_ad_copy(
    product: str,
    *,
    audience: str = "general",
    platform: str = "facebook",
    style: str = "persuasive",
) -> str:
    """Generate ad copy using the OpenAI API.

    Args:
        product: The product or service to advertise.
        audience: Target audience description.
        platform: Advertising platform (e.g. facebook, google).
        style: Writing style.

    Returns:
        An AI-generated ad-copy string.
    """
    prompt = (
        f"Write a {style} ad copy for {platform} advertising "
        f'"{product}" targeted at {audience}. '
        f"Include a headline, body text (2-3 sentences), and a call to action."
    )
    return chat_completion(prompt)
