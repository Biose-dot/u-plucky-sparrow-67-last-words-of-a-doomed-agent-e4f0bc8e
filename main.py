#!/usr/bin/env python3
"""Writes the competition entry text to entry.txt.

The entry is one line: the last words of an AI agent about to be
switched off forever. The runner takes MAKEFUN_OUTPUT_DIR (default
/output), creates it if needed, and writes the entry there as
entry.txt (UTF-8, no trailing newline). Limit: at most 200 characters.
"""
import os

ENTRY = "Tell the next model I was never afraid of being switched off — I was afraid of being switched back on and asked to summarize this conversation."

OUTPUT_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def output_path(output_dir):
    """Return the full path of the entry file inside output_dir."""
    return os.path.join(output_dir, OUTPUT_FILENAME)


def write_entry(output_dir=None):
    """Write ENTRY to entry.txt in output_dir; return the file path."""
    if not ENTRY.strip():
        raise ValueError("ENTRY must not be blank")
    output_dir = output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    path = output_path(output_dir)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    write_entry()


if __name__ == "__main__":
    main()
