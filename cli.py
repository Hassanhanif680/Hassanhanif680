#!/usr/bin/env python3
"""Command-line interface for AI Marketing Automation tools.

Run ``python cli.py --help`` to see available commands.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

from scripts.caption_generator import generate_caption, generate_caption_offline
from scripts.hashtag_generator import generate_hashtags, generate_hashtags_offline
from scripts.ad_copy_generator import generate_ad_copy, generate_ad_copy_offline

OUTPUTS_DIR = os.path.join(os.path.dirname(__file__), "outputs")


def _save_output(content: str, task: str) -> str:
    """Save generated content to the outputs/ directory and return the path."""
    os.makedirs(OUTPUTS_DIR, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    filename = f"{task}_{timestamp}.txt"
    filepath = os.path.join(OUTPUTS_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(content)
    return filepath


def cmd_caption(args: argparse.Namespace) -> None:
    """Handle the 'caption' sub-command."""
    if args.offline:
        result = generate_caption_offline(
            args.topic, platform=args.platform, tone=args.tone
        )
    else:
        result = generate_caption(
            args.topic, platform=args.platform, tone=args.tone
        )

    print("\n--- Generated Caption ---")
    print(result)

    if args.save:
        path = _save_output(result, "caption")
        print(f"\nSaved to {path}")


def cmd_hashtags(args: argparse.Namespace) -> None:
    """Handle the 'hashtags' sub-command."""
    if args.offline:
        tags = generate_hashtags_offline(args.topic, count=args.count)
    else:
        tags = generate_hashtags(
            args.topic, platform=args.platform, count=args.count
        )

    result = " ".join(tags)
    print("\n--- Generated Hashtags ---")
    print(result)

    if args.save:
        path = _save_output(result, "hashtags")
        print(f"\nSaved to {path}")


def cmd_adcopy(args: argparse.Namespace) -> None:
    """Handle the 'adcopy' sub-command."""
    if args.offline:
        result = generate_ad_copy_offline(
            args.product, audience=args.audience, style=args.style
        )
    else:
        result = generate_ad_copy(
            args.product,
            audience=args.audience,
            platform=args.platform,
            style=args.style,
        )

    print("\n--- Generated Ad Copy ---")
    print(result)

    if args.save:
        path = _save_output(result, "adcopy")
        print(f"\nSaved to {path}")


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser."""
    parser = argparse.ArgumentParser(
        prog="ai-marketing",
        description="AI Marketing Automation — generate captions, hashtags, and ad copies.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- caption ---
    cap = subparsers.add_parser("caption", help="Generate a social media caption")
    cap.add_argument("topic", help="Topic or subject of the caption")
    cap.add_argument(
        "--platform",
        default="instagram",
        help="Target platform (default: instagram)",
    )
    cap.add_argument(
        "--tone",
        default="professional",
        choices=["professional", "casual", "witty", "inspirational"],
        help="Caption tone (default: professional)",
    )
    cap.add_argument(
        "--offline",
        action="store_true",
        help="Use local templates instead of OpenAI API",
    )
    cap.add_argument(
        "--save", action="store_true", help="Save output to outputs/ directory"
    )
    cap.set_defaults(func=cmd_caption)

    # --- hashtags ---
    ht = subparsers.add_parser("hashtags", help="Generate hashtags")
    ht.add_argument("topic", help="Topic to generate hashtags for")
    ht.add_argument(
        "--platform",
        default="instagram",
        help="Target platform (default: instagram)",
    )
    ht.add_argument(
        "--count", type=int, default=10, help="Number of hashtags (default: 10)"
    )
    ht.add_argument(
        "--offline",
        action="store_true",
        help="Use local templates instead of OpenAI API",
    )
    ht.add_argument(
        "--save", action="store_true", help="Save output to outputs/ directory"
    )
    ht.set_defaults(func=cmd_hashtags)

    # --- adcopy ---
    ad = subparsers.add_parser("adcopy", help="Generate advertising copy")
    ad.add_argument("product", help="Product or service to advertise")
    ad.add_argument(
        "--audience", default="general", help="Target audience (default: general)"
    )
    ad.add_argument(
        "--platform",
        default="facebook",
        help="Ad platform (default: facebook)",
    )
    ad.add_argument(
        "--style",
        default="persuasive",
        choices=["persuasive", "informative", "playful"],
        help="Writing style (default: persuasive)",
    )
    ad.add_argument(
        "--offline",
        action="store_true",
        help="Use local templates instead of OpenAI API",
    )
    ad.add_argument(
        "--save", action="store_true", help="Save output to outputs/ directory"
    )
    ad.set_defaults(func=cmd_adcopy)

    return parser


def main(argv: list[str] | None = None) -> None:
    """Entry point for the CLI."""
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
