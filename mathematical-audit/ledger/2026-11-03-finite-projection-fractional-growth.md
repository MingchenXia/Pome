# Classified audit ledger — 2026-11-03: weighted finite projections

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Audit branch:** `review/mathematical-audit`.

| Finding | Status | Severity | Precise target and result | Correction / downstream | Unresolved boundary |
| --- | --- | --- | --- | --- | --- |
| `POME-AFFINE-FINITE-GROWTH-EXPONENT-001` | **verified conditional deduction**; original theorem not refuted | low | §9.61.4 converse, `docs/sections/affine-algebraicity-and-linear-growth/index.html`, main blob `8f2301f7696a0b230950918ae20a7f9e57be768b`, lines **44–60**; source `demailly-complex-geometry:A33B88FE`, permanent `D15F5F84A74A`. For pure closed analytic `A subset C^p x C^r` with `|w|<=C(1+|z|)^s`, `s>=0`, the finite-fiber polynomial has `deg c_(ell,j)<=floor(s*j)` and `A` is algebraic. For `s=0`, `A=C^p x F` with finite `F`. Exact irreducible sharp model `w^b=z^a` gives `s=a/b` and coefficient degree `a` at `j=b`. | Optional remark after Thm 9.61.4, not a replacement or direct patch. Related §9.61.5–6 implications not independently certified. [Full conditional proof](../reports/2026-11-03-polynomial-growth-finite-projections-sharp-fractional-degree.md). | Requires earlier finite-open-map and analytic critical-set analysis of §9.61.2 (source `demailly-complex-geometry:F8362024`, tag `D8FA405BDFAC`, lines **21–26**) and bounded holomorphic removability cited at 9.61.4 lines **50–56**; not a complete dependency-chain certification. |

**Coverage increment:** newly checked fractional-growth generalization and sharp rational-branch models at the previously partly reviewed §9.61, crosschecking equation 9.61.3 (`demailly-complex-geometry:7EDA0F03`, permanent `D6D620F9E57D`, lines **12–16**). Entire §9.61 remains **not certified**; no changes to the original **25 chapters / 747 numbered sections / zero fully mathematically certified sections** inventory.

**Prior statuses:** all existing confirmed errors, proof gaps, external dependencies, genuine duplicates, verified repairs and older conditional deductions remain as previously classified. The owner-deferred Demailly approximation/regularization and its Bergman, weighted-L2, OT, multiscale and positivity-loss proof programme remain **deferred-by-user**, not reopened and not certified.

**Write scope:** English audit Markdown only; neither source repository nor production main, reader pages, permanent tags, registry, tests, CI, formalization or website publication is changed.
