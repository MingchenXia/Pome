# Classified finding — 2026-11-04 — metric curvature rank versus intrinsic section growth

| Field | Value |
| --- | --- |
| Stable ID | `POME-SECTION-CURVRANK-METRIC-DEPENDENCE-001` |
| Status | **verified conditional deduction** |
| Severity | **low** (illustrative limitation, no false original theorem) |
| Production main SHA | `b6933b772f41b45918f7e25ed1afbbb1fd892272` |
| Integrated main file/blob | `docs/sections/flags-convex-bodies-and-section-growth/index.html` / `83557f0e15275253661fe679c75407e6636d497c` |
| Original source | `non-kahler-pluripotential-theory` (integrated public reading edition only) |
| Source labels | `:77A30A69` (Prop 19.9.19), `:CBB2BC97` (Cor 19.9.20), `:04D312FB` (Prop 19.9.23) |
| Permanent tags | `C8B2CB1B6819`, `14480FFA5B57`, `5C0C7B20BA7A` |
| Main line anchors | 391–426, 430–448, 503–516; contextual Example 19.9.25 lines 532–544 |
| Hypotheses tested | Connected compact complex manifold, a fixed holomorphic line bundle, arbitrary smooth Hermitian metrics (curvature not assumed semipositive), pointwise maximum curvature rank and semipositive-locus rank |
| New exact result | On one fixed complex `n`-torus and `L=O_X`, smooth metrics realize `r_h^+=r=0,1,...,n` while `h^0(X,L^p)=1`, `kappa(L)=0`, and the Euler polynomial of `L^p tensor E` is constant for every fixed `E`. |
| Proof and normalization | `phi_r=-sum_{j<=r} cos(2pi Re z_j)`, `dd^c phi_r=(i pi/2)sum cos(2pi Re z_j) dz_j wedge dbar z_j`; curvature exact, maximum rank `r`, semipositive rank `r` on explicit nonempty locus; maximum-modulus and Chern class calculations |
| Mathematical conclusion | The printed curvature-rank **upper bounds are correct**. Arbitrary metric curvature ranks cannot be intrinsic lower bounds on section-growth or Euler-polynomial degree. No correction to theorem statement needed. |
| Proposal | Optional example/remark after Cor 19.9.20, preserving history and canonical tags; do not edit production source |
| Affected downstream | Interpretations of §§19.9.19–20/.23 and comparison with sharp Example 19.9.25 |
| Unresolved prerequisites | General principalization, complex analytic image/Chow, full analytic HRR proof not recertified; no upstream theorem certified transitively |
| Deferred by user | Demailly regularization, Bergman, weighted L2, OT, multiscale atlas and positivity-loss programmes remain **deferred-by-user** |
| Coverage | New explicit metric-family and Chern/section-growth model for already partially audited §19.9; **not** full section verification |

[Complete independently calculated mathematical report](../reports/2026-11-04-torus-curvature-rank-versus-graded-growth.md). Prior confirmed errors, proof gaps, genuine duplications and deferred statuses are unchanged.
