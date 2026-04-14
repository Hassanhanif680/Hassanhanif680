"""Generate relevant hashtags for social media posts."""

import json
import os

from scripts.api_client import chat_completion

_TEMPLATES_PATH = os.path.join(
    os.path.dirname(__file__), os.pardir, "data", "templates", "hashtags.json"
)


def _load_hashtag_sets() -> dict[str, list[str]]:
    """Load hashtag sets grouped by category from the JSON data file."""
    with open(os.path.normpath(_TEMPLATES_PATH), encoding="utf-8") as fh:
        return json.load(fh)


def generate_hashtags_offline(
    topic: str,
    *,
    count: int = 10,
) -> list[str]:
    """Pick relevant hashtags from the local data file (no API key required).

    Args:
        topic: The subject to find hashtags for.
        count: Maximum number of hashtags to return.

    Returns:
        A list of hashtag strings.
    """
    data = _load_hashtag_sets()
    topic_lower = topic.lower()

    # Collect hashtags from categories whose name appears in the topic
    matched: list[str] = []
    for category, tags in data.items():
        if category.lower() in topic_lower or topic_lower in category.lower():
            matched.extend(tags)

    # Fallback: merge all categories
    if not matched:
        for tags in data.values():
            matched.extend(tags)

    # Deduplicate while preserving order, then trim
    seen: set[str] = set()
    unique: list[str] = []
    for tag in matched:
        if tag not in seen:
            seen.add(tag)
            unique.append(tag)
    return unique[:count]


def generate_hashtags(
    topic: str,
    *,
    platform: str = "instagram",
    count: int = 15,
) -> list[str]:
    """Generate hashtags using the OpenAI API.

    Args:
        topic: The subject to find hashtags for.
        platform: Target social media platform.
        count: Number of hashtags to generate.

    Returns:
        A list of hashtag strings.
    """
    prompt = (
        f"Generate {count} relevant and trending hashtags for a {platform} "
        f'post about "{topic}". Return only the hashtags, one per line, '
        f"each starting with #."
    )
    raw = chat_completion(prompt)
    return [
        line.strip()
        for line in raw.splitlines()
        if line.strip().startswith("#")
    ][:count]
