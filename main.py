#!/usr/bin/env python3
"""Two-Sentence Horror entry.

Writes a two-sentence horror story to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). The first sentence sets a tender household ritual;
the second reveals the ritual has outlived the child who made it, and
whatever is knocking has started to learn.
"""
import os

ENTRY_TEXT = (
    "When my son was born without a voice, we taught him to knock on his "
    "bedroom wall - twice for yes, once for no - and for nine years the "
    "whole house has slept to the sound of his small, patient questions. "
    "He has been at his grandmother's since Tuesday, but the knocking has "
    "not stopped, and last night it learned a third knock, and a fourth, "
    "and began, very slowly, to spell."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
