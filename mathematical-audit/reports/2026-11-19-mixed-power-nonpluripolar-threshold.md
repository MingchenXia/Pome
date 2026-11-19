# Mixed power-logarithmic non-pluripolar products: a sharp cross-threshold

**Date:** 2026-11-19. **Reviewed main:** b6933b772f41b45918f7e25ed1afbbb1fd892272. **Integrated section:** docs/sections/non-pluripolar-products--truncation-and-plurifine-locality/index.html, blob 81be8c5acc360c96bd3c5acba05a3cdb5fafaf4c, complete mathematical lines 7–165. The underlying example is **foundations-of-pluripotential-theory:2F8E45A2 / permanent tag 6F4C920FEDCA**, §13.2.9, lines 151–165. The definition/criterion and multilinearity are **13.2.2 / tag D59675D9F6D8** (lines 35–53) and **13.2.6 / tag 7F7123F92478** (lines 81–125).

**Finding POME-NPP-MIXED-POWER-CROSS-THRESHOLD-001 — low / verified conditional deduction.** This is a genuinely **mixed, two-exponent** extension of the existing printed Example 13.2.9, not a claim that the example is wrong. The *single-exponent diagonal criterion* was already reported as **POME-NPP-POWER-SINGULARITY-THRESHOLD-001** on 2026-10-30 and is **not** claimed as new. The new conclusion is the cross-condition a+b<1 and the possibility that the mixed product is locally finite even though one of the two self-products is not.

## Exact statement and normalization

Fix real exponents 0<a,b<1 and 0<R²<min(1-a,1-b). On

\[
U_R=\{(x,y)\in\mathbb C^2: |x|<R,\ 0<|y|<e^{-1}\}
\]

put \(L=-\log|y|\) and \(u_c(x,y)=(|x|^2-1)L^c\), for c=a,b. Extend both to the axis y=0 by the value -infinity, enlarging U_R to include that axis. They are plurisubharmonic, smooth and strictly psh off the axis. Their mixed non-pluripolar product is locally finite on the enlarged domain **if and only if**

\[
\boxed{a+b<1.} \tag{M}
\]

When a+b<1, for 0<rho<R and 0<s<e^{-1}, put K(rho,s)={|x|<=rho, |y|<=s}, T=-log s, and

\[
A=a(1-a)+b(1-b),\qquad B=A+2ab.
\]

Then the exact non-pluripolar mass of that cylinder is

\[
\boxed{\int_{K(\rho,s)}\langle dd^cu_a\wedge dd^cu_b\rangle
=\frac{A\rho^2-(B/2)\rho^4}{2(1-a-b)}\,T^{a+b-1}.} \tag{E}
\]

Here \(dd^c=(i/2\pi)\partial\bar\partial\), and \(dV_4=dA_xdA_y\). There is no mass on the axis. For a+b>=1 the mass of *every* cylinder meeting the axis with positive x-area is infinite (logarithmic divergence at equality, power divergence above it).

## Direct computation and proof

Write q=|x|². Since \(L_y=-1/(2y)\), \(L_{\bar y}=-1/(2\bar y)\), and \(L_{y\bar y}=0\) away from the axis, the complex Hessian of u_c has entries

\[
(u_c)_{x\bar x}=L^c,\quad
(u_c)_{x\bar y}=-\frac{c\bar x}{2\bar y}L^{c-1},\quad
(u_c)_{y\bar y}=\frac{c(1-c)(1-q)}{4|y|^2}L^{c-2}.
\]

Its determinant is

\[
\det H_c=\frac{c[(1-c)-q]}{4|y|^2}L^{2c-2}>0
\]

because q<R²<1-c. Consequently each u_c is strictly psh off the axis. It tends uniformly to -infinity as y tends to zero on compact x-cylinders, so its prescribed extension is psh by the removable-polar-set theorem cited by §13.2.9 (Theorem 5.11.1).

For smooth (1,1) Hessians in complex dimension two, the mixed wedge is

\[
 dd^c u_a\wedge dd^c u_b
 =\frac{(H_a)_{11}(H_b)_{22}+(H_b)_{11}(H_a)_{22}
 -(H_a)_{12}(H_b)_{21}-(H_b)_{12}(H_a)_{21}}{\pi^2}\,dV_4.
\]

Substitution yields the exact density

\[
\boxed{
dd^c u_a\wedge dd^c u_b
 =\frac{A-B|x|^2}{4\pi^2\,|y|^2}\,
 L^{a+b-2}\,dA_xdA_y
}\quad (y\ne0). \tag{D}
\]

The coefficient is strictly positive on U_R: positivity also follows directly from positive definiteness of both Hessians; algebraically \(B>0\) and \(A-Bq>0\) for q<R²<min(1-a,1-b).

On the common truncation set \(O_k=\{u_a>-k,\ u_b>-k\}\), both truncated potentials equal the smooth originals. By plurifine locality (the printed §13.2.2 / §13.2.6 and Theorem 5.47.22), the level-k truncated mixed measure equals \(1_{O_k}\) times (D). The sets O_k increase to the complement of the pluripolar axis, so monotone convergence identifies the increasing *trace measure*, possibly infinite, with (D) restricted off the axis. The exact local finiteness equivalence in Lemma 13.2.2 applies; there is **no** assumption that the mixed current exists globally before this criterion is checked.

Integrating (D) in the y-variable gives

\[
\int_{0<|y|\le s}\frac{L^{a+b-2}}{|y|^2}\,dA_y
=2\pi\int_T^\infty t^{a+b-2}\,dt.
\]

The integral is finite exactly when a+b<1, and equals \(2\pi T^{a+b-1}/(1-a-b)\) then. Furthermore,
\(\int_{|x|\le\rho}(A-B|x|^2)\,dA_x=\pi(A\rho^2-B\rho^4/2)\).
Combining yields (M)–(E), including every normalization factor. The coefficient in (E) is positive for 0<rho<R. For a+b>=1 the integrand is bounded below by a positive multiple of \(t^{a+b-2}\) on every smaller x-disc and hence diverges, so the local-finiteness criterion fails.

**Strict separation of mixed and self finiteness.** Take a=3/4, b=1/8 and any R²<1/4. Then a+b=7/8<1, so the mixed product is locally finite. But 2a=3/2>1, so the self-product \(\langle(dd^cu_a)^2\rangle\) is *not* locally finite. This disproves the potentially tempting implication “a finite mixed non-pluripolar product forces every self-product to be finite.” It does **not** contradict the printed multilinearity result, which assumes finiteness of the products to which it is applied. For a=b the density specializes to the previously documented one-parameter threshold; this specialization is a consistency check, **not** a new result.

## Direct integrated-reading audit and unresolved dependencies

All current §13.2 mathematical paragraphs **lines 7–165** were read directly: the Borel/plurifine truncation construction (7–16), Borel restrictions preserving positivity (Lemma 13.2.1, lines 20–27, tag 6632853A40C9), criterion and total-variation trace convergence (Lemma 13.2.2, lines 35–53), definitions (58–63), strong positivity (Proposition 13.2.5, lines 67–76, tag 1FAE60CC76F9), current invariance/locality/additivity/homogeneity (Proposition 13.2.6, lines 81–125), chart comparison and gluing (129–148), and Example 13.2.9 (151–165). Checks focused on the order of restriction versus limiting, the measurable plurifine sets, the local compactness quantifier in trace mass, and the distinction between locally finite and potentially infinite increasing trace measures. No independent new confirmed printed error or proof gap was identified.

**Proposed addition, not repair:** a separate optional mixed-family corollary after Example 13.2.9, explicitly labeling the cross-threshold and counterexample to self-finiteness inference. **Affected users/dependents:** discussions of mixed products in §13.2.6, §13.5 and §13.13, where finiteness of each factor's repeated product must not be inferred from one finite mixed product. Do not alter the printed theorem or permanent tags. All assertions remain conditional on the cited Bedford–Taylor localization (§7.2, §5.47), polar-extension (§5.11), and trace-measure tools (§5.3); their *complete upstream proof chains were not reverified*.

**Coverage delta:** +1 complete direct integrated section reading (§13.2), +0 complete upstream proof-chain certifications, and no claimed first-ever visit. Previous 2026-10-30 §13.2 partial result is preserved, not repeated. The user-excluded Demailly approximation/regularization and dedicated Bergman, L², Ohsawa–Takegoshi, multiscale atlas and positivity-loss proof-completion work remain **deferred-by-user**, neither resolved nor certified. No tests, builds, CI, public-site publication, source/registry edits or main changes.