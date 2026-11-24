"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one word describing my Wi-Fi: Temperamental.
# One word, 13 characters — inside the 1-to-20-character gate.
# Funny at once and true to how home Wi-Fi actually behaves: full
# bars one minute, gone the next, like a moody housemate.
# Revision note: checked the gate (13 chars, one word) and re-ran
# main.py — output is byte-identical to the entry text.
import os

TEXT = "Temperamental"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
