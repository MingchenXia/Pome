# POME-MAGNETIC-RIESZ-ATOM-C1-LOCUS-001

- **Date:** 2026-11-24.
- **Status:** verified conditional deduction.
- **Severity:** low.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated path:** `docs/sections/magnetic-models-and-spectral-localization/index.html`, blob `ee89de7d23cc96a8546c736ac7d068546b126f3a`.
- **Anchors:** §2.24.4 equation source `demailly-complex-geometry-4EE24E32`, tag `6919A4A3FD8F`, physical lines 31–35; §2.24.5 source `demailly-complex-geometry-E2C26C03`, tag `72E6618A3A3C`, lines 38–45; Lemma 2.24.6 source `demailly-complex-geometry-2FD17158`, tag `0F14CB3D46F3`, lines 49–71.
- **Hypotheses:** spectral measure identification and locally finite positive convolutions of the printed model, all \(b_j\ge0\), arbitrary real \(E\).
- **Conclusion:** \(\partial_E^-r_b=\mu_b([0,E))\), \(\partial_E^+r_b=\mu_b([0,E])\). Differentiability and joint \((b,E)\)-continuity of \(\nu_b\) hold precisely at energies with no \(\mu_b\)-atom. The atom is zero if some \(b_j=0\); otherwise it is \((\prod_j b_j/(2\pi))\) times the number of nonnegative integer \(p\)-vectors with \(\sum_j(2p_j+1)b_j=E\).
- **Proof:** finite local spectral mass, dominated one-sided difference quotients; Tonelli atomlessness for free-pair convolution; finite Landau-level enumeration; vague-convergence sandwich at non-atomic endpoints. See [complete anchored proof](../reports/2026-11-24-magnetic-spectral-derivatives-and-tensor-rotation.md).
- **Printed theorem error?** No. The original Lemma 2.24.6 correctly claims continuity of \(r_b\), not everywhere continuity of \(\nu_b\) or its derivative.
- **Dependencies:** printed oscillator spectral decomposition and local vague convergence; not a transitive certificate for the underlying operator theory. Affects only optional energy-differentiation arguments and use of counting densities at Landau thresholds.
- **Proposed correction:** none required; optional explanatory corollary with strict-inequality endpoints, without changing permanent tags or normalization.
- **Duplicates ruled out:** earlier 2026-10-27 one-pair exact midpoint deficit, Dirichlet \(O(R^{-1})\) rate, and 2026-11-15 multi-pair midpoint deficit are separate results and are not counted again.
- **Excluded subject:** Demailly approximation/regularization and its dedicated Bergman, L², OT, multiscale and positivity-loss programme all remain `deferred-by-user`.
