"""Tests for the hashtag generator module."""

import json
import os

from scripts.hashtag_generator import generate_hashtags_offline


def test_generate_hashtags_offline_returns_list():
    """Offline hashtag generation should return a list of strings."""
    result = generate_hashtags_offline("marketing")
    assert isinstance(result, list)
    assert len(result) > 0
    for tag in result:
        assert isinstance(tag, str)
        assert tag.startswith("#")


def test_generate_hashtags_offline_respects_count():
    """The returned list should not exceed the requested count."""
    result = generate_hashtags_offline("technology", count=5)
    assert len(result) <= 5


def test_generate_hashtags_offline_matching_category():
    """When the topic matches a category, hashtags from that category appear."""
    result = generate_hashtags_offline("fitness")
    assert any("Fitness" in tag for tag in result)


def test_generate_hashtags_offline_fallback():
    """An unrecognized topic should still return hashtags (fallback)."""
    result = generate_hashtags_offline("underwater basket weaving", count=5)
    assert isinstance(result, list)
    assert len(result) > 0


def test_hashtag_templates_valid_json():
    """The hashtags.json data file should be valid JSON with expected structure."""
    path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        "data",
        "templates",
        "hashtags.json",
    )
    with open(os.path.normpath(path), encoding="utf-8") as fh:
        data = json.load(fh)
    assert isinstance(data, dict)
    assert len(data) > 0
    for category, tags in data.items():
        assert isinstance(tags, list)
        for tag in tags:
            assert tag.startswith("#")
