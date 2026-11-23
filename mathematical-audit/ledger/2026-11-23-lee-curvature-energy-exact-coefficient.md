# POME-LEE-CURVATURE-ENERGY-EXACT-COEFFICIENT-001

- **Date:** 2026-11-23.
- **Reviewed main:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- **Severity/status:** **low / verified conditional deduction**, not a false printed theorem, not a complete upstream proof-chain certificate.
- **Integrated path and blob:** \`docs/sections/locally-conformally-kahler-geometry/index.html\` / \`6ebf8e604b45d3eb748037af506145273ca3875d\`; anchors **8, 82–124, 187–212, 395–419**.
- **Source family and tags:** \`non-kahler-pluripotential-theory\`; Proposition 23.2.7 \`11EBB7AD1165\`, Eq. 23.2.8 \`35851308DD2B\`, Proposition 23.2.14 \`E5F423FF7707\`.
- **Hypotheses:** compact connected complex \(X\), \(n\ge2\), smooth LCK \(\omega\) with \(d\omega=\lambda\wedge\omega\), \(d\lambda=0\), associated \(g\), and \(d^c=i(\bar\partial-\partial)/(4\pi)\).
- **Exact result:**
  \[
  \int_X\kappa_\lambda\wedge\omega^{n-1}
  =\frac{n-1}{4\pi n}\int_X|\lambda|_g^2\,\omega^n,\qquad
  \left.\frac{d}{dt}\right|_{t=0}\int_X(\omega+t\kappa_\lambda)^n
  =\frac{n-1}{4\pi}\int_X|\lambda|_g^2\,\omega^n .
  \]
- **Complete new calculation:** with \(\omega=\sum_j x_j\wedge y_j\), \(\lambda=\sum_j(a_jx_j+b_jy_j)\), \(\lambda^c=(4\pi)^{-1}\sum_j(a_jy_j-b_jx_j)\) in an orthonormal real unitary coframe, diagonal contraction gives \(\lambda\wedge\lambda^c\wedge\omega^{n-1}=|\lambda|_g^2\omega^n/(4\pi n)\). Apply the displayed Stokes Eq. 23.2.8 and differentiate a wedge polynomial. The scalar Hopf model \(\omega=\alpha+\beta\), \(\kappa_\lambda=\alpha\), \(\lambda\wedge\lambda^c=\beta\) validates sign, \(n\), and \(4\pi\).
- **Correction:** no mathematical correction necessary; an **optional** exact-norm sentence after Eq. 23.2.8 may improve clarity. No body/source/tag/registry edit performed.
- **Affected dependents:** quantitative positive Lee pairing (§23.2.10–11) and initial volume-ray derivative (§23.2.14–15); their conclusions remain correct.
- **Dependencies not certified:** generalized Lamari theorem 11.6.1, the modification/Kähler \(\partial\bar\partial\)-lemma, smooth Hermitian MA existence 14.2.1 and positive-current compactness. Excluded regularization remains **deferred-by-user**.
- **Report:** [full proof and actual chapter coverage](../reports/2026-11-23-lee-energy-normalization-and-trace-restricted-volume-rotation.md).
