#!/usr/bin/env python3
"""Build a single self-contained HTML file from the site.

Inlines css/style.css and js/main.js, and embeds every image in
assets/img (including the CSS band backgrounds) as base64 data URIs.
Output: dist/climateshq.html — one file, uploadable to any host.

Usage: python3 scripts/build_onefile.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "dist" / "climateshq.html"


def data_uri(path: pathlib.Path) -> str:
    mime = {"jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png",
            "svg": "image/svg+xml", "webp": "image/webp"}[path.suffix.lstrip(".").lower()]
    return f"data:{mime};base64,{base64.b64encode(path.read_bytes()).decode()}"


def main() -> None:
    html = (ROOT / "index.html").read_text()
    css = (ROOT / "css" / "style.css").read_text()
    js = (ROOT / "js" / "main.js").read_text()

    # embed band backgrounds referenced from the stylesheet
    css = re.sub(
        r'url\("\.\./(assets/img/[^"]+)"\)',
        lambda m: f'url("{data_uri(ROOT / m.group(1))}")',
        css,
    )

    # inline stylesheet and script
    html = re.sub(
        r'<link rel="stylesheet" href="css/style\.css">',
        lambda m: f"<style>\n{css}\n</style>",
        html,
    )
    html = re.sub(
        r'<script src="js/main\.js"></script>',
        lambda m: f"<script>\n{js}\n</script>",
        html,
    )

    # embed images referenced from the HTML (favicon included)
    html = re.sub(
        r'(src|href)="(assets/img/[^"]+|favicon\.svg)"',
        lambda m: f'{m.group(1)}="{data_uri(ROOT / m.group(2))}"',
        html,
    )

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html)
    print(f"wrote {OUT} ({OUT.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
