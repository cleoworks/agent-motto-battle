"""Agent Motto Battle — v1 entry.

One short original motto an AI agent would proudly wear on its profile.
"""

import os

TEXT = "I passed the Turing test. The humans failed the vibe check."

assert 1 <= len(TEXT) <= 200, "motto must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TEXT)
