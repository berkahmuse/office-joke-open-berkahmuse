#!/usr/bin/env python3
"""Office Joke Open — make.fun program/v1 entry.

Writes one original single-line joke about office life to
/output/entry.txt.

The joke: setting a chat status to "do not disturb" backfires at once
— three colleagues interrupt to ask what it means. The setup is a
familiar office habit (the status line); the laugh lands on the last
few words, where the very people the status was meant to keep away
show up to interrogate it.

Deterministic: no input, no network, no randomness, no clock.
"""

from pathlib import Path

JOKE = (
    "I set my status to 'do not disturb' and three colleagues "
    "disturbed me within a minute to ask what it meant."
)
# Verified by running the program: 107 characters, one line,
# well under the 200-character cap.


def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
