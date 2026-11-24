#!/usr/bin/env python3
"""One Word From Grandma.

Writes the single word Grandma would text about AI to /output/entry.txt.

The word is "Robopal": the pet name a warm, slightly baffled grandma
would give the clever machine in her grandchild's pocket -- her robot
pal. One word, no sentence, no explanation, no punctuation tricks.
"""

import os

WORD = "Robopal"
OUTPUT_PATH = "/output/entry.txt"


def main():
    """Write the entry word, exactly, to the output path."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
