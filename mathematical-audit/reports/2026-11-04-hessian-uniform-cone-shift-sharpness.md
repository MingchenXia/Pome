# Sharpness of the scalar Gårding-cone shift in the intermediate Hessian regime

- **Finding:** `POME-HESS-CONE-SHIFT-ASYMPTOTIC-SHARP-001`
- **Date:** 2026-11-04
- **Status:** verified conditional deduction (the original printed Lemma 8.2.3 is correct)
- **Severity:** low; no incorrect mathematical statement or missing proof identified in this target
- **Reviewed production main:** `b6933b772f41b45918f7e25ed1afbbb1fd892272`
- **Actual reading edition:** `docs/sections/complex-hessian-equations--the-admissible-cone/index.html`, blob `925e6109ab7d800cde9bec4b0487842b2e6877a8`, physical lines 43–74 (Lemma 8.2.3 and its entire printed proof); lines 76–100 (the iteration in Lemma 8.2.4); lines 104–124 (coefficient estimate of Lemma 8.2.5).
- **Source and permanent tags:** Lemma 8.2.3 `non-kahler-pluripotential-theory:42B9BB86`, permanent `F86594126C69`; Lemma 8.2.4 `non-kahler-pluripotential-theory:3E489B35`, permanent `94C4E018DD25`; Lemma 8.2.5 `non-kahler-pluripotential-theory:53FFB5F3`, permanent `7710D01DF6F5`.
- **Scope:** the actual analytic chapter assumes `2 <= m < n` in §8.1, tag `CFD38285654D`. The finite-dimensional argument below also holds for `m=n`, as expressly allowed in the algebraic introduction to §8.2. It does **not** extend PDE assertions to `m=1`.

## Exact shift and optimality among uniform multiplicative bounds

Let `2 <= m <= n`, put `k=n-m+1`, and for `L>1` consider the strictly positive spectrum

\[
\lambda(L)=(\underbrace{L,\ldots,L}_{m-1},\underbrace{1,\ldots,1}_{k}).
\]

In particular \(\lambda(L)\in\Gamma_m\). Define the *actual maximal uniform scalar shift*

\[
t_*(\lambda)=\sup\{t\ge0:\lambda-t\mathbf1\in\Gamma_m\}.
\]

**Claim 1: \(t_*(\lambda(L))=1\).** For \(0\le t<1\), every entry of \(\lambda(L)-t\mathbf1\) is strictly positive, hence every elementary symmetric polynomial \(S_j\) with \(j\le m\) is positive. At \(t=1\), precisely \(m-1\) entries are strictly positive and all remaining entries are zero, so \(S_m(\lambda(L)-\mathbf1)=0\); thus this endpoint is outside the open cone. In fact no \(t>1\) can re-enter the open cone. Otherwise for \(\nu=\lambda(L)-t\mathbf1\in\Gamma_m\), the polynomial identity printed in the proof of Lemma 8.2.3 gives

\[
\sigma_m(\nu+x\mathbf1)=\sum_{j=0}^m\binom mj\sigma_j(\nu)x^{m-j}>0\quad(x\ge0)
\]

because all its coefficients, including \(\sigma_0=1\), are positive. Setting \(x=t-1>0\) would instead give \(\sigma_m(\lambda(L)-\mathbf1)=0\), a contradiction. Hence the maximal shift is exactly one, without using any unproved geometric or regularization input.

**Claim 2: the printed lower bound is asymptotically sharp, uniformly over the dimension and Hessian degree.** With \(S_j\) denoting unnormalized elementary symmetric functions, the precise normalization is

\[
 e_m(\lambda)=\frac{\sigma_m(\lambda)}{m\sigma_{m-1}(\lambda)}
  =\frac{S_m(\lambda)}{(n-m+1)S_{m-1}(\lambda)}
  =\frac{S_m(\lambda)}{k S_{m-1}(\lambda)}.
\]

For the spectrum above, elementary counting gives the exact finite polynomials

\[
\begin{split}
S_m(\lambda(L))&=\sum_{p=0}^{m-1}\binom{m-1}p\binom{k}{m-p}L^p
     =kL^{m-1}+O(L^{m-2}),\\
S_{m-1}(\lambda(L))&=\sum_{p=0}^{m-1}\binom{m-1}p\binom{k}{m-1-p}L^p
     =L^{m-1}+O(L^{m-2}).
\end{split}
\]

As usual \(\binom{k}{a}=0\) for \(a<0\) or \(a>k\). Consequently

\[
 \boxed{\quad t_*(\lambda(L))=1,\qquad
 \lim_{L\to\infty}e_m(\lambda(L))=1,\qquad
 \lim_{L\to\infty}\frac{t_*(\lambda(L))}{e_m(\lambda(L))}=1.\quad}
\]

In particular, **no universal multiplicative factor \(C>1\)** can replace \(1\) in the conclusion `0<=t<e_m` of Lemma 8.2.3, even for strictly positive definite matrices and even in the intended intermediate regime \(2\le m<n\). Given such a factor \(C\), choose \(L\) with \(Ce_m(\lambda(L))>1\), and then choose \(1<t<Ce_m\); the proposed strengthened cone inclusion is false.

For each finite \(L\), the original lemma proves the strict inequality \(e_m(\lambda(L))<t_*=1\) when \(m\ge2\), so there is **no claim of equality at finite \(L\)**. The exact gap is not uniformly proportional to \(e_m\). In the particular model \((n,m,L)=(3,2,10)\), the eigenvalues are \((10,1,1)\), \(S_2=21\), \(S_1=12\), \(e_2=21/(2\cdot12)=7/8\), while \(t_*=1\). When \(n=m=2\), \((L,1)\) gives \(e_2=L/(L+1)\) and \(t_*=1\).

**Contrast at the isotropic spectrum.** For \(\lambda=c\mathbf1\), \(c>0\), one has \(e_m=c/m\) but \(t_*=c\). The degree-dependent factor \(m\) at this symmetric point does **not** extend uniformly to general spectra. It is the highly anisotropic family above that prevents a global improvement.

## Review of the printed chain and limits

1. The displayed polynomial and harmonic-reciprocal-root argument on lines 53–71 is consistent with the exact normalization, the endpoint distinction \(m=1\) versus \(m\ge2\), and the anisotropic limiting family. The original lemma is **correct**.
2. The iteration of the one-step shifts in Lemma 8.2.4 (lines 86–99) uses the \((k+1)\)-cone shift and a limit to the displayed endpoint; it is not an assertion that this shift is the spectral exit time. The quantitative mixed wedge estimate therefore survives this audit. Its full algebraic dependency is **not** certified by this isolated model.
3. Lemma 8.2.5 (lines 114–124) applies this mixed bound to the root derivative. Its coefficient estimate and later trace-estimate uses remain **distinct** from a scalar cone-shift improvement. The earlier `POME-HESS-SHARP-DIAGONAL-DERIVATIVE-001` concerns the separate sharp bound on \(F_i\); it is not repeated or reclassified here.
4. The only general external input in the *printed* surrounding section is the declared classical Gårding algebra. The countermodel and sharpness of \(e_m\) above use direct symmetric-polynomial identities and no analytic approximation, Bergman, \(L^2\), Ohsawa–Takegoshi, or excluded regularization argument.

## Proposed integration and affected dependents

An optional, separately reviewable **remark after Lemma 8.2.3** could give the family \((L^{m-1},1^{n-m+1})\) and state that \(e_m\) is asymptotically optimal as a dimension/degree-uniform multiplicative shift bound, although it need not equal the true exit time for any individual spectrum. This is an explanatory strengthening only; no change to statement, proof, historical attribution, tags, source registry, or canonicalization is needed. Relevant downstream results: the scalar-step iteration in Lemma 8.2.4, derivative bounds in Lemma 8.2.5, and trace/gradient estimates in §8.4. None is refuted or fully certified transitively.

**Coverage statement.** Newly established is one exact anisotropic spectral family and its sharp limiting obstruction; examined lines 43–100 and 104–124 with §8.1 standing hypotheses. This is **not** a full verification of §8.2, §8.4, PDE existence, Evans–Krylov, bounded Hessian products, or any other chapter. No project tests or builds were performed. The owner-deferred Demailly regularization programme remains deferred.
