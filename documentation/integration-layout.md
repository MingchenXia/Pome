# Integration layout and numbering

Reader numbering belongs to Pome's current organization, independently of the original manuscripts. This rule applies to every contributing source and future integration.

## Sections and subordinate material

`collection.json` assigns subjects to shared chapters. Its reviewed `section_promotions` identify stable canonical heading tags at which a long or mixed subject splits into smaller sections. Boundaries are checked in source order; a missing, repeated, or reordered boundary fails the build. The existing broad subject URL remains an overview with its introductory prose and links. It is not a second full copy of its child sections.

A retained source heading below a Pome section is a subsection. A heading that repeats its containing section's title is absorbed into that section. Its old tag URL redirects to the introduction inside the section, and its source metadata and content remain available. Chapter pages list sections and their retained subsections.

Section titles are followed directly by reading content. Do not display topic metadata descriptions as small explanatory subtitles beneath them.

The 15 October 2026 layout review subdivides 36 section groups at 413 reviewed headings. It separates complex Hessian equations, Gauduchon variational volume, equations with prescribed singularities, and historical notes into their own chapters. The collection has 25 chapters and 491 sections. Future edits should review subject coherence and reading length, rather than copy these counts or impose a word limit without mathematical judgment.

## Generated locators

Chapters and sections have locators `C` and `C.S`. Addressable subordinate blocks share one counter within their containing section: a subsection may be `3.2.1`, a theorem `3.2.2`, and its labelled equation `(3.2.3)`. Theorems, lemmas, definitions, propositions, examples, remarks, equations, figures, and retained headings all use this sequence. This makes each locator unique within a section; counters continue across sources and reset at the next Pome section. Absorbed introductory headings use `C.S` and do not consume a block number. Deduplicated source variants share the canonical entry's number.

`adapters/common.py` exports the original `number` and an explicit `caption` separately from source titles and semantic search terms. `scripts/structure.py` applies reviewed section boundaries. `scripts/numbering.py` assigns reader numbers after placement and deduplication. `scripts/collection.py` uses that map for headings, environment identifiers, equation labels, HTML references, references inside mathematics, navigation, search, and public inventories. Never extract a mathematical name from an internal LaTeX label.

Renumber only structured locators. Do not replace digits globally: mathematical dimensions, exponents, constants, logical list items such as (i)/(ii), and external references such as “Helms's Theorem 2.24, p. 36” retain their meaning. Source inventories under Sources retain original manuscript coordinates for provenance. A split or move may change display numbers; permanent tags and URLs must continue to resolve.

Equation labels sit beside their formulas in a two-column row. Long mathematics scrolls within its own column on narrow screens. Labelled align rows receive generated TeX tags inside their parent formula without duplicating their standalone HTML labels.

## Tags and verification

Show tags reveals tags for all addressable reading structures, including chapters and sections. A section reuses its absorbed introductory heading's tag when available; otherwise its tag derives from its stable route. Chapter tags also derive from stable routes. Renumbering does not change these identifiers. Subsections, mathematical statements, equations, and logical clauses keep their existing tags. A structure tag identifies content; it does not assert formalization.

Cite this page opens the citation panel immediately, including when clicked again with an existing `#cite` fragment. Direct citation links also expand the panel. Copy citation copies the displayed BibTeX entry; the permalink and title must identify the current reading page.

Footnotes use numbered links at their original positions in text or formulas. Note bodies follow the containing definition, theorem, proof, or prose block, with a return link to the reference. Number notes within each current Pome section and reuse those numbers on standalone entries. Logical list conditions keep their existing tags and anchors; only the complete statement has a formalization badge.

The mathematical body should read as Pome, independently of its source books. Rewrite source-specific introductions and preserve assumptions and conventions. Outside historical sections, use internal statements instead of external references whenever the required result is available. Keep necessary external inputs explicit; moving a citation must not disguise an unproved dependency.

An explicit source note is not required for every entry or reading section (owner instruction, 19 October 2026). Integrate the attribution of major results into the relevant subject sections of the project-wide history at the end of Pome, linking to the bibliography where useful. Avoid repeated “Sources” paragraphs in the mathematical text. Sources retains exact contributing revisions and the detailed original notes for consultation; this archive does not require a visible attribution block beside each result. An external theorem used as a proof input keeps its necessary hypotheses and a usable reference in the argument.

`reading/registry.json` records reviewed prose replacements with fingerprints of the original paragraphs. Check these against the raw exports before applying proof expansions; changed source prose requires another review. Reading edits change HTML and displayed captions, preserving source TeX, permanent tags, and proof guards. Set `retain_attribution` on a reviewed replacement when its original note must be archived even without a citation element. Exact SGPT locators resolve to current Pome entries; do not infer an internal reference merely from a similar theorem name, or replace a proof dependency by a link to the same statement. Sources pages retain the original attribution and commentary. Historical source exposition is retained under Sources. The shared historical chapter is rewritten by subject through `reading/history/registry.json`; its source fingerprints require review when upstream notes change. Former heading tags are aliases of the corresponding new section. Formal conjectures and problems retain their statements and tags in the problems chapter.

Before publication, run:

```sh
.venv/bin/python -m unittest discover -s tests
node --test tests/*.test.mjs
.venv/bin/python scripts/build.py --fetch
```

The build checks every structured visible source locator against the current collection numbers, along with all internal links and fragments. Regression tests cover subsection listings, section splits, numbering resets, merged variants, HTML/TeX references, equation rows, and stale-number rejection. Under the owner instruction of 23 October 2026, desktop/mobile browser checks are not required for every review, checkpoint, commit or publication. Run targeted browser checks for rendering, layout, navigation or interaction changes, or a concrete display defect; mathematics-only text, citation, metadata, record and fingerprint changes may reuse earlier relevant browser evidence with its exact scope and revision recorded. For shared rendering changes, select affected examples such as Kelvin transforms, Bedford–Taylor products, tag visibility, equation alignment and representative affected sources. Keep the applicable build, numbering and link checks.

## Audit corrections and historical synthesis (18 October 2026)

Embedded descendants of canonical statements follow the canonical parent after section promotion and before numbering. Parent lookup includes absorbed logical clauses, so an equation inside a merged alternative cannot retain its old source section. The regression covers a moved equation whose immediate parent is such a clause.

The historical chapter has ten sustained sections following Pome's analytic and geometric development. `scripts/history.py` checks coverage and source-prose hashes, preserves original notes under Sources, and maps old heading tags to the new reading sections. The original mathematical questions move intact to the problems chapter. Former topic and section routes remain redirects. Historical aggregation is prose editing, not a claim that its source statements are mathematical duplicates.

Capacity convergence on an entire open set retains its existing definition. A separate local definition tests every compact subset. The corrected monotone-net proposition asserts local convergence, and gives global convergence when the domain is the whole compact manifold. Guarded proof additions establish the net version, give the boundary-annulus counterexample, and derive weighted current convergence from the existing local bounded-product theorem.

## Repeated contextual displays

A reviewed `unlabelled_displays` record in `reading/registry.json` may remove an exact unlabelled `div.equation` when the surrounding prose links to the fully proved canonical theorem. The source, normalized display hash and replacement theorem are checked before publication. Equations with an ID or tag are rejected. The original display and surrounding edited attribution remain under Sources; mathematical source strings, permanent tags and proof guards are unchanged. This mechanism removes a repeated contextual display, rather than changing its formula.

## Composed statement introductions

The Analytic Methods source layout can provide an explicit `reader_context.prefix_chain` when an isolated statement needs both packet conventions and local subsection notation. Each prefix names a heading in the same selected packet and binds the exact native and rendered introduction with SHA-256. Native prefixes stop before the first formal statement or next heading. The chain must follow source order, end at its reviewed placement, and precede every listed target. Reversed, repeated, changed, or cross-packet prefixes fail the export. Copied introductions retain links but remove duplicate formula and tag ownership; mathematical statements and proofs remain unchanged. Existing single-prefix context bindings retain their earlier behavior, and neither form replaces the required final selection acceptance.
