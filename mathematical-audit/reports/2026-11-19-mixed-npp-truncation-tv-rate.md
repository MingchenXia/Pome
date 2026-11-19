# Exact total-variation convergence rates for canonical mixed non-pluripolar truncations

**Date:** 2026-11-19. **Reviewed production main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **New finding:** POME-NPP-MIXED-TRUNCATION-TV-RATE-001 (**low / verified conditional deduction**, not a printed false theorem or proof repair). **Integrated source:** docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, **whole directly read section**, mathematical lines 7–165. Primary anchors: Lemma 13.2.2, source foundations-of-pluripotential-theory:CE1D6DA5, permanent D59675D9F6D8, lines 35–53 (and Eq. 13.2.3 source F86748C9, permanent E88E33ACAD5B, lines 36–40); Example 13.2.9, source 2F8E45A2, permanent 6F4C920FEDCA, lines 151–165.

**Prior-art reconciliation is essential.** The mixed power-logarithmic psh family, its exact mixed density, the condition a+b<1, the cylinder mass formula, and the finite-mixed/infinite-self example were **already established** in the 2026-11-11 report **POME-NPP-MIXED-POWER-SUM-THRESHOLD-001** (reports/2026-11-11-mixed-nonpluripolar-power-sum-threshold.md). The 2026-10-30 report **POME-NPP-POWER-SINGULARITY-THRESHOLD-001** covered the diagonal a=b family. These are **existing results, not new findings on November 19**. This report proves a different result: the **exact rate with respect to the canonical level k** in Lemma 13.2.2, including quantitative total-variation convergence, the exact critical logarithmic coefficient, and the supercritical polynomial growth rate.

## Statement

Let \(0<a,b<1\), \(R^2<\min(1-a,1-b)\), and \(U=\{|x|<R,\ |y|<e^{-1}\}\subset\mathbb C^2\). Set \(L=-\log|y|\), \(u_c(x,y)=(|x|^2-1)L^c\) for y≠0 and \(u_c(x,0)=-\infty\), \(c=a,b\). These are psh by the proof already recorded on November 11. Let \(O_k=\{u_a>-k,u_b>-k\}\), and let \(S_k\) denote precisely the canonical **mixed** Bedford–Taylor truncation \(1_{O_k}dd^c\max(u_a,-k)\wedge dd^c\max(u_b,-k)\) of Lemma 13.2.2.

Put \(m=\max(a,b)\), \(A=a(1-a)+b(1-b)\), \(B=A+2ab\), and fix a cylinder \(K_{\rho,T}=\{|x|\le\rho,\ |y|\le e^{-T}\}\), where \(0<\rho<R\), \(T>1\). All mass and total-variation norms below refer to the convention \(dd^c=(i/2\pi)\partial\bar\partial\).

**Subcritical a+b<1.** The limiting non-pluripolar measure \(\mu=\langle dd^cu_a\wedge dd^cu_b\rangle\) exists and is locally finite, and for **every integer k>T^m** its exact positive **total-variation tail** on K is

\[
\boxed{
\left\|\mathbf1_K(\mu-S_k)\right\|_{\mathrm{TV}}
=C_{a,b,\rho}\,k^{-(1-a-b)/m},
\qquad
C_{a,b,\rho}
=\frac{1}{2\pi(1-a-b)}
\int_{|x|\le\rho}
\bigl(A-B|x|^2\bigr)(1-|x|^2)^{(1-a-b)/m}\,dA_x>0.
}\tag{TV}
\]

Thus the sharp canonical truncation exponent is precisely \((1-a-b)/\max(a,b)\), and there is **no hidden little-o improvement** for these examples. For \(a=3/4,b=1/8\) and \(R^2<1/4\), the exponent is \(1/6\), even though the first self-product is not locally finite.

**Critical a+b=1.** Though there is no locally finite limit, the canonical level-k mass has the precise growth, for k>T^m,

\[
\boxed{S_k(K_{\rho,T})
=\frac{\log k}{2\pi m}\int_{|x|\le\rho}(A-B|x|^2)\,dA_x
-\frac{1}{2\pi}\int_{|x|\le\rho}(A-B|x|^2)
 \left[\frac{\log(1-|x|^2)}{m}+\log T\right]\,dA_x.}\tag{C}
\]

In particular the logarithmic leading coefficient is strictly positive.

**Supercritical a+b>1.** For k>T^m we have the exact identity

\[
\boxed{
S_k(K_{\rho,T})
=\frac{k^{(a+b-1)/m}}{2\pi(a+b-1)}
\int_{|x|\le\rho}(A-B|x|^2)(1-|x|^2)^{-(a+b-1)/m}\,dA_x
-\frac{T^{a+b-1}}{2\pi(a+b-1)}
\int_{|x|\le\rho}(A-B|x|^2)\,dA_x.
}\tag{S}
\]

The leading coefficient is strictly positive. The boundary between these three regimes is **the previously established threshold**, not a new discovery.

## Proof of the new k-dependent identities

The already verified smooth mixed wedge density outside the pole axis is

\[
d\mu=\frac{A-Bq}{4\pi^2|y|^2}L^{a+b-2}\,dA_xdA_y,\qquad q=|x|^2.
\]

This equality is valid as the increasing trace-measure limit even when a+b≥1; one must not describe that infinite trace measure as a locally finite current.

For every \(L>1\), both u_a and u_b are negative and

\[
u_a>-k,\ u_b>-k
\quad\Longleftrightarrow\quad
(1-q)L^{\max(a,b)}<k
\quad\Longleftrightarrow\quad
L<U_k(q):=\left(\frac{k}{1-q}\right)^{1/m}.
\tag{O}
\]

The reduction to **max(a,b)** is the key additional observation not present in the November 11 threshold proof. For k>T^m and q≤rho² we have U_k(q)>T, so truncation restricts the polar logarithmic coordinate **exactly** to T≤L<U_k(q) over K. By Bedford–Taylor plurifine locality the canonical S_k is the smooth wedge density on O_k and zero off it. The y-plane polar-coordinate identity gives, for every nonnegative integrand,

\[
\int_{\{|y|\le e^{-T},\,L<U_k(q)\}}
\frac{L^{a+b-2}}{|y|^2}\,dA_y
=2\pi\int_T^{U_k(q)} t^{a+b-2}\,dt.
\]

Therefore the exact canonical mass, without an asymptotic approximation, is

\[
S_k(K_{\rho,T})=\frac1{2\pi}\int_{|x|\le\rho}
(A-Bq)\left[\int_T^{U_k(q)}t^{a+b-2}\,dt\right]dA_x.
\tag{I}
\]

If a+b=1, evaluate the inner integral as log U_k(q)-log T and substitute \(\log U_k(q)=[\log k-\log(1-q)]/m\), obtaining (C). If a+b>1, integrate the power to obtain (S), with \(U_k(q)^{a+b-1}=k^{(a+b-1)/m}(1-q)^{-(a+b-1)/m}\).

For a+b<1, the NPP limit \(\mu\) is finite on K, and **Lemma 13.2.2 gives the stronger Borel equality** \(S_k=\mathbf1_{O_k}\mu\). In top bidegree these are positive measures, so the total-variation norm of the difference equals its mass. Using (O) and the full tail \(L\ge U_k(q)\),

\[
\begin{aligned}
\|\mathbf1_K(\mu-S_k)\|_{\rm TV}
&=\frac1{2\pi}\int_{|x|\le\rho}(A-Bq)
\int_{U_k(q)}^\infty t^{a+b-2}\,dt\,dA_x\\
&=\frac1{2\pi(1-a-b)}k^{-(1-a-b)/m}
\int_{|x|\le\rho}(A-Bq)(1-q)^{(1-a-b)/m}\,dA_x.
\end{aligned}
\]

This proves (TV). Every coefficient is finite and strictly positive because the psh Hessians are strictly positive for q<R²<min(1-a,1-b). Exact equality for every sufficiently large k proves sharpness; no sequence/subsequence compactness, illicit interchange of measures, or extension of local finiteness into the a+b≥1 regimes was used.

## Broader direct proof review and status

During this run **every mathematical paragraph of integrated §13.2 (lines 7–165)** was directly checked: truncation/Borel/plurifine setup (7–16), Lemma 13.2.1 Borel restriction of positive currents (20–27, permanent 6632853A40C9), Lemma 13.2.2 increasing traces, total-variation convergence and zero polar mass (35–53), Definition 13.2.4 (58–63), Proposition 13.2.5 strong positivity (67–76), Proposition 13.2.6 current invariance, locality, additivity, homogeneous scaling (81–125), coordinate comparison and chart gluing (129–148), and Example 13.2.9 (151–165). No new confirmed printed error or independent proof gap was found. The earlier selected Nov 11 §13.2 review is **not** recounted as a fresh mathematical threshold discovery.

**Severity/status:** low / verified conditional deduction, only for (TV), (C), (S). The prior threshold and density are conditional inputs already recorded. **Proposed addition:** an optional quantitative convergence-rate remark after Lemma 13.2.2 or Example 13.2.9; not a correction to printed mathematics. **Dependents:** §13.3 cutoff-gradient limits, §13.5 global finiteness comparisons and §13.13 non-pluripolar product approximation can use this as a sharp obstruction to an unjustified uniform rate. In general one **cannot infer** this exponent for arbitrary psh singularities.

**Uncertified upstream dependencies:** complete §7.2 Bedford–Taylor products, §5.47 plurifine locality, §5.3 coefficient bounds, §5.11 extension across polar sets. No full upstream proof-chain certification, no project tests, builds or CI. User-excluded Demailly regularization and dedicated Bergman/L²/Ohsawa–Takegoshi/multiscale-atlas/positivity-loss programme remains **deferred-by-user**, not resolved/certified. The source, registry, permanent tags, main and published website were not changed.