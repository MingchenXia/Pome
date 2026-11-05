# Additive classification — 2026-11-06 — magnetic Riesz convex order

Main `b6933b772f41b45918f7e25ed1afbbb1fd892272`, integrated blob `ee89de7d23cc96a8546c736ac7d068546b126f3a`.
Exact proofs and anchors: [magnetic midpoint report](../reports/2026-11-06-magnetic-midpoint-riesz-convex-order.md).
Retain all earlier errors, gaps, candidates, external dependencies, duplications,
repairs, and owner-deferred categories unchanged.

| Stable finding ID | Severity | Status | Location and assessment | Proposed disposition |
| --- | --- | --- | --- | --- |
| `POME-MAGNETIC-MIDPOINT-RIESZ-CONVEX-ORDER-001` | low | verified conditional deduction | §2.24.4–7, permanent `6919A4A3FD8F`/`72E6618A3A3C`/`0F14CB3D46F3`/`DD3B970F19C7`, physical lines 31–54, 68–70. Coordinatewise midpoint convexity yields (r_{\mathbf b}(E)\le(E_+)^{n+1}/((4\pi)^n(n+1)!)), sharp at `b=0`; one pair has exact quadratic nearest-integer discrepancy. The printed lemma is **correct**. | Optional stronger Riesz coefficient; retain the printed Landau normalization. Direct dependent §2.24.8 (lines 89–109) is not certified. |
| `POME-MAGNETIC-COUNTING-FREE-BOUND-FAIL-001` | low | verified conditional deduction | §2.24.5–7, same labels, physical lines 38–54: for `n=1`, `E=(1+eps)b`, the magnetic counting density exceeds the zero-field count; a false *proposed* strengthening only. | **Do not** replace the counting constant in (2.24.7) by its free-field value. Retain strict energy interval and Landau endpoint convention. |

**Current-ToC scope:** §2.24 selected spectral measure and Riesz/counting
normalization only. The complete magnetic oscillator spectral theorem,
Dirichlet localization, other statements and dependencies are not
certified. Project historical inventory remains **25 chapters, 747 sections,
zero whole mathematical-section certifications**. All user-excluded
regularization/Bergman/L²/OT/multiscale/positivity-loss inputs remain
`deferred-by-user`, not resolved.
