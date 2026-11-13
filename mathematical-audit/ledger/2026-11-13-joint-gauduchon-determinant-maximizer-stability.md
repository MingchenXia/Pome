# 2026-11-13 — joint Gauduchon determinant/maximizer net stability

- **Stable finding ID:** POME-GAUD-DET-JOINT-DENSITY-GRAPH-NET-001
- **Severity/status:** low / **verified conditional deduction**, **not** a confirmed false theorem, not a complete certification.
- **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272
- **Sections, direct proof coverage:** 12.7.1–3 and 12.8.1–2; §12.15.1 checked for comparison only.
- **Integrated paths and blob SHAs:** docs/sections/a-gauduchon-variational-volume--a-compact-dual-problem-over-gauduchon-currents/index.html (1c0f7efb92914b8a55754bd5039d7319392fb03b), physical lines 13–105; docs/sections/a-gauduchon-variational-volume--supporting-probabilities-represented-by-maximizing-currents/index.html (ed1ad2bf6220cd086a44d7ee92ca7779666288d9), lines 5–98.
- **Permanent tags / original source labels:** Equation 12.7.1 A99038CD10B4 / non-kahler-pluripotential-theory:919BAA56; Lemma 12.7.2 FB6C2382E066 / :EF340E54; Theorem 12.7.3 0537569F9F52 / :B931D275; Lemma 12.8.1 47843166E777 / :E1B004B5; Theorem 12.8.2 E9E119AAA269 / :3606F8FD.
- **New mathematical result:** uniform-density perturbations yield quantitative \(e^{\pm\delta/n}\) bounds for \(M(F)\), net-asymptotic maximality \(D_F(T_i)\ge e^{-2\delta_i/n}M(F)\), same-current measure variation estimate, and the **joint** weak cluster limit of maximizing currents and determinant measures for arbitrary directed nets. Two-sign upper-semicontinuity tests prevent unjustified passage of nonlinear determinants through weak convergence.
- **Precise limiting hypothesis:** \(F_i,F\in C(X,\mathbb R)\), \(\|F_i-F\|_\infty\to0\); \(T_i\) are global maximizers for each \(F_i\); \(X\) compact connected of complex dimension \(n\ge2\). No assertion for generic \(L^1\) densities or total-variation convergence to a limit measure.
- **Proposed correction:** optional qualified corollary after §12.8.1; no direct source change.
- **Conditional input/affected dependents:** §11.7 compact Gauduchon-current set; §12.7.2 semicontinuity; §12.7.3 maximality; §12.8.2 support identification; potential §12.15 comparison. Upstream PDE/scalar/smoothness chains not certified.
- **Not duplicated:** 2026-11-02 §11.33–11.35 abstract support-probability bounded-L1 stability lacks joint maximizing-current/determinant measure lift; older §12.34 audit used §12.7.1 only for matrix normalization.
- **Coverage credits:** +0 conservative new numbered-section first visits (historical reconciliation pending); +0 entire-section certificates, 25 chapters/747 numbered sections.
- **Deferred:** Demailly approximation/regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programme **deferred-by-user**, not resolved or certified.
- **Report:** ../reports/2026-11-13-joint-gauduchon-determinant-maximizer-stability.md
