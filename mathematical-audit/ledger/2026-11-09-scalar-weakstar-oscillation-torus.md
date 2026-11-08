# Classified ledger — 2026-11-09 — high-frequency scalar homogenization

| Stable finding ID | Status | Severity | Printed result | Precise outcome |
| --- | --- | --- | --- | --- |
| `POME-SCALAR-WEAKSTAR-HOMOGENIZATION-001` | **verified conditional deduction** | **low** | Theorem 11.33.5 **correct**; Eq. 11.37.2 **correct** | Smooth uniformly bounded logarithmic densities (F_j=a\cos(2\pi jx)) weak-star converge to zero but (B_0(F_j)=-\log J(a)\not\to B_0(0)=0). Their normalized smooth solutions converge uniformly (O(j^{-2})); normalized MA and supporting probabilities converge weakly, not in TV. |

- **Main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Source anchors:** `docs/sections/normalization-and-weak-adjoint-measures--the-scalar-functional/index.html` blob `fff86de757578ed2be369ba752123f62f3d31044`, source `non-kahler-pluripotential-theory:D502EBBF`, permanent `5E3583383688`, lines 88–121. Supporting `docs/sections/normalization-and-weak-adjoint-measures--entropy-and-the-closed-case/index.html` blob `0710d0732ae7ef81de3d3d62206a0f9c6b5d321f`, Eq. 11.37.2 source `non-kahler-pluripotential-theory:65FF799F`, permanent `803909FECEC0`, lines 50–59.
- **Hypotheses and construction:** flat unit-area elliptic curve, (	heta=dV=omega), (arphi=0) model, (a>0), (F_j=a\cos(2\pi jx)). A periodic Poisson solution gives explicit normalized (u_j=j^{-2}(v(jx)-\max v)). Full derivation in [the proof](../reports/2026-11-09-scalar-weakstar-oscillation-torus.md).
- **Action proposed, not applied:** optional sharpness remark for Theorem 11.33.5; no replacement of its strong (L^1) premise, no changes to permanent tags or attribution.
- **Affected dependents:** potential weakenings of §§11.34–11.36 stability/duality; these were not recertified. No original result or existing classified finding reclassified.
- **Deferred by owner:** Demailly approximation/regularization and dedicated Bergman/(L^2)/OT/multiscale/positivity-loss work remains `deferred-by-user`.
