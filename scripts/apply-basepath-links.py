# -*- coding: utf-8 -*-
"""Convert root-relative clean URLs to path-relative ones for GH Pages project previews.

SEO absolute URLs (canonical / OG / JSON-LD / sitemap / llms) stay on the
production domain. Navigation and in-page links become path-relative so they
resolve under /REPOSITORY-NAME/ on GitHub Pages project sites and under / on
the custom domain.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://norm4mayor.ca"

PAGE_STEMS = sorted(p.stem for p in ROOT.glob("*.html"))
PAGE_STEMS_DESC = sorted(PAGE_STEMS, key=len, reverse=True)
STEM_ALT = "|".join(re.escape(s) for s in PAGE_STEMS_DESC if s != "index")

# Attributes that carry in-page / navigation URLs (NOT canonical/og absolute SEO).
NAV_ATTRS = "href|action|data-thank-you-path|data-next|formaction"


def to_path_relative(url: str) -> str:
    """Map a root-relative site URL to a path-relative clean URL."""
    if not url.startswith("/"):
        return url
    # External protocol-relative or accidental
    if url.startswith("//"):
        return url

    rest = url[1:]  # drop leading /
    if rest == "" or rest.startswith("?") or rest.startswith("#"):
        # homepage /, /#hash, /?query
        if rest.startswith("#"):
            return "./" + rest
        if rest.startswith("?"):
            return "./" + rest
        return "./"

    # /about-norm, /about-norm#x, /about-norm?x
    return rest


def rewrite_nav_urls(text: str) -> str:
    # href="/" , href="/#x" , href="/about-norm" , href="/about-norm#x"
    def attr_sub(m: re.Match[str]) -> str:
        raw = m.group("url")
        # Leave absolute http(s) alone (SEO + external)
        if raw.startswith("http://") or raw.startswith("https://") or raw.startswith("mailto:") or raw.startswith("tel:"):
            return m.group(0)
        # Leave in-page hash-only
        if raw.startswith("#"):
            return m.group(0)
        # Leave asset paths that still use extensions under /css /js /assets
        if re.match(r"^/(?:css|js|assets|docs)/", raw):
            return m.group(0)
        if raw.startswith("/") and re.search(r"\.(?:css|js|png|jpe?g|webp|gif|svg|pdf|ico|woff2?|ttf|map)(?:$|\?)", raw, re.I):
            return m.group(0)

        converted = to_path_relative(raw)
        return f'{m.group("attr")}={m.group("q")}{converted}{m.group("q")}'

    text = re.sub(
        rf"(?P<attr>{NAV_ATTRS})=(?P<q>[\"'])(?P<url>[^\"']+)(?P=q)",
        attr_sub,
        text,
        flags=re.I,
    )

    # Meta refresh url=/news
    text = re.sub(
        r"url=/(?P<path>[^\s\"'>]+)",
        lambda m: f"url={to_path_relative('/' + m.group('path'))}",
        text,
        flags=re.I,
    )

    # location.replace("/news")
    text = re.sub(
        rf"location\.replace\((?P<q>[\"'])/(?P<path>[^\"']*)(?P=q)\)",
        lambda m: f"location.replace({m.group('q')}{to_path_relative('/' + m.group('path'))}{m.group('q')})",
        text,
    )

    # JS string defaults
    text = text.replace('"/thank-you"', '"thank-you"')
    text = text.replace("'/thank-you'", "'thank-you'")

    return text


def main() -> None:
    changed: list[str] = []
    targets = list(ROOT.glob("*.html")) + list((ROOT / "_snippets").glob("*.html"))
    targets.append(ROOT / "js" / "main.js")

    for path in targets:
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        updated = rewrite_nav_urls(original)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))

    # Keep SEO files absolute on production — do not touch sitemap/llms/robots.
    print(f"updated {len(changed)} files")
    for f in changed:
        print(f"  {f}")


if __name__ == "__main__":
    main()
