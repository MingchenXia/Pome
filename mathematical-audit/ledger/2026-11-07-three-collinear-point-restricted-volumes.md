# Classified finding — 2026-11-07

| ID | Severity | Status | Main SHA | Actual coverage |
| --- | --- | --- | --- | --- |
| POME-RESVOL-THREE-COLLINEAR-WALL-001 | low | verified conditional deduction | b6933b772f41b45918f7e25ed1afbbb1fd892272 | §20.8.3 statement (HTML physical 64–66, transcendental-positive-cones:42C59BDB / tag 8DC7DAC31FB7) and §20.8.16 statement (physical 350–352, :682A1645 / tag 7ED04B77FCC6); independent smooth surface model, **not** general-proof certification |

Reading HTML: docs/sections/divisorial-restricted-volumes/index.html, blob 8eb1127568e77d6d045098361c366ceeb846b909.

**Mathematical result:** on Bl_(p1,p2,p3)(P²), where the three points lie on one line, D=dH-mΣEi (integers d>m>0) has volume (3/2)(d-m)² for m<d<3m and d²-3m² for d≥3m. Restricted ranks onto Ei are km-a_k+1, a_k=max{0,ceil(k(3m-d)/2)}, while those onto the (-2)-curve C equal max{0,k(d-3m)+1}. The independent coefficient-counting proof and the exact integral for directional derivative along E1 are in [the complete report](../reports/2026-11-07-three-collinear-point-restricted-volume-wall.md). The non-nef chamber has vol(D)>D², explaining why replacing a positive product with naive D·Ei gives a wrong restricted-volume value. No printed proposition is refuted.

**Affected dependents:** geometric interpretations of Theorem 20.8.3 and Proposition 20.8.16. The analytic proof of each, any regularization-dependent component of §20.8.1 and §20.8.16, and the general identification of analytic and algebraic restricted volume are NOT certified. **Excluded subject status remains deferred-by-user** (not resolved). Proposed change: report/example only; no production patch required.

**Classification ledger effect:** new verified conditional deduction only. Confirmed errors, proof gaps, genuine duplications, candidate issues, external dependencies, prior verified repairs and deferred entries are unmodified. No first-visit or complete-section recount.
