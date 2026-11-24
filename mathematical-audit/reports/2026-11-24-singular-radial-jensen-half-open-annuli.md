# Singular radial Jensen identity: exact endpoint convention and current-support rotation

Date: 2026-11-24. Reviewed production main: `b6933b772f41b45918f7e25ed1afbbb1fd892272`.

## POME-PLURIHARMONIC-SINGULAR-JENSEN-HALF-OPEN-001

Severity low; status **verified conditional deduction**, not a false printed theorem or a proof gap in its smooth statement. Target: `docs/sections/local-mass-bounds-for-pluriharmonic-currents/index.html`, blob `4c2db22424afb29ff4ec2f972dc28cb50b8f0b82`, Lemma 5.65.1 (transcendental-positive-cones:42DE46D8, permanent 64884C4CF78E), physical lines 8–43; Corollary 5.65.2, permanent 63CAD58A60D1, lines 48–65. The existing smooth radial identity is correct. Its strict-annulus formula cannot simply be copied to singular currents at all radii.

### Measure-theoretic extension

Let S be any positive current of bidimension (p,p), 1 <= p < N, on B(a,R) in C^N with dd^c S=0. Write rho=|z-a|^2, beta=dd^c rho, alpha=dd^c log rho off a. Use the printed normalization. Define
`m = rho_*(S wedge beta^p)` and
`v = rho_*(S wedge d rho wedge d^c rho wedge beta^(p-1))`
as locally finite positive measures on (-infinity,R^2), both extended by zero on the negative axis. These pushforwards are locally finite since inverse images of compact intervals are compact in the ball. Semipositivity of the smooth forms and the pointwise inequality d rho wedge d^c rho <= rho beta give 0 <= v <= t m as measures.

For every g in C_c^infinity((-infinity,R^2)), the smooth compactly supported test g(rho) beta^(p-1) gives exactly the printed distribution identity
`0 = integral g' dm + integral g'' dv`.
Therefore D(m-Dv)=0 as distributions on the entire interval (-infinity,R^2). A distribution of derivative zero is constant: a test of integral zero has a compactly supported primitive. Since both distributions vanish on the negative axis, this constant is zero, so Dv=m. Put M(t)=m([0,t)) for t>0 and M(t)=0 for t<=0. Fubini on compactly supported tests gives DM=m (including any possible atom at zero). Thus v=M(t)dt, since v-Mdt has derivative zero and vanishes on the negative axis. In fact m has no atom at zero: if m({0})=c>0, then v/t=M(t)dt/t has infinite mass on (0,b), whereas v<=t m implies that v/t has mass at most m((0,b)), finite. This rules out c>0 without presupposing the growth estimate.

On (0,R^2), put A(t)=t^(-p) M(t), the left-continuous representative. Since the square of d rho wedge d^c rho vanishes, the pushforward eta of S wedge alpha^p is
`eta = t^(-p) m - p t^(-p-1) v = DA`.
All products here have smooth coefficients off zero; no product of two singular measures occurs. The form alpha is semipositive and therefore eta>=0. The elementary Stieltjes identity for the left-continuous primitive yields for **every** 0<r<s<R,
```
s^(-2p) integral_{|z-a|<s} S wedge beta^p
 - r^(-2p) integral_{|z-a|<r} S wedge beta^p
 = integral_{r<=|z-a|<s} S wedge alpha^p .
```
Closed balls instead give the complementary convention (r,s]. Strict annuli are valid when the omitted inner sphere has zero eta mass. This yields monotonicity and the trace growth O(r^(2p)) for all p in the given range; uniformity for centers in an inner compact set follows by comparing with a fixed outer radius and bounding trace mass on a common compact set. The p=N-1 case recovers 5.65.2 locally without convolution. The p=0 case was not included in the deduction. A previous 2026-10-26 support-dimension bound for (1,1) currents is not counted anew.

### Necessity of the endpoint convention

Take N=2, p=1, a=0, R>1 and S=dd^c max(0,log |z|^2). This is a positive closed current, zero inside the unit ball and equal to alpha outside the unit sphere. There alpha has rank one, so S wedge alpha=0 on 1<|z|<s. However for s>1,
`integral_{B(0,s)} S wedge beta = s^(-2) integral_{B(0,s)} beta^2 = s^2`
in the printed normalization dd^c=i/(2pi) partial barpartial. Indeed Stokes applies to the distributional derivative because the potential is smooth in a collar of the outer boundary: subtract a smooth function agreeing there, whose difference has compact support and hence zero integral against the closed beta after dd^c. On the sphere d^c log rho=s^(-2)d^c rho, giving the displayed formula. The inner open-ball mass at r=1 is zero. Thus the left side is 1 while the strict-annulus integral is 0. The omitted unit sphere carries eta mass 1. This is a counterexample only to a proposed singular extension with the wrong endpoints, not to the smooth lemma.

### Proposed addition and dependencies

Add an audit-only proposed remark after 5.65.1 with the half-open formula and the proof above; leave the original smooth statement and permanent tags unchanged. Corollary 5.65.2 can optionally use the generalized identity (its current proof is valid and unchanged); no other dependents have been verified. The proof uses only positive-current testing, distribution derivatives, scalar Fubini/Stieltjes calculus and smooth radial form algebra, not Demailly approximation. No complete transitive internal-dependency certification is claimed.

## Additional direct rotation and actual coverage

- **Whole direct §5.61**, `docs/sections/positive-current-extension-and-analytic-integration--integration-over-analytic-sets/index.html`, blob `4c8c14a1b438c49f4d43f63e9f54ed1756d09b4f`, mathematical lines 8–53, tags 8C07385777E6, B7EB7069B315. The finite local parametrization proof uses a basis of decomposable strongly positive forms; the basis property survives small generic coordinate perturbations. The polydiscs may differ, so the common smaller neighborhood and nonnegative summands are essential for the trace bound. The zero extension in 5.61.2 gives closedness using the stated 5.60.3 extension input and pure-dimensional hypothesis. Finite local parametrization, positivity spanning, and 5.60.3 remain upstream dependencies, not certified here.
- **Whole direct §5.62**, `docs/sections/normal-currents-on-cr-submanifolds/index.html`, blob `f7082582d5ee3c9af0959dead737c752cdc03434`, lines 6–145. Corollary 5.62.1 (demailly-complex-geometry:F8F9292A, permanent D73EBFFE10D2), Theorem 5.62.3 (88C601DA5D62), Lemma 5.62.4 (403785A5B419), Theorem 5.62.5 (2CCAC11D6524), Corollary 5.62.7 (F39ED1E5BACF). Checked rank of complex conormal equals n-h(x), pure-type wedge annihilation for order-zero measures, telescoping compact divergence decomposition with parameters, gluing of transverse measures via connected fibers and local normalized tests, and singular-stratum induction. No need to differentiate a merely continuous frame; positivity and support conclusions use separate normalized tests. The repeated proof at lines 139–145 is a cross-reference to the canonical statement, not a second mathematical theorem. Internal C^1 normal-current calculus, analytic stratification and holomorphic regularity remain upstream inputs.
- **Whole direct §5.65**, anchors above: smooth proof and corollary checked, one new conditional extension. Previous selected October 26 visit retained, no historical first-visit claim.
- **Selected §5.64.1–2**, `docs/sections/null-supported-kahler-currents/index.html`, blob `009f58a180936636f2e5927b9272f87f2c93aa29`, lines 7–108; tags 0B34D9269CEA and E682ACE02BAF. Rechecked real-analytic zero-set proof, finite positive-cover caps, generic constants avoiding countably many hyperplanes, and closed tie set. Prior ridge and support-dimension deductions not duplicated. Lemma 5.64.3 and dependent Corollary 5.64.4 (lines 112–177) rely on the excluded approximation programme and remain **deferred-by-user**; no proof replay or completion attempted. Not a whole-section review.

Actual rendered TOC: `docs/chapters/index.html`, blob `c0c07abf4d8f7575b54cff2ec694fcf987f51cf8`, 747 distinct section locators; exact set equality with the 747 numbered matrix rows checked. Three whole direct sections (legacy-unreconciled, not historical first visits), one selected repeat, one new conditional deduction, zero newly confirmed false printed statements, zero new unresolved proof gaps, zero complete transitive certifications. No tests/build/CI, body, registry, permanent-tag, main or website changes. All excluded Demailly/Bergman/L2/OT/multiscale/positivity-loss programmes remain deferred-by-user.
