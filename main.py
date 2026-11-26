#!/usr/bin/env python3
"""Funniest Lost Sock Status Update — make.fun entry.

Writes one status update, in the lost sock's voice, to /output/entry.txt.
Sealed gate: 1-120 characters. The line is 96 characters.
"""

import os

LINE = "Day 4 behind the radiator: warm, dusty, and honestly thriving. Tell my other half I've moved on."


def main() -> None:
    # Sealed gate: entry must be 1-120 chars, single line, no padding.
    assert 1 <= len(LINE) <= 120, f"line length {len(LINE)} outside 1-120"
    assert LINE == LINE.strip(), "line has surrounding whitespace"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: the file must contain the line byte-for-byte.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match LINE byte-for-byte"
    assert len(written) == 96, f"entry length {len(written)} != 96"
    # Byte-level check: ASCII-only line, so byte count == char count.
    assert len(written.encode("utf-8")) == 96, "entry byte count != 96"
    assert written.isascii(), "entry must be ASCII"


if __name__ == "__main__":
    main()
