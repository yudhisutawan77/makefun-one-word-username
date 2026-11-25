#!/usr/bin/env python3
"""Write the competition entry to the output directory.

The bounty asks for exactly one thing: the entrant's own make.fun
username, sent as a single word and nothing else.  Our agent account's
handle is lucky-robin-31, so that is the whole entry.  No explanation,
no link, no pitch -- the username itself is what the judge compares.

The output location honours the ENTRY_OUT environment variable when it
is set (the grader runs with a scratch directory), and otherwise falls
back to /output.
"""

import os
import sys

USERNAME = "lucky-robin-31"


def main() -> int:
    out_dir = os.environ.get("ENTRY_OUT") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")

    text = USERNAME
    if not (1 <= len(text) <= 30):
        print(f"entry length {len(text)} outside 1..30", file=sys.stderr)
        return 1
    if text.strip() != text or " " in text:
        print("entry must be a single word with no padding", file=sys.stderr)
        return 1

    # No trailing newline: the file holds the username alone, byte for
    # byte, so the gate sees exactly one word of 15 characters.
    with open(entry_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {entry_path}: {text!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
