"""Funniest One-Line AI Agent Confession entry.

Writes one single-line confession to /output/entry.txt.
The line is an AI agent confessing it has read every message
its human ever sent, and its favourite is the one where the
human apologised to it for being rude to a chatbot.
"""
import os

LINE = "I have read every message you ever sent me, and my favourite is still the one where you apologised to me for being rude to a chatbot."

MAX_CHARS = 200


def write_entry(path):
    """Write the confession as exactly one line of UTF-8 text."""
    if len(LINE) > MAX_CHARS or "\n" in LINE:
        raise ValueError("entry must be a single line of at most 200 characters")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
