# POME-PSH-MONOTONE-NET-WEIGHTED-LP-POLAR-001

- **Date:** 2026-11-17.
- **Status / severity:** **verified conditional deduction**, **low**. Original Proposition 17.4.1 remains correct; no source theorem refuted.
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`; `docs/sections/relative-energy-and-perron-segments--continuity-and-compactness/index.html`, blob `6fd38d5ff9d0037e9d0d347814a95ad97331715f`; source `foundations-of-pluripotential-theory:24DDA159`; permanent `049F75F5547D`; lines 10–15, 71–72.
- **Finding:** the printed countable Choquet selection, combined with zero mass on pluripolar exceptional sets and an integrable initial dominating difference, yields **strong fixed-measure L^p convergence of the original increasing directed psh net**, without any cofinal sequence. Bounded subharmonic `max(k^-1 log|z|,-1)` shows the non-pluripolar condition is essential: area `L^p` norm is asymptotic to `[pi Gamma(p+1)/2^p]^(1/p)/k`, but every `delta_0` norm is exactly 1.
- **Hypotheses / boundary:** fixed finite positive measure `nu` charging no pluripolar sets, `1<=p<infinity`, `(U-u_i0) in L^p(nu)`; not a changing-measure or energy claim. The disc example is local, not a global counterexample.
- **Proposed correction:** optional conditional corollary, **not** a change to the original theorem; do not infer `L^p` convergence for polar-atomic measures.
- **Dependents:** optional fixed-reference integrability estimates in §§17.5–17.9, subject to separate hypotheses; existing analytical inputs not certified.
- **Report:** [source-anchored proof](../reports/2026-11-17-monotone-psh-nets-weighted-lp-polar-tests.md).
- **Coverage:** [exact run delta](../coverage/2026-11-17-ch17-monotone-net-weighted-lp.md); previously partly inspected §17.4, **+0 first sections / +0 whole certificates**.
- **Excluded:** all user-deferred approximation and its Bergman/L2/OT/multiscale/positivity-loss programme remain **deferred-by-user**.
