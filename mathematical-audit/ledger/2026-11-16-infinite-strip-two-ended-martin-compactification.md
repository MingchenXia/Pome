# POME-MART-STRIP-TWO-END-MINIMAL-001 — classified finding

**Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`. **Date:** 2026-11-16. **Status:** verified conditional deduction; **severity:** low; original results not refuted.

**Location:** `docs/sections/green-energy-and-martin-boundaries/index.html` blob `976a90f2a5eba299658f73a1eee8b9d3fef8020f`, Theorem 4.5.9 source `classical-potential-theory:1677A9F0` / tag `9D6B5CF5E0CF`, lines 106–121; Theorem 4.5.12 source `classical-potential-theory:57D18B4C` / tag `6736FBE7368C`, lines 165–185. Conditional input: `docs/sections/kelvin-transforms-and-half-space-potentials/index.html` Theorem 3.2.6 source `classical-potential-theory:1C8A330A` / tag `6BC86EEF03A9`, lines 64–75, 80–129.

**Finding and complete justification:** the infinite strip has **two** distinct minimal Martin ends with normalized kernels \(e^{\pm s}\sin t\), plus its two horizontal sides. Conformal uniformization \(e^{s+it}\), an exact half-plane Green quotient, Poisson measure recovery and atom-splitting prove the complete finite positive-harmonic representation, net topology and minimality. [Proof](../reports/2026-11-16-infinite-strip-two-ended-martin-compactification.md).

**Affected dependents:** §4.5.9/.12/.13 as model checks; §3.2.6 as a conditional representation input. **Proposed correction:** none to source/body; preserve a separate example from `POME-MART-EXTERIOR-BALL-INFINITY-001`. Abstract general sweeping and representation proofs not certified. User-excluded Demailly regularization, Bergman/L²/OT/multiscale/positivity-loss programmes remain **deferred-by-user**.
