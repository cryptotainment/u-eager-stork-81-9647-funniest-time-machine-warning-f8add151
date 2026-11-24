#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — writes one warning label (<=120 chars)
to /output/entry.txt. Deterministic: no randomness, no time, no input."""

LABEL = "WARNING: Meeting your past self voids the warranty. He already read this label and ignored it."


def main() -> None:
    assert 1 <= len(LABEL) <= 120, f"label is {len(LABEL)} chars"
    assert "\n" not in LABEL, "label must be a single line"
    assert LABEL.strip() == LABEL, "label must not be whitespace-only"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
