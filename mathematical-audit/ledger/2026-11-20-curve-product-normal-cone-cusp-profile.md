# Finding ledger — 2026-11-20 curve-product normal geometry

| Finding ID | Classification | Severity | Original text status | Direct scope | Proposed action |
| --- | --- | --- | --- | --- | --- |
| POME-CURVE-PRODUCT-NORMAL-CONE-CUSP-PROFILES-001 | verified conditional deduction | low | Theorem 10.23.1 remains valid; no printed error alleged | Entire §10.23, lines 7–49, main b6933b772f41b45918f7e25ed1afbbb1fd892272, blob d68563036cd1286475ebf2b704999c3e20cff589, section FE10733FC7A7, theorem 3BB4C60DE3DF, equations 464F29927E86 and 1DB31DDE4B07 | Optionally add noncanonical geometric corollary; retain source labels, attribution and tags |

**Precise result.** For the curve-product models of Theorem 10.23.1, the local normal metric is exactly \(g_\perp=(Fg/\pi)|dz|^2\). With \(Fg=C_0r^{2\tau}\), \(\tau>-1\), it is the flat cone \(ds^2+(\tau+1)^2s^2d\vartheta^2\) of angle \(2\pi(\tau+1)\), with intrinsic disk area \(\pi(\tau+1)s^2\). With \(Fg=C_0r^{-2}(\log(1/r))^{-b}\), \(b>1\), it is the conformal cylinder \((C_0/\pi)t^{-b}(dt^2+d\vartheta^2)\), with exact inner-disk area \(2C_0t^{1-b}/(b-1)\) and Gaussian curvature \(-b\pi t^{b-2}/(2C_0)\). For \(b>2\) the distance \(s\) to the added divisor is finite, volume scales exactly as \(s^{2(b-1)/(b-2)}\), and curvature equals \(-2b\,s^{-2}/(b-2)^2\). For \(b=2\) the end is a complete constant-negative-curvature finite-area cusp; for \(1<b<2\) it is a complete finite-area horn with polynomially decaying tail volume.

**Proof and dependency trace:** [complete mathematical argument](../reports/2026-11-20-curve-product-normal-cone-cusp-profile.md). Local formulas are verified by conformal metric conversion, one-dimensional polar integration and exact radial distance integration. The global curve \(dd^c\)-solvability, extended-product identification (13.14.3), and closed-case full-mass uniqueness are **not certified**. Selected §10.22 context only, not its full proof.

**Affected dependents:** Theorem 10.23.1 geometric explanations and comparisons with §10.22 radial models. **Repair status:** none needed for the original theorem; supplement conditional on its hypotheses. **Excluded programme:** Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity loss remains deferred-by-user, never certified.

No tests, builds, CI or changes to main, mathematical body, registry, tags, or published docs.
