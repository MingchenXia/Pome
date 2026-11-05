# 2026-11-06 — independent polyannular Laurent proof and an inverse-character inference slip

**Production main inspected:** b6933b772f41b45918f7e25ed1afbbb1fd892272.
**Integrated reading edition:** docs/sections/convex-analysis-and-toric-potentials--fans-divisors-and-character-sections/index.html, blob 7ad2e6dbdd0ce59e1bf08cd9cb3c046e8c87ff6c.
**Actual new scope:** Lemma 21.9.4, statement and proof at physical lines 112–136; Theorem 21.9.5, only its torus-action proof step at physical lines 153–166 (especially 166). The adjacent fan/orbit material 21.9.1–3 and theorem's other steps are *context*, not fully re-certified.

**Stable identities:** Lemma 21.9.4 = foundations-of-pluripotential-theory:D75B0BB2 / permanent 00432B20A966. Theorem 21.9.5 = foundations-of-pluripotential-theory:BD98CC5B / permanent 69D3D97E7701. The chart construction invoked in §21.9.5 is Theorem 21.8.3, foundation source 0F7315B0 / permanent E49F0370E203.

## POME-TORIC-LAURENT-ANNULAR-CAUCHY-001

**Classification:** low / verified conditional deduction (complete replacement *of the selected Laurent-series step*, conditional only on elementary annular Cauchy integral formula; **not** a claim that the printed lemma is false, an obligatory repair, or that all of §21.9 is certified).

For every holomorphic \(f\) on \((\mathbb C^*)^n\), define for \(m\in\mathbb Z^n\)
\[
c_m=\frac{1}{(2\pi i)^n}\int_{|\zeta_1|=r_1}\cdots\int_{|\zeta_n|=r_n}
f(\zeta)\prod_{j=1}^n\zeta_j^{-m_j-1}\,d\zeta_j .
\]
Each contour has positive orientation. Cauchy's theorem applied one variable at a time on the intervening annuli makes \(c_m\) independent of every \(r_j>0\). Parametrizing the contours recovers exactly the \((2\pi)^{-n}r^{-m}e^{-i\langle m,\theta\rangle}\) coefficient of printed Lemma 21.9.4, with no missing \(2\pi\) or sign.

**Direct reconstruction without citing a one-variable Laurent series theorem.** Fix a compact set \(K\subset(\mathbb C^*)^n\); choose \(0<a_j\le |z_j|\le b_j<\infty\) for all \(z\in K\), and set \(r_j^-=a_j/2,\ r_j^+=2b_j\). Each coordinate of a point \(z\in K\) lies strictly inside the annulus \(r_j^-<|z_j|<r_j^+\). Repeated *annular Cauchy formulas* give
\[
f(z)=\frac{1}{(2\pi i)^n}
\int_{\partial A_1}\cdots\int_{\partial A_n}
\frac{f(\zeta)}{\prod_j(\zeta_j-z_j)}\prod_jd\zeta_j,
\]
where each \(\partial A_j\) is the positively oriented outer circle **minus** the counterclockwise inner circle. On the outer circle use
\[
(\zeta_j-z_j)^{-1}=\sum_{q\ge0}z_j^q\zeta_j^{-q-1};
\]
on the inner circle use
\[
(\zeta_j-z_j)^{-1}=-\sum_{q\ge0}\zeta_j^qz_j^{-q-1}.
\]
The second minus sign cancels the *negative boundary orientation* of the inner component. The resulting sum over all \(2^n\) choices of inner/outer contours has a term \(c_mz^m\) for every \(m\in\mathbb Z^n\), the contour for coordinate \(j\) chosen outer if \(m_j\ge0\), inner if \(m_j<0\). Contour invariance identifies that integral with the original \(c_m\). Thus \(f(z)=\sum_m c_mz^m\) pointwise.

For normal convergence let \(C_K\) be the maximum of \(|f|\) on the \(2^n\) mixed product tori with radii \(r_j^\pm\). Choosing the same contours by the signs of \(m_j\) gives the **uniform** estimate
\[
|c_mz^m|\le C_K\prod_{j=1}^n
\begin{cases}(|z_j|/r_j^+)^{m_j},&m_j\ge0,\\
(r_j^-/|z_j|)^{-m_j},&m_j<0,\end{cases}
\le C_K2^{-\sum_j|m_j|}.
\]
Therefore \(\sup_K\sum_m|c_mz^m|\le 3^nC_K\). This justifies every exchange of sums and contour integrals above, uniformly on \(K\); the proof is not based on sequential compactness or an unproved interchange of limits. The coefficients are unique by integrating a normally convergent series termwise against the character \(e^{-i\langle m,\theta\rangle}\) on a fixed product torus. If \(f\) extends holomorphically to \(\mathbb C^n\) and \(m_j<0\), then \(\zeta_j^{-m_j-1}\) is a nonnegative integral power, so the \(j\)-contour integral vanishes by Cauchy's theorem. Thus the support is \(\mathbb Z_{\ge0}^n\) and the last clause of the lemma follows directly, *without* invoking a multivariate Taylor series.

**Dependency accounting:** elementary one-variable Cauchy theorem / annular integral formula remains a classical analytic input. This proof removes reliance on a separately quoted *one-variable Laurent series theorem* in the printed line 131. It does not independently verify §21.8.3 charts, §21.7.3 lattice counting, or global toric section reconstruction. The full printed Lemma 21.9.4 is correct under its stated hypotheses.

## POME-TORIC-ACTION-INVERSE-INFERENCE-001

**Classification:** low / confirmed error in **proof exposition only** (a missing inverse-character substitution, *not* an incorrect theorem statement, divisor sign, representation weight, or false final equality).

The proof of Theorem 21.9.5 at physical line 156 defines \(s_0=\chi^{-v}s_v\). At line 166 it correctly says that the coordinate frame \(s_v\) has section-action weight \(\chi^{-v}(\tau)\), but it then explains invariance of \(s_0\) using the transformation of the **opposite** function \(\chi^{v}\):
\[
(\tau\cdot\chi^{v})(z)=\chi^{-v}(\tau)\chi^{v}(z).
\]
This identity is true **for \(\chi^v\)** but does *not* directly imply invariance of \(\chi^{-v}s_v\). The required transformation is
\[
(\tau\cdot\chi^{-v})(z)=\chi^{v}(\tau)\chi^{-v}(z),
\quad
\tau\cdot(\chi^{-v}s_v)=\chi^v(\tau)\chi^{-v}\cdot\chi^{-v}(\tau)s_v=s_0.
\]
Only then does the final printed conclusion, that \(\chi^m s_0^k\) has weight \(\chi^{-m}\), follow in the stated proof. Thus the **result is correct** and its sign is correct; the *particular displayed justification* cites the wrong exponent.

**Concrete exact test.** For \(P=[0,1]\) on \(\mathbb P^1\), choose vertex \(v=1\), dense coordinate \(z=Z_1/Z_0\), frame \(s_1=Z_1\), and \(s_0=z^{-1}s_1=Z_0\). The diagonal torus action gives \(\tau\cdot s_1=\tau^{-1}s_1\) and \(\tau\cdot z^{-1}=\tau z^{-1}\), so \(s_0\) is invariant. In contrast, \(z\) has weight \(\tau^{-1}\) and would produce weight \(\tau^{-2}\) if combined with \(s_1\). This explicitly pinpoints the missing inversion, with no change to the printed theorem.

**Proposed minimal source/body *patch for later separate review*, not applied here:** In the proof sentence at line 166 replace “it maps the function \(\chi^{v}\) to \(\chi^{-v}(\tau)\chi^{v}\); therefore it fixes \(s_0\)” by “it maps the function \(\chi^{-v}\) to \(\chi^{v}(\tau)\chi^{-v}\); therefore it fixes \(s_0\).” Preserve all permanent labels and source history.

**Dependents:** direct readability of the character decomposition/contragredient torus weight in §21.9.5, and subsequent uses of this equivariant convention. The earlier audit POME-TORIC-POLYTOPE-TRANSLATION-WEIGHTS-001 (2026-11-02) already checked the *correct weights* under translated polytopes; the present item is a distinct text-local inference defect, **not** a relabeling or repetition of that result.

## Exact coverage, status and exclusions

First substantive *full selected proof* of the elementary analytic Lemma 21.9.4, plus a specific unambiguous proof-exposition sign check in 21.9.5. §21.9 already had prior partial audits; no new whole-section certification. The 25-chapter/747-section inventory is unchanged and **zero complete mathematical-section certificates** are claimed. Previous errors, proof gaps, external dependencies, duplicate analyses and deferred classifications are unaffected. Demailly approximation/regularization and its dedicated Bergman, weighted-L2, Ohsawa–Takegoshi, multiscale atlas and positivity-loss completion programme remain strictly **deferred-by-user**. No source, main, canonicalization, registry, permanent tag, build, formalization, CI or website edit was performed.
