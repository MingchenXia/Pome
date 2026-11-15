# Quantitative and codimension-sharp Levi summation in Pome §9.32

**Date:** 2026-11-15. **Finding:** \`POME-STEIN-LEVI-QUANT-CODIM-SHARP-001\`.  
**Classification:** low severity; **verified conditional deduction** (a pointwise strengthening and sharpness check). **Not a confirmed error, proof repair, or whole-section certification.**

## Version-pinned reading evidence

- Reviewed \`main\`: \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.
- Integrated reading edition: \`docs/sections/separation-strict-exhaustions-and-coverings--convexity-and-stein-spaces/index.html\`; Git blob \`169e9d3bc872e9fd89d5135e69204e33fccd3783\`.
- Lemma **9.32.2**, original source label \`demailly-complex-geometry:6CDD47BF\`, permanent tag \`1139FC60D126\`: statement **physical lines 12–16**, integrated proof **lines 21–36**, especially the common-subspace intersection at **line 30**.
- Theorem **9.32.4**, original label \`demailly-complex-geometry:0AFF477A\`, permanent tag \`B8D34CACDCCC\`: **lines 59–74**, especially **lines 65–73**.
- The standing ambient weak/strong \(q\)-convexity convention is at **line 7**. Its numerical parameter is a *codimension*, not an index of positive eigenvalues independent of ambient dimension. In the same section, Corollary **9.32.13**, tag \`001E137924A4\`, is at **lines 241–248**.

## Statement and proof of the quantitative refinement

Let \(V\) be an \(n\)-dimensional Hermitian vector space. Fix \(s\ge 1\), positive coefficients \(c_j>0\), integers \(r_j\ge0\), and Hermitian forms \(H_j\). Suppose that for every \(j\) there is a complex linear subspace \(W_j\subset V\) with
\[
\operatorname{codim}_{\mathbb C}W_j\le r_j,\qquad
H_j(v,\bar v)\ge \lambda_j\|v\|^2\quad(v\in W_j),
\qquad \lambda_j\ge0.
\]
Then \(W:=\bigcap_{j=1}^{s}W_j\) satisfies
\[
\operatorname{codim}_{\mathbb C}W\le \min\!\left(n,\sum_jr_j\right),\qquad
\left(\sum_jc_jH_j\right)|_W\ge
\left(\sum_jc_j\lambda_j\right)I_W. \tag{A}
\]
Indeed the map \(V\to\bigoplus_jV/W_j\) has kernel \(W\), giving the codimension bound. On \(W\) the inequalities add, proving (A). Thus if some \(\lambda_j>0\), the sum is strictly positive on a subspace of codimension at most \(\sum_jr_j\). In local ambient coordinates this proves the quantitative version of the *strong* conclusion of Lemma 9.32.2, with \(r_j=q_j-1\), \(q=1+\sum_jr_j\). For merely weak summands take every \(\lambda_j=0\). There is no compactness, global exhaustion, or discarded regularization input in this argument.

The coefficient \(\sum_jc_j\lambda_j\) and the **codimension bound** are simultaneously optimal for this *linear-algebraic summation rule*, even for global smooth quadratic functions on \(\mathbb C^n\). To see this, let \(r=\sum_jr_j\) with \(1\le r<n\), and split
\[
\mathbb C^n=B_1\oplus\cdots\oplus B_s\oplus W_0,
\quad \dim_{\mathbb C}B_j=r_j,\quad \dim_{\mathbb C}W_0=n-r.
\]
For \(\lambda_j>0\), define
\[
u_j(z)=\lambda_j\!\!\sum_{k\notin B_j}|z_k|^2
-A_j\!\!\sum_{k\in B_j}|z_k|^2,
\]
where the notation denotes coordinate sums for the indicated orthogonal blocks and \(A_j>c_j^{-1}\sum_{i\ne j}c_i\lambda_i\) whenever \(r_j>0\). Each Levi form \(H_{u_j}\) is \(\lambda_jI\) on \(B_j^\perp\), a subspace of codimension \(r_j\), so \(u_j\) is *strongly* \((r_j+1)\)-convex in the literal convention of §9.32. On each \(B_j\),
\[
H_{\sum_ic_iu_i}=
\Bigl(-c_jA_j+\sum_{i\ne j}c_i\lambda_i\Bigr)I<0,
\]
whereas on \(W_0\) it equals \((\sum_ic_i\lambda_i)I\). Consequently the sum has **exactly \(r\) negative and \(n-r\) positive Levi eigenvalues** and is not strongly \(r\)-convex (which would require a positive subspace of codimension at most \(r-1\)). Its positive eigenvalues attain equality in (A). This proves the asserted sharpness; for \(r=0\), the index \(q=1\) is already the smallest admissible one.

## Direct reading check of the integrated global argument

Theorem 9.32.4 sums nonnegative weak \(q_j\)-convex exhaustions on \(U=\bigcap_jU_j\). Its compactness step at **lines 65–71** is valid: a closed sublevel of the sum lies in the finite intersection of compact factor sublevels, because every summand is nonnegative, and the resulting set is closed there. The strong version uses the sum with one unflattened strong exhaustion; it is strict away from the intersection with that factor's exceptional set (**lines 73–74**). The compactness qualification on that exceptional set is essential; the original explicit \(\mathbb C\times\mathbb P^1\) example at line 78 is retained, not re-registered here.

The quadratic model above checks **only the pointwise Levi-index algebra** used by the intersection theorem. Its individual \(u_j\) are not proper exhaustions when \(r_j>0\); therefore it does **not** establish sharpness of the *global intersection theorem*, nor does it replace any upstream coherent vanishing or local embedding proof. Theorem 9.32.4 and Corollary 9.32.13 are not refuted.

## Status, dependencies and proposed documentation

- **Status:** verified conditional deduction, low. No false printed statement or newly confirmed proof gap. A proposed, non-production corollary is (A) and the exact quadratic sharpness witness.
- **Dependencies:** finite-dimensional Hermitian linear algebra; only the printed ambient \(q\)-convexity convention is needed. The global intersection application remains conditional on the established existence of weak/strong smooth exhaustions and their nonnegative normalization in Proposition 9.32.3.
- **Affected downstream uses:** the local Levi-index step in Theorem 9.32.4; its \(q=1\) Stein intersection consequence in Corollary 9.32.13. **No global optimality or complete transitive certification claimed.**
- **Coverage:** first direct mathematical-proof inspection this audit session of Lemma 9.32.2 and Theorem 9.32.4, with the definition and Corollary 9.32.13 inspected only for hypotheses/dependents. Earlier §9.32.6 and §9.32.8 audits remain distinct. This was **not** a first visit to numbered §9.32 and is **not** whole-section verification. Current main ToC: 25 chapters / 747 numbered sections.
- The user-excluded Demailly approximation/regularization and its Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale and positivity-loss programmes remain **deferred-by-user**, not resolved or certified. Nothing from that programme is used here.
- Review-only Markdown. No main/source/registry/canonicalization/tag edits, project build, test suite, CI, or publication.
