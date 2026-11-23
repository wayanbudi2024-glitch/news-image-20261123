# A news-image-20261123 entry (Python 3.13, standard library only): the
# image is the entry.png beside this file, and the program copies it to
# /output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB
# and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DST = OUT_DIR / "entry.png"

OUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)

# Fail loudly rather than hand the grader a truncated copy.
if DST.stat().st_size != SRC.stat().st_size:
    raise SystemExit("entry.png copy is incomplete")

# A whole PNG starts with its 8-byte signature; a truncated or corrupted
# copy would not, so refuse to hand the grader a broken file.
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
with DST.open("rb") as f:
    if f.read(8) != PNG_MAGIC:
        raise SystemExit("entry.png copy is not a valid PNG (bad magic bytes)")
