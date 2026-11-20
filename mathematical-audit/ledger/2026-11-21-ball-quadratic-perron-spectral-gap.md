# POME-BALL-QUADRATIC-PERRON-SPECTRAL-GAP-001

**Date:** 2026-11-21. **Severity:** low. **Status:** verified conditional deduction (not a printed error; no original theorem refuted).

**Baseline:** main \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`. Full direct §7.7 and §7.8 audit, original integrated HTML blobs \`928f3d3e36f2d03a42623b91487ecec7d189e6c7\` and \`0284d93a0ac26e28746e95afda5e6875f9feaba3\`.

**Anchor:** §7.7 Theorem 7.7.4 (\`foundations-of-pluripotential-theory:FEE18534\`, permanent \`9181532558D7\`, §7.7 physical lines 104–135), maximality Theorem 7.7.7 (source \`5C75D8E4\`, permanent \`BCFDDA1FCB7A\`, lines 160–174); §7.8 Corollaries 7.8.4 (\`66F302D3\`/\`EADDEAF9FAD9\`, lines 184–207) and 7.8.8 (\`88AEA1CD\`/\`142C8110B540\`, lines 250–282).

**Exact hypothesis and result:** On the unit ball, arbitrary Hermitian \(A\), \(\lambda=\lambda_{\min}(A)\), and \(g\) holomorphic near the closed ball, the homogeneous Dirichlet Perron solution for boundary values \(Q_A+\Re g\) is \(Q_A-\lambda|z|^2+\lambda+\Re g\), with complex Hessian \(A-\lambda I\ge0\), determinant zero. For \(n\ge2\), \(u_j=|z|^2-|z_j|^2\) are smooth maximal psh solutions, but their average has top MA measure \(((n-1)/n)^n\eta^n>0\); the Perron solution of the averaged boundary data exceeds their average by exactly \(((n-1)/n)(1-|z|^2)\). Proves strict concavity of the Perron operator in this model and nonclosure of maximal psh potentials under convex averaging.

**Proof:** [Complete algebra, normalization and comparison argument](../reports/2026-11-21-ball-quadratic-homogeneous-dirichlet-and-mixed-ma.md). **Proposed correction:** none required. Optional explanatory example after §7.7.7 without touching permanent tags. **Affected dependents:** §7.7.4/.7 and interpretation of the lower mixed-product bounds in §7.8.4/.8.

**Open:** transitive certification of the upstream Bedford–Taylor comparison and continuity, semiconcavity and mixed discriminant signature. The deduction is not a substitute for those proofs. **Deferred-by-user:** Demailly regularization/approximation and every named Bergman, L², OT, multiscale and positivity-loss proof-completion programme; not resolved or certified. **Coverage:** two current whole sections directly reviewed; zero complete transitive chains; no tests/builds/CI.
