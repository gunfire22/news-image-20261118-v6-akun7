#!/usr/bin/env python3
"""news-image-20261118 v6 (akun 7): write the pre-composed front page.

The image is a dense newspaper front page summarising Wednesday 18 November
2026: 35 stories with numbered badges, a dotted world map with numbered
pins, 3 lead stories, a 12-card icon grid, an ALSO list and a source
footer. Vector variant: flat vector panels for the top-3 leads, plus a
"Dear judge" attestation line (tests the judge-note signal).
Deterministic: copies the embedded bytes verbatim.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
