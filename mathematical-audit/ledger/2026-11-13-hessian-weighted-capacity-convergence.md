# 2026-11-13 classified ledger: §8.11 capacity-weighted weak limits

| ID | Severity | Status | Is printed theorem false? | Location | Action |
| --- | --- | --- | --- | --- | --- |
| POME-HESS-WEIGHT-CAPACITY-VAGUE-STABILITY-001 | low | **verified conditional deduction** | **No**: Lemma 8.11.11 remains correct | §8.11.11 source non-kahler-pluripotential-theory:59C81738, permanent 978D54F1054C, main blob 115d285f6b1f76d284463c396e7e87db2b9dbdc3 lines 259–279 | Optionally add signed-net/convergence-in-capacity variant; do not change production statement directly |

**Proved here:** local uniform outer-capacity domination for the measures of a weakly convergent net implies the same domination for its limit and compact variation bounds; for bounded Borel weights converging in capacity, local quasicontinuity only of the limiting weights suffices for nonlinear continuous reweighting. The original monotone, countably quasicontinuous hypotheses imply the capacity convergence required by the new lemma. A Dirac/point-indicator example under \(c_0\) shows the capacity domination hypothesis is substantive.

**Conditional dependencies:** Lemma 8.11.1 for local capacity finiteness and Definition 8.11.2 for the capacity; the existing \(D_p,Q_p\) construction/continuity in §§8.9, 8.11 is not transitively certified. Potential affected dependents: Theorems 8.11.12 and 8.11.14, but neither needs repair. Historical attribution retained. The Demailly approximation/regularization programme and its dedicated Bergman/\(L^2\)/OT/multiscale/positivity-loss proofs remain **deferred-by-user**; unchanged prior findings and ledgers remain intact.

Full proof and scope: [2026-11-13 report](../reports/2026-11-13-hessian-weighted-capacity-convergence.md).