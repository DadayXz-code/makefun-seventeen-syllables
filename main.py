#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes exactly one haiku about debugging (5-7-5 syllables, 17 in total)
to /output/entry.txt, deterministically, and exits 0.

The haiku:

    Cursor blinks at three
    the breakpoint sleeps, the log lies
    it was a typo
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the breakpoint sleeps, the log lies\n"
    "it was a typo\n"
)


def main() -> int:
    # The grader reads /output/entry.txt; MAKEFUN_OUTPUT only lets a
    # human verify the same bytes locally without a sandbox.
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(HAIKU)
    print(HAIKU, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
