# Classified audit finding — 2026-11-12

| Field | Exact value |
| --- | --- |
| Stable ID | `POME-PROJ-GRAPH-DIAGONAL-INTEGRAL-SIGNS-001` |
| Status | **verified conditional deduction** (not a false theorem, not a fully certified dependency chain) |
| Severity | **low**, useful integral orientation/sign check |
| Production main SHA | `b6933b772f41b45918f7e25ed1afbbb1fd892272` |
| Actual integrated file | `docs/sections/spectral-sequences-support-and-cup-products--the-integer-cohomology-ring-of-projective-space/index.html` |
| Integrated blob | `cb90abebae459659c273b9de67848f3feded35e3` |
| Source / permanent: lemma | `demailly-complex-geometry:1EB6C39D` / `419BAFBD0FA6`, lines 16–41 |
| Source / permanent: theorem | `demailly-complex-geometry:FF8EE3A7` / `0CD4D885B4B4`, lines 46–79 |
| Required hypotheses | `X=P^n_C`, `n>=1`, complex orientation, Pome signed `h=c_1^Z(O(1))`, holomorphic `f:X->X` with `f^*h=d h`, `d>=0` |
| New checked conclusion | `PD(Gamma_f)=(-1)^n sum_(j=0)^n d^j h_1^j h_2^(n-j)`; `PD(Delta)=PD(Gamma_id)`; intersections `sum_(j=0)^n d^j` and `(n+1)d^n` |
| Key proof method | Integral torsion-free cellular Kunneth basis; perfect complementary pairing; graph projection formula; independent graph-normal-bundle Euler crosscheck |
| Conditional inputs | Full integral projective ring Theorem 10.75.2; oriented Poincare duality and cap trace §§10.71–10.73; elementary integral cellular cross product; no excluded regularization input |
| Printed statement erroneous? | **No**; Theorem 10.75.2 correctly retains its nonstandard sign convention |
| Proposed correction | None required. Optional new standalone worked example after Theorem 10.75.2; proposed only |
| Affected dependents | Diagonal Gysin signs, graph intersections, simple fixed-point counts, normal Euler numbers for endomorphism graphs |
| Unresolved | Complete transitive certification of internal duality/comparison inputs; treatment of nontransverse fixed-point local multiplicities beyond the cohomological intersection number |
| Deferred by user | Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale-atlas and positivity-loss programme; neither resolved nor inspected here |
| Exact review | §10.75 lines 7–79, previously comparison-context visited; **0 first sections / 0 entire sections certified**; ToC 25/747 |
| Full argument | [2026-11-12 projective graph report](../reports/2026-11-12-projective-graph-diagonal-cohomology.md) |

No direct mutation of main, integrated math body, permanent tags, canonicalization or registry. No tests, builds, CI, or website publication performed.
