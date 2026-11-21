# POME-GUILLEMIN-ENTROPY-FACET-SCALING-RIGIDITY-001

- **Date:** 2026-11-21
- **Severity / status:** low / **verified conditional deduction**, not a false printed theorem or a repair of one.
- **Reviewed main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.
- **Integrated path:** `docs/sections/convex-analysis-and-toric-potentials--the-guillemin-reference-metric/index.html`, blob `4458eef6df84ef46d601d39506017387ed292e08`.
- **Exact anchor:** Theorem 21.10.1, Step 2 lines 37–66, Step 4 lines 75–88, source label `E94A20D6`, permanent tag `B471B994CE64`.
- **Hypotheses:** smooth positive-dimensional Delzant polytope (P), unchanged toric line bundle (L_P), unchanged lattice frames/coordinates; entropy (G_a=a\sum_\rho\ell_\rho\log\ell_\rho\) on (P), (a>0); dual weights (H_{v,a}=G_a^*(\operatorname{Trop}z)-\log|\chi^v(z)|^2\).
- **Result:** continuous metric for all (a>0); smooth on all charts iff (1/a\in\mathbb Z_{>0}\); smooth curvature is strictly positive everywhere iff (a=1\), while (a=1/p\), (p\ge2\), has semipositive degenerate normal curvature at the toric boundary. All other (a\) fail (C^\infty\) boundary extension.
- **Justification:** (F_a(x)=aF_0(x/a)\); in facet normal variables (r_i=|w_i|^{2/a}=t_i e^{1+g_i(t)}\), original Step 2 implicit-function Jacobian is invertible; the smooth potential in (r_i\) has boundary derivative (a e^{-1-g_i(q)}>0\), giving (H=H(0)+a e^{-1-g_i(q)}|w_i|^{2/a}+O(|w_i|^{4/a})\). The exponent controls smoothness and the normal complex Hessian. The exact (\mathbb P^1\) test is (H_{0,a}=a\log(1+|w|^{2/a})\).
- **Proposal:** optional qualification only; preserve current Theorem 21.10.1 and all attribution/source/permanent tags.
- **Affected potential dependents:** toric metric constructions §§21.8–21.14 if anyone proposes scaling the entropy; none of the *existing* (a=1\) statements is invalidated.
- **Proof, remaining dependencies and other scope:** [2026-11-21 full report](../reports/2026-11-21-guillemin-entropy-scaling-and-cross-chapter-audit.md). Original §21.10 has not been transitive-chain certified.
