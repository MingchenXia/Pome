# Independent audit: sharp disk harmonic-measure comparison and planar corner exponents

Date: 2026-11-04 (Asia/Shanghai). Reviewed production main: b6933b772f41b45918f7e25ed1afbbb1fd892272.
Current reading-edition path: docs/sections/perron-theory-and-fine-boundary-limits/index.html.
Pinned main blob: 4bc2fb9317e2b6f6bb5b2d90208c677da8275eba.
The chapter/section inventory is 25 chapters and 747 numbered sections. This is **selected new proof/model coverage**, not mathematical certification of an entire section or all dependencies.

## Directly inspected integrated entries

1. Theorem 4.4.2: source classical-potential-theory:410B64F2, permanent tag 09873BDAF3E0, physical main HTML lines 11-34. We checked the completed harmonic-measure integral representation, intra-component measure equivalence, the use of Harnack and the conclusion for the L^p norms. This report does **not** independently establish the general Perron existence/resolutivity theorem.
2. Lemma 4.4.3: source classical-potential-theory:65DB36A3, permanent tag 621606E7390C, physical lines 39-47. We checked its polar-boundary invariance with an explicit single-point infinite-data model; the general polar-set construction is a conditional input.
3. Theorem 4.4.5: source classical-potential-theory:7A2F4581, permanent tag 2F74CBABB2A6, physical lines 52-65. We checked the local-barrier definition and positivity requirements and compared the sharp corner model against its purely qualitative conclusion.
4. Theorem 4.4.6: source classical-potential-theory:2E88760E, permanent tag 123C9AB7C052, physical lines 70-81. We checked the exterior-cone and planar-exterior-segment hypotheses against explicit bounded sectors. General regular exhaustion construction and its finite-critical-radius argument are not certified here.

All source and permanent labels were read from the actual integrated HTML, rather than inferred from source theorem numbering. No source/book, canonical registry, entry or permanent-tag change is proposed.

## POME-PERRON-DISC-HARMONIC-MEASURE-SHARP-001

**Status:** verified conditional deduction; **severity:** low. Theorem 4.4.2 and Lemma 4.4.3 are not refuted. The condition is the standard identification of disk harmonic measure with the classical Poisson integral; the elementary disk derivation below verifies it directly for continuous boundary data.

Let D={|z|<1}, x=0 and y=r with 0<r<1 real. Write zeta=e^{i theta}. The Poisson kernels are

\[
d\omega_0(\zeta)=\frac{d\theta}{2\pi},\qquad
d\omega_r(\zeta)=P_r(\theta)\frac{d\theta}{2\pi},\qquad
P_r(\theta)=\frac{1-r^2}{1-2r\cos\theta+r^2}.
\]

**Justification of the measures.** The elementary Fourier expansion

\[
P_r(\theta)=1+2\sum_{k=1}^{\infty}r^k\cos(k\theta)
\]

holds absolutely for r<1 and gives integral one. Convolution with this kernel is harmonic in the disk, nonnegative for nonnegative boundary data, and tends uniformly to a given continuous boundary function by concentration of the Poisson kernels near theta=0. Uniqueness from the bounded harmonic maximum principle identifies it with the Perron solution and its representing measure, as in Theorem 4.4.2.

Since (1-r)^2 <= |e^{i theta}-r|^2 <= (1+r)^2, the exact density bounds are

\[
a_r:=\frac{1-r}{1+r}\ \le\ P_r(\theta)\ \le\
b_r:=\frac{1+r}{1-r}.
\]

Consequently, for every Borel E in the circle,

\[
a_r\,\omega_0(E)\le\omega_r(E)\le b_r\,\omega_0(E),
\]

and for every 1<=p<infinity and every complex measurable f,

\[
a_r^{1/p}\|f\|_{L^p(\omega_0)}
\le\|f\|_{L^p(\omega_r)}
\le b_r^{1/p}\|f\|_{L^p(\omega_0)}.
\]

These **are the smallest possible constants**: P_r(0)=b_r and P_r(pi)=a_r; normalized indicators of arcs shrinking to these respective boundary points make the quotients of measures (and pth powers of norm quotients) converge to the extreme values. The exact identification of null sets and completions follows because P_r is bounded above and below by strictly positive constants. Hence the same completed measurable functions and integrability thresholds occur for every interior point of the disk. For p=infinity, the essential supremum norms are exactly equal; the printed theorem only claims 1<=p<infinity.

There are two additional direct endpoint tests of the integrability and polar exceptions. If a boundary function equals +infinity at zeta=1 and zero everywhere else, put q(z)=log(2/|z-1|). This is positive harmonic on D, has boundary lower limit +infinity at 1, and is finite at every interior point. For every epsilon>0, epsilon q is an upper Perron competitor; zero is a lower competitor. Hence the upper and lower solutions are both zero. In particular, a polar boundary spike has no effect on harmonic measure, matching Lemma 4.4.3 in this model. In contrast, for the nonnegative extended boundary function |theta|^{-alpha} near theta=0 (and bounded elsewhere), its Poisson integral is finite at each interior point precisely when alpha<1. For alpha>=1, positivity and the lower bound P_r>=a_r force the integral to diverge at **every** interior point; the nonnegative extended Perron formula gives +infinity rather than a finite resolutive harmonic function. This confirms the necessity of the integrability qualification in Theorem 4.4.2.

**Proposed optional source clarification:** after Theorem 4.4.2, append the exact disk ratio constants and an infinite single-point boundary datum. They make the measure completion and the sharp nature of the Harnack comparison transparent, but do not repair an error.

**Affected dependents:** Lemma 4.4.3 (polar changes), the componentwise harmonic-measure L^p equivalence, and subsequent boundary-limit applications in §§4.4-4.5. Only the elementary disk special case is established here.

## POME-PERRON-WEDGE-CORNER-HOLDER-001

**Status:** verified conditional deduction; **severity:** low. Theorems 4.4.5-6 are not refuted. The direct proof below needs only holomorphicity of a power branch and bounded harmonic comparison, not the full general cone/exhaustion proof.

Let 0<beta<=2pi and

\[
D_\beta=\{z=r e^{i\theta}:0<r<1,\ 0<\theta<\beta\}.
\]

For beta<2pi this is a bounded open sector with exterior cone aperture 2pi-beta at the vertex 0. At beta=2pi it is the slit unit disk (the positive radial segment is removed); the vertex has an exterior segment, exactly the additional planar case of Theorem 4.4.6. Put kappa=pi/beta and

\[
u_\beta(re^{i\theta})=r^\kappa\sin(\kappa\theta).
\]

The branch z^kappa is holomorphic on D_beta and u_beta=Im z^kappa is harmonic and strictly positive. It is bounded by one and extends continuously to the Euclidean closure. Its boundary values g_beta are zero on both radial sides (and the vertex) and equal sin(kappa theta) on the outer circular arc. These boundary values are Lipschitz on the compact geometric boundary: on the circle sin(kappa theta) vanishes linearly at each endpoint; on the radial sides it is identically zero. This remains true at beta=2pi, where the two sides refer to the same geometric slit and give the same boundary value zero.

Because u_beta is itself a bounded harmonic function attaining g_beta continuously, it belongs simultaneously to the upper and lower Perron classes. Their comparison forces

\[
H_{g_\beta}(r e^{i\theta})=u_\beta(r e^{i\theta}).
\]

In particular, on the angular bisector,

\[
H_{g_\beta}(r e^{i\beta/2})=r^{\pi/\beta}.
\]

Thus **no universal boundary estimate of the form** |H_g(z)-g(0)|<=C|z|^alpha **can hold for all Lipschitz data on this fixed sector when alpha>pi/beta**: the quotient r^{pi/beta-alpha} tends to infinity. For a reentrant angle pi<beta<2pi, the sharp example has pi/beta<1 despite Lipschitz boundary data. For the slit disk beta=2pi the example realizes the exponent exactly 1/2. This quantitatively distinguishes the small-exterior-cone regime from the exterior-segment endpoint, while both are regular as asserted in Theorem 4.4.6.

The same function is a strictly positive harmonic local barrier at the vertex; this is a direct test of the positivity/vanishing requirements of Theorem 4.4.5. The exact exponent is **the exponent of this model and an upper bound for any universal estimate on this fixed domain**, not a claim of optimal Hölder regularity for every continuous datum or every arbitrary exterior-cone domain.

**Proposed optional source clarification:** add this planar-sector formula after the exterior-cone/segment discussion, explicitly marking regularity as qualitative, not a universal Lipschitz boundary modulus.

**Affected dependents:** qualitative regularity in Theorems 4.4.5-6, the boundary control used in the Green-function arguments of §4.4.8, and any attempted Hölder-strengthening of Perron boundary limits. No claim is made about their complete proofs.

## Scope, excluded work and remaining questions

The two findings are independent verified special-case consequences, **not confirmed errors, proof gaps, repairs, or duplicate theorems**. This run directly evaluated §4.4.2-3 and §4.4.5-6 against exact Poisson and wedge models; it did not check §§4.4.8-26 in full, the construction of general harmonic measure, the general compactness/saturated-family lemmas, or downstream Martin-boundary arguments. The user's excluded Demailly approximation/regularization and its Bergman, weighted L2, Ohsawa-Takegoshi, multiscale-atlas and positivity-loss proof programme remains **deferred-by-user**, neither resolved nor revisited. No external private material is copied here.

No build, repository test suite, CI, formal verification or publication was performed; all calculations are explicit independent mathematical checks. Reviewed main remains b6933b772f41b45918f7e25ed1afbbb1fd892272, 25 chapters / 747 numbered sections / **zero whole mathematical-section certifications**.