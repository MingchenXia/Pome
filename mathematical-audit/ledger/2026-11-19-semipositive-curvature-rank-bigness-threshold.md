# 2026-11-19 — Semipositive curvature rank and section-growth bigness

| ID | Status | Severity | Actual scope |
| --- | --- | --- | --- |
| `POME-SEMIPOSITIVE-FULLRANK-BIGNESS-IFF-001` | **verified conditional deduction** | low | §19.10.1 full direct audit; §§10.96.1, 19.9.16/17/20 dependency statements only |

**Reviewed:** main `b6933b772f41b45918f7e25ed1afbbb1fd892272`, `docs/sections/section-growth-of-semipositive-line-bundles/index.html` blob `41526a319c45c861a8303776f155096d1f36614a`, lines 5–22; source `demailly-complex-geometry:4B096A2D`, permanent `F31884F26A29`; equation `2B3916324C79`, lines 9–11.

**Finding:** for a connected compact complex `n`-fold (`n>=1`) with a *smooth semipositive* Hermitian holomorphic line bundle `L`, full curvature rank somewhere is equivalent to `\int\Omega_L^n>0`, positive `m^{-n}h^0(L^m)` limit, and `\kappa(L)=n`. Such an `X` is Moishezon. If maximal curvature rank `r<n`, the known §19.9.20 upper bound `h^0=O(m^r)` is sharp and has **no positive lower bound**: on `\mathbb P^r\times E^{n-r}`, `p^*\mathcal O(1)` and its infinite-order flat twists have identical rank-`r` curvature but `\binom{m+r}{r}` vs `0` sections.

**Original theorem:** correct (not refuted; not a repair). **Proposed action:** optional documented iff and rank-deficient caution; no direct source changes. **Dependencies:** §10.96.1 and §19.9.16/20 not transitively certified. **Existing prior art:** earlier §19.11 elliptic flat-twist model not reclassified as new. **Deferred-by-user** exclusions stay deferred.

[Full anchored proof](../reports/2026-11-19-semipositive-curvature-rank-bigness-threshold.md) · [coverage delta](../coverage/2026-11-19-ch19-semipositive-curvature-rank.md).
