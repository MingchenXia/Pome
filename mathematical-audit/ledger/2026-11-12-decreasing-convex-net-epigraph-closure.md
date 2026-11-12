# Classified finding ledger — 2026-11-12

| Stable finding ID | Severity | Status | Main SHA | Reviewed location | Result and disposition |
| --- | --- | --- | --- | --- | --- |
| POME-CONVEX-DECREASING-CLOSED-EPIGRAPH-GAP-001 | low | verified conditional deduction | b6933b772f41b45918f7e25ed1afbbb1fd892272 | §21.11.13, §21.11.15, Eq. 21.11.23, §21.11.24; docs/sections/convex-functions-and-convex-bodies/index.html, blob 2a123a863642a5a75caa173f0f73aff439a02ea4, lines 112–169 and 209–231; permanent tags 2F4F518BD56D, 61B746F5E884, E1AD8A1437E2, 258227E5D497 | Exact identity $(\inf_i F_i)^*=\sup_iF_i^*$; explicit uniformly equicoercive decreasing proper closed strictly convex $F_k=x^2+e^{-kx}+\chi_{[0,\infty)}$ whose pointwise infimum has a boundary jump at zero; $\operatorname{cl}\inf F_k \ne \inf\operatorname{cl}F_k$; conjugate $p_+^2/4$, biconjugate closed hull. Source assertions remain correct; optional warning only. |

**Detailed proof:** [report](../reports/2026-11-12-decreasing-convex-net-epigraph-closure.md).

**Dependency and scope:** The example and conjugation calculations are checked directly, while general Fenchel–Moreau remains an internal dependency, not a newly certified theorem. This is not a confirmed error, a genuine duplicate, or an applied source repair. Prior resolved/unresolved audit findings are unchanged. Demailly regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale/positivity-loss work retains **deferred-by-user**, not resolved/certified.
