# POME-OBSTACLE-ENVELOPE-OSCILLATION-MODULUS-001

- **Date:** 2026-11-23.
- **Main SHA:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Severity/status:** low / verified conditional deduction, not a false theorem and not a full proof-chain certification.
- **Main location:** `docs/sections/multiplier-ideal-envelopes-and-goodness--a-topology-on-ordinary-singularity-types--all-smooth-obstacles/index.html` blob `6bfe360706d85c21e83b0212de472de716d8c04c`, §18.12.1 lines 14–28, source `non-kahler-pluripotential-theory:B868A212`, permanent `DAA4A0418197`; supporting §18.11.1 obstacle shift lines 35–41 in blob `9b0718c3c09f9323e744945aad555c52bb270d93`, source `non-kahler-pluripotential-theory:4A5D2187`, permanent `760C8726BAE2`.
- **Hypotheses:** compact complex manifold, fixed admissible smooth real background \(\theta\), two ordinary types, smooth real obstacles \(F,G\), probability measure \(dV\); either the ordinary or ideal singularity envelope.
- **Deduction:** the change of two-class \(L^1(dV)\) envelope distance under an obstacle perturbation is at most \(\operatorname{osc}_X(F-G)\), instead of the printed sufficient \(2\|F-G\|_\infty\). An additive constant perturbation leaves these distances exactly unchanged.
- **Complete argument:** let \(m=\min(G-F)\) and \(M=\max(G-F)\). Translating a competitor by \(m\), respectively \(-M\), shows \(m\le P_G[h]-P_F[h]\le M\) a.e. for each class \(h\). Subtracting the inequalities for \(u\) and \(v\) bounds the pointwise change of their envelope differences by \(M-m\). Integrate against probability \(dV\) and use the reverse triangle inequality. Identical reasoning applies to ideal envelopes, since translations preserve all multiplier ideals. No approximations or limits are involved.
- **Proposed change:** optional proof strengthening to Proposition 18.12.1 only, via reviewable separate patch; no production modifications in this audit. **Dependents:** the dense-obstacle uniformity argument, §18.12.3 analytic closure; the latter's separate upstream inputs are not certified.
- **Limits:** no claim of optimal coefficient, no claim that a printed theorem is false, no Demailly/Bergman/L²/OT programme.
- **Full anchored report:** [2026-11-23 obstacle/flux audit](../reports/2026-11-23-obstacle-oscillation-and-hopf-flux-rotation.md).
