#!/usr/bin/env python3
"""Create lightweight JPEG thumbnails for the screenshot cards.

Usage (from the repository root):  python3 _build/make_thumbs.py
Reads images/*.png  ->  writes images/thumbs/<same-name>.jpg (600 px wide, top of screen only).
Needs Pillow:  pip install pillow
"""
import glob
import os

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "images")
DST = os.path.join(SRC, "thumbs")
WIDTH, MAX_RATIO = 600, 1.6

os.makedirs(DST, exist_ok=True)
n = 0
for path in sorted(glob.glob(os.path.join(SRC, "*.png"))):
    out = os.path.join(DST, os.path.basename(path)[:-4] + ".jpg")
    if os.path.exists(out) and os.path.getmtime(out) >= os.path.getmtime(path):
        continue
    im = Image.open(path).convert("RGB")
    w, h = im.size
    im = im.crop((0, 0, w, min(h, int(w * MAX_RATIO))))
    if w > WIDTH:
        im = im.resize((WIDTH, int(im.size[1] * WIDTH / w)), Image.LANCZOS)
    im.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    n += 1
print(f"{n} thumbnails written to images/thumbs/")
