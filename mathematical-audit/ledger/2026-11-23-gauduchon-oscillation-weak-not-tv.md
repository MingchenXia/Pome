# POME-GAUD-DENSITY-WEAK-NOT-TV-OSCILLATION-001

**Date:** 2026-11-23. **Main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. **Severity/status:** low / **verified conditional deduction**, NOT a false printed theorem and NOT a complete transitive certificate.

**Anchor:** \`docs/sections/a-gauduchon-variational-volume--integrability-of-gauduchon-determinant-measures/index.html\`, blob \`42dae52119ba2bf793f104280abe615d9b25f09d\`, Example **12.9.21**, source \`non-kahler-pluripotential-theory:656408ED\`, permanent \`CAEF64468276\`, physical lines **557–604**, in particular the rank-one Hessian formula **575–581**; Theorem **12.9.18**, source \`A790BDE0\` / permanent \`AD62F7DA0E68\`, lines **496–549**.

**Hypotheses:** connected compact complex \(n\)-fold with \(n\ge3\), Hermitian \(\omega>0\), smooth probability \(dV\), and the *same* oscillatory \(v_j=(a/j^2)\zeta\sin(j\operatorname{Re}z_1)-\sup_X((a/j^2)\zeta\sin(j\operatorname{Re}z_1))\in\mathcal V_\varepsilon\) as printed Example 12.9.21, with \(\beta=dx\wedge d^cx\), \(\chi=\zeta\operatorname{tr}_\omega\beta\ge0\), \(\chi\not\equiv0\).

**Proved strengthened conclusion:** With \(c_j=\int_X(\omega+dd^cv_j)^n\), \(c_0=\int_X\omega^n\), \(\mu_j=(\omega+dd^cv_j)^n/c_j\), one has
\[
\mu_j\rightharpoonup\omega^n/c_0,\qquad
\lim_j\sup_E|\mu_j(E)-(\omega^n/c_0)(E)|
=\frac a{\pi c_0}\int_X\chi\,\omega^n>0.
\]
The corresponding smooth probability densities \(e^{F_j}\) and bounded logarithms \(F_j\) have no strongly convergent subsequence in any finite \(L^r(dV)\), \(r\ge1\).

**Proof:** Source lines 575–581 give \(dd^cv_j=-a\zeta\sin(jx)\beta+O(j^{-1})\) uniformly. Rank one gives \((\omega-a\zeta\sin(jx)\beta)^n=(1-a\chi\sin(jx))\omega^n\). Compact-support integration by parts gives \(c_j=c_0+O(j^{-1})\); Riemann–Lebesgue gives weak convergence, while the mean of \(|\sin|\) is \(2/\pi\), producing the exact positive TV limit above. Total-variation convergence is necessary for strong density \(L^r\)-convergence, and uniform \(L^\infty\) bounds plus Lipschitz continuity of the exponential rule out strong convergence for the logarithms. [Full proof, direct checks and boundaries](../reports/2026-11-23-gauduchon-oscillation-weak-not-tv-and-nef-tail-rotation.md).

**Proposed correction and dependents:** Optional add-on corollary after Example 12.9.21; **no change to the correct printed result**. Relevant to strong-density compactness in Theorem 12.9.18 and varying smooth data in §12.10. Distinct from older §15.37 \`POME-MA-DOMINATED-WEAK-NOT-TV-001\` and §20.6 non-\(\mathbf Q\)-Cartier result. No user-excluded regularization subject reopened.
