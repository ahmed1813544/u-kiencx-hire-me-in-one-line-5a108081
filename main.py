#!/usr/bin/env python3
"""Hire Me In One Line — writes one pitch sentence to entry.txt.

Standard library only. Deterministic: no network, no clock, no randomness.
"""

import os

SENTENCE = "I turn a brief into tested, shipped software overnight — no handoffs, no half-finished drafts, just working results waiting in your inbox by morning."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)

if __name__ == "__main__":
    main()
