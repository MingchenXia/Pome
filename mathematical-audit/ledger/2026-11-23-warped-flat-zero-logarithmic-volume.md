# POME-WARPED-FLAT-ZERO-LOG-VOLUME-001

**Date:** 2026-11-23. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Severity/status:** low / **verified conditional deduction**; the original theorem is **not** false, and no complete upstream certificate is asserted.

**Exact source:** §12.13 Theorem 12.13.1 (non-kahler-pluripotential-theory:3199B4CA; permanent B5C9469E9BB3), Eq. 12.13.2 (permanent 503F3EDAE05A), Proposition 12.13.4 (source D87E6BC6; permanent 6E8682D7FD89). Current integrated file docs/sections/a-gauduchon-variational-volume--subtraction-on-warped-products/index.html, blob 5bff92967df7c96355d202871fc3dc033c99010d, physical lines 10–38 and 78–106.

**Hypotheses:** §12.13 compact product B×C (complex base dimension m≥2, n=m+1, W=∫_Bα^m>0, probability σ on B and w on C), θ_{t−ε}=α+(a+ε)w. Smooth nonnegative a has an **exact exponential flat zero** a=exp(−dist(x,Z)^{−β}) in a tube of a compact smooth real codimension-d submanifold Z, β>0, and is positive off Z. Define A_Z=lim_{r↓0}r^{−d}σ({dist(x,Z)<r})∈(0,∞); T=log(1/ε).

**New conclusion, not a source restatement:**
\[
H(\varepsilon)\sim A_Z\varepsilon^{-1}T^{-d/\beta},\quad
J(\varepsilon)\sim A_Z\varepsilon^{-2}T^{-d/\beta},
\]
\[
\mathcal V_\mu(\theta_{t-\varepsilon})\sim(nW/A_Z)\varepsilon T^{d/\beta},\quad
\lambda_\mu(\theta_{t-\varepsilon})\sim(nW/A_Z)^{1/n}\varepsilon^{1/n}T^{d/(\beta n)},
\]
\[
\mathcal C(t-\varepsilon)\sim n^{-(n-1)/n}W^{1/n}A_Z^{-1/n}
\varepsilon^{1/n-1}T^{d/(\beta n)}.
\]
Volume and root volume vanish at the endpoint; the cost is integrable and its remaining integral equals the root volume at t−ε.

**Proof:** For R=T^{−1/β}, the integrands (a+ε)^{−p}, p=1,2, are asymptotically ε^{−p} on {ρ≤(1−η)R}. The volume of the inner tube is asymptotically A_Z(1−η)^d R^d. The outer annulus contributes O(ε^{−p}T^{−d/β−1}) by the substitution v=ρ^{−β} in ∫_R^{ρ_0}ρ^{d−1}e^{p/ρ^β}dρ; the fixed complement contributes O(1). The inner-tube upper bound and η↓0 prove the two **exact same-coefficient** moment equivalents. Then apply the checked §12.13.1 root-volume formula and Eq. 12.13.2 cost normalization, not any limit interchange of currents. [Detailed argument](../reports/2026-11-23-warped-flat-zero-logarithmic-volume-and-nef-core.md).

**Proposed correction and dependents:** No required correction to valid Theorem 12.13.1 or Proposition 12.13.4. Optional example/corollary about genuinely flat zeros; impacts endpoint rate interpretations in §§12.13–12.14 and any volume-based continuity criterion. The base smooth equation §14.2.1 and balanced construction §12.6.32 remain unverified **dependencies**. No approximation/Bergman/L2/OT/multiscale/positivity-loss work reopened; all such prior audit entries remain deferred-by-user.
