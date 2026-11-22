# POME-IDEAL-CURVE-PROJECTION-ONLY-CONTINUOUS-AT-ZERO-001 — exact continuity locus of ideal projection on a curve

- **Date:** 2026-11-22. **Status:** low / **verified conditional deduction**. Not a false theorem or a complete transitive proof-chain certification.
- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated anchor:** `docs/sections/multiplier-ideal-envelopes-and-goodness--geometry-of-ideal-classes/index.html`, blob `64b1c0de9266a28727de07ca3502a13ab974f001`, Theorem 18.6.4 lines 43–86, source `E7B73391`, permanent `A55ADED04CFD`; discontinuity discussion lines 91–104; projection Theorem 18.4.2, source `3A211D73`, permanent `7F20FD198864`.
- **Hypotheses:** connected compact Riemann surface (Y); smooth strictly positive (	heta), (int_Y	heta=1); smooth positive probability (mathrm dV); normalized (	heta)-psh compactum (mathcal K_	heta) with (L^1(mathrm dV)) topology.
- **Claim:** (Pi(u)=P_	heta[u]_{mathcal I}) is continuous on (mathcal K_	heta) **exactly at (u=0)**.
- **Reason:** for any normalized (v), (vlePi(v)le0), proving (L^1)-continuity at zero. At every (u), finite rational atomic Green models (a_j	o u) satisfy (Pi(a_j)=a_j), while smooth Poisson solutions (s_j	o u) (from weak smooth-probability approximation of (	heta+mathrm{dd}^{mathrm c}u)) satisfy (Pi(s_j)=0). Continuity forces (u=0). Connectedness and curvature mass one are used essentially.
- **Upstream:** current §18.6.4's atomic ideal-model density, current §18.4.2 projection, normalized psh (L^1)-compactness, the ordinary Green/Poisson operator on a curve, and harmonic uniqueness. Complete independent proofs of the entire transitive chain are **not** claimed.
- **Correction:** none required. **Proposed optional addition:** conditional corollary to §18.6.4; do not alter source or permanent tags. **Dependents:** §18.6 topology and any future (L^1)-continuity claim for (Pi).
- **Full proof:** [dated report](../reports/2026-11-22-curve-ideal-projection-continuity-and-background-mass.md).
- **Deferred by user:** Demailly regularization, Bergman, L², Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion; no certification implied.
