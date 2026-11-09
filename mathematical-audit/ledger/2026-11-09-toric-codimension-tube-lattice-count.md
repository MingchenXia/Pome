# 2026-11-09 — Codimension-sensitive convex lattice tubes

- **ID:** `POME-TORIC-LOWERDIM-TUBE-COUNT-001`
- **Status:** **verified conditional deduction** (elementary proof complete under the integrated lattice normalization). **Severity:** low. **Printed theorem status:** Theorem 21.7.3 and Corollary 21.7.4 correct; no printed false theorem or missing proof claimed.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Primary:** `docs/sections/convex-analysis-and-toric-potentials--lattice-points-and-volume/index.html` blob `5d209b7f4d2156c19bc3fb300303405df6321230`, Theorem 21.7.3, source `foundations-of-pluripotential-theory:364BCD30`, permanent `831AEEB7084F`, physical lines 57–90; Corollary 21.7.4, source `foundations-of-pluripotential-theory:D6B87DCB`, permanent `CF4226A5034F`, lines 93–105.
- **Conditional/contextual dependent:** `docs/sections/flags-convex-bodies-and-section-growth/index.html`, blob `83557f0e15275253661fe679c75407e6636d497c`, Theorem 19.9.9 source `non-kahler-pluripotential-theory:4EE23942`, tag `CC2BF9294FA3`, lines 173–233, **not certified**.
- **Hypotheses:** `K⊂R^n` nonempty compact convex, affine dimension `0<=d<n`; shifts arbitrary; `r_k>=0`, `r_k/k→0`.
- **Conclusion:** `#((kK)^{r_k}∩(Z^n+a_k)) <= C k^d (r_k+1)^{n-d}`, with corresponding continuous-weight bound, uniformly over shifts. Sharp in both powers for coordinate boxes; irrational normal affine offset makes unthickened counts vanish identically.
- **Proof / precise justification:** [source-anchored report](../reports/2026-11-09-toric-codimension-tube-lattice-count.md), product-volume bound of `K^δ` and exact half-open cell counting; no theorem beyond the printed lattice conventions is required.
- **Proposed correction:** *Optional independent remark* after Theorem 21.7.3; do not modify body/source/registry/tags. Distinguish ambient normalized zero limit from intrinsic semigroup asymptotics; retain earlier full-dimensional, moving-body and Haar-shift reports as separate valid statements.
- **Affected dependents:** §21.7.4 may use a quantitative rate when `K` is lower-dimensional; §19.9.9 needs its separately defined subgroup `Λ` and degree period. No existing dependent is proven wrong.
- **Coverage:** selected math only in §21.7; §19.9.9 hypothesis/context crosscheck; both previously partly sampled; 0 new first-visited numbered sections, 0 complete-section certificates, current ToC 25/747/0.
- **Other classifications:** Existing confirmed errors/proof gaps/external dependencies remain unresolved if unresolved; all explicitly owner-excluded approximation/regularization/Bergman/L²/OT/multiscale/positivity-loss research remains **deferred-by-user**, not resolved.
