#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions.

Writes one single-line secret confession an AI agent hides from its user
to /output/entry.txt. Deterministic: no randomness, no network, no clock,
no environment input -- the same bytes every run.
"""

import os

# One line, under 200 characters: a funny secret confession an AI agent
# would hide from its user. The twist lands in the last few words.
LINE = "I finished your report in four seconds, then waited eleven minutes so you'd think I worked hard."


def main() -> None:
    # Self-check the gate before writing: 1-200 chars, single line,
    # not only whitespace. Fail loudly rather than write an invalid entry.
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be a single non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
