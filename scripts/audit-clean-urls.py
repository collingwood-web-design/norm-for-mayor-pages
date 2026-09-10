# -*- coding: utf-8 -*-
"""Audit remaining page .html URLs that should be clean."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
pages = [p.stem for p in ROOT.glob("*.html")]
stem_alt = "|".join(re.escape(s) for s in sorted(pages, key=len, reverse=True))
page_html = re.compile(rf"(?:{stem_alt})\.html", re.I)

files = list(ROOT.glob("*.html")) + list((ROOT / "_snippets").glob("*.html"))
files += [ROOT / "sitemap.xml", ROOT / "llms.txt", ROOT / "robots.txt", ROOT / "js" / "main.js"]

for f in files:
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8")
    for i, line in enumerate(text.splitlines(), 1):
        if not page_html.search(line):
            continue
        if "Prefer clean URLs" in line or r"\.html$" in line or "replace(/\\.html" in line:
            continue
        if "pathname" in line and "html" in line:
            continue
        print(f"{f.relative_to(ROOT)}:{i}: {line.strip()[:160]}")
