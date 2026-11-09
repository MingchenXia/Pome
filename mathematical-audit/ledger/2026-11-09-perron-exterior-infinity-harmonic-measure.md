# Classified finding — exterior Perron measure at infinity (2026-11-09)

- **Stable ID:** `POME-PERRON-EXTERIOR-INFINITY-ATOMIC-MASS-001`.
- **Severity / status:** **low / verified conditional deduction**, **original Theorems 4.4.12 and 4.4.17 correct**. Not a false theorem, proof gap, already-applied repair or resolved prior dependency.
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Main proof location:** `docs/sections/perron-theory-and-fine-boundary-limits/index.html`, blob `4bc2fb9317e2b6f6bb5b2d90208c677da8275eba`. Full source labels, permanent tags and physical line anchors appear in [the detailed report](../reports/2026-11-09-perron-exterior-harmonic-measure-at-infinity.md).
- **Specific hypotheses:** exterior of a closed Euclidean radius-\(R>0\) ball in \(\mathbb R^d\), \(d\ge2\), **infinity excluded from the domain but included in the compactified boundary**; arbitrary continuous real sphere datum \(g\), arbitrary real value \(b\) at infinity.
- **Exact conclusion:** finite-sphere harmonic measure density \(Q_R=(r^2-R^2)/(\sigma_{d-1}R|x-\zeta|^d)\), its total mass \(1\) for \(d=2\) and \((R/r)^{d-2}\) for \(d\ge3\); boundary infinity atom \(0\) or \(1-(R/r)^{d-2}\), respectively. In two dimensions the far-end limit is the sphere average of \(g\), independent of \(b\); in higher dimensions it equals \(b\).
- **Justification:** exact Kelvin factors and normalized ball Poisson kernel; explicit bounded harmonic higher-dimensional solution; in dimension two the *admissible* Perron upper/lower competitors \(A_g\pm\varepsilon\log(r/R)\) squeeze the solution, without a limit/measure interchange.
- **Dependencies still conditional:** internal ball Poisson and compactified Perron comparison/representation; no general compactified boundary theorem certified.
- **Proposed correction:** optional independent example after 4.4.17; **no mathematical statement needs changing**. Keep attribution, distinct kernels, conventions and permanent tags.
- **Affected dependents:** §4.4 compactified boundary use and §4.5 Martin/Perron distinction; no specific erroneous dependent asserted.
- **Distinct prior entry:** `POME-MART-EXTERIOR-BALL-INFINITY-001` concerns the normalized **Martin** kernels/minimality, not probability harmonic measures or the two-dimensional Perron upper/lower sandwich. Do not conflate.
- **Coverage:** newly reviewed selected steps within previously partly sampled §4.4, **zero first sections, zero full section certifications; actual ToC 25/747/0**.
- **Deferred scope unchanged:** user-excluded Demailly approximation/regularization and Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss programme stays **deferred-by-user** (neither solved nor reopened). No main/source/build/CI/publication changes.
