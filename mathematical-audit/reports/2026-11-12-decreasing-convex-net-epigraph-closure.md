# Decreasing closed convex nets: conjugacy commutes with infima, closure does not

**Finding ID:** POME-CONVEX-DECREASING-CLOSED-EPIGRAPH-GAP-001  
**Date:** 2026-11-12  
**Severity / status:** low / verified conditional deduction. The printed results are **not false**.  
**Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272  
**Integrated reading edition:** docs/sections/convex-functions-and-convex-bodies/index.html, blob 2a123a863642a5a75caa173f0f73aff439a02ea4.  
**Scope:** §21.11, with direct mathematical review of Lemma 21.11.13 (physical lines 112–141), Definition 21.11.15 (143–157), Equation 21.11.23 (214–220), Theorem 21.11.24 (223–231), and the linked Proposition 21.11.16 (158–163) as context. Source labels, in order: sgpt:E17DE993, sgpt:BBDFED14, sgpt:E288ED21, sgpt:1A7E065D, sgpt:B29EAAF0. Corresponding permanent tags: 2F4F518BD56D, 61B746F5E884, E1AD8A1437E2, 258227E5D497, E013E1966E44. The precise source-label and permanent-tag mapping is fixed to the reviewed reading-edition blob.

## Exact general infimum/conjugate identity

Let \(N\) be any finite-dimensional real vector space, \(M=N^*\), and let \((F_i)_{i\in I}\) be any nonempty family of extended-real-valued functions \(F_i:N\to[-\infty,+\infty]\). Write \(F=\inf_i F_i\) pointwise. With the standard extended-real conventions for subtracting \(F_i\) from a finite scalar, for every \(p\in M\),
\[
\boxed{F^*(p)=\sup_{i\in I}F_i^*(p).}
\]
Indeed,
\[
\begin{aligned}
F^*(p)
 &=\sup_{x\in N}\big(\langle p,x\rangle-\inf_i F_i(x)\big)\\
 &=\sup_{x\in N}\sup_{i\in I}\big(\langle p,x\rangle-F_i(x)\big)\\
 &=\sup_{i\in I}\sup_{x\in N}\big(\langle p,x\rangle-F_i(x)\big).
\end{aligned}
\]
The last equality exchanges two *suprema*, not limits of measures, and requires neither a sequence nor compactness. When \((F_i)\) is decreasing and convex, the printed Lemma 21.11.13 additionally ensures that \(F\) is convex. The identity does **not** imply that the pointwise infimum is lower semicontinuous, even if every \(F_i\) is closed and proper.

## A coercive, strictly convex countermodel to closure interchange

Take \(N=M=\mathbb R\), with the standard pairing, and for each integer \(k\ge1\) set
\[
 F_k(x)=
 \begin{cases}
 x^2+e^{-kx},&x\ge0,\\
 +\infty,&x<0.
 \end{cases}
\]
Each \(F_k\) is proper, closed and strictly convex on its effective domain: on \((0,\infty)\) its second derivative is \(2+k^2e^{-kx}>0\), and it is continuous from the right at \(0\). The family decreases pointwise as \(k\) increases. It has a uniform lower bound \(F_k(x)\ge x^2\) on its domain and is **uniformly equicoercive**: for every real \(R\), all \(R\)-sublevel sets are contained in the same compact interval \([0,\sqrt{\max(R,0)}]\).

Nevertheless its pointwise infimum is
\[
 F(x)=\begin{cases}
 +\infty,&x<0,\\
 1,&x=0,\\
 x^2,&x>0.
 \end{cases}
\]
This is a proper convex function, exactly as Lemma 21.11.13 states, but **not closed**: \(\lim_{x\downarrow0}F(x)=0<F(0)=1\). Its lower-semicontinuous convex closure is
\[
 G=\operatorname{cl}F,\qquad
 G(x)=\begin{cases}x^2,&x\ge0,\\+\infty,&x<0.\end{cases}
\]
Thus the closure operator fails to commute with this decreasing infimum, despite uniform equicoercivity:
\[
 \boxed{\operatorname{cl}(\inf_{k}F_k)=G\ne F=\inf_{k}\operatorname{cl}F_k.}
\]
The same phenomenon occurs in a decreasing *net*, because this sequence is itself a directed net. No unsupported sequential-compactness principle is used.

## Direct conjugate and biconjugate calculation

At \(x=0\), \(\langle p,0\rangle-F(0)=-1\). On \(x>0\) the objective is \(px-x^2\), so taking \(x\downarrow0\) for \(p\le0\), or the maximizer \(x=p/2\) for \(p>0\), gives
\[
 \boxed{F^*(p)=G^*(p)=\frac{(\max\{p,0\})^2}{4}.}
\]
This formula also follows from the general infimum/conjugate identity: for fixed \(p\), \(F_k^*(p)\) increases with \(k\), and
\[
 \sup_k F_k^*(p)=
 \sup_{x\ge0}\left(px-x^2-\inf_k e^{-kx}\right)
 = \sup_{x>0}(px-x^2)\vee(-1).
\]
The supremum at \(x=0\) must be handled **separately**, since \(\inf_k e^{-k\cdot0}=1\), not zero. The resulting answer is the displayed \(p_+^2/4\).

Finally,
\[
 F^{**}(x)
 =\sup_{p\in\mathbb R}\left(px-\frac{p_+^2}{4}\right)
 =\begin{cases}x^2,&x\ge0,\\+\infty,&x<0,\end{cases}
 =G,
\]
where for \(x<0\) one lets \(p\to-\infty\), and for \(x\ge0\) the optimum is \(p=2x\). This verifies the conclusion of printed Theorem 21.11.24 **directly for this boundary-discontinuous example**, with no reliance on its external Fenchel proof. It also verifies precisely why replacing that theorem's \(F^{**}=\operatorname{cl}F\) by \(F^{**}=F\) would be incorrect.

## Reading-edition consequence and dependency boundary

- **No source theorem error:** Lemma 21.11.13 asserts convexity, not closedness or preservation of properness. Theorem 21.11.24 correctly includes the closure in its biconjugation identity.
- **Possible optional clarification (not an applied patch):** after Lemma 21.11.13, explicitly warn that decreasing limits of closed proper convex functions can fail to be closed, even with compact common sublevel bounds; after Theorem 21.11.24, retain its closure operator in any downstream limiting argument.
- **Dependents to audit for misuse:** §21.11 closure and Legendre duality (21.11.15–.24), and any toric or Okounkov argument that tries to identify a decreasing limit with its biconjugate without first establishing lower semicontinuity. No such downstream misuse is claimed without direct inspection.
- **Proof status:** all explicit inequalities, conjugates and the sup–sup identity above are proved here. General finite-dimensional Fenchel–Moreau and the linked proof-expansion dependencies are **not** re-certified. Nothing in the excluded Demailly approximation/regularization, Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas, or positivity-loss programme was reopened.
- **Coverage accounting:** direct selected proof-level inspection in previously sampled §21.11; **+0 first-visited numbered sections; +0 fully certified sections**. The last verified table of contents contains 25 chapters and 747 numbered sections.
- **Write discipline:** this is review-only English Markdown. No source/body/registry/tag/main/CI/site modifications.
