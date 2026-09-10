# -*- coding: utf-8 -*-
"""Audit clean-URL + base-path regressions."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
pages = [p.stem for p in ROOT.glob("*.html")]
stem_alt = "|".join(re.escape(s) for s in sorted(pages, key=len, reverse=True))
page_html = re.compile(rf"(?:{stem_alt})\.html", re.I)
root_nav = re.compile(
    r"""(?:href|action|data-thank-you-path|formaction)=["'](/[^"']*)["']""",
    re.I,
)

files = list(ROOT.glob("*.html")) + list((ROOT / "_snippets").glob("*.html"))
files += [
    ROOT / "sitemap.xml",
    ROOT / "llms.txt",
    ROOT / "robots.txt",
    ROOT / "js" / "main.js",
]

print("=== page .html still exposed in URLs? ===")
found = False
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
        # HTML comments naming source files are OK
        if line.strip().startswith("<!--") or "PAGE:" in line:
            continue
        print(f"{f.relative_to(ROOT)}:{i}: {line.strip()[:160]}")
        found = True
if not found:
    print("none")

print("=== root-relative nav links (break GH project previews)? ===")
found = False
for f in list(ROOT.glob("*.html")) + list((ROOT / "_snippets").glob("*.html")) + [ROOT / "js" / "main.js"]:
    if not f.exists():
        continue
    text = f.read_text(encoding="utf-8")
    for i, line in enumerate(text.splitlines(), 1):
        for m in root_nav.finditer(line):
            url = m.group(1)
            if re.match(r"^/(?:css|js|assets)/", url):
                continue
            if re.search(r"\.(?:css|js|png|jpe?g|webp|svg|pdf|ico)(?:$|\?)", url, re.I):
                continue
            # Absolute SEO uses https:// — not matched here
            print(f"{f.relative_to(ROOT)}:{i}: {url}")
            found = True
if not found:
    print("none")

print("=== SEO host check (must be norm4mayor.ca, not github.io) ===")
seo_files = [
    ROOT / "sitemap.xml",
    ROOT / "llms.txt",
    ROOT / "index.html",
    ROOT / "news.html",
]
for f in seo_files:
    text = f.read_text(encoding="utf-8")
    if "github.io" in text:
        print(f"FAIL {f.name} contains github.io")
    else:
        print(f"ok {f.name}")
