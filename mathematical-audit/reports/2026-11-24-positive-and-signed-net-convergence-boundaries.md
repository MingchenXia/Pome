# Positive and signed measure nets: exact hypotheses and cross-chapter rotation

Reviewed main: b6933b772f41b45918f7e25ed1afbbb1fd892272. Audit head at entry: 0a6ebc845a051d8132c6a5a97b56ec15e3b99185. Date: 2026-11-24.

## POME-MEASURE-NET-SIGNED-TAIL-BOUNDARY-001

Severity: low. Status: verified conditional deduction and independent counterexamples to stronger variants; **not a confirmed error in the printed theorem**. Proposed action: add the positive-measure converse and the signed-net caution as a remark; no production patch.

Anchor: [§2.6](https://github.com/MingchenXia/Pome/blob/b6933b772f41b45918f7e25ed1afbbb1fd892272/docs/sections/measures-and-distributions--weak-convergence-of-measures/index.html), blob 45720b2399a645a1a9a8148873fdc01c634fc5d7; Proposition 2.6.1 (source 915FBB91, permanent 4DFD880D9E4D), lines 16–34, particularly eventual bounds at 23–29; Proposition 2.6.3 (source A9ED3F7E, permanent 54258F39AC23), lines 57–73. The positive-measure convention in §2.2.1 (permanent 901C72102EF9, lines 11ff, blob f0086e0d7fa46b8d1756eebb839b0ba14e663863) and the separately defined signed measure at lines 231–246 matter. Proposition 2.6.1 is correct as stated. The signed extension is not implicit in it.

### A. Exact converse to the tightness condition

Suppose finite positive Radon measures \(\mu_i\) on an open Euclidean set \(\Omega\) converge vaguely as a net to a finite positive Radon measure \(\mu\). Then the following are equivalent:

1. narrow convergence;
2. convergence of the total masses;
3. eventual uniform tightness in the precise sense of Proposition 2.6.3.

Indeed, (1) implies (2) by the bounded continuous test 1, and (3) implies (1) by the printed proposition. To prove (2) implies (3), fix \(\epsilon>0\), choose a compact \(K_0\) with \(\mu(\Omega\setminus K_0)<\epsilon/2\), and choose a continuous compactly supported cutoff \(0\le\eta\le1\) equal to one on \(K_0\). Let \(K=\operatorname{supp}\eta\). Then
\[
  \mu_i(\Omega\setminus K)\le\mu_i(\Omega)-\int\eta\,d\mu_i
   \longrightarrow \mu(\Omega)-\int\eta\,d\mu
   <\epsilon/2.
\]
Thus the tails are eventually smaller than \(\epsilon\). This is a net argument using just two scalar convergence conditions, not a sequential Prokhorov argument. If the vague limit is not assumed finite, condition (3) still forces finiteness as in the original proposition. Condition (2) here specifically requires a finite limiting mass.

### B. Distributional versus vague convergence: positivity cannot be dropped

Take \(\Omega=(-2,2)\), \(K=[-1,1]\), and a compactly supported continuous function \(f\) on \(\Omega\) that equals \(|x|\) on \(K\). Direct the finite subsets \(F\) of real smooth compactly supported tests by inclusion. For each \(F=\{\phi_1,\ldots,\phi_r\}\), the restriction \(f|_K\) does not lie in the linear span of the restrictions of these tests (it is not differentiable at zero).

There are finitely many points of \(K\) and real coefficients defining an atomic signed measure \(\sigma_F\) with
\[
 \int\phi\,d\sigma_F=0 \quad(\phi\in F),\qquad
 \int f\,d\sigma_F=1.
\]
For a self-contained justification, consider the vectors \((\phi_1(x),\ldots,\phi_r(x),f(x))\) in \(\mathbb R^{r+1}\) for \(x\in K\). Their span contains \((0,\ldots,0,1)\): otherwise some linear functional vanishes on the span but not on this last vector, expressing \(f|_K\) as a linear combination of the smooth restrictions. Express the last vector as a finite real linear combination of evaluations. The corresponding finite sum of point masses is \(\sigma_F\).

Every fixed smooth test is annihilated on a tail (and complex tests reduce to their real and imaginary parts). Consequently \(\sigma_F\to0\) in distributions, but not vaguely, even though all supports lie in the same compact \(K\). This is not a counterexample to §2.6.1, which assumes positive distributions.

A sufficient signed variant is: for each compact \(L\Subset\Omega\), the total variations \(|\sigma_i|(L)\) are bounded on some tail, with the tail allowed to depend on \(L\), and the signed distributional limit is a signed Radon measure \(\sigma\). The same fixed-support uniform approximation of a continuous test by smooth tests as in lines 23–29 works with \(|\sigma_i|(L)+|\sigma|(L)\) in place of \(2C\). No simultaneous tail bound for all compacts is needed.

### C. Even narrow convergence of a signed net does not imply an eventually uniform TV bound

Again take \(K=[-1,1]\Subset\Omega\). Direct the pairs \((F,N)\), where \(F\) is a finite set of real bounded continuous functions on \(\Omega\) and \(N\) a positive integer, by inclusion in \(F\) and the usual order in \(N\). Choose more distinct points of \(K\) than the number of functions in \(F\). The matrix of their function evaluations has a nonzero real kernel vector. The corresponding nonzero finite signed atomic measure has zero integral against every element of \(F\). Normalize its total variation to exactly \(N\), calling it \(\tau_{F,N}\).

For every bounded continuous test, its integral against this net is eventually exactly zero. Hence \(\tau_{F,N}\to0\) narrowly, and also vaguely and distributionally. But \(\|\tau_{F,N}\|_{\rm TV}=N\to+\infty\). In particular, there is no eventually uniform variation bound even on the fixed compact support. Pointwise eventual boundedness of scalar nets is not uniform boundedness of a single common family of functionals; the usual sequential Banach–Steinhaus inference cannot simply be transferred to arbitrary nets. The construction uses only finite-dimensional linear algebra and the directed-set definition. It does not depend on regularization of singular potentials.

Potentially affected applications: the vague compactness argument §2.7.3, signed-current tests elsewhere, and finite-map signed measure calculus §5.43.16. These are **scope cautions, not claims that the present proofs misuse signed nets**. §2.7.3 explicitly works with positive Radon measures and cutoff bounds. §5.43.16 proves an exact TV identity without an unjustified convergence step. No existing theorem is altered or refuted.

## Actual coverage

- **§2.6**, entire integrated mathematical lines 7–102, blob 45720b2399a645a1a9a8148873fdc01c634fc5d7, path above. Checked positive distribution-to-vague passage, open/compact portmanteau, eventual tightness, escaping-mass examples, rational tent approximation and diagonal extraction. In the last proof the common compact support is for the approximants of one fixed test; this suffices. The diagonal is used for a sequence, not an arbitrary net.
- **§2.7**, complete repeat, lines 7–89, `docs/sections/measures-and-distributions--nets-and-compactness/index.html`, blob 7e4a226a48f88a97b3db1a8dd7d8582c909aeea1. Willard subnet triple order is directed with an increasing final map; ultrafilter convergence and product compactness use finite intersections; §2.7.3 positive cutoff compactness is valid subject to its Riesz input; Arzelà–Ascoli finite covering proof uses equicontinuity at finitely many centers. Prior 2026-11-21 full read retained, not counted as first coverage.
- **§5.12**, entire mathematical lines 7–127, `docs/sections/plurisubharmonic-functions--kiselman-s-minimum-principle/index.html`, blob e26179ee7cbb45fe10f7b4aabb9057ca33739a87. Theorem 5.12.1 permanent 1F87EF4FCF69: real Hessian H, mixed B and complex C give the Schur complement \(C-BH^{-1}B^*\), exactly with factors 1/2 and 1/4 in the complex blocks (42–62). Checked fiber convexity of the inner parallel domain (66), compact sublevels ensuring the barrier blows up only at the indicated boundary (68–84), monotone nested domains and pointwise infimum limit (92–94). Corollary 5.12.2 permanent 2C1A82803889, lines 100–127: reciprocal boundary-distance convexity and affine tilt. Ordinary local radial convolution here is the classical elementary proof of the minimum principle, not Demailly approximation of currents.
- **§5.23**, entire mathematical lines 7–57, `docs/sections/plurisubharmonic-functions-and-singularities--changes-of-background/index.html`, blob 57c9cc9f1a10adf7925ef159c1095ca270150962. Proposition 5.23.1 permanent 237930AECE45: sign of the translation \(u-f\), same positive current, bounded smooth difference by compactness. Proposition 5.23.2 permanent B16999654254: zero coefficients explicitly omitted; no undefined \(0(-\infty)\).
- **§5.24**, entire mathematical lines 7–161, `docs/sections/plurisubharmonic-functions-and-singularities--maxima-and-the-maximum-principle/index.html`, blob af8c44279c1e18f00174d613473b1d175beaa44a. Verified the factor 2 in frozen-background maximum and gluing inequalities (17–39), a.e. comparison by ball means, Liouville and periodic sublogarithmic growth, local pluripolar removal and two-coordinate isolated-puncture argument (120–148), and the upper-test Hessian condition (154–160). Local removal relies on the upper-envelope theorem and polar-null-volume property; these upstream results not transitively certified. This is not a global Demailly approximation argument.
- **§5.43**, selected only: `docs/sections/plurisubharmonic-functions-and-singularities--pullback-and-descent/index.html`, blob e5cccf608a51dd1629374fc68a1d3d7e6fd15958. Reviewed §§5.43.15–20, lines 270–411: weighted fiber trace and TV scaling, finite maximum Lelong formula, pullback of polar curvature, descent and \(L^1\)/capacity comparison under modification. In §5.43.16 permanent 151A1D744DE7, lines 319–345, disjoint Jordan carriers justify the exact TV equality; the ramification-weighted atom formula is consistent with the log factorization. §5.43.20 permanent D7CDD8CAD2AC, lines 395–410, uses fixed exceptional collars before the convergence limit; does not assert a uniform linear comparison. The all-weight ideal criterion cited in §5.43.15 is not certified here and the excluded approximation programme was not reopened. Earlier selected disk/submersion/curve context was consulted; no whole-section claim.

The actual rendered contents `docs/chapters/index.html` (blob c0c07abf4d8f7575b54cff2ec694fcf987f51cf8) has 747 section locators; exact set comparison with the current SECTION_MATRIX rows gave no missing or extra locators. Four whole direct reads on previously unreconciled rows, one complete repeat, one selected section; historical first visits unasserted. One new finding (positive converse and two independent signed-net counterexamples), zero newly confirmed printed theorem errors, zero new unresolved proof gaps, zero complete upstream proof-chain certifications. No build, test suite, CI, source, registry, permanent-tag or publication changes. Demailly approximation/regularization and its dedicated Bergman, L2, Ohsawa–Takegoshi, multiscale-atlas and positivity-loss programmes remain deferred-by-user, not resolved or certified.
