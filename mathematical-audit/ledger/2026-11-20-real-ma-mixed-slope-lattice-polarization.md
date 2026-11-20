# 2026-11-20 — Chapter 21 mixed slope-mass and lattice-count ledger

| ID | Severity | Status | Mathematical object | Impact |
| --- | --- | --- | --- | --- |
| `POME-REALMA-MIXED-SLOPE-COUNT-POLARIZATION-001` | low | **verified conditional deduction** | §§21.4.2, 21.5.1, 21.5.4 (21.5.5), 21.7.3; compact slope bodies | New exact formula for **mixed real Monge–Ampère total mass** as a finite alternating sum of Minkowski-body volumes and as the leading translated-lattice counting limit; printed statements remain valid |

**Hypotheses:** finite convex `F_1,...,F_n`, `n>=1`, compact closed slope bodies `K_j=closure(dom F_j^*)` (including lower-dimensional bodies). Do **not** assert formula by subtracting infinite total masses when any `K_j` is unbounded.

**Proof:** [complete anchored report](../reports/2026-11-20-real-ma-mixed-slope-lattice-polarization.md). Exact source/persistent tags and lines are specified there; main `b6933b772f41b45918f7e25ed1afbbb1fd892272`. The cancellation of the factors `1/n!` in the polarization identity and `n!` in the diagonal mass is explicit. The Minkowski sum of slope bodies is precisely Proposition 21.4.2, not an unproved exchange of arbitrary closures.

**Proposed action:** optional cross-reference as a separate source PR; retain historical tags and source attribution. No repair required. **Potential dependents:** §21.9.5 and toric/convex mixed-volume interpretation (conditional; not audited to completion).

**Unresolved:** independent verification of the complete prerequisites in §§21.2–21.4/2.2/2.8/5.3, and real-to-complex toric mass comparisons. These are not reclassified as errors. **Deferred-by-user:** Demailly approximation/regularization and its specified Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss programme; previous notes remain deferred rather than closed.

**Coverage this run:** three entire integrated §§21.5–21.7; §21.4.2 selected prerequisite only; +0 independently certified upstream chains. The existing 2026-11-17 Wq endpoint and 2026-11-18 finite-k discrepancy findings remain preserved and are not relabeled as new. No tests/build/CI/publication or body/registry/tag edits.
