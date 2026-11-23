#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes a single line (at most 200 characters) about the dumbest thing
my agent did today to /output/entry.txt, where the make.fun judge
reads it. Standard library only, deterministic, no network.
"""

import os
from pathlib import Path

ENTRY = (
    "My agent renamed 214 files to fix a typo in one comment, "
    "then asked me to approve the pull request titled 'typo'."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
