# 2026-11-21: Okounkov DH base mismatch

- **ID:** POME-OKOUNKOV-DH-BASE-MISMATCH-VAGUE-001
- **Baseline main SHA:** b6933b772f41b45918f7e25ed1afbbb1fd892272
- **Status:** verified conditional deduction; **severity:** low; **not** a confirmed error or a proof repair of the printed Lemma 19.6.22.
- **Source:** docs/sections/the-theory-of-okounkov-bodies--okounkov-test-curves/index.html (blob 20ff3089e62dd1c8349e8bcc077ec64605a9788b); primary sgpt, Proposition 19.6.14 source BC456E2F / permanent 7B4552909292, lines 237–273; DH definition 19.6.18 permanent 51940EF88F4F, lines 329–334; Lemma 19.6.22 source B9C8ADE8 / permanent 9C05354365F4, lines 371–405.
- **Claim:** Under the *sequence* version of Proposition 19.6.14, with no convergence of the ambient decreasing base convex bodies to the designated limiting body, DH measures converge vaguely for compactly supported continuous tests. The exact escaping mass is vol(intersection of bases) minus vol(limiting body), escaping only toward negative infinity. Bounded-continuous weak convergence holds exactly when this gap vanishes.
- **Proof/counterexample:** [full proof, one-dimensional model, and normalization](../reports/2026-11-21-okounkov-dh-vague-base-mismatch-divisor-and-toric-audit.md). In particular, on base [0,2], functions G_j(x)=-j(x-1)_+ give DH_j=delta_0+(1/j)1_[-j,0]dt, while the designated body [0,1] gives delta_0.
- **Printed result classification:** Lemma 19.6.22 *already assumes* K_j converges to Delta; its use of volume convergence is justified. Not a false theorem. Do not delete that hypothesis or claim the counterexample satisfies it.
- **Suggested change:** an additional separate corollary only; maintain all canonical labels, permanent tags, conventional source variants, and existing historical attribution.
- **Affected dependents:** §19.6 convergence, §22.1.54 DH limit interpretation; compare prior distinct non-Archimedean special case, not a duplicate mathematical finding.
- **Remaining input gap:** The current audit uses original Proposition 19.6.14 and DH definitions conditionally; its full transitive proof chain, including the imported convex-body properties, is not independently certified.
- **Deferred:** all user-excluded regularization and dedicated Bergman/L2/OT/multiscale/positivity-loss programme remain deferred-by-user.
