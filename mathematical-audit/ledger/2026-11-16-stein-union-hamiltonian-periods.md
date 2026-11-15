# POME-STEIN-UNION-HAMILTONIAN-SPHERES-001 — exact holomorphic Hamiltonian form and infinitely many sphere periods

- **Date / reviewed main:** 2026-11-16 / `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Status / severity:** verified conditional deduction / low; **not** a false theorem or identified proof gap.
- **Exact source:** `docs/sections/separation-strict-exhaustions-and-coverings--an-increasing-union-of-affine-stein-surfaces/index.html`, blob `26b2e856fc24b04616b0840caec5c688cc045ffa`; §9.27 source `demailly-complex-geometry:36411603`, tag `E65337AF838D`; Example 9.27.1 source `demailly-complex-geometry:BBFF78A8`, tag `F00C66A8D202`; source lines 8–12, 18–30, 32–35, 41–46.
- **Mathematics checked:** compatible nowhere-vanishing (dz\wedge dw/w) on the open union; (\iota_{w\partial_w-t\partial_t}\Omega=-dz); smooth compact spheres (C_j) with exact periods (2\pi i\int_{1/(j+1)}^{1/j}F(z)dz) against every polynomial (F). Lagrange interpolation proves (\{[C_j]\}) linearly independent in ordinary (H_2(X;\mathbf C)).
- **Affected dependents:** adds invariants of the model of Example 9.27.1, without changing its Stein/non-Stein assertion; §9.26 local separation and §9.32 Stein criteria only contextual.
- **Correction proposed:** none to the printed theorem; retain the new auxiliary proof as an optional supplemental remark. No main, body or canonicalization modification authorized.
- **Limits:** no proof-chain transitive certification, no global cohomology-ring determination, no project tests/build. User-excluded regularization/Bergman/L²/OT/multiscale/positivity-loss work remains **deferred-by-user**.
- **Report:** [full proof](../reports/2026-11-16-stein-union-hamiltonian-periods-infinite-h2.md); [coverage](../coverage/2026-11-16-ch9-stein-union-hamiltonian-periods.md).
