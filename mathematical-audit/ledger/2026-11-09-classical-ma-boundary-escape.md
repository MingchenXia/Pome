# Finding ledger: POME-CLASSICAL-MA-BOUNDARY-ESCAPE-001

- **Date:** 2026-11-09.
- **Stable finding ID:** POME-CLASSICAL-MA-BOUNDARY-ESCAPE-001.
- **Status:** verified conditional deduction; **severity:** low. No incorrect printed theorem or proof step is asserted.
- **Main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Primary integrated path/blob:** docs/sections/classical-monge-ampere-measures-at-one-exceptional-point/index.html / 902375361e37c15e45e7f4b7055bfe4cd6a6db9d.
- **Anchors:** §7.18.1, source klimek-pluripotential-theory:E69DEC85, permanent 00C5CD9B3208, physical lines 42–54; §7.18.2, source klimek-pluripotential-theory:E1312773, permanent AD17D2D77F97, lines 56–72; bounded-perturbation pole invariance appears in proof expansion lines 34–40.
- **Dependencies crosschecked only:** §7.28.1, source demailly-complex-geometry:F96C3380 / permanent 1BBBF8109419, lines 5–10, blob 21dc39a9b02a4c1820f081a0c3a82e9f8ffca727; §7.2.4, source foundations-of-pluripotential-theory:01D6FA68 / permanent 706A589A680C, lines 89–95, blob 18bd2395f3b76941b2c677079c09eb6accc5a9cb.
- **Precise counterexample:** On the complex unit ball, u=log|z| and u_j=log|z|+(c/j)(|z|^{2j}-1), c>0. They have one common isolated pole and zero boundary values, u_j increases to u with sup norm of their finite difference at most c/j, but M_{u_j}(B_R)=(1/2+cR^{2j})^n and M_{u_j}(B)=(1/2+c)^n, whereas M_u=2^{-n}delta_0. The excess converges to a uniformly distributed mass on the boundary, not a mass in the open domain.
- **Complete justification:** [report](../reports/2026-11-09-classical-ma-boundary-escape.md), radial Hessian determinant plus spherical integration, fixed pole mass, monotonically increasing potentials, and exact boundary concentration. The nonmonotone a_j=j^{-1/2} variant gives divergent global mass despite uniformly vanishing perturbation.
- **Mathematical distinction:** printed fixed-pair comparison and mass-preserving lower truncation remain valid; printed decreasing *local* continuity remains valid. What fails is the unprinted upgrade from local/vague weak convergence to total mass convergence without boundary tightness.
- **Affected dependents:** possible applications of §§7.18 and 7.28 that exchange the approximation index with exhaustion B_R up to R=1; no erroneous downstream statement has been identified from this example.
- **Proposed correction:** explanatory Example or Remark, no direct source change.
- **Scope accounting:** first selected §7.18 visit; no complete-section certification. §7.28 and §7.2 crosschecked only. The project ToC remains 25 chapters / 747 numbered sections / zero whole-section certifications. Existing resolved/unresolved ledgers are not reclassified. Excluded regularization programme stays **deferred-by-user**.