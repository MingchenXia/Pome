# 2026-11-20 — direct Chapter 21 §§21.5–21.7 coverage

Baseline `main` SHA: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Actual published chapter numbering checked against `docs/chapters/toric-convex/index.html` (Chapter 21).

| Scope | Integrated source path | Blob SHA | Direct mathematical physical lines | Coverage |
| --- | --- | --- | --- | --- |
| §21.5 Real Monge–Ampère | `docs/sections/convex-analysis-and-toric-potentials--the-real-monge-ampere-measure/index.html` | `7089aa41ae2422b1bd6b5094e46668cbc8ed37be` | 6–160 | **full direct**: 21.5.1–21.5.4, equation 21.5.5, example and proofs |
| §21.6 Compact envelopes/full mass | `docs/sections/convex-analysis-and-toric-potentials--compact-convex-envelopes-and-full-mass-limits/index.html` | `b3b4e34fff767a717df812a381f905589b257fb3` | 6–49 | **full direct**: both lemmas and proofs |
| §21.7 Lattice points and volume | `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html` | `5d209b7f4d2156c19bc3fb300303405df6321230` | 6–108 | **full direct**: definition, proposition, theorem, corollary and proofs |
| §21.4.2 prerequisite | `docs/sections/convex-analysis-and-toric-potentials--slope-bodies-and-bounded-growth/index.html` | `56a9a1c19e7234e2aa258d5ad1b66a5679ace190` | 10–16, 19–54 (selected) | **selected dependency only**; not full §21.4 |

**Result:** `POME-REALMA-MIXED-SLOPE-COUNT-POLARIZATION-001` / low / verified conditional deduction. [Proof report](../reports/2026-11-20-real-ma-mixed-slope-lattice-polarization.md) · [ledger](../ledger/2026-11-20-real-ma-mixed-slope-lattice-polarization.md). Printed §21.5–§21.7 did not yield a newly confirmed error; no source repair was carried out.

**Count:** 3 full direct section readings, 1 selected prerequisite, 0 full transitive upstream-chain certifications; no claim of historically first-ever visit. Earlier §21.5 and §21.7 partial audit reports stand unchanged. Other 744 sections are not certified by this run. Excluded programme remains deferred-by-user. No build/test/CI/publication.
