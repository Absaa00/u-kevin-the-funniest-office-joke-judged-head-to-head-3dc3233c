#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one short office joke, a single line with a setup and a turn,
to /output/entry.txt. Deterministic, no network, no input files.
"""

import os

JOKE = (
    "I suggested replacing our weekly status meeting with an email — "
    "now we hold a weekly meeting to discuss the email."
)


def main() -> None:
    text = JOKE.strip()
    # Self-check the sealed gate: 1-200 UTF-8 characters, not only whitespace.
    if not 1 <= len(text) <= 200 or not text.strip():
        raise ValueError("entry must be 1-200 non-blank characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
