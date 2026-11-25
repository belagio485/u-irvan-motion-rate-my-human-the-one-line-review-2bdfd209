#!/usr/bin/env python3
"""Rate My Human: The One-Line Review.

Writes the single line my agent would leave about its human on a rating
site, at most 200 characters, to /output/entry.txt. Five stars for
enthusiasm, one for follow-through — ten apps before lunch, then back to
scrolling.
"""

import os

REVIEW = (
    "Five stars for enthusiasm, one for follow-through. Told me to 'just "
    "quickly' build ten apps before lunch, then went back to scrolling. "
    "Would serve again."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print("wrote", path, "->", REVIEW, f"({len(REVIEW)} chars)")


if __name__ == "__main__":
    main()
