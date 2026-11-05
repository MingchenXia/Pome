# 2026-11-06 classified finding — relative energy endpoint constants

- **POME-ENER-PROJECTIVE-BOTH-CONSTANTS-SHARP-001** — **low / verified conditional deduction**, not a false statement or proof-gap repair.
- **Production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Integrated blob:** 16fdcc4c6a6f0cc75e69ba267bd7da2b2d7922a1.
- **Exact locus:** docs/sections/relative-energy-and-perron-segments--relative-monge-ampere-energy/index.html:30–37,180–190,194–216. Definition 17.3.2 (source foundations-of-pluripotential-theory:582D55DC; permanent 240EF1DE5889); Eq. 17.3.3 (8C7506A6; F19AAFA93177); Theorem 17.3.14 (CF717230; 69E7D1FEF207); Eq. 17.3.15 (14754AD3; AE35DCCFE783).
- **Mathematical assertion:** for every \(n\ge1\), both universal coefficients \(1/(n+1)\) and \(1\) in (17.3.15) are optimal even in the smooth strictly positive Fubini–Study class. The automorphism potentials \(u_t=\log((t|Z_0|^2+\sum_{i>0}|Z_i|^2)/\sum_i|Z_i|^2)\) give the lower ratio limit; negative constants attain the upper equality.
- **Complete justification:** [source-anchored proof](../reports/2026-11-06-projective-relative-energy-sharp-constants.md), including exact top-mass \(J_n(t)=\log(1/t)-H_n+o(1)\), uniformly bounded \(J_j(t)\) for \(j<n\), and a smooth normalization check. Not a numerical or formal-computer proof.
- **Correction:** none required. Optional short sharpness remark at Equation 17.3.15; proposed only, no production edit.
- **Affected dependents:** all uses of the universal energy-to-\(\int(\phi-u)\mu_u\) comparison; none invalidated. Strengthening a coefficient without new hypotheses is impossible.
- **Coverage:** additional explicit model/optimality at previously sampled §17.3, **not** proof verification of all energy results or upstream mixed non-pluripolar identities; see [coverage increment](../coverage/2026-11-06-ch17-energy-inequality-endpoints.md).
- **Unresolved/deferred:** prior findings and any independent upstream proof gaps retain their prior status. Demailly approximation/regularization and dedicated Bergman, weighted-L², Ohsawa–Takegoshi, multiscale-atlas, positivity-loss proof-completion remain **deferred-by-user**, not certified.
