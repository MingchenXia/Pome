# 2026-11-23 — Gauduchon surface relative entropy and cross-metric trace estimates

Reviewed main: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`; branch: \`review/mathematical-audit\`. Both are **verified conditional deductions**, **not** original-theorem errors or fully certified PDE/elliptic proof chains. [Anchored full report](../reports/2026-11-23-gauduchon-surface-kl-and-trace-cross-metric.md).

## POME-GAUDUCHON-SURFACE-SCALAR-KL-001
- **Severity / status:** low / verified conditional deduction.
- **Exact source:** \`docs/sections/smooth-monge-ampere-equations--normalization-for-the-gauduchon-equation/index.html\`, blob \`07303e817cd642d6f34b8ff2c1b876a4b299c4ac\`, Theorem 14.18.2 source \`non-kahler-pluripotential-theory:67056566\`, tag \`F90961841CA0\`, lines 32–62; Example 14.18.3 source \`non-kahler-pluripotential-theory:D7692D79\`, tag \`8AC1A3B0F2AF\`, lines 69–77.
- **Hypotheses:** smooth Gauduchon surface scalar equation and normalized smooth positive density. For \(H=G-F\), the gap \(b(F)-\int H\,d\mu_F-b(G)\) equals exactly \(\mathrm{KL}(\mu_F\Vert\mu_G)\), zero iff \(H\) is constant. Summing the reverse gap gives the Jeffreys divergence.
- **Proof:** \(\mu_F=e^F\gamma^2/Z_F\), \(b(F)=C-\log Z_F\); \(\log(d\mu_F/d\mu_G)=\log(Z_G/Z_F)-H\). Integrate against \(\mu_F\) and use strict Jensen. [Full details](../reports/2026-11-23-gauduchon-surface-kl-and-trace-cross-metric.md).
- **Proposed correction:** optional surface corollary only, no alteration to §14.18. Existing general Bregman/adjoint monotonicity \`POME-GAUD-ADJOINT-GRADIENT-MONO-001\` is *not* duplicated.
- **Affected dependents:** smooth surface normalization stability/identifiability (conditional).

## POME-GAUDUCHON-TRACE-CROSS-METRIC-HOLDER-001
- **Severity / status:** low / verified conditional deduction.
- **Exact source:** \`docs/sections/gauduchon-traces-and-the-topology-of-potentials/index.html\`, blob \`1516feb665870be31c5be159edb6c2cf1898db8c\`, Theorem 11.31.2 source \`non-kahler-pluripotential-theory:8C0421FB\` tag \`160CE026081B\` lines 45–62; Corollary 11.31.6 source \`non-kahler-pluripotential-theory:7FBCB410\` tag \`AA6333BC6B20\` lines 106–115; Proposition 11.31.7 source \`non-kahler-pluripotential-theory:5B0B54B7\` tag \`56D7737A1AF0\` lines 120–157.
- **Hypotheses:** two fixed admissible Gauduchon traces on the same compact normalized potential space. Each trace metric \(D_i\) obeys \(C_i^{-1}\|u-v\|_1\le D_i\le C_i\|u-v\|_1^{1/2}\). Therefore \(D_2\le C_2C_1^{1/2}D_1^{1/2}\) and the reversed inequality. The corresponding change-of-trace image homeomorphisms are bi-Hölder. **No universal optimality** is claimed.
- **Proposed correction:** optional corollary, not a source repair. **Affected dependents:** quantitative topology of Gauduchon traces with fixed backgrounds.
- **Unresolved inputs:** elliptic inverse estimates and topological compactness of normalized potentials remain dependencies; no upstream certification.

All user-excluded regularization/Bergman/\(L^2\)/OT/multiscale/positivity-loss proof-completion is **deferred-by-user**, not reopened.