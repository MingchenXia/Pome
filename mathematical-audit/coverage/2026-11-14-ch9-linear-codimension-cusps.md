# 2026-11-14 precise additive coverage — Chapter 9, §9.31

**Baseline:** current production main `b6933b772f41b45918f7e25ed1afbbb1fd892272`, 25 chapters / 747 numbered sections in actual `docs/index.html`. The audit matrix has **already partially visited §9.31**; this increment credits **0 newly first-visited numbered sections** and **0 complete section certifications**.

| Item | Exact physical anchor in integrated main | Work performed | Certification limit |
| --- | --- | --- | --- |
| Theorem 9.31.1 | `docs/sections/separation-strict-exhaustions-and-coverings--complete-kahler-metrics-on-regular-open-sets/index.html`, blob `3faaef942f4822127e09c63a463d654d346696c2`, lines 7–23, `demailly-complex-geometry:232F4B65 / 214C6B3DF885` | Checked regular-open hypothesis against all linear-subspace complements | Analytic division from §6.28 remains **unreviewed** and its excluded dedicated proof programme not entered |
| Example 9.31.2 | Same file/blob, lines 25–42, `demailly-complex-geometry:12510407 / D80B90CDCDA1` | Independently derived smooth complete Kähler metric for arbitrary deleted linear subspace, sharp `|log epsilon|^{-k}` collar mass, codimension-one vs codimension-two+ pseudoconvexity threshold | Full theorem chain and global `L2` construction **not certified** |
| Scope comparison | Earlier puncture finite-cusp ID `POME-PUNCTURE-KAHLER-FINITE-CUSP-001` | Preserved existing point case; newly handles positive-dimensional deleted loci and codimension-dependent mass exponent | Neither prior finding nor current statement is repeated as complete source verification |

**New ID:** `POME-LINEAR-CODIM-COMPLETE-KAHLER-CUSP-001`, low / **verified conditional deduction**. [Proof](../reports/2026-11-14-linear-codimension-complete-kahler-cusps.md) · [ledger](../ledger/2026-11-14-linear-complement-kahler-codimension.md).

**Deferred-by-user:** Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale atlas, positivity-loss programme. No tests, build, CI, publication, or production writes.
