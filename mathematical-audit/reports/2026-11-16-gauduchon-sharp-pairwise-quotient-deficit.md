# 2026-11-16 — A sharp unconditional anisotropy deficit for the Gauduchon quotient

**Stable finding ID:** POME-GAUD-QUOTIENT-SHARP-PAIRWISE-ANISOTROPY-001. **Severity:** low. **Status:** verified conditional deduction (a new quantitative consequence); the printed theorem is correct. **Not** a confirmed error or a printed proof gap.
**Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Reading-edition file:** docs/sections/a-gauduchon-variational-volume--the-quotient-and-the-smooth-equation/index.html, blob 9ec67161d46b3ba20afa1b1c9a0c84f29322763e.
**Section:** 12.2, permanent tag \`43BF29E33E59\`, source variant \`non-kahler-pluripotential-theory\`.
**Target:** Definition 12.2.1, source label \`non-kahler-pluripotential-theory:6E1DBC11\` / permanent \`0C4AF7E2CEBB\`, physical lines 16–21; Theorem 12.2.3, source label \`non-kahler-pluripotential-theory:876DF057\` / permanent \`2DB664A6EFDF\`, lines 58–80 (matrix AM–GM at 69–75, conformal equality and uniqueness at 77). Proposition 12.2.2, source \`non-kahler-pluripotential-theory:CEFAD6D9\` / permanent \`4AF37F3C8091\`, lines 25–45, supplies the definition's ambient cone.
**Adjacent dependents:** Theorem 12.3.1 (source \`non-kahler-pluripotential-theory:6B1A74F2\`, permanent \`2220E0C47510\`), Proposition 12.3.2, and the second-variation Proposition 12.4.1 are compared only as downstream context, not recertified.

## Statement, including all normalizations

Let \(X\) be a connected compact complex manifold of complex dimension \(n\ge 2\), \(\mu\) a smooth strictly positive volume form, and \(\theta\in\mathscr P\) a smooth real \((1,1)\)-background admitting a positive smooth representative. Assume the **existing** smooth Monge–Ampère theorem used in §12.2.3, so that
\[
 \Omega=\theta+dd^c u>0,\qquad \Omega^n=c\,\mu,\qquad c>0.
\]
Let \(\gamma>0\) be **any smooth Gauduchon metric** (\(dd^c\gamma^{n-1}=0\)), not necessarily close to a minimizer. Write \(a_1(x),\dots,a_n(x)>0\) for the eigenvalues of the Hermitian endomorphism \(\gamma^{-1}\Omega\), and put
\[
 g=(a_1\cdots a_n)^{1/n},\qquad
 r_i=\frac{a_i}{g},\qquad \prod_i r_i=1,\qquad
 \mathcal A_\gamma(x)=\sum_{1\le i<j\le n}(\sqrt{r_i}-\sqrt{r_j})^2.
\]
The expression \(\mathcal A_\gamma\) is independent of the ordering of eigenvalues and invariant under pointwise conformal rescaling of \(\gamma\). Define the smooth probability measure
\[
 d\sigma_\gamma=
 \frac{(\mu/\gamma^n)^{1/n}\gamma^n}
 {\int_X(\mu/\gamma^n)^{1/n}\gamma^n}.
\]
The quotient in Definition 12.2.1 has the **dimension-sharp global stability estimate**
\[
 \boxed{
 \frac{\int_X\theta\wedge\gamma^{n-1}}
 {\int_X(\mu/\gamma^n)^{1/n}\gamma^n}
 -c^{1/n}
 \;\ge\;
 \frac{c^{1/n}}{n(n-1)}
 \int_X\mathcal A_\gamma\,d\sigma_\gamma.}
 \tag{A}
\]
The coefficient \(1/[n(n-1)]\) is **best possible**, even with \(X\) a flat complex torus and \(\Omega,\gamma\) constant-coefficient Kähler forms. For \(n=2\) equation (A) is an **identity for every** \(\gamma\); for \(n\ge3\) equality in (A) holds only when \(\gamma\) is pointwise conformal to \(\Omega\), hence (among Gauduchon metrics) a positive constant multiple of the unique Gauduchon representative in that conformal class. Consequently a quotient deficit tending to zero forces the *weighted conformal-anisotropy energy* in (A) to tend to zero. **No unweighted norm convergence, uniform pointwise ellipticity, or singular-potential result is asserted.**

## Direct proof without any regularization programme

At each point, diagonalizing \(\Omega\) relative to \(\gamma\) yields the identity
\[
 \frac{\Omega\wedge\gamma^{n-1}}{\gamma^n}
 =\frac1n\sum_{i=1}^n a_i
 =g\,\frac1n\sum_i r_i.
\]
The standard determinant volume comparison is exactly
\[
 g\,\gamma^n=(\Omega^n/\gamma^n)^{1/n}\gamma^n
 =c^{1/n}(\mu/\gamma^n)^{1/n}\gamma^n.
\]
For arbitrary positive real numbers \(r_i\) with \(\prod_i r_i=1\), the pairwise identity gives
\[
 \begin{aligned}
 \frac1n\sum_i r_i-1
 &-\frac{1}{n(n-1)}\sum_{i<j}(\sqrt{r_i}-\sqrt{r_j})^2\\
 &=\frac{2}{n(n-1)}\sum_{i<j}\sqrt{r_i r_j}-1 \ \ge\ 0.
 \end{aligned} \tag{B}
\]
Indeed, each index occurs in precisely \(n-1\) pairs, so the **geometric mean of all \(\binom n2\) numbers \(\sqrt{r_i r_j}\) is exactly one**; their arithmetic mean is at least one. This is a finite-dimensional arithmetic–geometric mean argument, not a limiting/compactness statement.

Multiplying (B) by \(g\,\gamma^n\), integrating, and using \(dd^c\gamma^{n-1}=0\) and smooth Stokes,
\[
 \int_X\Omega\wedge\gamma^{n-1}
 =\int_X\theta\wedge\gamma^{n-1},
\]
yields (A) after division by the positive denominator. The existing Theorem 12.2.3 identifies \(c^{1/n}\) with the minimum of the quotient, conditional on its smooth Monge–Ampère and Gauduchon-representative inputs.

When \(n=2\), (B) has one pair, whose geometric mean is identically one, proving the exact identity. If \(n\ge3\), equality in the arithmetic–geometric mean of pair products requires every \(\sqrt{r_i r_j}\) to be equal; comparing pairs with a common index forces all \(r_i\) to agree. Their product is one, hence \(r_1=\dots=r_n=1\). Thus the exact lower-bound equality case is pointwise conformity; the uniqueness clause of §12.2.3 then yields the Gauduchon minimizer statement, with its Gauduchon uniqueness prerequisite explicitly retained.

## Best-possible constant inside the admissible geometric class

Take \(X=\mathbb C^n/(\mathbb Z^n+i\mathbb Z^n)\) and any constant-coefficient diagonal Kähler form \(\Omega\), rescaled so \(\int_X\Omega^n=1\). Set \(\theta=\Omega\) and \(\mu=\Omega^n\), hence \(c=1\). For \(t>1\), take the *constant coefficient* Kähler metric \(\gamma_t\) with relative eigenvalues
\[
 (r_1,\ldots,r_n)=
 (t^{2(n-1)},t^{-2},\ldots,t^{-2}).
\]
Their product is one, so \(g=1\), and every \(\gamma_t\) is smooth, closed, and Gauduchon. Both \(d\sigma_{\gamma_t}\) and \(\mathcal A_{\gamma_t}\) are constant across the torus. Directly,
\[
 \begin{aligned}
 Q_t-c^{1/n}
 &=\frac{t^{2(n-1)}+(n-1)t^{-2}}{n}-1,\\
 \mathcal A_{\gamma_t}
 &=(n-1)(t^{n-1}-t^{-1})^2.
 \end{aligned}
\]
Therefore
\[
 \lim_{t\to\infty}
 \frac{Q_t-c^{1/n}}{\int\mathcal A_{\gamma_t}\,d\sigma_{\gamma_t}}
 =\frac1{n(n-1)}.
\]
No larger universal coefficient can replace that in (A). When \(n=2\), equality already holds for every \(t>1\). This sharpness is not merely formal matrix algebra: all metrics, volume forms and potentials meet the actual hypotheses of the printed quotient theorem.

## Classification and scope

The printed Theorem 12.2.3 and Proposition 12.2.2 are **not refuted**: (A) strengthens their finite-dimensional AM–GM step by an explicit quantitative defect, without replacing the original equality-case proof. The only conditional inputs are the **already integrated** smooth equation \(\Omega^n=c\mu\) (Theorem 14.2.1) and the existence/uniqueness of the conformal Gauduchon representative (Theorem 11.4.2); this report does **not** certify those theorems or their downstream claims. No Demailly approximation, Bergman kernel, \(L^2\) extension, Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof was examined.

**Proposed correction:** no source theorem correction. Optionally add (A) as a separately reviewed quantitative remark after the AM–GM proof in §12.2.3, preserving both permanent/source tags. **Affected dependents:** quantitative near-minimizer statements in §§12.3–12.4 may use the weighted energy, but no derivative or Hessian claim is certified here. **Coverage:** newly inspected the actual integrated Def. 12.2.1, Proposition 12.2.2, Theorem 12.2.3, their precise normalization/Stokes/equality steps, and the already printed downstream §12.3.1 statement as context. §12.2 was previously partially audited: **+0 first-visited numbered sections, +0 whole-section certifications**; 25 chapters / 747 numbered sections in the current main ToC. No source/body, registry, tags, build, CI, or website changes.
