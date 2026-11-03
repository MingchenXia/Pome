# Additive classified ledger — 2026-11-03 — logarithmic total mass and obstacle support

**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. Exact main reading file: **docs/sections/logarithmic-total-mass-and-bounded-obstacle-support/index.html** (blob 47387388cb62e2b99cf6f78370c914aa6f75909d).

| Stable finding ID | Severity / status | Anchors and hypotheses | Verified result / proposed action / dependents |
| --- | --- | --- | --- |
| POME-LOGMASS-ASYMPTOTIC-SLOPE-001 | Low / **verified conditional deduction**; no false original theorem | §16.34.1, source klimek-pluripotential-theory:7D93BBF9, permanent B5EE2E185F5F, physical lines 7–26; locally bounded PSH $u,v$, proper $v$, $0<\liminf u/v\le\limsup u/v<\infty$ | Exact mass sandwich $a^nM(v)\le M(u)\le b^nM(v)$, including infinite mass; in particular ratio $1$ yields equality. Optional strengthening after original proposition; dependents: logarithmic full mass §13.5.1 and §16.34.2. |
| POME-LOGMASS-OPEN-BALL-SUPPORT-001 | Low / **verified conditional deduction**; original theorem correctly uses closure | §16.34.2, source klimek-pluripotential-theory:63C4C42B, permanent 01D4425BEF42, physical lines 47–69; $E=B_R$ | $V_E^*=\max(0,\log(|z|/R))$, $\mu_E=2^{-n}\sigma_{\partial B_R}$: $\mu_E(E)=0$, $\mu_E(\overline E)=2^{-n}$. Do not canonicalize “on E” with “on closure E”. Dependent equilibrium-measure support and obstacle arguments in chapter 16. |

**Full proof and normalized radial calculation:** [dated English report](../reports/2026-11-03-asymptotic-slope-mass-and-open-ball-equilibrium-support.md).

**Boundaries and old-state preservation:** Complete bounded Bedford–Taylor comparison, decreasing continuity and the global cohomological computation in §13.5.1 were used as internal stated inputs, not independently recertified. No new **confirmed error**, **proof gap**, **external dependency**, **genuine duplication** or **verified repair** is asserted. Existing statuses are unchanged. All owner-excluded Demailly approximation/regularization, dedicated Bergman, weighted L², Ohsawa–Takegoshi, multiscale atlas, and positivity-loss proof completion remain **deferred-by-user**, not resolved. Current ToC is 25 chapters / 747 sections / zero complete mathematical-section certifications. Audit Markdown only.
