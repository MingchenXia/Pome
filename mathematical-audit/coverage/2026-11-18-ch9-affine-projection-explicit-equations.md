# 2026-11-18 — Chapter 9 §9.61 full direct review and explicit finite equations

**Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; **review branch:** `review/mathematical-audit`.

| Actual numbered section | Main integrated file and blob | Precise material inspected | New status |
| --- | --- | --- | --- |
| 9.61 Affine algebraicity and linear growth | `docs/sections/affine-algebraicity-and-linear-growth/index.html`, blob `8f2301f7696a0b230950918ae20a7f9e57be768b` | §9.61.1 conventions lines 5–8; Lemma 9.61.2 lines 10–29; Thm 9.61.4 lines 31–63; Cor. 9.61.5 lines 65–79; Prop. 9.61.6 lines 81–93; **all printed proof paragraphs directly inspected** | **whole-section direct mathematical review**, upstream hypotheses not transitively certified |
| 9.58 | cited `docs/sections/finite-type-algebraic-models-and-analytic-structure-sheaves--finite-type-models-and-nilpotent-structure/index.html` | Noetherian/Nullstellensatz used conditionally; no repeat of earlier §9.58 work | contextual only |

**New finding:** [POME-AFFINE-PROJECTION-EXPLICIT-EQUATION-COUNT-001](../ledger/2026-11-18-affine-projection-explicit-equation-count.md), **low / verified conditional deduction**. A proper degree-d projection of a linearly bounded pure analytic set in C^p x C^r is cut out set-theoretically by **N=d(r-1)+1 predetermined fiber-polynomial equations**, each total degree ≤d; any N distinct Vandermonde evaluation parameters suffice. [Full mathematical proof](../reports/2026-11-18-affine-projection-explicit-equation-count.md). No false printed theorem.

**Coverage update:** **+0** first-time numbered section, **+1** whole-section *direct* proof inspection (§9.61), **+0** fully verified transitive dependency chain. Actual chapter-9 ToC §9.58–9.70 read; global 25 chapters/747 sections is the retained previous inventory, not a claim of fully auditing it. Older 2026-11-03 fractional-growth audit retained as separate. No project tests/builds/CI, site or production edits. Excluded Demailly approximation, Bergman/L2/OT/multiscale/positivity-loss work remains **deferred-by-user**.
