# POME-HESS-PENALTY-OBSTACLE-CONTRACTION-001 — 2026-11-18

- **Status / severity:** **verified conditional deduction / low**, *not* a false theorem, proof-gap certification, or unconditional PDE existence proof.
- **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; §8.6 integrated HTML \`docs/sections/complex-hessian-equations--proper-equations-and-admissible-approximation/index.html\` blob \`841dd207876499be9d83045facf862a323e60994\`.
- **Exact source anchors:** Lemma 8.6.1, source \`non-kahler-pluripotential-theory:91CAEA62\`, permanent \`8B310CC2C1A1\`, lines 11–36; Lemma 8.6.2 source \`761F7FD5\`, permanent \`B8367971A40D\`, lines 45–94; Lemma 8.6.5 source \`32B364F9\`, permanent \`DFE78235C5E9\`, lines 129–169; Theorem 8.6.6 tag \`68BE4F589DCE\`, lines 174–201 **context only**.
- **Hypotheses:** compact connected Hermitian \(X\), \(2\le m<n\), smooth real \(h_i\), \(N>0\), \(b_i>0\), **existing** smooth strictly \(\Gamma_m\) solutions from Lemma 8.6.1; arbitrary smooth \(h_i\) need not be admissible.
- **Result:** writing \(w_i=W_{N,b_i}(h_i)\), \(d=h_1-h_2-\log(b_1/b_2)/N\), \(\min d\le w_1-w_2\le\max d\). This yields sharp monotonicity, translation covariance, uniform 1-Lipschitz and exact prefactor shifts. For strictly admissible smooth \(h\) with \(0<a_h\le H_m(h)/\omega^n\le A_h\), the sharper \(\log(a_h/b)/N\le W_{N,b}(h)-h\le\log(A_h/b)/N\) holds; no such strict-obstacle bound claimed generally.
- **Proof:** \(\Gamma_m\) monotonicity of \(H_m\) at maxima/minima of \(w_1-w_2\); constant obstacle \(h=c\) gives exact sharpness \(w=c-\log b/N\). Linearized elliptic resolvent identity \((N-L_w)\dot w=N\dot h\) is a conditional check.
- **Correction proposal:** optional supplementary corollary after 8.6.5, **not** a change to published statements. Preserve the original weaker general approximation rate and all existing external dependencies.
- **Affected dependents:** §§8.6.2/.5/.6, §8.7.1; original PDE existence and §8.7 products not transitive-certified. No Demailly/Bergman/L²/OT/multiscale/positivity-loss work.
- **Coverage:** already partially visited §8.6, **+0 first sections / +0 fully certified**, actual 25/747.
- **Full proof:** [anchored report](../reports/2026-11-18-hessian-penalty-obstacle-order-contraction.md); [exact coverage](../coverage/2026-11-18-hessian-penalty-obstacle-order-contraction.md).
