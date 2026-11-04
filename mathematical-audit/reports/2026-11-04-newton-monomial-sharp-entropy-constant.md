# A sharp entropy constant for Newton-polytope monomial bounds

**Finding:** POME-CONVEX-MONOMIAL-ENTROPY-OPTIMUM-001. **Severity/status:** low / verified conditional deduction. **Original printed lemmas are correct:** this strengthens their boundedness criterion to an exact sharp constant and an attainment criterion; it is not a theorem repair or a proof-gap claim.

**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (2026-11-04). **Exact integrated reading edition:** docs/sections/convex-functions-and-convex-bodies/index.html, blob 2a123a863642a5a75caa173f0f73aff439a02ea4. **Section:** 21.11, specifically the concluding previously unsampled "Several lemmata" passage (physical lines 771–860). **Lemma 21.11.60:** source label sgpt:66C95CF5; permanent tag B1B557E6282F; lines 773–819; displayed Equation 21.11.61 source sgpt:47539ADA, permanent EF4C4E285442, lines 777–782. **Lemma 21.11.62:** source sgpt:5CDD1487; permanent tag 81D915E5313D; lines 823–860. The statement/source label and the stable public permalink are not interchangeable with the displayed reader number.

## Precise improvement

Let m>=1 and let b_1,...,b_m be finitely many (possibly repeated) points of R^n; write K=conv{b_i}. For a in R^n, define
\[
Q(a)=\sup_{x\in\mathbb R^n}\frac{\exp(\langle a,x\rangle)}
{\sum_{i=1}^{m}\exp(\langle b_i,x\rangle)}.
\]
Let
\[
\mathcal P(a)=\{p=(p_i)\in[0,1]^m:\ \sum_i p_i=1,\
\sum_i p_i b_i=a\},\qquad
H(p)=-\sum_i p_i\log p_i,\quad 0\log0=0.
\]
Then, **with no generic-position or distinctness hypothesis**:

1. If a is outside K, Q(a)=+infinity.
2. If a is in K, the feasible polytope \(\mathcal P(a)\) is compact and
   \[
      \boxed{Q(a)=\exp\!\bigl(-\max_{p\in\mathcal P(a)} H(p)\bigr)}.
   \]
   Thus \(1/m\le Q(a)\le1\).
3. The finite supremum is *attained by some x* if and only if a lies in the relative interior of K. If a lies on a proper relative face, the exact constant is only approached along a normal ray, not attained at any finite x.

For the integer exponents of printed Lemma 21.11.60, put \(a=\alpha\), \(b_i=\beta_i\), \(x_j=\log|z_j|^2\). This yields the exact supremum of the displayed Laurent-monomial ratio over \((\mathbb C^*)^n\). For the real a and nonnegative-integer \(b_i\) of printed Lemma 21.11.62, the exact infimum of \(\log\sum_i e^{\langle b_i,x\rangle}-\langle a,x\rangle\) is \(\max_{\mathcal P(a)}H\) when a is in K and minus infinity otherwise. The proof actually permits arbitrary real b_i. These are parallel but *not identically formulated*: the first is about integral Laurent monomials, the second about real log-sum-exp.

## Self-contained proof

**Outside the convex hull.** Strict finite-dimensional separation supplies v with \(\langle v,a\rangle>\max_i\langle v,b_i\rangle\). Evaluate at \(x=t v\) and let \(t\to+\infty\); the quotient tends to infinity.

**Universal entropy bound.** For any probability vector p and any real numbers \(s_i\), the elementary weighted AM–GM / logarithmic concavity inequality gives
\[
\log\sum_i e^{s_i}\ge\sum_i p_i s_i+H(p).
\]
Indeed, apply Jensen's inequality for log to \(\sum_{p_i>0}p_i(e^{s_i}/p_i)\le\sum_i e^{s_i}\). With \(s_i=\langle b_i,x\rangle\) and a feasible p, this gives
\[
\langle a,x\rangle-\log\sum_i e^{\langle b_i,x\rangle}
\le -H(p).
\]
For all feasible p, taking the maximal entropy \(H_*\) implies \(Q(a)\le e^{-H_*}\).

**All active coordinates of the entropy maximizer are positive.** Let G be the smallest face of the polytope K containing a. Every face of a polytope is exposed, and \(a\in\operatorname{relint}G\). Write \(I_G=\{i:b_i\in G\}\). A convex representation of a has p_i=0 outside \(I_G\), because any supporting affine functional exposing G vanishes on the mean only if it vanishes on every point with positive weight. There exists a feasible vector q that is *strictly positive at every index* in \(I_G\): let \(\bar b=|I_G|^{-1}\sum_{i\in I_G}b_i\); by relative interior, for sufficiently small \(\epsilon>0\),
\((a-\epsilon\bar b)/(1-\epsilon)\in G\), and combine its convex representation with \(\epsilon\) times the uniform distribution on \(I_G\). Compactness and continuity give an entropy maximizer p*. If \(p^*_i=0\) for an index in \(I_G\), the feasible perturbation \((1-\epsilon)p^*+\epsilon q\) increases entropy for small positive \(\epsilon\): the newly positive coordinate contributes \(-c\epsilon\log\epsilon\), dominating all O(\epsilon) changes at previously positive coordinates. Hence \(p^*_i>0\) exactly for \(i\in I_G\).

**Finite exponential representation on G.** On the relative interior of the affine feasible slice of the probability simplex supported on \(I_G\), stationarity of H at p* says that \((\log p^*_i+1)_{i\in I_G}\) annihilates all vectors u with \(\sum_i u_i=0\) and \(\sum_i u_i b_i=0\). Elementary linear algebra then gives real c and \(\lambda\in\mathbb R^n\) with \(\log p^*_i=c+\langle\lambda,b_i\rangle\). Thus
\[
p^*_i=\frac{e^{\langle\lambda,b_i\rangle}}
{\sum_{j\in I_G}e^{\langle\lambda,b_j\rangle}}\quad(i\in I_G).
\]
Consequently
\[
\langle a,\lambda\rangle-\log\sum_{i\in I_G}e^{\langle\lambda,b_i\rangle}
=\sum_{i\in I_G}p^*_i\log p^*_i=-H_*.
\]
If G=K, set x=lambda; the upper bound is attained. Otherwise let v expose G with
\(\langle v,b_i\rangle=c_G\) on G and strictly smaller values outside G. Since \(\langle v,a\rangle=c_G\), evaluating x=lambda+t v and sending t to +infinity deletes precisely the outside-G exponentials, and the log quotient tends to \(-H_*\). This proves the reverse bound, including duplicate exponents and lower-dimensional K.

**Criterion for actual finite attainment.** If the quotient has a finite maximum at x, differentiation of its log gives
\[
a=\frac{\sum_i e^{\langle b_i,x\rangle}b_i}{\sum_i e^{\langle b_i,x\rangle}}.
\]
The weights on *every* b_i are strictly positive, so this barycenter lies in relint K. The converse has already been proved by G=K. No coercive-limit theorem, sequential compactness for potential nets, or interchange of analytic limits is used.

## Exact test models and nonduplicate scope

- b=(0,2), a=1 on the real line: feasible p=(1/2,1/2), so Q=1/2. In Laurent form \(|z|^2/(1+|z|^4)\le1/2\), with equality when \(|z|=1\).
- b=(0,1,2), a=1: the maximizing distribution is uniform on three points, Q=1/3, attained at x=0; the Laurent ratio is \(|z|^2/(1+|z|^2+|z|^4)\).
- b=(0,0,1), a=0: the unique feasible p=(1/2,1/2,0) has entropy log 2, giving Q=1/2, approached as x tends to minus infinity, **never attained**. This tests a boundary face with repeated exponents.
- b=(0,2), a=3: Q=+infinity, agreeing with strict separation.

The original printed proofs of Lemmas 21.11.60 and 21.11.62 correctly establish boundedness **if and only if** convex-hull membership. The new statement is stronger but conditional on exactly the displayed finite family; no original theorem is false, there is no new omission in an original proof, and the two historically distinct but related lemma versions must not be automatically canonicalized together.

**Proposed editorial addition only:** after Lemma 21.11.62, insert the maximum-entropy exact-constant formula, with boundary-face nonattainment and repeated exponents as a short optional remark. Keep all tags, original proofs and source attribution. Potential dependents: future use of Newton-polytope monomial domination and the toric logarithmic-weight inequalities of §§21.11–21.13. No current dependent is identified as invalid. This audit does not certify any full §21.11 theorem chain or all convex Alexandrov results.

**Scope/verification:** Directly inspected the two printed statements, their separation/AM–GM proofs and associated equation in main; hand-verifiable finite-dimensional convex arguments above. Previously sampled §21.11 material is not relogged. Demailly approximation/regularization and the dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programme remain **deferred-by-user**, not resolved or reexamined. No executable tests, project build, CI, formalization or website publication were run. Inventory remains 25 chapters, 747 numbered sections, zero fully certified mathematical sections.
