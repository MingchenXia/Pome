# Exact determinant-density range and geometric concentration audit — 2026-11-27

Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`. Audit parent: `3975da5612f1f4152a70b20be81a1e9be070408a`.

## POME-GAUDUCHON-DETERMINANT-EXACT-BALL-001

**Severity:** low. **Status:** verified conditional deduction, not a printed error. The support-function identity in Theorem 12.18.8 is strengthened to an exact range assertion, not just a description of its closed convex hull.

### Anchors and inputs

- `docs/sections/a-gauduchon-variational-volume--geometric-bounds-and-determinant-concentration/index.html`, blob `6316720e1ce9112dc6b9b2f62db91361cba7e0cc`, physical lines 104–124 (Lemma 12.18.6, tag 5771D42397D7; intrinsic coefficient formula (12.18.7), tag DCAEAF642D39), 130–196 (Theorem 12.18.8, permanent 3EA495FF9D1A, source non-kahler-pluripotential-theory:6957E040; equation 12.18.9, source 1F4A2E2C, permanent 290803738499).
- `docs/sections/a-gauduchon-variational-volume--a-compact-dual-problem-over-gauduchon-currents/index.html`, blob `1c0f7efb92914b8a55754bd5039d7319392fb03b`, lines 10–26 (compactness and normalization convention), 39–66 (Lemma 12.7.2, tag FB6C2382E066, upper semicontinuity for continuous positive roots).
- `docs/sections/a-gauduchon-variational-volume--integrable-densities-in-the-compact-gauduchon-problem/index.html`, blob `1b7a423b1f46d3f1e7b6211c14cd2d4e85cc4a73`, lines 23–62 (Theorem 12.10.1, tag 41D17749328B, general tail criterion for attainment; context). That general attainment theorem is not itself a new finding. Earlier POME-GAUD-FIXED-ROOT-STABILITY-001 is also not recounted.

### Statement

Keep all hypotheses and normalization of 12.18.8: connected compact complex X of dimension n>=2, smooth probability volume dV, positive Hermitian beta satisfying dd^c(beta^j)=0 for 1<=j<=n-1, h=beta+dd^c u>0 with smooth real u, V=int beta^n, C=V^(-1/n), q=n/(n-1). Write G=G_h=G_beta for normalized positive dd^c-closed (n-1,n-1)-currents; k_T is the density of the intrinsic determinant measure Gamma_0(T) relative to dV.

1. Every nonnegative k in L^q(dV) with norm exactly C is realized as k_T by at least one T in G, without any regularity or positive lower bound on k.
2. If G contains a current S singular with respect to dV (all coefficient measures singular), then
   { k_T : T in G } = { k in L^q(dV) : k>=0, ||k||_q<=C }.
   In fact for any T in G and 0<=s<=1, k_(sT+(1-s)S)=s k_T almost everywhere.
3. The extra hypothesis holds when X contains a nonempty compact irreducible analytic curve, including the fixed flat tori E^n of 12.18.2 and 12.18.17. No smoothness of the realizing current or continuity of the map T -> k_T in the critical norm is asserted.

### Proof

Theorem 12.18.8 gives k_T>=0 and ||k_T||_q<=C for every T, and the exact support function sup_T int p k_T = C||p||_n for nonnegative p in L^n. To see attainment directly using the stated compactness and Lemma 12.7.2, choose smooth positive p_j -> p in L^n (smooth approximation of nonnegative functions, e.g. nonnegative smooth partition-of-unity convolutions followed by a positive constant). Holder gives uniformly over T:
|int (p_j-p) k_T| <= C||p_j-p||_n.
For p_j the functional is weakly upper semicontinuous by Lemma 12.7.2 with F=n log p_j. Hence the limit is upper semicontinuous on the compact G, and attains its maximum. This argument uses compactness, not sequential compactness; the approximating functions may be a sequence because L^n is norm metrizable.

Given k>=0 with ||k||_q=C, choose p=(k/C)^(q-1). Then ||p||_n=1 because n(q-1)=q. Let T maximize the p functional. Equality int p k_T=C forces ||k_T||_q=C and equality in Holder. Explicitly, for a=k_T/C and b=k/C, Young's inequality gives a b^(q-1) <= a^q/q + b^q/n, with equality precisely when a=b. Both integrals of powers are one, so the nonnegative Young defect integrates to zero and a=b almost everywhere. Thus k_T=k, even if k vanishes on a set of positive measure. This proves (1); it identifies the determinant density of every maximizer for this root, not necessarily the current.

For (2), choose a dominating coefficient measure in any chart of the form dV+nu_s, where nu_s is a finite positive singular measure dominating the singular coefficients of both T and S. The absolutely continuous matrix of sT+(1-s)S relative to dV is exactly s times that of T. Formula (12.18.7), whose scalar determinant root is homogeneous of degree one, gives equality of the absolutely continuous parts of Gamma_0(sT+(1-s)S) and s Gamma_0(T). The singular part of each determinant measure is zero by 12.18.8, since both currents lie in G by positivity, closedness under dd^c and affine trace normalization. Hence the equality holds for the measures themselves, also at s=0 and s=1. This reasoning avoids applying a determinant to a sum of mutually singular matrices without specifying the reference measure. For arbitrary nonzero k with norm at most C, realize the sphere element C k/||k||_q by (1), then take s=||k||_q/C; the zero density is realized by S. The opposite inclusion is the printed bound.

For (3), the integration current [Z] of a compact analytic curve Z is positive closed of bidegree (n-1,n-1), finite mass, with positive trace degree int h wedge [Z]. Its coefficients are supported on the analytic curve of real volume zero because n>=2. Therefore S=[Z]/int h wedge [Z] has the required properties. On E^n take a coordinate elliptic curve. Even when n=2 the argument is valid. This uses only the usual positive closed analytic-cycle current input for the curve, or direct integration/Stokes on the smooth coordinate curve in the torus examples.

### Scope, correction and dependents

No source correction is required; propose adding this as a corollary of 12.18.8 with the explicit singular-current premise for the full ball. The sphere part alone is unconditional relative to the printed hypotheses and dependencies. The support function alone would not prove the full ball statement without the singular-current construction. The range is therefore exactly a closed convex positive ball on the examples in 12.18.2/17 despite the nonlinear determinant map. The printed failure of critical power continuity in 12.18.17 is unaffected. No assertion about a general X with no singular normalized current, uniqueness for merely measurable roots, smooth representatives for the ball, or convergence of potentials is made. Relevant conceptual dependents: 12.10.1 (attainment versus tail condition), 12.18.13/.15 (fixed entire determinant family under a background gauge), 12.18.17 (critical concentration). No new transitive proof certificate: the smooth MA existence theorem 14.2.1, mass invariance 11.1.7, compactness of the normalized cone 11.7, and the named Lusin/elliptic inputs remain conditional. No regularization programme reopened.

## Coverage and direct checks

Whole current integrated 12.18 mathematical lines 7–361, including all seven numbered statements (12.18.1, .2, .6, .8, .13, .15, .17). Checked:
- 12.18.1: dd^c(g^2) identity, monotonicity/homogeneity of lower mass, and exponent q; surface case uses the Gauduchon theorem.
- 12.18.2: cofactor normalization h^(n-1)/n!, area-one bump normalization, Fourier potential with Delta psi=4 pi(f-1), telescoping dd^c identity for powers, strict Jensen inequality and concentration exponents 2-2 alpha p.
- 12.18.6/.8: factor n(n!)^(-1/n) in the coordinate formula, degree-one homogeneity under reference measure change, integration by parts, mass normalization in A^n=V r^n/int r^n, and q duality. No approximation of the current cone by smooth currents is assumed.
- 12.18.13/.15: dd^c for functions of x_1, the first relative block and its determinant; 2(1-epsilon)^2-tau^2>0 under the stated bounds. dd^c of the off-diagonal perturbation vanishes because its terms repeat a first-coordinate differential. Lower powers split into the surface powers and closed curve powers, so the dd^c conditions persist. The fixed class assertion for the closed example does not imply a de Rham class for the nonclosed example.
- 12.18.17: Fourier series differentiates with factor 4 pi, uniform convergence by the summable m^-2 majorant, weak Poisson convergence, only one first-coordinate factor in the bounded Bedford–Taylor expansion, and the two mutually singular coefficient matrices of ranks 1 and n-1. Critical power loss is compatible with determinant-measure mass tending to zero; roots vary, not a fixed smooth density.

Contextual read: entire 12.7 lines 7–105 (already reviewed, no added full-section count), selected 12.10 lines 7–137. Also inspected selected nonexcluded portions of 12.19 (root matrix and Schur estimate, lines 210–304, and product arguments 313–344; no whole-section review; excluded regularization not reopened), and 16.28/16.29 excerpts (not credited toward coverage or certification). Current chapter 12 contents list exactly 36 sections, matching matrix IDs; global matrix has 747 unique section rows. Legacy visits are not reconciled, so no historical first-visit claim. New direct whole: 1; new conditional deduction: 1; new confirmed printed errors: 0; demonstrated proof gaps: 0; complete upstream certifications: 0. No build, tests, CI, source/registry/permanent-tag changes or publication. All excluded programmes remain deferred-by-user.
