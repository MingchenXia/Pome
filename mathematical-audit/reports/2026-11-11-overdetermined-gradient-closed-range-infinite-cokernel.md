# 2026-11-11 — Overdetermined elliptic gradient: sharp closed range and infinite-dimensional cokernel

**Stable finding:** \`POME-ELL-OVERDETERMINED-GRADIENT-COKERNEL-001\`  
**Severity:** low. **Status:** **verified conditional deduction**, not a false theorem or a source repair.  
**Reviewed production \`main\`:** \`b6933b772f41b45918f7e25ed1afbbb1fd892272\`.  
**Integrated reading-edition file:** \`docs/sections/differential-operators-and-elliptic-regularity--elliptic-operators-of-arbitrary-order/index.html\`, exact main blob \`24bf19943a31d603485b8e14f63fe05b1f55dd47\`.  
**Provenance:** \`demailly-complex-geometry:90E5290C\` / permanent \`0D76F8A1E29B\`, Lemma 2.18.1 (physical lines 29–58); \`demailly-complex-geometry:5AEC3D70\` / \`DB125476638D\`, Theorem 2.18.3 (lines 122–153); \`demailly-complex-geometry:E1228506\` / \`912C25048C3D\`, Theorem 2.18.4 (lines 155–198). The section heading has tag \`36FFBD062A7E\`.

## Exact theorem and sharp hypothesis boundary

Fix an integer \(m\ge 2\), let \(X=\mathbb R^m/\mathbb Z^m\) with its standard flat metric and probability Lebesgue volume, and consider the scalar-to-one-form first-order operator
\[
D=d:H^{s+1}(X,\mathbb C)\longrightarrow H^s(X,T^*X\otimes\mathbb C),\qquad s\in\mathbb R.
\]
Use the **canonical Fourier Sobolev norms**
\[
\|u\|_{H^t}^2=\sum_{k\in\mathbb Z^m}(1+|k|^2)^t|\widehat u(k)|^2,\quad
\|\alpha\|_{H^t}^2=\sum_k(1+|k|^2)^t|\widehat\alpha(k)|^2,
\]
with \(\widehat u(k)=\int_Xu(x)e^{-2\pi i k\cdot x}\,dx\).

The principal symbol \(i\xi:\mathbb C\to\mathbb C^m\) (or \(2\pi i\xi\) under the Fourier realization) is injective for \(\xi\ne0\). Consequently the injective-symbol hypotheses of the printed Theorem 2.18.3 apply, while the **equal-bundle-rank** hypothesis in Theorem 2.18.4 does not.

For **every real \(s\)** the following exact decomposition holds:
\[
\boxed{
H^s(X,T^*X\otimes\mathbb C)
=\operatorname{Ran}(D)\ \widehat\oplus\ Z^s,\qquad
Z^s=\{\alpha\in H^s: k\cdot\widehat\alpha(k)=0
\text{ for every }k\in\mathbb Z^m\setminus\{0\}\}.
}
\tag{1}
\]
Here the sum is orthogonal in the **specified Fourier \(H^s\) inner product**, not an assertion about all possible equivalent Sobolev norms. Its projection onto \(\operatorname{Ran}(D)\) is the explicit bounded Fourier multiplier
\[
\widehat{\Pi_\parallel\alpha}(k)=
\begin{cases}
\dfrac{k(k\cdot\widehat\alpha(k))}{|k|^2},&k\ne0,\\
0,&k=0.
\end{cases}
\tag{2}
\]
The kernel of \(D\) is the constant functions, its range is closed, but its cokernel is **infinite-dimensional**, containing the mutually independent smooth divergence-free forms \(e^{2\pi i jx_1}\,dx_2\) for every nonzero integer \(j\). Therefore \(D\) is **not Fredholm**, despite being injective-symbol elliptic and enjoying the full-order Sobolev estimate.

More precisely, the following optimal estimate holds with no unmentioned lower-order term:
\[
\boxed{
\|u-\widehat u(0)\|_{H^{s+1}}
\le\frac{\sqrt2}{2\pi}\,\|du\|_{H^s},\qquad s\in\mathbb R.
}
\tag{3}
\]
The coefficient \(\sqrt2/(2\pi)\) is attained by any single Fourier mode of lattice length \(1\), hence is best possible in the specified norms. Thus a uniform coercive estimate **plus finite kernel** does not imply Fredholmness unless one also controls the adjoint/cokernel.

For comparison, when \(m=1\) the same operator has equal bundle ranks, kernel of dimension \(1\), and cokernel consisting only of constant one-forms, also of dimension \(1\): it **is Fredholm of index zero**. The dimension jump from one to two is a concrete sharp boundary of the rank hypothesis.

## Proof by exact Fourier decomposition

The Fourier convention in §2.18 (physical line 7) gives
\[
\widehat{Du}(k)=2\pi i\,k\,\widehat u(k).
\]
For \(k\ne0\), every \(a\in\mathbb C^m\) has the orthogonal splitting
\[
a=\frac{k(k\cdot a)}{|k|^2}
+\left(a-\frac{k(k\cdot a)}{|k|^2}\right),
\]
where the first summand is parallel and the second is orthogonal to \(k\). At \(k=0\), \(Du\) is zero and all constant one-forms belong to \(Z^s\). Because the matrix-valued projection has operator norm at most one independently of \(k\), it defines a norm-one projection on \(H^s\) for each real \(s\). The orthogonal complement \(Z^s\) is consequently closed.

To see that every parallel-frequency field \(\alpha\) with \(\widehat\alpha(0)=0\) lies in the actual range, define
\[
\widehat u(0)=0,\qquad
\widehat u(k)=\frac{k\cdot\widehat\alpha(k)}{2\pi i|k|^2}
\quad(k\ne0).
\]
For every \(k\ne0\),
\[
(1+|k|^2)^{s+1}|\widehat u(k)|^2
\le\frac{1+|k|^2}{(2\pi)^2|k|^2}
(1+|k|^2)^s|\widehat\alpha(k)|^2
\le\frac{2}{(2\pi)^2}(1+|k|^2)^s|\widehat\alpha(k)|^2.
\]
Thus \(u\in H^{s+1}\), and \(Du=\alpha\), proving (1) and a bounded right inverse onto the range.

Applying this same inequality directly to \(\alpha=du\) proves (3). If \(\widehat u(k)\) is supported at \(k=e_1\), then \((1+|k|^2)/|k|^2=2\), giving equality; hence no smaller universal constant is possible. The kernel consists precisely of the zero-frequency scalars.

For every \(j\ne0\), the form \(e^{2\pi i jx_1}dx_2\) is a smooth Fourier mode with wave vector \(je_1\) perpendicular to coefficient vector \(e_2\). It belongs to \(Z^s\) for every \(s\). These infinitely many modes are linearly independent, so \(\operatorname{codim}\operatorname{Ran}D=\infty\). By contrast \(m=1\) forces every nonzero-frequency \(Z^s\) coefficient to vanish and leaves only \(k=0\), a one-dimensional cokernel.

The Fourier calculation is direct and independent of analytic regularization. The compact torus Fourier-series/Plancherel setup and the distinction between injective principal symbols and invertible equal-rank symbols agree with the printed §2.18 conventions; no Demailly approximation, Bergman, \(L^2\)-extension, or positivity-loss programme is used.

## Mathematical disposition and coverage

**Conclusion:** The printed Theorems 2.18.3 and 2.18.4 are **not refuted**. The example explains precisely why one cannot remove *equal bundle ranks* from the Fredholm statement merely because the injective-symbol regularity estimate is available. The difference is an infinite-dimensional adjoint kernel/cokernel, not loss of range closedness, failure of coercivity, or a sign/normalization issue.

**Proposed optional text:** After Theorem 2.18.4, remark that the gradient \(d\) on \(T^m\), \(m\ge2\), has injective symbol and closed range in all Sobolev orders but infinite-dimensional divergence-free cokernel; the equal-rank premise cannot be dropped. This is a proposed annotation only, **not** an edit to the theorem or any permanent tag. Its dependents are interpretations of Theorems 2.18.3–4 and any extension of the Fredholm conclusion to rectangular injective-symbol complexes.

**Previous-work comparison:** The older \`POME-ELL-FREDHOLM-LOWERORDER-001\` in the coverage matrix concerns **index stability under lower-order perturbations** of an already Fredholm equal-rank operator. The present countermodel instead distinguishes **coercive closed range from finite codimension** for an overdetermined operator. It is not a repeated homotopy/index calculation.

**Actually read:** the integrated Fourier norm and compactness proof Lemma 2.18.1, the regularity theorem 2.18.3, and the Fredholm theorem/proof 2.18.4, including the proof's use of the adjoint ellipticity under equal ranks. This is **new selected mathematical verification** in previously partially reviewed §2.18: **0 first numbered-section visits**, **0 fully certified sections**. The actual main ToC remains **25 chapters / 747 numbered sections**. This audit neither reconstructs all global elliptic parametrices nor certifies the upstream general Sobolev or spectral theorem chains.

**External/deferred ledger:** no new external proof input is required for the explicit Fourier model; any upstream Fourier/Plancherel and global parametrix arguments outside this computation remain unverified. All owner-excluded Demailly approximation/regularization and dedicated Bergman, \(L^2\), Ohsawa–Takegoshi, multiscale-atlas and positivity-loss proof work remains **deferred-by-user**, not resolved or certified. No tests, builds, CI, formalization, website publication, source/main/registry/canonicalization/tag edits were performed.
