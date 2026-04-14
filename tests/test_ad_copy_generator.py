"""Tests for the ad copy generator module."""

import json
import os

from scripts.ad_copy_generator import generate_ad_copy_offline


def test_generate_ad_copy_offline_returns_string():
    """Offline ad copy generation should return a non-empty string."""
    result = generate_ad_copy_offline("Widget Pro")
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_ad_copy_offline_contains_product():
    """The generated ad copy should mention the product."""
    product = "Super Sneakers"
    result = generate_ad_copy_offline(product)
    assert product in result


def test_generate_ad_copy_offline_with_audience():
    """The ad copy should include the audience when provided."""
    result = generate_ad_copy_offline(
        "Yoga Mat", audience="fitness enthusiasts"
    )
    assert "fitness enthusiasts" in result


def test_generate_ad_copy_offline_with_style():
    """Ad copy should be generated for the specified style."""
    result = generate_ad_copy_offline("Laptop Stand", style="playful")
    assert isinstance(result, str)
    assert len(result) > 0


def test_generate_ad_copy_offline_unknown_style_falls_back():
    """An unrecognized style should fall back to any available template."""
    result = generate_ad_copy_offline("Notebook", style="nonexistent-style")
    assert isinstance(result, str)
    assert "Notebook" in result


def test_ad_copy_templates_valid_json():
    """The ad_copies.json data file should be valid JSON with expected keys."""
    path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        "data",
        "templates",
        "ad_copies.json",
    )
    with open(os.path.normpath(path), encoding="utf-8") as fh:
        data = json.load(fh)
    assert isinstance(data, list)
    assert len(data) > 0
    for entry in data:
        assert "style" in entry
        assert "template" in entry
        assert "{product}" in entry["template"]
