# Pome

<img src="site/assets/pome-mascot.png" alt="Pome pomegranate mascot" width="120" align="right">

A shared mathematical reference combining definitions, theorems, and proofs from contributing texts. Browse by **shared chapter or permanent tag**, search across all content, and see each statement's formalization status.

**[Read Pome](https://mingchenxia.github.io/Pome/)** · [Source contributions](https://mingchenxia.github.io/Pome/sources/)

## Content and organization

The collection integrates the following sources at the revisions registered in `books.json`:

- [Foundations of pluripotential theory](https://github.com/MingchenXia/foundations-of-pluripotential-theory).
- [Singularities in global pluripotential theory (SGPT)](https://github.com/MingchenXia/SGPT).
- **Singularities in Hermitian pluripotential theory**, from the author's private `non-kahler-pluripotential-theory` repository. Only the authorized reading edition is published; the source repository remains private.

- **Classical potential theory: supplements after Helms**, from `Gerby-Literature/main`, including the merged `codex/helms-whole-book` work. The supplement follows the recorded complete-book review and includes harmonic boundary limits, Green functions, polar sets, sweeping, Perron theory, the Wiener criterion, energy and Martin boundaries, with reconstructed proofs and attribution. The retained scan and research records stay private.

- **Local and global pluripotential theory: supplements after Klimek**, from `Gerby-Literature/main`. The reviewed supplement adds explicit proofs and supporting mathematics across the existing subjects, with 216 source tags and three reviewed canonical merges. The book scans and private research records stay private.

- **Complex analysis, cohomology and differential geometry**, the reviewed Demailly supplement from `Gerby-Literature/main`. Its selected proofs join the existing mathematical subjects; retained books and private review files are excluded.

- **Transcendental positive cones**, the reviewed supplement after Tosatti with BDPP foundations, volume variation, divisorial restricted volumes and balanced-cone duality. The arguments and prerequisites join the existing subjects, with major attribution in the project history.

- **Isolated plurisubharmonic singularities**, the reviewed supplement after Li–Xia on isolated poles with zero Lelong number and positive residual Monge–Ampère mass. Explicit polynomial iterates, separated maximum products and finite logarithmic thresholds join the existing subjects; major attribution belongs in the project history.

- **Relative canonical bundles and positive foliations**, the reviewed Cao–Păun supplement at its separately pinned source revision. Its relative canonical, singular metric and foliation results join the existing subjects. See [the selected mathematics and source controls](documentation/relative-canonical-positive-foliations.md).

- **Singular metrics, generation and canonical systems**, the selected supplement after Demailly's *Analytic Methods in Algebraic Geometry*. The current candidate selects eighty reviewed proof packets across singular estimates, generation and jets, cohomology, curvature limits, canonical systems and geometric counterexamples. The earlier sixty-nine-packet selection has a successful ordinary full build and targeted desktop/mobile context checks; the eleven-packet extension requires its own final source pin and build. Complete-book and recursive dependency closure remain separate research tasks. Existing compact Nadel and diagonal monomial statements are reused canonically. See [scope, validation and source controls](documentation/analytic-methods-integration.md).

Only each manuscript's active input graph is included. Excluded drafts and private research material are not exported.

The collection has **25 shared chapters**, ordered by mathematical subject across the sources. Chapter 1 contains only conventions; manuscript prefaces, acknowledgments, introductions, and part overviews are omitted. Reader numbering follows the current Pome chapters and sections; source metadata and exact revisions are collected under Sources rather than repeated beside every statement. The chapter structure is curated independently of the original tables of contents. The historical chapter follows the development across the collection in connected subject sections; original source notes remain under Sources, and formally stated questions belong to the problems chapter. Existing book and topic URLs continue to resolve.

Reviewed duplicates have one canonical entry and one search result. Alternative source wording, proofs, and formalization badges remain accessible within that entry. Numbered clauses stay inside their parent statements, retaining their own tags and anchors; formalization status belongs to the complete parent statement. `collection.json` records each reviewed statement fingerprint: a changed statement requires a new review before it can be merged again. Results with different hypotheses remain separate.

All interface text and project documentation are in English. The source texts and formal proofs remain in their original repositories and retain their licenses.

The reading interface follows the Stacks Project: compact navigation, a breadcrumb trail, and a reading column with page tools at the side. It adapts to computers, tablets, and phones; long equations and tables scroll inside the reading column.

- Chapter pages list **sections and subsections**. Section pages show the full text, definitions, theorems, equations, and proofs directly, with individual entry permalinks. Nested statements and equations are displayed once rather than repeated as separate list items.
- **Previous** and **Next** links appear above and below each page, following one complete order through chapters, sections, and statements. Breadcrumbs return directly to the containing section or chapter.
- Statement headings retain manuscript names and use generated Pome numbers, such as **Definition 3.2.1**. Internal LaTeX labels are searchable identifiers and are never shown as reader headings. Permanent tags are hidden initially and can be revealed with **Show tags**.
- Search accepts mathematical subjects, phrases, statement numbers, or tags. An exact unambiguous tag opens its entry directly. Each page also has a permalink and a copyable BibTeX citation.

The color palette follows the [Stacks Project](https://stacks.math.columbia.edu/): white pages, black text, blue links (`#1d5cb4`), and warm gray navigation (`#d9d8d1` and `#edece6`). Theme colors are defined in `site/assets/book.css` and shared across the collection.

## Comments

Every reading page has its own public comment thread, backed by [GitHub Discussions](https://github.com/MingchenXia/Pome/discussions). The inline [giscus](https://giscus.app/) panel lets readers sign in with GitHub, comment, reply, and react. Readers can also open or start the same page's discussion directly on GitHub. The maintainer moderates the threads there. No credentials are included in the site.

GitHub Discussions is enabled. Inline comments require the [giscus GitHub App](https://github.com/apps/giscus) to be installed for **only `MingchenXia/Pome`**. `comments.json` holds the public repository and discussion-category IDs; `giscus.json` limits the allowed site origins. Threads use stable page identifiers, so changing a heading or manuscript revision does not create a new thread. A GitHub link remains available when the embedded service cannot load. See [comment setup and moderation](documentation/comments.md).

## Formalization badges

Every tagged statement displays a badge:

| Badge | Meaning |
| --- | --- |
| Not recorded | No formalization mapping has been supplied. |
| Pending verification | A proof repository is linked, but the current revision has not been verified. |
| ✓ 0 sorry | The mapped declaration at the linked exact revision passed the recorded proof and axiom checks. |

No formalization repositories have been supplied yet, so the collection currently shows **Not recorded**. A repository link alone cannot produce a verified badge. New proof commits revert to pending until verified. See [the evidence requirements](documentation/formalizations.md).

## Adding content

Supply a source repository link and, when available, its formalization repository. Integration records the active LaTeX entry point, stable source labels, shared chapters, and the correspondence with formal declarations.

- `books.json` registers contributing source repositories and tracked revisions.
- `collection.json` defines the shared chapters, subject assignments, and reviewed canonical entries.
- `formalizations.json` records declaration mappings and verification evidence.
- `proofs/registry.json` and its HTML fragments add proofs and necessary qualifications to the shared reading edition. Statement and original-proof fingerprints require review when upstream mathematics changes; see [proof expansion review](documentation/proof-expansions.md).
- `adapters/` exports each source through the pinned official Gerby renderer.
- [Integration layout and numbering](documentation/integration-layout.md) defines section promotion, redundant-heading removal, current-section numbering, equation layout, and tag visibility.
- [Deployment and updates](documentation/deployment.md) documents the export and publishing contracts.

## Updates without CI

GitHub Actions CI is disabled at the author's request. Builds run locally, and `scripts/publish.py` commits the checked static output to `docs/` on `main`. GitHub Pages serves that folder at `/Pome/`. The repository uses a single branch; the former `gh-pages` history is merged into `main`. Authored project documentation lives in `documentation/`.

Updates are **on request only**. There is no scheduled monitoring or publication. When the author asks to update Pome, `scripts/update.py` checks all registered source and formalization revisions, rebuilds changed content, checks internal links, and verifies the published revision. Publication commits that change only generated `docs/` files do not trigger another rebuild on the next requested check. The former hourly automation has been removed.

## Local build and publication

Requires Python 3.11+, Git, Node.js, npm, XeLaTeX with the `standalone`, TikZ and `doublestroke` (`dsfont.sty`) packages, and Poppler (`pdftocairo`); publication also uses the authenticated GitHub CLI (`gh`). The private Hermitian and Gerby-Literature sources require authenticated read access; credentials stay outside the project.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
npm ci --prefix vendor --ignore-scripts --no-audit --no-fund
.venv/bin/python -m unittest discover -s tests
node --test tests/*.test.mjs
.venv/bin/python scripts/build.py --fetch
python3 -m http.server 8000 --directory _site
```

Open `http://localhost:8000`. With authorized push access to `MingchenXia/Pome`, publish a completed build or check for upstream updates:

```sh
.venv/bin/python scripts/publish.py
.venv/bin/python scripts/update.py
```

The on-request updater requires a clean `main` checkout and uses a fast-forward pull. It never overwrites uncommitted edits. To preview an existing source checkout, set its `checkout_env` from `books.json` to the absolute path before building. The five Gerby-Literature contributions tracking `main` can point to the same clean checkout. The analytic-methods selection uses `ANALYTIC_METHODS_SOURCE_DIR` and its separately registered revision. Requested update checks ignore preview overrides and fetch the tracked sources afresh.

## Pome on GitHub Pages

[Gerby](https://gerby-project.github.io/) provides the LaTeX-to-tag renderer used here. This static export includes chapters and sections, individual entries, full-text search, citations, formalization badges, and self-hosted MathJax. GitHub Pages serves the reading edition; comments persist in GitHub Discussions through giscus. The Flask/database backend is not required.
