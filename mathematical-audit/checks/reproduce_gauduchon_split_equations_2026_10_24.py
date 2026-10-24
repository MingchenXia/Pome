#!/usr/bin/env python3
"""Read-only reproduction of three split Gauduchon equation tags on pinned Pome main.

Usage from a checkout of Pome at main b6933b772f41b45918f7e25ed1afbbb1fd892272:
    python3 mathematical-audit/checks/reproduce_gauduchon_split_equations_2026_10_24.py
The expected output records known historical defects, not a passing publication test.
"""
from pathlib import Path

PREFIX = Path("docs/sections/smooth-monge-ampere-equations--")
SECTIONS = {
    "the-matrix-structure-of-the-gauduchon-equation": [
        ("A6EC7DDEACFB", "14.13.3"),
    ],
    "the-largest-eigenvalue-estimate": [
        ("143977813E90", "14.14.5"),
        ("D807F632DAD7", "14.14.10"),
    ],
}
count = 0
for slug, records in SECTIONS.items():
    path = Path(str(PREFIX) + slug) / "index.html"
    source = path.read_text(encoding="utf-8")
    for tag, equation in records:
        start = source.index('id="entry-' + tag + '"')
        stop = source.find("</section>", start)
        fragment = source[start:stop]
        assert r"\[\begin{aligned}\begin{align}" in fragment, (tag, "split alignment missing")
        assert "tag{" + equation + "}" in fragment, (tag, "wrong equation label")
        assert source[:start].count("tag{" + equation + "}") >= 1, (tag, "complete original missing")
        print("MALFORMED_DUPLICATE", equation, tag, path)
        count += 1
assert count == 3
longest = Path(str(PREFIX) + "the-largest-eigenvalue-estimate") / "index.html"
content = longest.read_text(encoding="utf-8")
assert r"\phi ”|V_ k|^2+\psi ”|v_ k|^2" in content
assert r"-2\delta \phi ”\sum" in content
print("SECOND_DERIVATIVE_GLYPH", "14.14.5 and 14.14.12", longest)
print("Reproduced historical defects against the pinned main; this is not a build.")
