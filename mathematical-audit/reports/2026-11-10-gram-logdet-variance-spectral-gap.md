# 2026-11-10 — Finite-rank Gram logarithmic determinants: variance and a strict spectral gap

**Finding:** `POME-GRAM-LOGDET-VARIANCE-SPECTRAL-GAP-001`  
**Classification:** low / **verified conditional deduction** (an additional finite-dimensional estimate; no printed theorem is refuted).  
**Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`.  
**First proof-level section visit:** §18.34, *The determinant functional*. **No entire section or upstream analytic proof chain is certified.**

## Exact integrated anchors

- `docs/sections/partial-kernels-and-quotient-equilibrium--the-determinant-functional/index.html`, blob `626a4c74bb7f5e6659320052c54ec29902646b61`; section permanent tag `3AC0CF30AE00`.
- Definition of \(\mathcal F_m^{(r)}\), physical lines **10–16**; Proposition **18.34.1**, source `non-kahler-pluripotential-theory:576F8072`, permanent `A1D3D26087E7`, statement lines **20–28**, replacement proof and projection square lines **33–55**.
- Normalized probability and correlation kernel, equations **18.34.15**, **18.34.17**, physical lines **265–293**; Lemma **18.34.16**, source `non-kahler-pluripotential-theory:C7EB694C`, permanent `66CB6C16A6B7`, proof lines **298–305**.
- Proposition **18.34.18**, source `non-kahler-pluripotential-theory:0C4BDB09`, permanent `4920A08E02F1`, lines **314–375**, contains the compatible first-order variation and total-variation estimates; the new result below is *second-order* and is not a restatement of its existing bounds.
- Standing norm and probability measure only: `docs/sections/partial-kernels-and-quotient-equilibrium--selected-spaces-and-partial-bergman-kernels/index.html`, blob `81983c5cf4bb50d5de9006906d9fdab07137e6f4`, §18.30 source hypotheses, physical lines **7–25**. No local kernel estimates or approximation theorems are being audited.

## Precisely scoped statement

Let \(X\) be a **connected** compact complex manifold, \(L\to X\) a holomorphic line bundle with fixed smooth Hermitian metric \(h\), and let \(\nu\) be a smooth probability measure with **strictly positive density**. Fix \(m\ge1\), \(r\ge1\), and a **nonzero**, fixed finite-dimensional subspace \(V_m\subset H^0(X,L^m)\) with \(N=\dim_\mathbb C V_m>0\). It may be the selected space of §18.30; no property of its selection beyond being a fixed holomorphic subspace enters the proof. For \(v\in C(X,\mathbb R)\), use the published weighted norm, Gram determinant functional \(\mathcal F_m^{(r)}\), normalized probability \(\mu_v=B_{m,v}\nu/N\), and Berezin-type operator \(\mathcal Q_v\) of Lemma 18.34.16.

**Claim A (exact polarized curvature).** For every real \(f,g\in C(X)\),
\[
 D^2\mathcal F_m^{(r)}(v)[f,g]
  =-\frac{r!N}{m^{r-1}}\,
       \langle f,(I-\mathcal Q_v)g\rangle_{L^2(\mu_v)}. \tag{A}
\]
In particular the curvature is unchanged by adding a constant to either argument, and
\[
 0\le -\frac{m^{r-1}}{r!N}D^2\mathcal F_m^{(r)}(v)[f,f]
       \le \operatorname{Var}_{\mu_v}(f)
       \le \frac14(\operatorname{osc}_X f)^2. \tag{B}
\]
For two arguments, its absolute value is bounded by
\[
 |D^2\mathcal F_m^{(r)}(v)[f,g]|
 \le \frac{r!N}{m^{r-1}}
   \sqrt{\operatorname{Var}_{\mu_v}(f)
         \operatorname{Var}_{\mu_v}(g)}. \tag{C}
\]

**Claim B (positive spectral gap at each fixed weight).** \(\mathcal Q_v\) is finite rank, and its \(1\)-eigenspace on \(L^2(\mu_v)\) consists **exactly of constants**. Writing
\[
 \lambda_*(m,v,V_m)
   =\sup \sigma\!\left(\mathcal Q_v\bigm|_{\mathbf1^\perp}\right),
\]
we have \(0\le\lambda_*<1\) (the space \(\mathbf1^\perp\) is nonzero for positive-dimensional \(X\)). Thus
\[
 (1-\lambda_*)\,\operatorname{Var}_{\mu_v}(f)
 \le -\frac{m^{r-1}}{r!N}D^2\mathcal F_m^{(r)}(v)[f,f]
 \le \operatorname{Var}_{\mu_v}(f). \tag{D}
\]
When the mean-zero space is trivial, the inequality is tautological and the spectral-gap notation can be omitted. The constants in (D) **depend on the fixed \(m,v,V_m\)**; no uniform-in-\(m\) coercivity is claimed.

**Claim C (sharp upper endpoint).** The coefficient \(1/4\) in the oscillation bound (B) is optimal as a supremum over smooth real test functions, even for a one-dimensional section space on \(X=\mathbb P^1\). The factor \(1\) preceding the variance in (B) is attained for all test functions in the same example.

## Complete finite-dimensional verification

Take an orthonormal basis \(s_1,\ldots,s_N\) for the weighted norm at \(v\) and put \(F_j(x)=e^{-mv(x)/2}\ell_x(s_j)\) in a local unit evaluation, as in physical lines 272–275 of the reading edition. Then \(B_v=\sum_j|F_j|^2\), \(\mu_v=B_v\nu/N\), and the published kernel is \(C_v(x,y)=\sum_j F_j(x)\overline{F_j(y)}\).

For real \(f,g\), the finite sum and Fubini give
\[
 \langle f,\mathcal Q_vg\rangle_{\mu_v}
 =\frac1N\iint f(x)g(y)|C_v(x,y)|^2\,d\nu(x)d\nu(y)
 =\frac1N\sum_{i,j}
      \left(\int f F_i\overline{F_j}\,d\nu\right)
      \overline{\left(\int g F_i\overline{F_j}\,d\nu\right)}. \tag{1}
\]
This expression is real on real arguments and symmetric after summation. In particular \(\mathcal Q_v\) has rank at most \(N^2\), is selfadjoint and positive semidefinite. The first marginal identity in Lemma 18.34.16 gives \(\mathcal Q_v\mathbf1=\mathbf1\). The Markov/Jensen argument there gives \(\|\mathcal Q_v\|_{L^2}\le1\).

In an orthonormal frame, the projection-square formula in the proof of Proposition 18.34.1 (physical lines 40–49) reads
\[
 D^2\mathcal F_m^{(r)}(v)[f,f]
 =-\frac{r!}{m^{r-1}}
     \left\{\sum_j\|fs_j\|_{v}^2
        -\sum_{i,j}|\langle fs_j,s_i\rangle_v|^2\right\}.
\]
Its two terms are respectively \(N\int f^2d\mu_v\) and \(N\langle f,\mathcal Q_v f\rangle_{\mu_v}\) by (1). Polarization proves (A). On mean-zero functions the positive contraction \(\mathcal Q_v\) has spectrum contained in \([0,1]\). Since \(I-\mathcal Q_v\) kills constants, spectral positivity and \(\|I-\mathcal Q_v\|\le1\) give the first inequality in (B) and the covariance bound (C) by Cauchy–Schwarz for the positive form \(I-\mathcal Q_v\). Popoviciu's inequality for any probability measure supplies \(\operatorname{Var}_\mu(f)\le(\operatorname{osc}_X f)^2/4\).

It remains to justify the **strict** gap instead of inferring it merely from nonnegative curvature. Let \(q\in L^2(\mu_v)\) be *real* and satisfy \(\mathcal Q_vq=q\). Equation (A)'s quadratic-form identity, extended from continuous functions to \(L^2(\mu_v)\) by density and the boundedness of all finite-rank terms, gives
\[
 0=N\langle q,(I-\mathcal Q_v)q\rangle_{\mu_v}
    =\sum_j\|(I-P_v)(q s_j)\|_{v}^2. \tag{2}
\]
Indeed, \(\sum_j\|q s_j\|_v^2=N\int|q|^2d\mu_v<\infty\), so all products exist in the ambient weighted \(L^2\). Fix a nonzero \(s=s_j\). Equation (2) says that \(qs=t\) almost everywhere for some holomorphic \(t\in V_m\). On a ball where \(s\ne0\), the holomorphic quotient \(t/s\) is real almost everywhere for the strictly positive volume density, hence real everywhere by continuity and therefore locally constant by the open mapping theorem. The holomorphic identity theorem on connected \(X\) gives \(t=cs\) globally, and \(q=c\) \(\mu_v\)-almost everywhere: the zero locus of a nonzero holomorphic section is \(\nu\)-null. The same applies to real and imaginary parts of any complex fixed point because \(\mathcal Q_v\) preserves real functions. Thus the \(1\)-eigenspace is precisely the constants.

A selfadjoint **finite-rank** contraction has only finitely many nonzero eigenvalues; the remaining spectrum is \(0\). Since \(1\) is simple, its restriction to the orthogonal complement of constants has norm \(\lambda_*<1\), proving (D). This is a fixed-parameter conclusion only: the proof produces **no positive lower bound independent of \(m\), of the weight, or of the choice of the section space**.

For sharpness, let \(X=\mathbb P^1\) with normalized Fubini–Study \(\nu\), take \(L\) trivial, \(V_m=\mathbb C\mathbf1\), and \(v=0\). Then \(N=1\), \(\mu_0=\nu\), and \(\mathcal Q_0f=\int f\,d\nu\); hence
\[
 -\frac{m^{r-1}}{r!}D^2\mathcal F_m^{(r)}(0)[f,f]
    =\operatorname{Var}_\nu(f).
\]
Choose smooth \(f_k\) taking values in \([-1,1]\), tending almost everywhere to \(+1\) on a hemisphere and \(-1\) on its complement, with transitions in shrinking equatorial collars. Dominated convergence gives \(\operatorname{Var}_\nu(f_k)\to1\), while \(\operatorname{osc}_X f_k=2\). Thus the universal oscillation constant \(1/4\) is sharp as a supremum, without claiming attainment by a nonconstant smooth function.

## Verdict, impact, and open boundary

**Verdict:** No incorrect statement was found in the directly inspected finite-dimensional parts of §18.34; Proposition 18.34.1 and Lemma 18.34.16 supply the required identities. The finding is a **verified conditional deduction** (a quantitative new corollary), not a theorem repair. It does not establish the general real-analytic and Gevrey assertions of §§18.34.5–.6, prove the analytic partial-equilibrium limits, or verify the complete source-to-reading-edition dependency chain.

**Proposed text-only correction/addition (not applied):** A short corollary after Lemma 18.34.16 or Proposition 18.34.18 stating (A), (B), (D), with a warning that the spectral gap depends on \(m,v,V_m\). This informs quantitative concavity and perturbation estimates elsewhere in §18.34 without altering Proposition 18.34.18's existing sharp total-variation estimates. No downstream theorem is declared false or certified merely by this addition.

**User-deferred dependencies:** Demailly approximation/regularization and the dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof-completion programme remain **deferred-by-user**. Here the selected subspace and all its norms are fixed and only finite-dimensional Gram and Markov algebra is checked; none of those excluded estimates is reopened. The historical source attribution is retained.

**Precise coverage:** First *selected proof-level* visit to the previously inventory-only **§18.34**; inspected published definition and Propositions 18.34.1, 18.34.18, Lemma 18.34.16 and §18.30 standing norm as context. No whole §18.34 certification; **+1** first numbered-section mathematical proof visit, **+0** complete certifications. Current project inventory remains **25 chapters / 747 numbered sections**. No builds, tests, CI, full formal mathematical verification or publication in this review.
