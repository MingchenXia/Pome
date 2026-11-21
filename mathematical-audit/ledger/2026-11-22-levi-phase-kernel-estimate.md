# POME-LEVI-PHASE-CAUCHY-ESTIMATE-001

**Date:** 2026-11-22. **Status:** low / verified conditional deduction; **not** an incorrect source theorem or a claim of complete upstream certification. **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.

**Anchors:** \`docs/sections/levi-foliations-and-boundary-regularity/index.html\`, blob \`8c022608e6bb846204f1eb000ef2d4d873183441\`, Lemma 9.63.2 at physical lines 8–18, source \`demailly-complex-geometry:1E6C08BD\`, permanent \`6F469AB373C2\`; equation 9.63.3 permanent \`F5B6ECCA47FD\`. Dependent Theorem 9.63.4 at lines 24–68, source \`demailly-complex-geometry:B87F9D00\`, permanent \`A6B15EBA6E91\`.

For two functions satisfying the identical fixed-torus hypotheses of Lemma 9.63.2, write \(b_i=\operatorname{Im}H_i|_{\mathbb T_r}\) and \(a_i=\operatorname{Re}H_i(0,\cdot)\). On \(\overline{P_\rho}\times J\), \(0\le j\le l\), every holomorphic multi-index \(\alpha\) satisfies
\[
\|\partial_z^\alpha\partial_t^j(H_1-H_2)\|_\infty
\le \mathbf1_{\alpha=0}\|\partial_t^j(a_1-a_2)\|_\infty
+\left[2\prod_h\frac{\alpha_h!r_h}{(r_h-\rho_h)^{\alpha_h+1}}+\mathbf1_{\alpha=0}\right]\|\partial_t^j(b_1-b_2)\|_\infty.
\]
The exact Cauchy kernel derivative and differentiation under the **fixed compact torus integral** prove this inequality with no sequential compactness assumption. The proof is fully written in [the dated report](../reports/2026-11-22-levi-phase-nuclear-pullbacks-ringed-space-rotation.md).

**Proposed correction/addition:** optional quantitative corollary to 9.63.2 with the explicit interior constants; no statement correction required. **Affected dependent:** 9.63.4 transverse regularity of Levi foliations, conditionally on the earlier §9.34.1 Levi-bracket/Frobenius input (not independently certified). No boundary \(C^l\) estimate, full foliations perturbation theorem, or transitive upstream proof certificate follows. Original attribution must remain.
