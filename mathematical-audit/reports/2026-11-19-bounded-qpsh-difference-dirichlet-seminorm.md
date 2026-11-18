# Non-pluripolar Dirichlet seminorm from bounded-difference integration by parts (§17.2)

**Date:** 2026-11-19.
**Finding ID:** POME-NPP-IBP-DIRICHLET-SEMINORM-001.
**Severity:** low.
**Status:** verified conditional deduction; no printed theorem is refuted.

## Baseline, integrated anchors and exact scope

- Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
- Integrated reading edition: docs/sections/relative-energy-and-perron-segments--integration-by-parts-for-bounded-differences/index.html, blob 5779ef1a17a52e02052c7485a7aa04adf606aace, physical lines 7–230 (241 lines in file).
- Signed-current definition (17.2.1): source foundations-of-pluripotential-theory:563C886F; permanent tag 6B17AADE0338, approximately lines 20–35.
- Weak convergence Lemma 17.2.2: source foundations-of-pluripotential-theory:AA6423AA; permanent 5F05F95AAF1F, lines 48–74.
- Bounded-difference integration Lemma 17.2.3: source foundations-of-pluripotential-theory:7175CBB3; permanent ECFE5ECCB550, lines 77–153; auxiliary chi and zeta at lines 125–149.
- Symmetric integration-by-parts Theorem 17.2.5: source foundations-of-pluripotential-theory:609B8782; permanent 3E698B84D63D, lines 155–195; equation (17.2.6), permanent 93ACF4FD4967.
- Negativity Lemma 17.2.7: source foundations-of-pluripotential-theory:D31C3788; permanent 52C5A516B8C8, lines 198–230.

This run directly read every mathematical paragraph in the current §17.2, including the independence of presentation, Kähler truncation, capacity passage, parameter polynomial polarizations, and final comparison argument. This does not certify transitive dependencies.

## Verified deduction: a real Hilbertian seminorm

Let X be compact Kähler, dim_C X = n >= 1. Fix arbitrary closed positive (1,1)-currents T_1,...,T_{n-1}; set R = <T_1 wedge ... wedge T_{n-1}>, or R=1 for n=1. Let V be the real vector space of bounded quasi-psh differences modulo equality outside pluripolar sets. Every a in V has a presentation a=phi_1-phi_2 quasi-everywhere with phi_1 and phi_2 of the same singularity type.

Define the finite real bilinear functional

\[
 Q_R(a,b)=-\int_X a\,dd^c b\wedge R,
\]

where the signed measure is **precisely** the measure constructed in (17.2.1), not a presumed classical Bedford–Taylor product with unbounded factors.

**Result.** Q_R is well-defined, symmetric and positive semidefinite. In particular,

\[
 \left|\int_X a\,dd^c b\wedge R\right|^2
 \le \left(-\int_X a\,dd^c a\wedge R\right)
      \left(-\int_X b\,dd^c b\wedge R\right).
\]

Consequently ||a||_R=Q_R(a,a)^{1/2} is a seminorm on V; its null space is orthogonal to all of V, and V modulo the null space has a positive-definite inner product. The coefficient 1 in the Cauchy–Schwarz bound is sharp whenever the quotient is nonzero.

### Self-contained deduction from the printed §17.2 ingredients

1. The discussion following (17.2.1) gives independence of the common positive background and of the presentation, using the quasi-everywhere equality of quasi-psh functions and multilinearity of non-pluripolar products. Products do not charge pluripolar sets, hence changing bounded Borel representatives on such a set changes no integral. Adding presentations and swapping the two components for negative scalars make V a real vector space; multilinearity in the signed factor gives Q_R bilinear.
2. Theorem 17.2.5 states exactly that \(\int a\,dd^c b\wedge R=\int b\,dd^c a\wedge R\), so Q_R is symmetric.
3. Given a=phi_1-phi_2, choose a common sufficiently positive smooth background kappa. Because a is bounded, phi_1 and phi_2 have the same singularity type. Applying Lemma 17.2.7 to this pair yields Q_R(a,a)>=0.
4. For every t in R, positivity gives
   \[
   0\le Q_R(a+tb,a+tb)=Q_R(a,a)+2tQ_R(a,b)+t^2Q_R(b,b).
   \]
   If Q_R(b,b)>0, the quadratic discriminant is nonpositive, proving Cauchy–Schwarz. If Q_R(b,b)=0, positivity for both large positive and negative t forces Q_R(a,b)=0. Expanding Q_R(a+b,a+b) now proves the triangle inequality. The same inequality shows that every null vector is orthogonal to all vectors.
5. Sharpness is already witnessed in the smooth case: take T_i=omega for a Kähler form omega, and a nonconstant real smooth function a on connected X (present a as a-0 in a sufficiently positive background). By Stokes,
   \[
   Q_{\omega^{n-1}}(a,a)
   =\int_X da\wedge d^c a\wedge\omega^{n-1}>0.
   \]
   Taking b=c a with c nonzero gives equality. The general singular R need *not* have constants as its only null vectors (e.g. R=0 gives a zero seminorm).

## Direct proof review and boundaries

- Lemma 17.2.2: separates convergence in capacity of variable bounded weights from weak convergence of measures against one fixed quasi-continuous weight. Uniform capacity absolute continuity is essential; no setwise convergence is asserted.
- Lemma 17.2.3, Steps 1–2: plurifine locality on finite loci and deep-sublevel agreement justify truncation, while a strict positive Kähler margin allows the perturbed max construction.
- Lemma 17.2.3, Step 3: the claim at line 131 that the four potentials are lambda-kappa-psh concerns the **four original potentials in zeta_0**, not the perturbed potentials in zeta_epsilon; this correctly yields \(dd^c\chi\ge-(4\lambda/5)\kappa\). The common comparison capacity, not vague weak convergence, controls weighted limits. Step 4 compares polynomial constant coefficients after adding a large Kähler form. No erroneous normalization was found here.
- Theorem 17.2.5: the repeated-current polynomial in t is followed by the homogeneous polarization in positive parameters r_i. Equality on the open simplex suffices to identify every homogeneous coefficient.
- Lemma 17.2.7: the mass comparison for max(u,v-t-epsilon), plurifine locality, and a nonnegative layer-cake integral yield the diagonal sign.

**Classification:** this is a verified **conditional** mathematical consequence, not a new error, independent proof gap, or certification of the entire upstream chain. If desired, the Cauchy–Schwarz/quotient-seminorm assertion could be proposed as a corollary after Lemma 17.2.7, without altering permanent tags or source attribution.

Upstream inputs not completely checked here: non-pluripolar locality/multilinearity (13.2.6), finiteness (13.5.4), fixed-singularity mass invariance (13.8.8–9), capacity domination and quasi-continuity (16.25.6, 16.27.17–18), and their own predecessors. Dependents include relative-energy first/second variations and concavity (§17.3), and future uses of a non-pluripolar Cauchy–Schwarz estimate. The distinction between a correct printed theorem and complete proof-chain verification is maintained.

**Coverage:** +1 entire §17.2 directly reviewed; +0 upstream proof-chain certifications; first-ever visit count not asserted pending reconciliation of all legacy reports. The actual index contains 25 chapters / 747 sections. Excluded Demailly regularization/Bergman/L2/Ohsawa–Takegoshi/multiscale/positivity-loss programmes remain **deferred-by-user** (not resolved or certified). No build, test, CI, source/body, main, registry, permanent-tag or website operation in this run.
