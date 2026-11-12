# Finding ledger — 2026-11-12: noncompact finite-level mass

| Finding | Severity | Status | Actual claim | Minimal counterexample | Proposed correction | Dependents |
|---|---|---|---|---|---|---|
| `POME-NPP-LEVEL-FINITE-NONCOMPACT-001` | medium | **confirmed error (noncompact scope)** | §13.14 Theorem 13.14.3 says `MA^ext_theta(u)(D_t)<infinity` for all smooth `theta`, `u in PSH(X,theta)` without compactness | `X=C^n`, standard `theta=dd^c|z|^2>0`, `u=0`: every `D_t=X`, and `MA^ext=theta^n` has infinite total mass | State `MA^ext(K intersect D_t)<infinity` for each compact `K` and `t>0`; retain σ-finiteness; deduce global finite level mass on compact `X` | Only noncompact uses of finite-level **total** mass; local truncation, σ-finiteness, compact applications unchanged |

Anchors: main `b6933b772f41b45918f7e25ed1afbbb1fd892272`; `docs/sections/non-pluripolar-monge-ampere-measures/index.html` blob `5d0f652ffaaaef81cf74d1786082e429f71b3b89`, Theorem 13.14.3 source `non-kahler-pluripotential-theory:059FFA20`, permanent `99C7ACBB2589`, lines 61–91; Lemma 13.14.2 source `:84DD8892`, permanent `D36A46B4DD86`, lines 24–57. Exact proof, compact local repair and impact are in [the report](../reports/2026-11-12-npp-level-finiteness-noncompact-counterexample.md).

**Deferred-by-user** (unchanged, neither resolved nor certified): Demailly approximation/regularization and dedicated Bergman, L², OT, multiscale atlas, positivity-loss programme. All previously resolved and unresolved findings retain their earlier statuses. No source fix applied.
