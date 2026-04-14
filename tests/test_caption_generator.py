"""Tests for the caption generator module."""

import json
import os

from scripts.caption_generator import generate_caption_offline


def test_generate_caption_offline_returns_string():
    """Offline caption generation should return a non-empty string."""
    result = generate_caption_offline("digital marketing")
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_caption_offline_contains_topic():
    """The generated caption should contain the requested topic."""
    topic = "email marketing"
    result = generate_caption_offline(topic)
    assert topic in result


def test_generate_caption_offline_with_tone():
    """Captions generated with a specific tone should use matching templates."""
    result = generate_caption_offline("SEO", tone="casual")
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_caption_offline_with_unknown_tone_falls_back():
    """An unrecognized tone should fall back to any available template."""
    result = generate_caption_offline("branding", tone="nonexistent-tone")
    assert isinstance(result, str)
    assert "branding" in result


def test_caption_templates_valid_json():
    """The captions.json data file should be valid JSON with expected keys."""
    path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        "data",
        "templates",
        "captions.json",
    )
    with open(os.path.normpath(path), encoding="utf-8") as fh:
        data = json.load(fh)
    assert isinstance(data, list)
    assert len(data) > 0
    for entry in data:
        assert "tone" in entry
        assert "template" in entry
        assert "{topic}" in entry["template"]
