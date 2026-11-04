# Classified mathematical-audit entry — 2026-11-04

| Field | Record |
| --- | --- |
| Stable ID | **POME-CONVEX-MONOMIAL-ENTROPY-OPTIMUM-001** |
| Severity | **low** |
| Status | **verified conditional deduction**. Original printed Lemmas 21.11.60 and 21.11.62 are correct; this is neither a confirmed error, proof gap, repair, external input nor genuine duplication. |
| Reviewed main SHA | b6933b772f41b45918f7e25ed1afbbb1fd892272 |
| Exact integrated reading file | docs/sections/convex-functions-and-convex-bodies/index.html |
| Main HTML blob | 2a123a863642a5a75caa173f0f73aff439a02ea4 |
| Anchors | Lemma 21.11.60, sgpt:66C95CF5 / permanent B1B557E6282F, physical lines 773–819; Equation 21.11.61, sgpt:47539ADA / EF4C4E285442, lines 777–782; Lemma 21.11.62, sgpt:5CDD1487 / 81D915E5313D, lines 823–860. |
| Actual hypotheses | Finite nonempty list of exponents (repetitions allowed); original first lemma integer Laurent exponents and alpha in Z^n; second lemma beta_i in N^n, alpha in R^n. The new proof also works for arbitrary real exponent vectors. |
| Exact verified deduction | For K=conv{beta_i} and P(alpha)={p_i>=0, sum p_i=1, sum p_i beta_i=alpha}, sup_x exp(alpha·x)/sum_i exp(beta_i·x)=exp(-max_{p in P(alpha)}H(p)) if alpha in K, and +infinity otherwise, where H(p)=-sum p_i log p_i. Supremum attained at finite x precisely for alpha in relint K. |
| Complete justification | Weighted logarithmic Jensen bounds the quotient by exp(-H(p)). An entropy-maximizing feasible p* is strictly positive at all indices on the minimal face containing alpha; constrained first-order stationarity gives an exponential-family representation. An exposing normal ray removes terms outside the face and attains the bound in the limit. Strict separation proves divergence outside K. The proof includes repeated exponents and lower-dimensional K. |
| Mathematical verdict | Both printed iff statements and their proofs are correct. Their distinct Laurent-integer and real-logsumexp scopes must be preserved; shared geometry does not license deleting one canonical version. |
| Proposed correction | Optional explanatory sharp-constant/face-attainment remark after Lemma 21.11.62; **proposal only**. Retain original source labels, permanent tags and attribution. |
| Affected dependents | Possible later uses of monomial/Newton-polytope domination and toric logarithmic weights in §§21.11–21.13; no currently erroneous dependent identified. |
| Actual new coverage | New detailed analysis of previously unsampled Lemmas 21.11.60/.62 and Equation .61 in previously partly audited §21.11; not entire-section certification. |
| Audit limits | Older resolved/unresolved/deferred findings unchanged. All expressly excluded regularization/Bergman/weighted-L2/OT/multiscale/positivity-loss work remains **deferred-by-user**, not certified. |
| Verification | Finite-dimensional hand proof and exact example models only; no executable tests, build, CI, formalization, or site publication. |
| Full report | [Exact proof](../reports/2026-11-04-newton-monomial-sharp-entropy-constant.md) |

The current inventory retains **25 chapters / 747 numbered sections / zero completely mathematically certified sections**.
