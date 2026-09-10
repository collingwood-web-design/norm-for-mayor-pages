# -*- coding: utf-8 -*-
"""Convert public URLs and internal links to clean (extensionless) form.

Keeps on-disk *.html filenames for GitHub Pages. Rewrites user-facing and SEO
URLs only. Filesystem paths in Python (open/read of *.html) are left alone.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://norm4mayor.ca"

PAGE_STEMS = sorted(p.stem for p in ROOT.glob("*.html"))
PAGE_STEMS_DESC = sorted(PAGE_STEMS, key=len, reverse=True)
STEM_ALT = "|".join(re.escape(s) for s in PAGE_STEMS_DESC)

CLIENT_REDIRECT = """    <script>
      /* Prefer clean URLs when someone lands on the .html form. */
      (function () {
        var path = window.location.pathname;
        if (!/\\.html$/i.test(path)) return;
        var clean = path.replace(/\\.html$/i, "");
        if (/\\/index$/i.test(clean)) clean = clean.replace(/\\/index$/i, "/") || "/";
        if (clean === "") clean = "/";
        window.location.replace(clean + window.location.search + window.location.hash);
      })();
    </script>
"""


def clean_path(stem: str, fragment: str = "", query: str = "") -> str:
    """Path-relative clean URL for navigation (GH Pages project-safe)."""
    if stem == "index":
        path = "./"
        if query:
            path = f"./?{query}"
        if fragment:
            path = f"{path}#{fragment}" if query else f"./#{fragment}"
        return path

    path = stem
    if query:
        path += f"?{query}"
    if fragment:
        path += f"#{fragment}"
    return path


def clean_abs(stem: str, fragment: str = "", query: str = "") -> str:
    """Absolute production clean URL for SEO metadata only."""
    base = f"{SITE}/" if stem == "index" else f"{SITE}/{stem}"
    if query:
        base += f"?{query}"
    if fragment:
        base += f"#{fragment}"
    return base


def rewrite_text(text: str, *, urls_only: bool) -> str:
    # Absolute site URLs
    text = re.sub(
        rf"{re.escape(SITE)}/(?P<stem>{STEM_ALT})\.html"
        rf"(?:\?(?P<query>[^\"'\s#>]*))?(?:#(?P<frag>[^\"'\s]*))?",
        lambda m: clean_abs(m.group("stem"), m.group("frag") or "", m.group("query") or ""),
        text,
    )

    # Root-absolute /page.html
    text = re.sub(
        rf"(?P<prefix>['\"=\(\s]|^)/(?P<stem>{STEM_ALT})\.html"
        rf"(?:\?(?P<query>[^\"'\s#>]*))?(?:#(?P<frag>[^\"'\s]*))?",
        lambda m: f"{m.group('prefix')}{clean_path(m.group('stem'), m.group('frag') or '', m.group('query') or '')}",
        text,
        flags=re.M,
    )

    # Common URL-bearing attributes with relative page.html
    attr_alt = "href|content|action|data-thank-you-path|data-next|formaction"
    text = re.sub(
        rf"(?P<attr>{attr_alt})=(?P<q>[\"'])(?P<stem>{STEM_ALT})\.html"
        rf"(?:\?(?P<query>[^\"'#]*))?(?:#(?P<frag>[^\"']*))?(?P=q)",
        lambda m: (
            f'{m.group("attr")}={m.group("q")}'
            f'{clean_path(m.group("stem"), m.group("frag") or "", m.group("query") or "")}'
            f'{m.group("q")}'
        ),
        text,
        flags=re.I,
    )

    # Meta refresh + JS location.replace
    text = re.sub(
        rf"url=(?P<stem>{STEM_ALT})\.html(?:#(?P<frag>[^\"'\s>]*))?",
        lambda m: f"url={clean_path(m.group('stem'), m.group('frag') or '')}",
        text,
        flags=re.I,
    )
    text = re.sub(
        rf"location\.replace\((?P<q>[\"'])(?P<stem>{STEM_ALT})\.html"
        rf"(?:#(?P<frag>[^\"']*))?(?P=q)\)",
        lambda m: (
            f"location.replace({m.group('q')}"
            f"{clean_path(m.group('stem'), m.group('frag') or '')}"
            f"{m.group('q')})"
        ),
        text,
    )

    text = text.replace('"thank-you.html"', '"thank-you"')
    text = text.replace("'thank-you.html'", "'thank-you'")

    if not urls_only:
        # Remaining quoted relative page refs (JSON-LD strings, etc.)
        text = re.sub(
            rf"(?P<q>[\"'])(?P<stem>{STEM_ALT})\.html"
            rf"(?:\?(?P<query>[^\"'#]*))?(?:#(?P<frag>[^\"']*))?(?P=q)",
            lambda m: (
                f'{m.group("q")}'
                f'{clean_path(m.group("stem"), m.group("frag") or "", m.group("query") or "")}'
                f'{m.group("q")}'
            ),
            text,
        )

    return text


def inject_client_redirect(text: str) -> str:
    if "Prefer clean URLs when someone lands" in text:
        return text
    return re.sub(r"(<head[^>]*>)", r"\1\n" + CLIENT_REDIRECT, text, count=1, flags=re.I)


def main() -> None:
    changed: list[str] = []

    stub_redirects = {"activities.html", "experience.html", "priorities.html"}
    for path in list(ROOT.glob("*.html")) + list((ROOT / "_snippets").glob("*.html")):
        original = path.read_text(encoding="utf-8")
        updated = rewrite_text(original, urls_only=False)
        if path.parent.name != "_snippets" and path.name not in stub_redirects:
            updated = inject_client_redirect(updated)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))

    for rel in ("sitemap.xml", "robots.txt", "llms.txt", "js/main.js"):
        path = ROOT / rel
        if not path.exists():
            continue
        original = path.read_text(encoding="utf-8")
        updated = rewrite_text(original, urls_only=False)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(rel)

    for path in (ROOT / "scripts").glob("*.py"):
        if path.name == "apply-clean-urls.py":
            continue
        original = path.read_text(encoding="utf-8")
        updated = rewrite_text(original, urls_only=True)
        if updated != original:
            path.write_text(updated, encoding="utf-8", newline="\n")
            changed.append(str(path.relative_to(ROOT)))

    print(f"updated {len(changed)} files")
    for f in changed:
        print(f"  {f}")


if __name__ == "__main__":
    main()
