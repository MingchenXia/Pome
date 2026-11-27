# 2026-11-27 — Curve section growth for countably many atoms

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Finding: **POME-CURVE-COUNTABLE-ATOMS-SECTION-GROWTH-001** (low / verified conditional deduction; not a printed theorem error).

## Anchors and scope

Integrated reading edition: docs/sections/holomorphic-sections-and-hermitian-mass/index.html, blob 5f00431e7986d899dc833c89175686b75f09371d. Theorem 19.8.11, permanent 1E6D5AA611CC, source CB9DFB6A, physical lines 255–288; bounded section algebra at lines 215–251 (Example 19.8.9, permanent D1A2270A67A3, source 0EC2EB60). The printed theorem assumes finitely many logarithmic poles with bounded remainders, and is not refuted. Its ordinary boundedness hypothesis is essential for its simultaneous dimension conclusion.

Selected nonexcluded checks: lines 104–213 (repeat: degree-zero and finite trace inequalities), 215–288 (repeat and new deduction), 291–354 and 360–368 (homogeneous section count and curvature degree only), 370–386 (dimension consequence only). Poincaré–Lelong signs, degree-zero trivialization, finite-divisor residual class, exact floor/ceiling conventions, Riemann–Roch growth, homogeneous Taylor coefficients and degree computation agree with the printed hypotheses. No whole-section or upstream certificate. The Bergman/regularization and dedicated L2 proof-completion programmes are deferred-by-user; no kernel approximation, extension theorem or positivity-loss work is undertaken. This is a curve divisor-counting result, not a continuation of those programmes.

## Exact section counts for arbitrary curve weights

Let X be a connected compact Riemann surface, L a holomorphic line bundle with smooth curvature beta and degree ell, and u a beta-PSH function not identically minus infinity. Write T=beta+dd^c u, a finite positive measure of total mass ell, and c_p=T({p}). With the printed dd^c normalization these are the coefficients of log|z|^2. The nonzero c_p form a countable family, and d=sum_p c_p <= ell. Define the finite integral effective divisor D_m=sum_p floor(m c_p) p. It is finite since each contributing atom is at least 1/m.

Then for every positive integer m,
\[
\mathcal H_m(u)=H^0(X,L^m(-D_m)),
\qquad
\lim_{m\to\infty}\frac{\dim\mathcal H_m(u)}m=\ell-d.
\]
This is an extension of the integrable-section half of 19.8.11, not of the bounded-section half or its mass identification.

Local justification without a regularization theorem: in a coordinate disk, after adding a smooth local curvature potential to u, subtract c_p log|z|^2 from the resulting subharmonic function. Its residual positive Riesz measure has no atom at the center, so its canonical subharmonic representative v is bounded above on a smaller disk. A germ of order k has integrand comparable to |z|^{2(k-m c_p)} exp(-m v), with bounded smooth factors. If k-m c_p <= -1, the upper bound on v proves divergence. Conversely, if k-m c_p > -1, choose conjugate exponents a,b>1 such that a(k-m c_p)>-1. On a sufficiently small disk the residual measure has mass M<1/(mb). By the local logarithmic Riesz representation on a smaller disk, v is the logarithmic potential of that restricted measure plus a harmonic term bounded there. If M>0, Jensen's inequality for its normalization to a probability gives
\[
e^{-mb v(z)}\le C\int |z-w|^{-2mb M}\,\frac{d\mu(w)}M.
\]
The integral in z over the smaller disk is uniformly bounded in w since mbM<1. If M=0, the residual is harmonic there. Hence exp(-m v) belongs locally to L^b. Hölder proves integrability of the weighted germ. This yields exactly k>=floor(m c_p), including integer endpoints. The proof uses the elementary local logarithmic Riesz representation, Jensen and Hölder; no asymptotic Bergman or extension input. Compactness patches local integrability into the global equality.

For the growth, 0<=floor(m c_p)/m<=c_p, and termwise convergence and dominated convergence on the countable atomic family yield deg D_m/m -> d. Thus deg(L^m(-D_m))/m -> ell-d. If ell>d, the degree tends to infinity and Riemann–Roch plus Serre duality give, for all sufficiently large m,
\[
\dim\mathcal H_m(u)=m\ell-\sum_p\lfloor m c_p\rfloor+1-g.
\]
If ell=d the degree is nonnegative and o(m), and h^0<=degree+1 by evaluation at distinct points, so the normalized dimension tends to zero. The same elementary argument covers ell=0. The upstream Riesz representation, Riemann–Roch/duality and Poincaré–Lelong are explicit mathematical inputs, not newly certified here.

## Sharp separation from bounded sections: dense atoms with positive residual degree

On X=P^1 take L=O(1) and normalized Fubini–Study beta. Choose distinct dense points p_j and positive c_j with sum d strictly between zero and one. For each p choose its normalized logarithmic Green function g_p=log(chordal distance squared), with g_p<=0 and dd^c g_p=delta_p-beta. The L^1(beta) norms are independent of p by unitary invariance and finite by local logarithmic integrability. Hence the decreasing partial sums u_N=sum_{j<=N} c_j g_{p_j} have an L^1 limit u, not identically minus infinity, with its canonical beta-PSH representative given by the decreasing limit. Distributional differentiation gives
\[
T=(1-d)\beta+\sum_j c_j\delta_{p_j}.
\]
In particular the only atomic mass is the prescribed family, and the above theorem yields normalized integrable-section growth 1-d>0.

But every nonzero section s of L^m with bounded weighted squared norm off {u=-infinity} must vanish at each p_j. Indeed u<=c_j g_{p_j}, and near p_j a section nonvanishing there has norm bounded below; along points outside the pole set (which has area zero) approaching p_j, its weighted squared norm diverges at least as |z|^{-2m c_j}. Since a nonzero section has only finitely many zeros, this is impossible. Consequently W_m(u)=0 for every m>=1, although H_m(u) grows linearly. No section of the bounded graded algebra survives in positive degree.

In this particular model the non-pluripolar mass is 1-d: in dimension one the non-pluripolar measure is the restriction of T to the finite locus of u (conditional on the printed non-pluripolar restriction property), the smooth part gives the polar locus zero mass, and every atom lies on the pole locus. Thus the bounded-section growth can even vanish when the non-pluripolar mass is positive. In general the section-count formula only measures the atomic defect; diffuse polar mass can also be lost from the non-pluripolar measure, as already recorded in POME-POLAR-CURVE-AFFINE-NPP-MASS-SPECTRUM-001. That older example and the finite logarithmic rounding-gap result are not counted again.

## Disposition

No correction of the printed theorem is required; retain its finite bounded-remainder premise. Proposed optional addition: the arbitrary-curve integrable divisor formula and dense-atom counterexample immediately after 19.8.11. The bounded graded series of 19.9 must not be identified with the integrable spaces in this generality; no error in 19.9 is asserted without checking its specific hypotheses. The trace theorem 19.8.7 and the finite logarithmic statement remain distinct.

Current table of contents docs/chapters/index.html compared with SECTION_MATRIX.md: 747 section numbers, 747 distinct matrix rows, no missing or extra numbers. Current scope is selected only, not a first-ever review. Zero whole sections, one selected section, one new conditional deduction, zero new confirmed printed errors or demonstrated proof gaps, zero complete upstream proof-chain certifications. No builds, tests, CI, source, registry, tag or website edits.
