# Classified ledger — 2026-11-09 — oscillatory scalar homogenization

| Stable ID | Classification | Severity | Result | Source anchors |
| --- | --- | --- | --- | --- |
| `POME-SCALAR-WEAKSTAR-HOMOGENIZATION-001` | **verified conditional deduction**; original theorem **correct** | **low** | On the flat unit elliptic curve, \(F_j=a\cos(2\pi jx)\rightharpoonup^*0\) with \(B_0(F_j)=-\log J(a)<0=B_0(0)\), although normalized solutions converge uniformly \(O(j^{-2})\) and MA/supporting probabilities converge weakly (not in TV). | Theorem 11.33.5: `non-kahler-pluripotential-theory:D502EBBF` / `5E3583383688`; Eq. 11.37.2: `non-kahler-pluripotential-theory:65FF799F` / `803909FECEC0`. |

**Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Integrated §§11.33/11.37 blobs `fff86de757578ed2be369ba752123f62f3d31044` (physical lines 88–121) and `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f` (lines 50–61). Complete proof and all hypotheses: [the report](../reports/2026-11-09-scalar-weakstar-oscillation-torus.md).

**Status distinction:** the printed **strong \(L^1\)** hypothesis is indispensable for this type of continuity claim; no printed theorem is refuted. Proposed *optional* remark only. Affected potential extensions: scalar/adjoint stability §§11.34–11.36; their original statements and earlier audit statuses are preserved, not recertified.

**Excluded scope:** Demailly approximation/regularization, Bergman, weighted-\(L^2\), OT, multiscale atlas and positivity-loss proof programme remains **deferred-by-user**. No source/main/tag/registry edit or build/CI/publication.
