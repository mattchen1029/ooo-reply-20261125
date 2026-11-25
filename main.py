"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Writes a single funny out-of-office auto-reply, one line long, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

MIN_CHARS = 1
MAX_CHARS = 160
OUTPUT_NAME = "entry.txt"

REPLY = "I'm out of office until Monday. Your email will be answered in the order of how much I like you."


def validate_reply(text):
    """The gate requires UTF-8 text of 1-160 chars, a single line, not blank."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"reply must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}")
    if "\n" in text.strip():
        raise ValueError("reply must be a single line")
    if not text.strip():
        raise ValueError("reply must not be only whitespace")


def write_entry(text, out_dir):
    validate_reply(text)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(REPLY, out_dir)


if __name__ == "__main__":
    main()
