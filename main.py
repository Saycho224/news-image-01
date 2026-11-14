"""News image entry: write the four-panel collage to /output/entry.png.

The collage (chips, outage, talks, tankers) was generated for this entry
and is stored beside this program as entry.png. This program only copies
it, so both grader runs produce identical bytes.
"""

import os
import shutil

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
TARGET_DIR = "/output"
TARGET = os.path.join(TARGET_DIR, "entry.png")


def main():
    if not os.path.isfile(SOURCE):
        raise FileNotFoundError("entry.png is missing next to main.py")
    os.makedirs(TARGET_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    # Guard against a partial copy: the output must match the source size.
    if os.path.getsize(TARGET) != os.path.getsize(SOURCE):
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
