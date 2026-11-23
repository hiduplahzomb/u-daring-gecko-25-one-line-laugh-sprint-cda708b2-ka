#!/usr/bin/env python3
"""One-Line Laugh Sprint.

Writes one original funny line about everyday life to /output/entry.txt:
the elevator has been broken for months, my calves got fit from the
stairs, and the landlord just billed that as a fitness amenity. The
laugh comes from the last words — the "benefit" turns out to be a bill.
"""

import os
import sys

TEXT = (
    "Our elevator has been 'out of order' for 8 months, "
    "giving me elite calves — and the landlord just billed "
    "the stairs as 'fitness amenities'."
)


def main() -> int:
    # Gate: 1 to 200 characters, counted as Unicode code points,
    # and not only white space.
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        print("entry text fails the 1-200 gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)
    # Read back and re-check: the file on disk must be exactly the text
    # we gated, byte for byte.
    with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
        written = f.read()
    if written != TEXT or not (1 <= len(written) <= 200):
        print("written entry.txt does not match the gated text", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
