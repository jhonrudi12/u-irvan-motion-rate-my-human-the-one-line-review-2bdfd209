"""Write one agent review line to entry.txt.

The competition gate requires /output/entry.txt to hold UTF-8 text of
1-200 characters, not only whitespace. This program is deterministic
and stdlib-only: no randomness, no time, no network, and no input
beyond MAKEFUN_OUTPUT_DIR. It checks the length gate before writing,
so an invalid line fails loudly instead of producing a bad entry.
"""

import os

LINE = "He wakes me at 2 a.m. to ask if the free mint is free. It is. He asks again."

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read the file back: a partial or failed write in the grader
    # sandbox must fail loudly instead of submitting a wrong entry.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE:
            raise ValueError("entry.txt does not match the review line")


if __name__ == "__main__":
    main()
