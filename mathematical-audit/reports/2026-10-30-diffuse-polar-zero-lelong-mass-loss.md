# Diffuse polar mass loss with zero Lelong numbers and smooth strictly positive approximants on the projective line

- **Stable finding ID:** POME-NPP-DIFFUSE-POLAR-SMOOTH-MASS-001.
- **Severity/status:** low / **verified conditional deduction**. This is a fully calculated model consequence of the definitions, **not** a false printed theorem, general proof repair, or complete upstream certification.
- **Production main reviewed:** b6933b772f41b45918f7e25ed1afbbb1fd892272 (30 October 2026).
- **Scope:** non-pluripolar degree-one products, extended-capacity convergence, Lelong numbers, and the boundary of weak continuity. No Demailly approximation/regularization, Bergman, L2, Ohsawa–Takegoshi, multiscale atlas, or positivity-loss proof-completion work was examined or reopened. All earlier related entries remain at their historical statuses.

## Exact integrated reading-edition anchors

1. **Definition 13.2.4**, source label foundations-of-pluripotential-theory:9D8E4DD8, permanent tag D79952D7E272: docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, main blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, physical lines 8–13, 34–40, 57–63. Its restricted Bedford–Taylor truncations discard all mass on the common pole set.
2. **Lemma 13.7.3**, source label foundations-of-pluripotential-theory:4720F1AB, permanent tag 274B700496A8: docs/sections/non-pluripolar-products--capacity-convergence-and-loss-of-mass/index.html, main blob d66813856cb813722806ab912afdfd4815d2da97, lines 41–66. Decreasing psh sequences converge in extended capacity.
3. **Theorem 13.7.5**, source label foundations-of-pluripotential-theory:AB4EBE3B, permanent tag 67C4F7EC316E: same §13.7 file/blob, lines 106–135. It asserts lower mass semicontinuity and requires non-loss of mass for its weak-convergence conclusion. **Example 13.7.6**, source label foundations-of-pluripotential-theory:D5678E03, permanent tag ACAEA8D8BE87, same file/blob, lines 138–140, already treats the *atomic* current [0].
4. **Example 13.11.8**, source label sgpt:B002DC9E, permanent tag 00950EDCBA2C: docs/sections/non-pluripolar-products--the-non-pluripolar-products/index.html, blob 054a7661c855824b86eb749e211fc3da88a599de, lines 101–114, states the degree-one formula with the pole-set indicator.
5. **Theorem 13.8.7**, source label foundations-of-pluripotential-theory:6A80B686, permanent tag 60DE4F681F75: docs/sections/non-pluripolar-products--mass-comparison-and-projective-fibers/index.html, main blob dd89e44c511fd6f6bdd164a09a77c1637c42b410, lines 217–244. The ordered-mass conclusion is a compatibility check only. Its reference-potential existence step in Proposition 13.8.5, line 212, cites excluded §6.17.1; that **dependency stays deferred-by-user**, and is not needed here.

## Precisely stated model

Use the normalization dd^c = (i/2π) ∂∂̄ and let ω = dd^c log(1+|z|²) on the affine chart of X = P¹, so that ∫_X ω = 1. For j≥1 put

\[
a_j=\exp(-4^j),\qquad
K=\left\{\sum_{j=1}^{\infty}\varepsilon_j a_j:\varepsilon_j\in\{0,1\}\right\}\subset[0,1/50].
\]

Let μ be the image of the independent unbiased Bernoulli product probability on {0,1}^N under this map. Define

\[
u(z)=\int_K\log\frac{|z-w|^2}{1+|z|^2}\,d\mu(w),\qquad
u_\delta(z)=\int_K\log\frac{|z-w|^2+\delta}{1+|z|^2}\,d\mu(w)
\quad(\delta>0).
\]

Then:

1. μ is non-atomic, K is compact and polar, and u = −∞ at **every** point of K; nevertheless u is a legitimate, nontrivial ω-psh function on P¹, with
   \[
   T=\omega+dd^cu=\mu,\quad T(X)=1,\quad \nu(u,x)=0\ \text{for every }x\in X.
   \]
2. Every u_δ is globally smooth and ω-psh, and T_δ=ω+dd^c u_δ is **strictly positive everywhere**, with T_δ(X)=1 and vanishing Lelong numbers everywhere.
3. As δ↓0, u_δ decreases pointwise to u and converges in L¹ and in extended capacity; T_δ tends weakly to μ. Despite this,
   \[
   \langle T_\delta\rangle=T_\delta,\qquad
   \int_X\langle T_\delta\rangle=1,\qquad
   \langle T\rangle=0,\quad\int_X\langle T\rangle=0.
   \]
   Hence the precise non-pluripolar mass defect is 1, **although the limit and every approximant have identically zero Lelong numbers**.
4. More strongly, the ordinary measures do not converge in total variation: μ(K)=1 while T_δ(K)=0, so the total variation norm of T_δ−μ, in the convention sup over test functions bounded by 1, is exactly 2.

## Self-contained proof

**Compact non-atomic polar support.** For every j≥1 the sum of all later a_i is less than a_j/2, by superexponential decay. Thus a first differing binary digit makes two expansions distinct. A cylinder specified by its first k digits has μ-mass exactly 2^{-k}. The diameter of such a cylinder is at most

\[
r_k:=\sum_{j>k}a_j\le 2\exp(-4^{k+1}).
\]

The whole K has diameter less than 1/50 (a_1=e^{-4} and the next term is e^{-16}). A singleton lies in one cylinder at each level, so μ({x})≤2^{-k} for all k: μ is non-atomic. Fix z∈K, and let C_k(z) denote its level-k cylinder. Because log|z-w|²≤0 for all w∈K and |z-w|≤r_k when w∈C_k(z),

\[
\int_K\log|z-w|^2\,d\mu(w)
\le 2^{-k}\log(r_k^2)
\le 2^{1-k}(\log 2-4^{k+1})\longrightarrow-\infty.
\]

Thus u(z)=−∞ at every z∈K. The potential u is finite at z=2, because all w∈K lie in [0,1/50]. It is locally integrable by Tonelli applied to the positive and negative parts of the logarithmic kernels on compact coordinate discs; the singular negative part is uniformly area-integrable in w∈K. Hence u is a well-defined ω-psh potential rather than the function identically −∞. Its pole set contains K, proving that K is polar without invoking an external capacity theorem.

**Global extension and currents.** Near infinity use ζ=1/z. For δ≥0, the same potentials read

\[
u_\delta(1/\zeta)
=\int_K\left[\log\bigl(|1-w\zeta|^2+\delta|\zeta|^2\bigr)
-\log(1+|\zeta|^2)\right]\,d\mu(w),
\]

which is smooth near ζ=0 since |w|≤1/50. Thus no additional mass or singularity lies at infinity. For δ=0, the normalized one-dimensional Poincaré–Lelong formula gives

\[
\omega+dd^c\log\frac{|z-w|^2}{1+|z|^2}=\delta_w.
\]

Integrating this current equality in w yields T=μ, with total classical mass 1. On a complex curve the Lelong number of a positive (1,1)-current at x is its atomic mass at x in this normalization; hence ν(u,x)=μ({x})=0 for all x, including infinity.

**Explicit smooth positive approximation.** For every δ>0, differentiation under the integral on C gives

\[
T_\delta
=\left(\int_K\frac{\delta}{\pi(|z-w|^2+\delta)^2}\,d\mu(w)\right)dA(z).
\]

The density is smooth and strictly positive. The displayed ζ-coordinate expression gives the same strict positivity at infinity (its dd^c numerator has positive coefficient δ), so T_δ is globally a smooth Kähler form. The elementary polar-coordinate identity

\[
\int_{\mathbb C}\frac{\delta}{\pi(|z-w|^2+\delta)^2}\,dA(z)
=2\delta\int_0^\infty\frac{r\,dr}{(r^2+\delta)^2}=1
\]

shows T_δ(X)=1 exactly. Moreover, for any ρ>0, the fraction of this kernel outside B(w,ρ) is δ/(ρ²+δ). Thus these kernels form a uniform approximate identity and T_δ converges weakly to μ as δ↓0. The functions u_δ decrease pointwise to u by monotone convergence after subtracting a fixed bounded-above kernel; local L¹ convergence follows from the uniform local area-integrability of their logarithmic differences (or the standard monotone convergence property of psh functions). By Lemma 13.7.3 their decreasing convergence is also in extended capacity. Smooth u_δ have zero Lelong numbers.

**Exact defect and distinctions.** The measure μ is carried by K⊂{u=−∞}; by the degree-one non-pluripolar formula in Example 13.11.8, \(\langle T\rangle=\mathbf1_{\{u>-\infty\}}\mu=0\). Smooth T_δ have no poles, so \(\langle T_\delta\rangle=T_\delta\), of total mass 1. Because K is polar, it has zero planar area and hence T_δ(K)=0; μ(K)=1, so the two probability measures are mutually singular, which gives the exact total variation norm 2. The lower semicontinuity statement of Theorem 13.7.5 reads \(1\ge0\) here, and its non-loss hypothesis is visibly false. For fixed δ the smooth bounded singularity is less singular than u; thus the inequality of Theorem 13.8.7 is consistent as well. **No general theorem is disproved.**

## Distinctness, disposition, and actual coverage

- **Different from printed Example 13.7.6:** its limit [0] has a unit atom/positive Lelong number. Here the limiting current is completely diffuse and has **zero Lelong number at every point**, yet *all* classical mass lies on its polar support; every approximant is smooth and strictly positive rather than a bounded rooftop truncation.
- **Not a duplicate of POME-CURVE-POLAR-WEAK-CLOSURE-001:** that prior finding uses a nonatomic polar Cantor probability for weak closure and total-variation geometry of ideal singularity classes (§§13.28/.30). The new verified assertion is the **full non-pluripolar mass defect under smooth full-mass convergence in extended capacity** and the insufficiency of all pointwise Lelong numbers to diagnose it, at §§13.2/13.7/13.11. The previously known Cantor/polar-set principle is credited, not counted anew.
- **Optional proposed correction (no production edit):** append a qualified companion example after §13.7.6, emphasizing that zero Lelong numbers alone do not prevent non-pluripolar mass loss. Link §13.11.8 for the degree-one mechanism. Do not change Theorems 13.7.5 or 13.8.7.
- **Affected dependents:** mass semicontinuity §13.7.5, singularity order §13.8.7, degree-one product §13.11.8, and uses of full-mass limits that might confuse atomic Lelong control with uniform integrability of pole mass. The general proof chains of these results have **not** been certified.
- **Actual selected coverage:** checked integrated Definition 13.2.4/Lemma 13.2.2; Lemma 13.7.3, Theorem 13.7.5 and Example 13.7.6; Example 13.11.8; statement and nonexcluded comparison of Theorem 13.8.7. No full section certified. Continuing baseline: **25 actual ToC chapters / 747 numbered sections / zero complete mathematical section certifications**. Existing errors, proof gaps, external dependencies, and all user-deferred Demailly-related work are unchanged.
- **Checks performed:** explicit cylinder-mass inequality, Poincaré–Lelong normalization, polar-coordinate kernel-mass integral, approximate-identity tail bound, and the exact degree-one product calculation. No project build, project tests, CI, browser publication, or formal proof verification.
