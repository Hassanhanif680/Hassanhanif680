"""Tests for the CLI module."""

import os
import sys

from cli import build_parser, main, _save_output


def test_build_parser_caption():
    """Parser should accept the 'caption' sub-command with required args."""
    parser = build_parser()
    args = parser.parse_args(["caption", "AI tools", "--offline"])
    assert args.command == "caption"
    assert args.topic == "AI tools"
    assert args.offline is True


def test_build_parser_hashtags():
    """Parser should accept the 'hashtags' sub-command with required args."""
    parser = build_parser()
    args = parser.parse_args(["hashtags", "marketing", "--count", "5", "--offline"])
    assert args.command == "hashtags"
    assert args.topic == "marketing"
    assert args.count == 5


def test_build_parser_adcopy():
    """Parser should accept the 'adcopy' sub-command with required args."""
    parser = build_parser()
    args = parser.parse_args(
        ["adcopy", "Running Shoes", "--style", "playful", "--offline"]
    )
    assert args.command == "adcopy"
    assert args.product == "Running Shoes"
    assert args.style == "playful"


def test_save_output_creates_file(tmp_path, monkeypatch):
    """_save_output should write content to a file in the outputs directory."""
    monkeypatch.setattr("cli.OUTPUTS_DIR", str(tmp_path))
    path = _save_output("hello world", "test_task")
    assert os.path.isfile(path)
    with open(path, encoding="utf-8") as fh:
        assert fh.read() == "hello world"


def test_main_caption_offline(capsys):
    """Running 'caption --offline' should print a caption to stdout."""
    main(["caption", "SEO tips", "--offline"])
    captured = capsys.readouterr()
    assert "Generated Caption" in captured.out
    assert len(captured.out.strip()) > 0


def test_main_hashtags_offline(capsys):
    """Running 'hashtags --offline' should print hashtags to stdout."""
    main(["hashtags", "marketing", "--offline"])
    captured = capsys.readouterr()
    assert "Generated Hashtags" in captured.out


def test_main_adcopy_offline(capsys):
    """Running 'adcopy --offline' should print ad copy to stdout."""
    main(["adcopy", "Smartwatch", "--offline"])
    captured = capsys.readouterr()
    assert "Generated Ad Copy" in captured.out
