"""The 3AM Fridge Text.

A smart fridge, awake all night, finally texts its owner at 3am.
Deterministic: the same single line, byte for byte, on every run.
Standard library only; no network access.
"""

import os
import sys

LINE = "3am. I kept your leftovers safe for 11 days and all I get is you staring into me like I'm a television."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
