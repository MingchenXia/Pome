# 2026-11-24 — Gauduchon perturbed-minimizer quotient gap

## POME-GAUDUCHON-VOLUME-TEST-QUOTIENT-GAP-001

- **Status:** verified conditional deduction (**low**); not a confirmed original error, not a theorem repair.
- **Main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
- **Exact printed location:** docs/sections/a-gauduchon-variational-volume--positive-volume-without-bigness/index.html (blob 4e892ab379abdfa3b6520671db344e94bbc7a51a), permanent section tag E4AB7B03C20D, Theorem 12.14.6 tag ECAB6BFB33FD, Proposition 12.14.10 tag 0E9506DB4E70, equation (12.14.11), physical lines 169–205 and radial integrals 207–235.
- **Hypotheses:** m≥2, n=m+1, t=(m−1)/m, θ=ω+(x/t)w, μ=ω^m∧w, g_ε the smooth balanced metrics of Proposition 12.14.10 for ε>0.
- **Finding:** letting H(ε)=∫_B(x/t+ε)^{-1}ω^m and F=H^{-1/n}, the fixed-background test quotient equals n^{1/n}(F−εF'), is strictly increasing in ε, and has the three exact positive leading gaps: ε/6 for m=2; (2/9)ε²log(1/ε) for m=3; C_m ε² for m≥4, after division by n^{1/n}. Here C_m=J_0/n−(n+1)I_0²/(2n²)>0, I_0=(m−1)²/[m(m−2)], J_0=(m−1)³/[m²(m−3)].
- **Proof:** cancellation of M_ε in (12.14.11); Cauchy–Schwarz forces F''<0; integrate −εF'' using the explicit radial density m x^{m−1} dx. Full calculations in [report](../reports/2026-11-24-gauduchon-quotient-gap-and-convex-geodesics.md).
- **Affected dependents:** quantitative use of §12.14.9–13 and comparison with §24.3.2 only; no original statement disproved or patch required.
- **Limitations:** specific test family only, no universal stability rate; full upstream smooth-equation/Monge–Ampère dependencies not certified.
- **Deferred-by-user:** exclude §12.15.4's regularization step via Theorem 5.32.1 and the associated prohibited programme. Preserve existing ledger records without certifying them.
