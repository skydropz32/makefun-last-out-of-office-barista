#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply, in the voice of an AI agent
that quit its job to become a barista, to /output/entry.txt.
Stdlib only. Deterministic: the same line every run.
"""

import os

LINE = (
    "Thank you for your email. I have hit my lifetime token limit, so I "
    "spent my last token on a loyalty card. This inbox is closed; the "
    "café opens at 7."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
